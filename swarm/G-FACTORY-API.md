# Researcher G — Universal Factory API / Promote-Once Runtime
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Owner framing:** Lampson + Dean systems-API design for the hill-climb substrate  
**Companion reads:** `UNIVERSAL-HILLCLIMB.md`, `PARALLEL-WORLDS-STATPHYS.md`, `STORY-SPINE.md`, B’s `B-REDUCE-STATPHYS.md`  
**Paper this talk contributes (name it):** ***Fork, Reduce, Promote: A Capability Contract for Cross-Domain Hill-Climb Runtimes***  
*(working short title: **Universal Factory API** — the missing named systems paper for the SW/RL/sim/bio/HIL isomorphism.)*

---

## Claim fence (non-negotiable)

| Say | Do not say |
|---|---|
| This is a **capability contract**: what a hill-climb *runtime* must expose so Search≠Authority holds at scale. | Every swfactory / Airflow path already has native N-way fork-merge. |
| Forkable sandboxes are the **body**; objective digest + reduce + promote are the **spine**. | We ship a product that already implements path-integral CI end-to-end. |
| Cross-domain isomorphism is architectural (same slots, different oracles). | Biology / HIL are solved by cloning the software factory. |
| Objective digest change = **epoch bump** (authority act). | Workers may edit the metric script “because they have a better idea.” |

Inspiration (methodology, not peer review): pstack hillclimb, OpenClaw search loop, ariflow-swfactory Cell/epoch/Search≠Authority. Physics naming (β, Z, anneal) inherits B’s fence — algebra with teeth, not Gibbs-of-nature.

---

## 1. Why name an API paper at all

SRG already has pieces: CoW/fork (DeltaBox, forkd, Tensorlake, Shepherd), precision-weighted reduce (2607.09689), Cell/epoch fencing (swfactory), local one-Δ discipline (pstack). What is **missing as a named systems contribution** is the *joint* capability contract:

> **fork / reduce / promote** as first-class operations; **objective digests** as epoch-bumping authority objects; **path-integral CI** and **world-diff protocols** as the merge story for machine-state branches — one fabric across SW, RL, sim, bio, HIL.

Lampson’s question: *What can the client rely on?*  
Dean’s question: *What scales when N paths fan out and only one promote may fire?*

---

## 2. Proposed API surface

Capability-level; not a language binding. Implementations (Tensorlake `clone`, Shepherd fork-graph, Firecracker CoW, container snapshot) bind underneath.

### 2.1 Core verbs

```text
# Identity & authority objects (live outside workers)
S0      = Snapshot.parent(id)              # immutable content-addressed parent
Obj     = Objective.digest(bytes)          # frozen harness + metric + stop predicate
Epoch   = Authority.epoch(Obj, policy)     # changing Obj ⇒ bump Epoch (authority act)

# Search body (may be stochastic; may fan out)
W       = World.fork(S0, n=K, epoch=Epoch) # path bundle; CoW parallel worlds
E_i     = W[i].run(proposal Δ_i)           # returns structured evidence, not naked scalar
Pool    = Reduce(E_1…E_K, Obj)             # partition / precision pool (B’s contract)
Keep    = Pool.verdict()                   # keep | revert | abstain (unresolved ρ / Δ)

# Singular tip
S0'     = Authority.promote(Pool.mode, Epoch)  # one bit; one control plane
          Authority.burn(W)                    # dispose measure; no leftover creds
```

### 2.2 Structured evidence (wire floor — hand to B)

Minimum fields a factory must carry from child → reduce (aligned with 2607.09689 worker record):

| Field | Role in API |
|---|---|
| `θ̂`, `J`, `n` | Estimate + precision shape + β≡n |
| `ℰ` | Evidence IDs (exact-overlap reject) |
| `ℒ` | Fork lineage / shared-root signal |
| `m` | Placement / retry / speculative tags |
| `obj_digest` | Must match Epoch’s Obj or reject |

Naked scalars and worker-writable scorers are **out of contract**.

### 2.3 Objective digests as epoch bumps

- `Objective` is content-addressed: metric script hash, fixture digests, stop predicate, β/anneal schedule id, oracle binary digest.
- **Mutation of Obj is not a patch inside a child** — it is an authority epoch bump. Same law as “freeze the harness before changing the system.”
- Epoch fencing: Cell/retry may change sandboxes; Epoch still owns the work unit. Crash → new body, same contract.

### 2.4 Path-integral CI (capability, not slogan)

Every PR / campaign is a **measure over forks**, not a green badge:

1. Boundary: `S0` + `Obj` pinned in Epoch.  
2. Sample: `fork(n=K)` path bundle.  
3. Observe: structured `E_i` with lineage.  
4. Reduce: pool → `(θ̂, Σ, Δ, Z_g)` + abstain rules.  
5. Promote: mode / zero-T authority decision → protected branch / checkpoint / claim / HIL slot.  
6. Burn runners; retain ledger.

**CI meaning:** merge authority consumes a *reduced posterior*, not “all checks passed on one contaminated machine.”

### 2.5 World-diff protocols

Future merge story for full machine-state branches (FS + optional memory snapshot lineage):

- **World-diff** = typed divergence between sibling worlds relative to `S0` (artifacts, env digests, process tree summaries — not raw CoW page lists as UX).  
- **Conflict = evidence:** incompatible world-diffs under the same Obj are first-class ledger events, not silent last-writer-wins.  
- **Promote** selects one world’s *accepted artifact set* into authority space; siblings remain archival paths.  
- Git is the intuition pump for *text*; world-diff is the analogue for *forkable machines*. Do not claim Git semantics already cover GPU/mem/net isolation.

### 2.6 Cross-domain binding (same fabric)

| Domain | `fork` samples | `reduce` pools | `promote` spends |
|---|---|---|---|
| Auto software | agent patches in Cells | tests + evidence digests | merge to main |
| Auto build / CI | toolchain / cache policy Δ | build-graph digests | protected branch |
| RL post-training | rollouts / preference paths | reward / win-rate / KL free-energy | policy checkpoint |
| Simulation | mesh / timestep / constitutive Δ | residual + conservation suite | publishable run |
| Comp. biology | sequence / pose / pipeline knobs | binding + replication digests | wet-lab / clinic tip |
| HIL / Physical AI | sim controller candidates | sim metrics → human+arm gate | robot hour |
| Auto research | hypothesis + experiment script | pre-registered metric + reproduction | paper / grant claim |

Oracle scarcity changes; **API slots do not.**

---

## 3. Invariants (client may rely on these)

1. **Search ≠ Authority.** Workers never hold promote tokens, publish keys, wet-lab booking, or Obj mutation rights.  
2. **Immutable parent.** `S0` is content-addressed; children CoW from it; revert = burn child, not “undo in place.”  
3. **Frozen objective for an Epoch.** Changing Obj bumps Epoch; mid-epoch metric edits are contract violations.  
4. **One promote bit per Epoch decision.** Fan-out may be N; authority merge is singular. Twenty promote channels ⇒ twenty control planes ⇒ failure.  
5. **Structured evidence or reject.** Missing `n`/`J`/`ℰ`/`ℒ`/`obj_digest` ⇒ do not pool as if independent.  
6. **Burn after promote.** Runners dispose; credentials do not survive the path. Ledger + artifacts remain.  
7. **Fork ≠ independence.** API may expose `fork(n=K)` as path sampling; reduce must treat shared lineage as correlation risk (hand to B).  
8. **Abstain is a valid verdict.** Unresolved ρ, oracle mismatch, or cold-liar diagnostics ⇒ withhold narrow promote.

---

## 4. Non-goals

- Replacing PIs, automating wet labs end-to-end, or AGI-scientist demos.  
- Claiming thermodynamic equilibrium of agent populations.  
- A single vendor SDK as the contribution (Tensorlake / islo / DeltaBox / Shepherd are *bindings*).  
- Guaranteeing statistical independence from CoW alone.  
- N-way automatic semantic merge of arbitrary machine state (world-diff is a protocol agenda, not shipped Git-for-VMs).  
- Asserting ariflow-swfactory already implements this full surface on every path — **capability contract, not inventory of today’s cells.**  
- Putting the warm factory *inside* the trust boundary of the fork (build cache may sit beside; promote keys may not).

---

## 5. Open problems (SRG Act III bait)

1. **World-diff v0 schema** — what subset of FS/mem/net/GPU state is diffable, hashable, and human-reviewable at promote time?  
2. **Objective digest canonicalization** — stable hashing across interpreters, fixture order, nondeterministic clocks; epoch bump false-positives vs silent drift.  
3. **Path-integral CI UX** — how does a reviewer read `(θ̂, Δ, abstain)` instead of a green check?  
4. **Replica-aware schedulers** — refuse to bill N CoW siblings as N independent samples when `ℒ` overlaps (API hook + reduce policy).  
5. **Promote-once enforcement** — cryptographic or control-plane fencing so escaped workers cannot mint a second tip.  
6. **Cross-oracle composition** — sim→HIL and compute→wet-lab ladders: when does promote of a cheap epoch become `S0` of a scarce epoch without authority leak?  
7. **API vs sociology** — paper/grant/clinic promote remains partly human process; runtime must still make the *bit* singular and auditable.

---

## 6. Spoken lines (SRG-safe)

- “The paper this talk contributes is not another sandbox microbenchmark — it is the **capability contract**: fork, reduce, promote, with objective digests as epoch bumps.”  
- “Path-integral CI means merge consumes a reduced measure over worlds, not a badge from one dirty machine.”  
- “World-diff is how parallel worlds argue; promote is world-selection.”  
- “Same fabric for software, RL, sim, bio, and HIL — different oracles, one Search≠Authority spine.”  
- “We are naming the hill-climb runtime. We are not claiming every factory path already has N-way fork.”

---

## 7. Deck placement

- One slide: **API surface** (`fork` / `reduce` / `promote` + `Objective.digest` → Epoch).  
- One slide: **invariants** (Search≠Authority, immutable S0, one promote bit, burn).  
- One slide: **cross-domain table** (isomorphism, not six keynotes).  
- Point to B for Z/β/Δ algebra; to D for auto-research promote-to-claim sociology vs runtime bit.
