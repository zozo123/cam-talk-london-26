"""Finite-world reference model of speculative sandbox scheduling.

This is a deterministic research *toy*, not an islo adapter, a production
scheduler, or a proof that passing a test means a patch is semantically correct.
The success-event sets form an explicit, assumed joint distribution.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import hmac
import json
from typing import Callable, Mapping


class Admission(Enum):
    INADMISSIBLE = "inadmissible"
    USE_WARM = "use-warm"
    FORK = "fork"


@dataclass(frozen=True)
class ForkGates:
    state_declared: bool
    fidelity_tested: bool
    private_writes: bool
    unique_identity: bool
    host_authority: bool
    external_effects_fenced: bool

    @property
    def satisfied(self) -> bool:
        return all(vars(self).values())


@dataclass(frozen=True)
class WorkCosts:
    trials: int
    warm_preparation: float
    parent_preparation: float
    capture: float
    restore: float
    execution: float
    verification: float
    divergence: float

    def __post_init__(self) -> None:
        if self.trials < 1:
            raise ValueError("trials must be >=1")
        for key, value in vars(self).items():
            if key != "trials" and value < 0:
                raise ValueError("all costs must be nonnegative")

    @property
    def warm(self) -> float:
        return self.trials * (self.warm_preparation + self.execution + self.verification)

    @property
    def fork(self) -> float:
        return self.parent_preparation + self.capture + self.trials * (
            self.restore + self.execution + self.verification
        ) + self.divergence


def admit(gates: ForkGates, costs: WorkCosts) -> Admission:
    if not gates.satisfied:
        return Admission.INADMISSIBLE
    return Admission.FORK if costs.fork < costs.warm else Admission.USE_WARM


@dataclass(frozen=True)
class Branch:
    name: str
    successful_worlds: frozenset[int]
    cost: float = 1.0
    latency: float = 1.0

    def __post_init__(self) -> None:
        if self.cost < 0 or self.latency < 0:
            raise ValueError("costs must be nonnegative")


class FiniteWorldScheduler:
    """Exact conditional likelihoods for an illustrative known joint model.

    In reality these success-event sets are unknown and a predictive model must
    be trained and evaluated out of sample. Only observed FAILs update feasible
    worlds; timeouts/cancellations are *not* silently counted as failures.
    """

    def __init__(self, worlds: set[int], branches: list[Branch]):
        if not worlds:
            raise ValueError("non-empty finite world model required")
        if len(set(b.name for b in branches)) != len(branches):
            raise ValueError("branch names must be unique")
        if any(not b.successful_worlds <= worlds for b in branches):
            raise ValueError("branch success events must be subsets of worlds")
        self.worlds = frozenset(worlds)
        self.feasible = frozenset(worlds)
        self.branches = {b.name: b for b in branches}
        self.attempted: set[str] = set()
        self.events: list[tuple[str, str]] = []
        self.accepted: str | None = None

    def predicted_pass(self, name: str) -> float:
        if name not in self.branches:
            raise KeyError(name)
        if not self.feasible:
            return 0.0
        return len(self.branches[name].successful_worlds & self.feasible) / len(self.feasible)

    def choose_next(self, *, benefit: float = 1.0, cost_weight: float = 0.1,
                    latency_weight: float = 0.0) -> str | None:
        if self.accepted is not None:
            return None
        scored = []
        for name, branch in self.branches.items():
            if name not in self.attempted:
                score = (benefit * self.predicted_pass(name)
                         - cost_weight * branch.cost - latency_weight * branch.latency)
                scored.append((score, name))
        if not scored:
            return None
        score, name = max(scored, key=lambda v: (v[0], -list(self.branches).index(v[1])))
        return name if score > 0 else None

    def record(self, name: str, outcome: str) -> None:
        if name not in self.branches or name in self.attempted:
            raise ValueError("unknown or repeated branch")
        if outcome not in {"pass", "fail", "timeout", "cancelled"}:
            raise ValueError("unknown outcome")
        self.attempted.add(name)
        self.events.append((name, outcome))
        if outcome == "pass":
            self.accepted = name
        elif outcome == "fail":
            self.feasible = self.feasible - self.branches[name].successful_worlds
        # A timeout or cancellation provides no oracle observation about success.

    def coverage(self, names: set[str]) -> float:
        covered: set[int] = set()
        for name in names:
            covered.update(self.branches[name].successful_worlds)
        return len(covered) / len(self.worlds)


def example_scheduler() -> FiniteWorldScheduler:
    return FiniteWorldScheduler(set(range(16)), [
        Branch("family-A", frozenset(range(6))),
        Branch("family-A-clone", frozenset(range(6))),
        Branch("independent-C", frozenset({6, 7, 8, 9})),
        Branch("alternate-D", frozenset({0, 6, 10, 11, 12})),
    ])


@dataclass(frozen=True)
class Receipt:
    task_digest: str
    artifact_digest: str
    verifier_digest: str
    evaluation_id: str
    epoch: int
    verdict: str
    mac: str


class TrustedController:
    """Minimal host-owned receipt/epoch contract; HMAC is only a toy authenticator.

    The verifier callable runs outside the child and is not controlled by it.
    It may nevertheless be incomplete: a pass is never labelled proof of semantic
    correctness. Production needs durable storage, key management, atomic CAS,
    real isolation, and crash-consistency guarantees.
    """

    def __init__(self, task_digest: str, verifier_digest: str, secret: bytes):
        if not secret:
            raise ValueError("secret required")
        self.task_digest = task_digest
        self.verifier_digest = verifier_digest
        self._secret = secret
        self.epoch = 0
        self._store: dict[str, bytes] = {}
        self._evaluations: set[str] = set()
        self._receipts: dict[str, Receipt] = {}
        self.promoted: str | None = None
        self.ledger: list[tuple[str, str, int]] = []

    @staticmethod
    def digest(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    def _seal(self, fields: tuple[str, str, str, str, int, str]) -> str:
        payload = json.dumps(fields, separators=(",", ":"), ensure_ascii=True).encode()
        return hmac.new(self._secret, payload, hashlib.sha256).hexdigest()

    def check(self, artifact: bytes, *, evaluation_id: str,
              verifier: Callable[[bytes], bool]) -> Receipt:
        if not evaluation_id or evaluation_id in self._evaluations:
            raise ValueError("duplicate/empty evaluation ID")
        self._evaluations.add(evaluation_id)
        digest = self.digest(artifact)
        self._store[digest] = artifact  # persist before check receipt
        try:
            passed = bool(verifier(artifact))
            verdict = "pass" if passed else "fail"
        except Exception:
            verdict = "error"
        fields = (self.task_digest, digest, self.verifier_digest,
                  evaluation_id, self.epoch, verdict)
        receipt = Receipt(*fields, self._seal(fields))
        self._receipts[evaluation_id] = receipt
        self.ledger.append((evaluation_id, verdict, self.epoch))
        return receipt

    def promote(self, artifact: bytes, receipt: Receipt, *, expected_epoch: int) -> bool:
        fields = (receipt.task_digest, receipt.artifact_digest,
                  receipt.verifier_digest, receipt.evaluation_id,
                  receipt.epoch, receipt.verdict)
        if not hmac.compare_digest(self._seal(fields), receipt.mac):
            return False
        if receipt.task_digest != self.task_digest or receipt.verifier_digest != self.verifier_digest:
            return False
        if expected_epoch != self.epoch or receipt.epoch != self.epoch:
            return False
        if receipt.verdict != "pass" or self.promoted is not None:
            return False
        if self._receipts.get(receipt.evaluation_id) != receipt:
            return False
        if self.digest(artifact) != receipt.artifact_digest:
            return False
        if self._store.get(receipt.artifact_digest) != artifact:
            return False
        self.promoted = receipt.artifact_digest
        return True

    def next_epoch(self) -> None:
        self.epoch += 1
        self.promoted = None
