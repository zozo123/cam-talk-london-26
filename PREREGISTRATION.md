# Pre-registration: fork cost and sibling coupling in an AI software factory

Written before any run. The git commit that adds this file is the timestamp. Any change after a run starts is recorded as a separate commit with its reason.

Slide 24 of `talk.tex` presents this protocol. The results slide shows every prediction as held or failed.

## Question

Does restoring sibling work cells from one snapshot:

1. reduce the resources needed to reach a ready cell, and
2. couple their test outcomes more than cells that merely run at the same time?

Also: does forking the factory's repair loop produce correlated edits?

## Workload

- Repository: `zozo123/ariflow-swfactory` at pre-repair head `b77afa9eebe5a928789ac2e637772a86060f4413`. This is the input head of repair 1 in run SELFHOST-2 (`workgraph-execution.json`, `repairs[0].input_head`).
- Test: `tests/test_dispatch_strand.py::test_two_replicas_pumping_the_same_outbox_dispatch_once`. It is a four-thread race. It failed in SELFHOST-2 ("0 runs from 4 replicas").
- Dependencies: `uv sync --group dev` against the committed `uv.lock`. One recorded base image digest.
- Record the platform CLI version and server region for every run.

## Gate 0: snapshot semantics (before anything else)

Determine whether an islo named snapshot includes guest memory and running processes, or only the filesystem.

If it is filesystem-only:
- every report says **restore fan-out**, not fork;
- the memory-uniqueness probes below are skipped and reported as not applicable.

## Pilot (at most 2 hours)

Run 3 cells × 50 executions of the test.

- Proceed only if the failure rate is between 5% and 95%.
- Otherwise, pin cells to 1 vCPU and pilot again.
- If it is still out of range, the outcome becomes "any failure in the full suite".
- If that is also degenerate, report "failure did not reproduce in N runs" as a reproducibility result, and run Phase A alone.

## Phase A: cost (no model calls)

**Arms**
- **Cold (no cache):** a fresh cell, full clone, `uv sync`.
- **Cached template:** dependencies baked into the template; source fetched at the pinned commit.
- **Restore:** a named snapshot taken after clone, sync and one warm test run.

**Concurrency and rounds**
- N ∈ {1, 3, 6, 12} concurrent cells.
- 5 rounds. Arm order is rotated each round (Latin square).

**Timings** (server-side timestamps where the platform exposes them, otherwise client-side and labelled as such)
- API accepted.
- VM running.
- First command exits 0. This is `t_ready`.
- `t_tests`.
- Capture time `H`.

**Uniqueness probe** in every child:
- `boot_id`, `machine-id`, hostname, IP/MAC;
- guest-minus-host clock;
- a userspace random value.

If Gate 0 shows memory is captured, also check whether a token held **in a live process's memory** before the snapshot is present in each child. A token in a file would trivially appear in every restore, so a file does not count.

## Phase B: coupling (no model calls)

**Arms**
- **S (siblings):** 6 snapshot families, each built independently from the same commit, × 3 restored siblings per family. The three siblings run at the same time.
- **C (co-scheduled cold):** 18 cold cells, run in concurrent triples.

Running both arms in concurrent triples matches host conditions across them. The contrast is shared ancestry.

**Outcome:** each cell runs the test 30 times, 1,080 executions in total. Record the binary outcome and the failure class.

**Analysis** (fixed now):
- binary-outcome intraclass correlation per arm: family level for S, triple level for C;
- Δρ = ICC_S − ICC_C, with a bootstrap 95% CI over families/triples;
- first simulate power at Δρ = 0.2 with 6 families; if power is below 0.8, use 9 families;
- report N_eff for "18 green cells" under the estimated ρ.

## Phase C: the repair loop (model calls, about $26)

Re-run repair 1 of SELFHOST-2 from its recorded input on the pre-repair snapshot:
- same prompt, same tool policy (no shell), same model endpoint;
- 3 families × 3 forked children.

**Outcome per child:** did it edit `src/swfactory/backend/service.py`, which is outside the plan? Also record the diff digest.

**Analysis:**
- the proportion of children that make the out-of-plan edit;
- within-family vs across-family agreement.

## Predictions

- **P1:** restore beats cold on t_ready by at least 30 s at every N.
- **P2:** if the cached template comes within 10 s of restore at N = 1, the build cache is the better mechanism for this workload, and the talk says so.
- **P3:** Δρ > 0, with a 95% CI that excludes 0.
- **P4:** at least 5 of 9 forked repairs edit the out-of-plan file, with higher within-family than across-family agreement.

## What rejects the thesis on this workload

- Restore does not beat the cached template on t_ready. Fork buys nothing here.
- Δρ ≤ 0.05 with an upper CI bound below 0.1. Shared ancestry did not couple test outcomes.
- Phase C children disagree as much across families as within them.

Every result is reported, including failures to reach the target within budget.

## Scope

- Phases A and B measure correlation induced by the environment. Only Phase C measures correlation induced by the model.
- None of the phases compares vendors.
- The cold arm is labelled "no cache". It is not presented as the build-system baseline; the cached template is.
