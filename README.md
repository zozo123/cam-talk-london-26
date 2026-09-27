# Forkable Sandboxes: The Runtime Layer for AI Software Factories

> **SCRATCH PAD** for Cambridge CompLab Systems Research Group · not the final deck · living speaker notebook

| | |
|---|---|
| **Talk** | [Forkable Sandboxes: The Runtime Layer for AI Software Factories](https://www.talks.cam.ac.uk/talk/index/273181/) |
| **Series** | Computer Laboratory Systems Research Group Seminar |
| **When** | Thu 15 October 2026 · 15:00–16:00 (Asia/Jerusalem label: IDT+… check local) |
| **Where** | FW11 (+ Teams) |
| **Contact** | Yaman Rawas-Kalaji |
| **Speaker** | Yossi Eliaz |
| **Repo status** | Scratch pad — story, physics lens, papers, claim fences |

**Published abstract (faithful):** systems challenges of forkable isolated environments — filesystem state, networking/credentials, reproducibility, fast cloning, build/test, recovery, observability; architecture, trade-offs, open problems.

---

## One-sentence talk

Coding agents, RL post-training, and hardware-in-the-loop all need the same thing: **cheap forked machines for search, and a separate authority that never lives inside those machines.**

Forkable sandboxes are that machine. Everything else is orchestration.

**Mantra:** Burn the runner. Keep the proof. Fork the machine, not the trust.

**Shared law (liquid-methodology):** Durable intent. Disposable execution. Singular authority. Deterministic convergence.  
Create entropy where exploration pays; destroy entropy before promotion.

---

## Three inspirations → one law

| Source | What it contributes | What it is *not* in this talk |
|---|---|---|
| **pstack** | Fearless parallelism: many agents, multi-model swarm, verification before trust; hillclimb discipline (one metric, one Δ, keep/revert) | Not a Cursor plugin demo; not “how to prompt” |
| **OpenClaw** | The agent *loop* (tools, sessions, sandboxed body) | Not a robotics OS; agents engineer software, they don’t drive motors |
| **ariflow-swfactory** | Control plane: Cell, epoch, Search≠Authority, Airflow lifecycle, evidence, promotion | Not a product pitch; methodology as systems contract |

---

## The scarcity ladder

```
cheap & plural                          scarce & singular
─────────────────────────────────────────────────────────
agent samples / patches                 merge to main
RL rollouts / policy candidates         checkpoint promote
sim / synthetic HIL                     real arm / human hour
forked sandbox                          controller acceptance
     SEARCH  ─────────────────────────►  AUTHORITY
```

A million compiles (or rollouts) are search.  
One robot hour (or one merge) is authority you can burn.

Forkable sandboxes make the left column economically real.  
They must not become the right column.

---

## Universal hill-climb (the isomorphism)

Forkable sandboxes are not “better VMs.” They are the **machine that makes scientific iteration cheap** for every domain that looks like:

> propose → isolate → measure → keep or revert → promote once

That loop is **hill-climbing**. Auto-software, auto-build, auto-research, biology, simulation, RL post-training, and HIL are the *same loop* with different oracles and different scarcity at the tip.

### Hillclimb discipline (pstack, generalized)

1. Own **one metric** and a stop predicate.
2. **Freeze the harness** before changing the system.
3. **Decision log** — one row per attempt.
4. **One change per attempt.** Measure. Keep or full revert.
5. Fan independent hypotheses into **separate machines** — serialize only shared state.
6. Push past plateaus; don’t relax the predicate.
7. **Promote** through a review gate.

Without fork, “revert” is a prayer. Without a frozen harness, “better” is theater. Without singular promote, the swarm becomes twenty control planes.

### Schema (must live outside the forked worker)

| Slot | Meaning | Outside worker? |
|---|---|---|
| **Objective** | What “uphill” means (objective digest) | Yes — changing it is authority |
| **State S₀** | Named snapshot / content-addressed parent | Yes — immutable parent |
| **Proposal Δ** | Patch, hyperparam, sequence, protocol, mesh | Generated in child |
| **Oracle O** | Tests, reward, assay, residual, preference | Criteria owned by controller |
| **Evidence E** | Metric, logs, digests, lineage | Retained with provenance |
| **Verdict** | keep / revert | Controller + gate |
| **Promote** | Merge, checkpoint, publish, book HIL slot | Singular authority |

**Law:** Search may be stochastic. The objective digest, the parent snapshot id, and the promote bit may not.

### One loop, many factories

```text
        ┌──────────── objective digest (authority) ────────────┐
        ▼                                                      │
   snapshot S₀ ──fork──► child₁…N ──run──► evidence Eᵢ         │
        │                     │                                 │
        │                     ▼                                 │
        │              reduce / compare (precision, lineage)    │
        │                     │                                 │
        │              keep? ──no──► burn child, log revert     │
        │                 │yes                                  │
        │                 ▼                                     │
        └────────── promote once ──► new S₀' / release ─────────┘
                         burn runners
```

| Domain | Proposal | Oracle (examples) | Scarce tip |
|---|---|---|---|
| **Auto software** | agent patch | tests, types, eval harness | merge to main |
| **Auto build / CI** | toolchain / cache policy | build time, correctness digests | protected branch |
| **RL post-training** | rollout / preference sample | reward model, win-rate, KL | policy checkpoint |
| **Simulation science** | mesh, timestep, constitutive param | residual, conservation, validation | publishable run |
| **Computational biology** | sequence, docking, pipeline knobs | binding score, wet-lab assay | wet lab / clinic |
| **HIL / Physical AI** | controller candidate from sim | sim metrics → human + arm | robot hour |
| **Auto research** | hypothesis + experiment script | pre-registered metric + reproduction | paper / grant claim |

**Biology and sim are not special cases.** Expensive oracles demand more cheap forked search before the tip — same scarcity ladder as “million compiles / one robot hour.”

### Failure modes without forkable bodies

| Failure | Symptom |
|---|---|
| Contaminated search | Trial N leaves state Trial N+1 inherits |
| Fake independence | Parallel agents share one FS → correlated “wins” |
| Unrevertability | No snapshot → hillclimb dies |
| Authority leak | Worker holds merge / wet-lab / publish keys |
| Harness drift | Metric script edited beside the subject |
| Evidence theater | Green badge without lineage; siblings cite shared gold |

Cambridge owns the **body**. Brain (model) and judge (objective) are interfaces.

---

## Parallel worlds, path integrals, statistical physics

A forkable sandbox turns one warm machine into **N parallel worlds** that share a past and diverge in the future.

| Physics | Systems |
|---|---|
| Microstate | Sandbox (FS + mem + processes) |
| Path / history | Agent or rollout trajectory in one child |
| Path integral / Σ e^{−βE} | Fan-out over forks, then **reduce** |
| Action / energy | Loss, reward cost, residual, assay score |
| β (inverse temperature) | Sample size / precision / information weight |
| Partition function Z | Normalizer of the reduce |
| Free-energy landscape | Objective landscape the hill-climb walks |
| Equilibrium / anneal | Promote — entropy collapse |
| Correlated replicas | CoW siblings sharing weights/gold — *fake N* |

**Claim fence:** thermodynamic form is an *interpretation* of precision-weighted pooling under local asymptotic normality (see [arXiv:2607.09689](https://arxiv.org/abs/2607.09689)). Do **not** claim agent forks are Gibbs ensembles of nature. Claim: **the algebra systems people need already looks like statistical mechanics**.

### Path-integral factory

```
S₀ ──fork──► world₁…N ──run──► (θ̂, n, J, lineage)
                │
                ▼
         Z = reduce(…)     ← statistical physics
                │
         promote(mode)     ← singular authority
         burn(worlds)
```

Operationally:

1. Snapshot S₀ = shared past (boundary condition).
2. Fork N children = sample paths.
3. Each child returns (estimate, precision, n, provenance) — not a naked scalar.
4. Reduce ≈ approximate the integral / pool natural parameters.
5. Promote = mode / zero-T for *authority*; keep finite-T uncertainty in *evidence*.

**Tensorlake / forkd / Mitos / Shepherd** make step 2 cheap.  
**Boltzmann MapReduce** makes step 4 honest.  
**swfactory / Airflow** make step 5 singular.  
**pstack hillclimb** = local walk on one path; **GEAR / swarm** = multi-path / population.

Without (2) you cannot sample the path measure.  
Without (4) you average liars.  
Without (5) every path becomes a control plane.

### Parallel worlds as systems API (not MWI cosplay)

- **Branch** = child after fork (`checkpoint(MEMORY)` → clone).
- **“Interference”** (dangerous) ≈ correlated workers — fake independence.
- **“Decoherence”** (useful) ≈ isolate credentials, network, evidence lineage.
- **World-selection** = promote.

Desired API shape:

```
world = sandbox.fork()
worlds = sandbox.fork(n=K)
Z = reduce(worlds, objective)
authority.promote(Z.mode)
burn(worlds)
```

### Stat-phys toolkit for the deck (pick ≤4)

1. **β = n** — colder (larger n) workers dominate; a “cold liar” hijacks unless clipped.
2. **Annealing** — liquid factory: explore hot → promote cold.
3. **Free energy vs energy** — score + complexity/cost/KL (RL already lives here).
4. **Fluctuation–dissipation / noise** — harness must beat noise (median of N, frozen lever).
5. Phase transitions / replica method — Q&A only.

### Landscape in the physics picture

| System | Role |
|---|---|
| **Tensorlake** | Durable configuration space: MicroVM worlds, memory snapshots, suspend, Git/FS field, function fan-out |
| **forkd / Mitos / crucible** | Fast propagator — cheap branching |
| **Shepherd** | Formal path algebra: typed events, fork/replay, Tree-RL |
| **HF SandboxPool** | Density vs isolation |
| **Safactory / AgentRL** | Coupled sampling + learning |
| **AIDE² / GEAR / DGM** | Outer loop on the search policy itself |
| **swfactory** | Thermostat + fence: Cell/epoch; Search≠Authority |
| **Boltzmann reduce** | Partition function for worker factors |

### Future as open problems (not prophecy)

1. Path-integral CI — merge is a reduced posterior, not a green badge.
2. World-diff protocols — CoW divergence merge; conflict = evidence.
3. Objective digests as epoch bumps.
4. Replica-aware schedulers — refuse correlated siblings as independent N.
5. One fork fabric, many oracles (SW / RL / sim / bio).
6. Physics-honest auto-research — spend scarce tips only after reduce says the free-energy drop is real.

---

## Act structure (45 min + 15 Q&A)

### Act 0 — Hook (3 min)

Autocomplete wrote code. Agents *run* code.  
The missing OS layer isn’t another model — it’s a machine you can **fork like a process**.

Line: *Docker made apps portable. Forkable sandboxes make agent trajectories portable.*

Cold-open alternate: Science has always been hill-climbing. Agents made proposals cheap. The bottleneck moved to **honest isolation and honest measurement**.

### Act I — The execution contract (12 min)

Six surfaces (matches published abstract):

1. **Filesystem state** — workspace as snapshotable object  
2. **Networking + credentials** — brokered wire; no ambient keys in the child  
3. **Reproducibility** — named snapshot → identical restore  
4. **Fast cloning** — CoW microVM economics (~ms–hundreds ms), not rebuild-from-dockerfile  
5. **Build / test / rollout execution** — warm factory *beside* the fork, not inside trust  
6. **Recovery + observability** — crash ≠ authority; receipts outlive the machine  

Trade-off SRG will love: container vs gVisor vs Firecracker-class microVM — isolation thickness vs fork latency vs density.

### Act II — Three factories, one primitive (15 min)

```
snapshot → fork N → run searchers → reduce evidence → promote once → burn runners
```

| Factory | Searchers | Reduce | Promote | Burn |
|---|---|---|---|---|
| **Software** | agent patches in Cells | tests + evidence digests | human/Airflow gate → main | sandboxes |
| **RL post-training** | rollouts / preference samples | reward / preference / uncertainty-aware pool | checkpoint / policy release | rollout envs |
| **HIL** | sim / synthetic / teleop proposals | graded evidence L0–Ln | human + scarce hardware slot | trial cells |

Enrichment: one isomorphism slide for sim / bio / auto-research — depth stays on FS/net/creds/clone/recovery/reduce.

**pstack’s gift:** fearless parallelism only works when each arm gets its *own* verifiable machine. Swarm without fork is theater.  
**OpenClaw’s gift:** agent = searcher; sandbox = body. Without fork+rollback, exploration contaminates the next trial.  
**swfactory’s gift:** Cell + epoch fencing. Worker ≠ authority. Sibling forks reusing the same evidence are not independent confirmation.

**Act II½ (optional 3–4 min) — Boltzmann reduce:** fork makes workers cheap; it does **not** make them independent. Reduce must carry precision, sample size, provenance — or a cold liar hijacks the pool.

### Act III — Open systems problems (8 min)

1. **Fork ≠ independence** — shared weights, prompts, caches, gold files  
2. **Credential leases across forks** — capability handles, not env inheritance  
3. **Warm cache vs isolation** — share compile heat without sharing trust  
4. **Acceptance boundary** — agent output = evidence; controller criteria = authority (NYC cousin, one sentence)  
5. **HIL as the extreme** — when promote costs a robot hour, burn search *before* the scarce slot  

Literature gaps (for SRG Q&A):

- Almost nobody measures *evidence* correlation across CoW siblings (papers optimize *execution* independence).
- Fork-DAG reducers rarely abstain when correlation is unresolved.
- Oracle ownership / verifier tampering (Rebound→Remedy) — Search≠Authority underspecified as a systems contract.
- Credential / identity refresh on fork — peer literature thin.
- Warm shared pages as side channels.
- Cross-domain factory isomorphism — **this talk’s named contribution**.
- Promote-once as a runtime primitive (not just sociology).
- Adaptive selection / winner’s curse in Best-of-N.

### Close (2 min)

Mantra again. Three questions for SRG:

1. What is the right API for “forkable machine” (FS, net, GPU, display)?  
2. Where should warm state live so density doesn’t become a side channel?  
3. How do you fence authority when children outlive parents?

---

## Deck max-5 citations

| # | Cite | Slide job |
|---|---|---|
| 1 | **Firecracker** (NSDI’20) | Pedigree: microVM isolation + snapshot |
| 2 | **DeltaBox** ([2605.22781](https://arxiv.org/abs/2605.22781)) *or* **Crab** ([2604.28138](https://arxiv.org/abs/2604.28138)) | ms CoW C/R for agent search |
| 3 | **Shepherd** ([2605.10913](https://arxiv.org/abs/2605.10913)) | Meta-agent fork + Tree-RL + reversible trace |
| 4 | **Boltzmann / Evidence-Aware MapReduce** ([2607.09689](https://arxiv.org/abs/2607.09689)) | Reduce after fork; Search≠Authority |
| 5 | **SWE-bench** *or* **Rebound→Remedy** ([2604.01476](https://arxiv.org/abs/2604.01476)) | Isolated coding oracle **or** oracle must leave the fork |

Speaker-notes only: AIDE² / RRSI / AI Scientist, OpenHands, SandboxEscapeBench, OpenRath, Xu–Kaffes ([2510.05556](https://arxiv.org/abs/2510.05556)), SaMOSA / RialTo.

Full curated biblio: [`scratch/PAPERS-AND-SOURCES.md`](scratch/PAPERS-AND-SOURCES.md).

---

## Differentiation vs other October talks

| Talk | Room | One idea they keep |
|---|---|---|
| **Cambridge SRG Oct 15** | Systems | Forkable machine as runtime; Search≠Authority; path/reduce |
| **RustChinaConf Oct 17** | Rust/CI | Million compiles / one robot hour; warm Cargo factory |
| **Zenity NYC Oct 21** | Security | Four doors; acceptance boundary; Door 4 |

Same universe. Different punchline. No reused 15-minute script.

---

## Spoken lines

- “Hill-climbing is not a coding trick. It’s the shape of every closed-loop improvement system.”
- “OpenClaw is the searcher. The sandbox is the body. Airflow is the spine. Promotion is the brain stem — singular.”
- “A fork is a parallel world with a shared past. A promote is world-selection.”
- “Path integrals taught us to sum over histories. Agent factories finally have a machine that can *sample* them.”
- “β is not mystic — in the Gaussian reduce it’s the sample size. Cold workers shout louder.”
- “Statistical physics gave us the *reduce*. Systems still owe us the *fork* and the *fence*.”
- “Tensorlake and friends make worlds cheap. The open problem is making the partition function trustworthy.”
- “Auto-research fails the day the experiment and the scorekeeper share a writable machine.”
- “Biology doesn’t need a different sandbox story. It needs a more expensive oracle and a stricter tip.”

---

## Claim fence (hard)

**Say:** substrate for agentic software + RL-style fan-out; HIL as scarcity metaphor / upstream CI tax; physics as interpretation with teeth; related systems (Shepherd / DeltaBox / Crab) as cousins, not owned prior work.

**Don’t say:** we accelerate GPU RL training; OpenClaw drives actuators; we rewrote HIL-SERL; IB is a robot OS; fork guarantees statistical independence; every swfactory path already has native N-way fork-merge; vendor latencies as our benchmarks; AGI scientist / wet-lab replacement; agent forks are literal Gibbs ensembles of nature.

Cite liquid-methodology honestly: forkable sandboxes are a **capability contract**, not a claim that the default executor already launches N candidate sandboxes per issue.

---

## Yossi public artifacts (related)

| Artifact | URL |
|---|---|
| Evidence-Aware MapReduce | https://arxiv.org/abs/2607.09689 |
| boltzmann-mapreduce | https://github.com/zozo123/boltzmann-mapreduce |
| The Sandbox Shift (field manual) | https://zozo123.github.io/sandboxes-why-how-when/ |
| islo.dev sandboxes | https://islo.dev/sandboxes/ |
| Personal site | https://zozo123.github.io/ |

---

## Repo layout (scratch pad)

```
README.md                          ← you are here (all story lines)
scratch/
  STORY-SPINE.md                   ← locked acts + claim fence
  UNIVERSAL-HILLCLIMB.md           ← isomorphism depth
  PARALLEL-WORLDS-STATPHYS.md      ← path integrals / β / Tensorlake
  PAPERS-AND-SOURCES.md            ← Top 15 + clusters A–F + deck five
```

**Still to build:** timed speaker outline, architecture diagram (S₀→fork→reduce→promote), optional recorded fork demo (not live dependency), deck.

---

*Scratch pad seeded 2026-09-27. Prefer primary arXiv/USENIX over tertiary SEO. Refresh HF trending weekly before 15 Oct.*
