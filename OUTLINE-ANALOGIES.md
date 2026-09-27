# Outline analogies — Cambridge SRG · cam-talk-london-26

**Claim fence:** analogy **illuminates**, does not prove. Physics = schedule/algebra lens. **No Gibbs-of-nature. No second-law-for-CI. No Everett MWI as proof.**

**Domains (every beat gets all five):**
1. **SW eng** — existing engineering / software practice  
2. **CS theory** — SW theory or CS theory  
3. **Biology**  
4. **Physics** — schedule/algebra lens only  
5. **Deep learning (DL)**

**Legend:** one talk-useful one-liner per domain. Primary on stage = first bold tip in OUTLINE.md; full set lives here.

---

## Act 0 — Hook

| Domain | Analogy |
|---|---|
| **SW eng** | `fork(2)` / process clone — Docker made *apps* portable; forkable sandboxes make *agent trajectories* portable. |
| **CS theory** | Fork-join / process algebra — cheap spawn of isolated worlds that share a causal past. |
| **Biology** | Binary fission / clonal lineage — daughters inherit ancestor state, then diverge under selection. |
| **Physics** | Branching trajectories under a shared initial slice \(S_0\) — schedule lens for “parallel worlds,” **not** Everett-as-proof. |
| **DL** | Multi-seed runs from one ckpt — same init, many trajectories; the missing piece is the *machine*, not another model. |

**Stage one-liner:** “Not another model — an OS primitive you already trust for processes.”

---

## Act I — Execution contract (six surfaces)

### Filesystem state

| Domain | Analogy |
|---|---|
| **SW eng** | Volume / ZFS / LVM snapshot — workspace as a named, restore-identical object. |
| **CS theory** | Persistent / CoW trees — a versioned state handle, not a mutable bag of files. |
| **Biology** | Cryo-checkpoint / blastocyst freeze — named developmental state you can thaw identically. |
| **Physics** | Named initial-condition slice \(S_0\) on the configuration manifold you branch from. |
| **DL** | **Checkpointing ≈ \(S_0\)** — workspace as `model.ckpt`: named, restore-identical, the object you fork from. |

### Networking + credentials

| Domain | Analogy |
|---|---|
| **SW eng** | Capability remint / short-lived tokens on spawn — no ambient `getenv` keys; child gets a *new* wire. |
| **CS theory** | Object-capability (ocap) model — authority flows via unforgeable refs, not ambient ACLs. |
| **Biology** | Tissue barrier / immune token remint — circulating access does not cross a fork boundary wholesale. |
| **Physics** | Boundary reassignment of a conserved charge — no ambient “key” survives the cut without remint (lens). |
| **DL** | Per-rollout sealed tool context / rotated API keys — secrets are not baked into the weight file. |

### Reproducibility

| Domain | Analogy |
|---|---|
| **SW eng** | Hermetic builds (Bazel-class) — named inputs → bit-identical outputs. |
| **CS theory** | Deterministic replay / same causal history ⇒ same observation. |
| **Biology** | Clonal replicate under controlled conditions — genotype + environment named ⇒ phenotype repeat. |
| **Physics** | Identical \(S_0\) under deterministic dynamics ⇒ identical trajectory (illumination, not a lab claim). |
| **DL** | Frozen weights + fixed seed — named snapshot → bit-identical restore before a run. |

### Fast cloning

| Domain | Analogy |
|---|---|
| **SW eng** | CoW `fork` / microVM snapshot clone — ms economics, not rebuild-from-Dockerfile. |
| **CS theory** | Path-copying / persistent heaps — \(O(1)\) logical clone; pay on write. |
| **Biology** | Mitotic division — shared genome until differentiation writes diverge. |
| **Physics** | Cheap replicas of a shared phase point — fan-out cost ≪ re-thermalize-from-scratch (schedule lens). |
| **DL** | **Ensemble ≈ fork fan-out** — CoW siblings over a shared past, not a cold start each time. |

### Build / test / rollout

| Domain | Analogy |
|---|---|
| **SW eng** | Canary / blue-green *beside* prod — warm staging path next to the live tip. |
| **CS theory** | Speculative execution / shadow traffic — specialist probes before the commit gate. |
| **Biology** | Stem-cell niche → tissue specialists — warm progenitors route into roles; tip stays gated. |
| **Physics** | Parallel basins / multi-channel search — specialists explore; one cool gate to the tip (schedule). |
| **DL** | **MoE ≈ fork experts** — warm factory *beside* the fork; the tip stays one gated path. |

### Recovery + observability

| Domain | Analogy |
|---|---|
| **SW eng** | WAL / receipts outlive the process — crash ≠ authority; evidence survives the machine. |
| **CS theory** | ARIES / write-ahead intent — durable record before mutable state is trusted. |
| **Biology** | Fossil / scar / epigenetic mark — evidence outlives the cell that produced it. |
| **Physics** | Irreversible recording of dissipative events — the ledger is not the living trajectory. |
| **DL** | Metrics store + ckpt survive a crashed job — live GPU ≠ proof; receipts do. |

**Act I trade-off (spoken):** isolation ladder ≈ choosing a wall untrusted shells cannot walk through — denser ≠ stronger evidence. (No five-domain table; not a contract surface.)

---

## Act II — Three factories

### Software factory

| Domain | Analogy |
|---|---|
| **SW eng** | CI matrix / parallel PR cells over shared `main` — fearless parallelism needs *own* machine. |
| **CS theory** | MapReduce / fork-join over shared input — siblings share a root; reuse ≠ confirmation. |
| **Biology** | Clonal variant screen — sibling mutants share ancestry; correlated hits ≠ independent species proof. |
| **Physics** | Replica search over a shared proposal generator \(H\) — correlated replicas, not i.i.d. draws (lens). |
| **DL** | **Batch ≈ siblings** — parallel Cells / patches as a minibatch over shared \(S_0\); sibling reuse ≠ confirmation. |

### RL post-training

| Domain | Analogy |
|---|---|
| **SW eng** | Judge / scorer service outside the sandbox — candidate cannot rewrite the rubric. |
| **CS theory** | Oracle machine / interactive proof — verifier outside the prover’s write set. |
| **Biology** | Fitness assay owned by the environment — organism does not get to edit the ruler. |
| **Physics** | External potential / measurement apparatus outside the child — \(E\) sealed outside the fork (lens). |
| **DL** | **RLHF reward model ≈ oracle outside policy** — soft temp = Epoch policy, not worker-owned β. |

### HIL

| Domain | Analogy |
|---|---|
| **SW eng** | Hardware-in-loop / staging before prod canary — expensive tip after cheap sims. |
| **CS theory** | Hierarchical / bandit search with a costly arm — cheap probes before the expensive pull. |
| **Biology** | **Phenotype screen** — a million genotype / sim forks ≠ one organism-assay (robot) hour. |
| **Physics** | Coarse cheap dynamics, then rare expensive measurement — scarcity ladder under drive (lens). |
| **DL** | Sim-to-real / domain-randomization fan-out → scarce real rollouts at the tip. |

**Loop mnemonic (spoken):** snapshot → fork N → search → reduce → promote → burn ≈ ckpt → ensemble → train → distill/pool → early-stop tip → **dropout** the runners.

---

## Act II½ — Two slides

### A — Fork ≠ independence

| Domain | Analogy |
|---|---|
| **SW eng** | Same-base CI flaky suite — shared fixture ⇒ correlated failures, not \(N\) independent greens. |
| **CS theory** | Exchangeability ≠ independence; common-cause DAG — shared ancestor induces dependence. |
| **Biology** | Founder effect / clonal interference — shared root ⇒ variance floor on diversity claims. |
| **Physics** | Replica correlation under shared initial measure — cheap branches ≠ i.i.d. samples (**not** Gibbs-of-nature). |
| **DL** | **DDP ≠ evidence independence** — shared init ⇒ variance floor; reduce needs \((\hat\theta,J,n,\mathcal{E},\mathcal{L})\), not a naked scalar. |

### B — Anneal + driven sink

| Domain | Analogy |
|---|---|
| **SW eng** | Staged rollout / feature-flag cool-down → freeze promote — schedule owned by release authority. |
| **CS theory** | Simulated annealing / Metropolis keep=accept, revert=reject — control algorithm, not a nature proof. |
| **Biology** | Developmental canalization — plasticity cools into irreversible differentiation at the tip. |
| **Physics** | SA cool schedule; **promote = absorbing sink under drive (NESS)**, not closed equilibrium — fence. |
| **DL** | **LR schedule ≈ anneal \(T\)** (Epoch digest = schedule id); **early stopping ≈ promote gate**. |

**Fence reminder:** SA / MH / SGD cousins = *schedule language*. Do not say the factory equilibrates. No second-law-for-CI.

---

## Act III — Open problems

### Fork ≠ independence

| Domain | Analogy |
|---|---|
| **SW eng** | Shared-fixture CI — default abstain when lineage collides; greens are not i.i.d. votes. |
| **CS theory** | Common-cause dependence — shared root ⇒ default abstain unless lineage is scored. |
| **Biology** | Clonal interference — correlated progeny do not multiply evidence. |
| **Physics** | Replica ρ floor under shared measure — reduce needs lineage (lens; no Gibbs claim). |
| **DL** | Same as II½ A: **DDP ≠ evidence independence** — correlated ensemble under shared root. |

### WIRE leases

| Domain | Analogy |
|---|---|
| **SW eng** | Capability remint / short-lived tokens on fork — ambient credentials are the CVE. |
| **CS theory** | ocap / Confused Deputy — authority must be re-granted; CoW’d secrets are ambient ambient. |
| **Biology** | Passport remint at tissue borders — inherited circulating keys are a leak, not a feature. |
| **Physics** | Boundary condition reset for conserved charges — fork cuts the wire; remint or abstain (lens). |
| **DL** | Tool-calling key rotation per rollout — sealed context; no ambient secret in the child. |

### Warm CoW channels

| Domain | Analogy |
|---|---|
| **SW eng** | Noisy-neighbor / shared-cache pack-by-trust — density without a trust boundary is a bus. |
| **CS theory** | Covert-channel taxonomy (timing, storage) — CoW pages as unintended shared memory. |
| **Biology** | Quorum / metabolite crosstalk between “isolated” colonies sharing a medium. |
| **Physics** | **Heat / timing side channel** — warm pages as unintended bus; pack-by-trust so density ≠ covert channel. |
| **DL** | Shared KV-cache / activation crosstalk across “isolated” serving lanes — factory-beside, not shared warm trust. |

### Sealed oracle

| Domain | Analogy |
|---|---|
| **SW eng** | External judge service — scorer digest owned by controller, not by candidate sandbox. |
| **CS theory** | Verifier outside prover write set — interactive-proof hygiene for CI grades. |
| **Biology** | Blind assay / sealed scoring plate — organism cannot rewrite the fitness ruler. |
| **Physics** | Measurement apparatus outside the system — \(E\) / grade sealed; worker never owns the thermometer. |
| **DL** | **RLHF RM / judge outside policy** (Rebound foil) — digest owned by controller. |

### Path-integral CI

| Domain | Analogy |
|---|---|
| **SW eng** | Merge consumes structured evidence — not a green badge; abstain is a first-class outcome. |
| **CS theory** | Evidence-aware reduce / lineage-weighted pool — MapReduce with an abstain bit, not majority vote. |
| **Biology** | Meta-analysis across related cohorts — pool effect sizes + heterogeneity, not raw win counts. |
| **Physics** | Path measure → reduced summary \((\hat\theta,\Delta,\mathrm{abstain})\) — \(Z_g\) diagnostic only if II½ ran; **not** Bayes evidence. |
| **DL** | **Distillation ≈ reduce** — many teacher trajectories → one student tip; structured, not naked scalar. |

### Promote-once API

| Domain | Analogy |
|---|---|
| **SW eng** | Single-writer tip / release train — compute may fan out; tip absorbs once. |
| **CS theory** | Absorbing decision / one-shot commit protocol — workers never own the stop bit. |
| **Biology** | Irreversible differentiation / canalization tip — many progenitors; one committed fate. |
| **Physics** | Absorbing sink under drive — tip ≠ equilibrium free-energy min (NESS fence). |
| **DL** | **Early stopping ≈ promote gate** — one absorbing tip; compute vs tip. |

### World-diff / β-as-Epoch

| Domain | Analogy |
|---|---|
| **SW eng** | Infra-as-code / config digest bump — schedule change is an epoch, not a worker dial. |
| **CS theory** | **Git conflict = evidence**; world-diff is that for machines. Epoch bump on digest change = hyperparam change. |
| **Biology** | Speciation / niche split recorded as evidence — conflict is signal, not noise to squash. |
| **Physics** | Thermostat / β owned by Epoch policy — **no worker thermostat**; schedule id in `Objective.digest`. |
| **DL** | Hyperparam / schedule change = new Epoch — workers train; they do not edit the LR schedule. |

### Name the contribution

| Domain | Analogy |
|---|---|
| **SW eng** | *Fork, Reduce, Promote* as a **POSIX-shaped capability contract** — named surface, not “already shipped everywhere.” |
| **CS theory** | Capability / interface contract (not an inventory of products) — what every honest factory must expose. |
| **Biology** | Bauplan / body-plan contract — conserved slots (fork / reduce / tip) across taxa of factories. |
| **Physics** | Algebra + schedule contract — knobs named; no claim nature’s Gibbs holds in CI. |
| **DL** | Training API contract (ckpt / step / eval / stop) — the runtime analogue for agent factories. |

---

## Close

| Domain | Analogy |
|---|---|
| **SW eng** | Tear down the runner pod; keep the signed artifact + receipts — machine dies, proof lives. |
| **CS theory** | Ephemeral worker / durable log — fork the process graph, not the trust root. |
| **Biology** | Apoptosis of exploration lineages — kill unused paths; keep the surviving tip + scars (receipts). |
| **Physics** | Quench unused trajectories; retain the absorbing tip + ledger — burn heat, keep the record (lens). |
| **DL** | **Dropout ≈ burn runners** — kill unused paths; keep the proof (tip + receipts). Fork the *machine*, not the *trust*. |

**Mantra (unchanged):** Burn the runner. Keep the proof. Fork the machine, not the trust.

---

## Cheat sheet — preferred stage primaries

| Beat | Primary on stage | Full set |
|---|---|---|
| Act 0 | SW eng `fork(2)` / Docker leap | → this file |
| FS state | DL checkpointing ≈ \(S_0\) | → this file |
| Net + creds | SW eng capability remint | → this file |
| Reproducibility | DL frozen weights + seed | → this file |
| Fast cloning | DL ensemble ≈ fork fan-out | → this file |
| Build/test/rollout | DL MoE ≈ fork experts | → this file |
| Recovery | SW eng WAL / receipts | → this file |
| Software factory | DL batch ≈ siblings | → this file |
| RL post-training | DL RLHF RM ≈ oracle | → this file |
| HIL | Bio phenotype screen | → this file |
| II½ A | DL DDP ≠ evidence independence | → this file |
| II½ B | DL LR schedule ≈ anneal \(T\) | → this file |
| III Fork≠indep | DL DDP ≠ indep | → this file |
| III WIRE | SW eng capability remint | → this file |
| III Warm CoW | Physics heat/timing channel | → this file |
| III Sealed oracle | DL RLHF RM outside policy | → this file |
| III Path-integral CI | DL distillation ≈ reduce | → this file |
| III Promote-once | DL early stopping ≈ promote | → this file |
| III World-diff | CS Git conflict = evidence | → this file |
| III Contribution | SW eng capability contract | → this file |
| Close | DL dropout ≈ burn runners | → this file |

---

## Twelve best (stage-ready)

1. **Checkpointing ≈ \(S_0\)** — FS as restore-identical object.  
2. **Ensemble ≈ fork fan-out** — CoW siblings, shared past.  
3. **Batch ≈ siblings** — software-factory Cells; reuse ≠ confirmation.  
4. **MoE ≈ fork experts** — warm factory beside the fork.  
5. **RLHF reward model ≈ oracle outside policy** — sealed scorer.  
6. **DDP ≠ evidence independence** — variance floor under shared root.  
7. **Distillation ≈ reduce** — path-integral CI / abstain.  
8. **LR schedule ≈ anneal \(T\)** — Epoch digest owns the cool-down.  
9. **Early stopping ≈ promote gate** — one absorbing tip.  
10. **Dropout ≈ burn runners** — Close mantra.  
11. **Capability remint ≈ WIRE leases** — no ambient keys after CoW.  
12. **Phenotype screen ≈ HIL tip** — million sims ≠ one robot hour.

---

*Analogies · 2026-09-27 (IDT) · 5 domains × every beat · illuminates ≠ proves · aligns CLAIM-FENCE + OUTLINE.*
