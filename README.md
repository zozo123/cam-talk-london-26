## Canonical academic stage deck

The repository now carries **two reproducible stage cuts**:

- [talk.tex](talk.tex) + [academic/](academic/) — **canonical full academic deck**: 38 slides total, 34 core + 4 optional/deep slides.
- [FULL-ACADEMIC.md](FULL-ACADEMIC.md) — complete academic story, six-act structure, slide map, pacing and cut strategies.
- [SPEAKER-NOTES-ACADEMIC.md](SPEAKER-NOTES-ACADEMIC.md) — teaching notes, definitions, transitions, Q&A anchors and 30/40/60-minute cuts.
- [talk-30min.tex](talk-30min.tex) + [slides/](slides/) — preserved concise 30-minute conference-style cut.
- [FINAL-DECK.md](FINAL-DECK.md) — concise-cut story and timing.
- [SPEAKER-NOTES-30MIN.md](SPEAKER-NOTES-30MIN.md) — concise-cut delivery script.
- [TOPICS.md](TOPICS.md) — complete repo-wide topic map.
- [TRAINING-ENVIRONMENTS.md](TRAINING-ENVIRONMENTS.md) — coding-RL/RLVR environment and reset thesis.
- [WORLD-MODELS-BRIDGE.md](WORLD-MODELS-BRIDGE.md) — Dreamer / Contrastive World Models ↔ executable-world bridge.
- [CLAIM-FENCE.md](CLAIM-FENCE.md) — hard DO / DO-NOT-SAY stage card.

Build locally with `make` for the full academic deck, or `make short` for the 30-minute cut. GitHub Actions builds both PDFs and uploads them as artifacts.

---

# Forkable Sandboxes: The Runtime Layer for AI Software Factories

> **FINAL TALK REPO** for Cambridge CompLab Systems Research Group · canonical stage deck + research notebook

| | |
|---|---|
| **Talk** | [Forkable Sandboxes: The Runtime Layer for AI Software Factories](https://www.talks.cam.ac.uk/talk/index/273181/) |
| **Series** | Computer Laboratory Systems Research Group Seminar |
| **When** | **Thu 15 October 2026 · 15:00–16:00 Europe/London (BST, UTC+1)** — talks.cam local Cambridge time |
| **Also** | 14:00–15:00 UTC · **17:00–18:00 IDT** (Asia/Jerusalem) · 10:00–11:00 EDT (US East) |
| **Where** | FW11 (+ Microsoft Teams) |
| **Contact** | Yaman Rawas-Kalaji |
| **Speaker** | Yossi Eliaz — Principal Engineer, Incredibuild / islo.dev · Lecturer, HIT - Holon Institute of Technology |
| **Repo status** | **Canonical full academic deck is `talk.tex` + `academic/`; concise cut is `talk-30min.tex` + `slides/`** |

**DST note:** UK falls back **25 Oct 2026**. Slot is still **BST** — never label GMT/UTC+0. Verified against talks.cam `dtstart=20261015T150000` (no `Z`). Detail: [`scratch/TIME.md`](scratch/TIME.md).

**Published abstract (faithful):** systems challenges of forkable isolated environments — filesystem state, networking/credentials, reproducibility, fast cloning, build/test, recovery, observability; architecture, trade-offs, open problems.

---

## One-sentence talk

**World models make imagination cheap. Forkable sandboxes make interaction cheap.**

For executable software worlds, a snapshot lets us branch real futures from one authenticated past; the controller keeps evidence and authority outside those disposable worlds.

Coding agents, RL post-training, and hardware-in-the-loop then share one systems contract: **Fork, Reduce, Promote.**

**Mantra:** Burn the runner. Keep the proof. Fork the machine, not the trust.

**Shared law (liquid-methodology):** Durable intent. Disposable execution. Singular authority. Deterministic convergence.  
Create entropy where exploration pays; destroy entropy before promotion.

---

## Panel consensus (from 7 researchers + H schedule)

Locked claims from swarm A–G ([`swarm/ROUNDTABLE.md`](swarm/ROUNDTABLE.md) · [`swarm/`](swarm/)). H (anneal/MCMC/SGD) and upcoming I (non-equilibrium / Hamiltonian) deepen the dynamics fence — not extra stage claims:

1. **A — Fork ≠ independence.** Peer CoW fork is *execution* independence (DeltaBox / Crab / Shepherd ms only, attributed). Shared snapshot root ⇒ unresolved ρ; reduce must not bill \(K\) siblings as i.i.d.
2. **B — Worker contract + abstain.** Wire \(r_k=(\hat\theta,J,n,\mathcal{E},\mathcal{L},m)\); \(\beta_k\equiv n_k\). Unresolved ρ / digest mismatch / cold-liar → `verdict=abstain`. Physics = algebra with teeth, **not** Gibbs-of-nature.
3. **C — Oracle leaves the fork.** Rebound→Remedy / SpecBench: sealed controller digests; RUN≠EVAL; Firecracker-class outer wall for untrusted bodies. Child scores = evidence, never authority.
4. **D — Same loop, scarce tips.** `propose→isolate→measure→keep/revert→promote` across SW/RL/sim/bio/HIL. Two-phase promote: `Promote.compute` vs `Promote.tip`. Metric edits = hard epoch bump.
5. **E — Fork copies memory; credentials must not.** WIRE = opaque leases + broker remint (`secretInheritance: reissue`). Literature thin → Act III agenda, not shipped science.
6. **F — Warmth is a wire.** Pack by trust domain, not NUMA fill; share compile heat as CAS+lease **beside** the fork; structural CoW OK inside pack, KSM/cross-tenant maps off.
7. **G — Capability contract.** Named contribution: *Fork, Reduce, Promote* — `Objective.digest` mutations are epoch bumps; path-integral CI; promote-once outside the CoW body. Not a claim every Airflow path already has N-way fork.

**H (dynamics, not an 8th slide claim):** SA / MH / Langevin–SGD / RL temperature = schedule language of the liquid factory; Cell = MH move; Epoch owns \(T\) / \(E\); workers never get the thermostat ([`swarm/H-ANNEALING-MCMC-SGD.md`](swarm/H-ANNEALING-MCMC-SGD.md)). **I:** driven / open / NESS; \(H\) = proposal generator; promote = absorbing sink ([`swarm/I-NONEQUILIBRIUM-HAMILTONIAN.md`](swarm/I-NONEQUILIBRIUM-HAMILTONIAN.md)).

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
| **Verdict** | keep / revert / abstain | Controller + gate |
| **Promote** | Merge, checkpoint, publish, book HIL slot | Singular authority |

**Law:** Search may be stochastic. The objective digest, the parent snapshot id, the β/anneal schedule, and the promote bit may not.

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

### Driven / open systems (not closed equilibrium)

The factory is a **driven, open** system: proposals and exploration budgets inject entropy; oracles and humans dissipate it; **promote is a sink** (absorbing boundary / entropy collapse), not a claim the swarm thermalized.

| Non-eq object | Systems twin |
|---|---|
| Drive / flux | Proposal stream, RL rollouts, swarm fan-out, edit budget |
| Dissipation | Oracle measurement, reduce, burn runners, KL friction |
| Sink / absorbing state | **Promote once** — merge / checkpoint / tip; irreversible work at the gate |
| \(H(q,p)\) | **Proposal generator** only — what the isolated searcher *wants* (not closed mechanics) |
| NESS at fixed Epoch \(T\) | Steady swarm fork/burn with flat dashboard ≠ thermodynamic equilibrium |
| Agent / outer Hamiltonian | Harness / search-policy loop (AIDE² · GEAR · DGM) — still under frozen Obj |

**Fence:** say *driven / open / dissipative / NESS*; \(H\) = proposal generator. Do **not** say detailed balance holds, closed Hamiltonian agents, or promote = free-energy minimum of a closed lab. Toolkit: [`swarm/I-NONEQUILIBRIUM-HAMILTONIAN.md`](swarm/I-NONEQUILIBRIUM-HAMILTONIAN.md).

### Annealing family ↔ liquid factory (same T schedule)

Four cousins, one Search≠Authority cut — **worker must not own β or energy**:

| Cousin | What it maps to in the factory | Who owns T / β / E |
|---|---|---|
| **Simulated annealing** | Epoch anneal schedule: explore hot → cool gates → \(T\to0\) promote | Controller Epoch (`obj_digest` + schedule id) |
| **MCMC / Metropolis–Hastings** | Propose Δ in a fork; **accept = keep**, **reject = full revert** (burn child) | Accept rule lives *outside* the child |
| **SGD / Langevin** | Local noisy ascent on one path (pstack one-Δ); Langevin noise ≈ harness-beating measurement noise | Step size / noise scale = harness policy, not worker whim |
| **RL temperature** | Softmax / entropy bonus / KL-to-ref as finite-T exploration; checkpoint = zero-T tip | Reward model + β schedule sealed with oracle |

Operational rhyme:

1. High \(T\) / small β → wide fan-out, diverse proposals, swarm / GEAR population.
2. Cool / raise β (or effective \(n\)) → precision-weighted reduce, fewer survivors.
3. \(T\to0\) → singular promote (merge / checkpoint / wet / paper tip).
4. Burn the measure — dispose runners; receipts outlive machines.

**Fence:** matches SGD / SA / MCMC / RL-temperature *intuition* without claiming equilibrium thermodynamics or closed-system thermalization. \(T\to0\) promote is a **sink under drive** (H + I), not an equilibration proof. Bumping the anneal / β schedule id = **hard epoch bump** (joint B↔G↔H). Workers must not “cool themselves” by inflating \(n_k\).

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
2. **Annealing / MCMC keep–revert** — liquid factory T schedule; MH accept = keep in fork, reject = burn.
3. **Free energy vs energy** — score + complexity/cost/KL (RL already lives here; temperature is exploration).
4. **Fluctuation–dissipation / noise** — harness must beat noise (median of N, frozen lever; Langevin cousin).
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

---

## Act III open problems

SRG-ready problems distilled from swarm A–G (not prophecy):

1. **Fork ≠ independence** — no peer ρ under CoW; default `abstain` on shared snapshot root until an overlap model ships; replica-aware schedulers must refuse fake \(N\).
2. **WIRE leases** — capability handles across forks (mint / attenuate / revoke / epoch); scrub+remint cost vs ms-class fork; literature thin (Xu–Kaffes names the hole).
3. **Warm CoW channels** — shared past as fault-timing / residency / write-set wire; pack-by-trust; factory-beside-fork for compile heat without sharing trust.
4. **Sealed oracle** — controller-owned digests + attestation \(a_k\); child cannot mint \((n,J)\); held-outs never in writable overlay (Rebound / SpecBench).
5. **Path-integral CI** — merge consumes reduced measure \((\hat\theta,\Delta,\mathrm{abstain})\), not a green badge; \(Z_g\) diagnostic only.
6. **Promote-once API** — `Promote.compute` vs `Promote.tip`; cryptographic / control-plane fence so escaped workers cannot mint a second tip; tip kinds ∈ {merge, checkpoint, robot_hour, wet_slot, paper_claim}. Promote = **sink** in a driven factory (not closed equilibrium).
7. **World-diff protocols** — CoW divergence merge for machine state; conflict = evidence (Git intuition, not Git coverage of GPU/mem/net).
8. **β / anneal as Epoch policy** — schedule id in `obj_digest`; workers must not own temperature or energy (Search≠Authority on the thermostat).

---

## Act structure (45 min + 15 Q&A)

Timed outline with slide intents + when to say β/Z: [`OUTLINE.md`](OUTLINE.md).  
Claim fence one-pager: [`CLAIM-FENCE.md`](CLAIM-FENCE.md).  
Act II + II½ speaker notes: [`scratch/SPEAKER-NOTES-ACT2.md`](scratch/SPEAKER-NOTES-ACT2.md).

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

**Act II½ (optional 3–4 min) — Boltzmann reduce + anneal:** fork makes workers cheap; it does **not** make them independent. Reduce must carry precision, sample size, provenance — or a cold liar hijacks the pool. T schedule = liquid factory (SA/MH/SGD/Langevin/RL-T cousins); MH keep/revert in fork; RL temperature = exploration, not worker-owned β. Factory is **driven/open** — promote is a sink, not equilibration (H; I upcoming).

### Act III — Open systems problems (8 min)

Lead with the eight problems above; leave path-integral CI + promote-once + WIRE as the questions you want back.

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
| 2 | **DeltaBox** ([2605.22781](https://arxiv.org/abs/2605.22781)) *or* **Crab** ([2604.28138](https://arxiv.org/abs/2604.28138)) | ms CoW C/R for agent search — *peer tables only* |
| 3 | **Shepherd** ([2605.10913](https://arxiv.org/abs/2605.10913)) | Meta-agent fork + Tree-RL + reversible trace |
| 4 | **Boltzmann / Evidence-Aware MapReduce** ([2607.09689](https://arxiv.org/abs/2607.09689)) | Reduce after fork; Search≠Authority; β≡n |
| 5 | **SWE-bench** *or* **Rebound→Remedy** ([2604.01476](https://arxiv.org/abs/2604.01476)) | Isolated coding oracle **or** oracle must leave the fork |

Speaker-notes only: AIDE² / RRSI / AI Scientist, OpenHands, SandboxEscapeBench, OpenRath, Xu–Kaffes ([2510.05556](https://arxiv.org/abs/2510.05556)), SaMOSA / RialTo, SpecBench.

Full curated biblio: [`scratch/PAPERS-AND-SOURCES.md`](scratch/PAPERS-AND-SOURCES.md).

**Number fence (A):** on-slide latencies only from peer tables (DeltaBox T2–4, Crab ≤1.9%, Shepherd T3). Eng (forkd / Tensorlake / E2B) = verbal landscape. Never invent ms.

---

## Differentiation vs other October talks

| Talk | Room | One idea they keep |
|---|---|---|
| **Cambridge SRG Oct 15** | Systems | Forkable machine as runtime; Search≠Authority; path/reduce |
| **RustChinaConf Oct 17** | Rust/CI | Million compiles / one robot hour; warm Cargo factory |
| **Zenity NYC Oct 21** | Security | Four doors; acceptance boundary; Door 4 |

Same universe. Different punchline. No reused 15-minute script.

---

## Spoken lines (≤10)

1. “Hill-climbing is not a coding trick. It’s the shape of every closed-loop improvement system.”
2. “Docker made apps portable. Forkable sandboxes make agent trajectories portable.”
3. “A fork is a parallel world with a shared past. A promote is world-selection.”
4. “Fork makes workers cheap. It does **not** make them independent.”
5. “β is not mystic — in the Gaussian reduce it’s the sample size. Cold workers shout louder.”
6. “Annealing is the liquid factory: explore hot, reduce with teeth, promote as sink, burn the runners — driven, not equilibrated.”
7. “Metropolis keep/revert in a fork; the accept rule lives outside the child — Search≠Authority on the thermostat.”
8. “Statistical physics gave us the *reduce*. Systems still owe us the *fork* and the *fence*.”
9. “Auto-research fails the day the experiment and the scorekeeper share a writable machine.”
10. “Path-integral CI means merge consumes a reduced measure over worlds, not a badge from one dirty machine.”

---

## Claim fence (hard)

**Say:** substrate for agentic software + RL-style fan-out; HIL as scarcity metaphor / upstream CI tax; physics as interpretation with teeth (anneal / MCMC / SGD / RL-T as *cousins*; factory = driven/open, promote = sink); related systems (Shepherd / DeltaBox / Crab) as cousins, not owned prior work; capability contract, not shipped N-way everywhere.

**Don’t say:** we accelerate GPU RL training; OpenClaw drives actuators; we rewrote HIL-SERL; IB is a robot OS; fork guarantees statistical independence; every swfactory path already has native N-way fork-merge; vendor latencies as our benchmarks; AGI scientist / wet-lab replacement; agent forks are literal Gibbs ensembles of nature; detailed balance / closed equilibrium holds in the factory; promote is an equilibrium free-energy minimum; workers may own β / energy / anneal schedule; \(Z_g\) is Bayesian model evidence.

Full stage card: [`CLAIM-FENCE.md`](CLAIM-FENCE.md).

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
OUTLINE.md                         ← timed 45+15 speaker outline
CLAIM-FENCE.md                     ← stage do/don’t one-pager
scratch/
  TIME.md                          ← slot verification
  STORY-SPINE.md                   ← locked acts + claim fence
  UNIVERSAL-HILLCLIMB.md           ← isomorphism depth
  PARALLEL-WORLDS-STATPHYS.md      ← path integrals / β / Tensorlake
  SPEAKER-NOTES-ACT2.md            ← Act II + II½ (Boltzmann + anneal)
  PAPERS-AND-SOURCES.md            ← Top 15 + clusters A–F + deck five
swarm/                             ← panel A–I + ROUNDTABLE
```

**Still to build:** architecture diagram (S₀→fork→reduce→promote), optional recorded fork demo (not live dependency), deck.

---

*Scratch pad seeded 2026-09-27; deep refinement 2026-09-27 (IDT). Prefer primary arXiv/USENIX over tertiary SEO. Refresh HF trending weekly before 15 Oct.*
