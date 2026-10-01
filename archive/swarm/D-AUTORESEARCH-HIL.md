# Researcher D — Auto-research / HIL / Universal hillclimb
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** AIDE² 2609.26457 · RRSI 2609.24972 · AI Scientist (+v2) · GEAR 2605.13874 · Darwin Gödel Machine 2505.22954 · AutoResearchClaw 2605.20025 · scarcity ladder / HIL as tip  
**Companion reads:** `UNIVERSAL-HILLCLIMB.md`, `STORY-SPINE.md`, `PAPERS-AND-SOURCES.md` §D, `PARALLEL-WORLDS-STATPHYS.md`  
**Claim fence (non-negotiable):** the *architecture* of auto-research is the loop `propose → isolate → measure → keep/revert → promote` — **NOT** replaced PIs, wet-lab AGI, or “solved science.” Systems punchline: keep/revert and promote must be honest at scale; hypothesis generation is the cheap side.

---

## 1. Isomorphism slide claims (one slide max — Act II enrichment)

Same loop; different proposal / oracle / scarce tip. Depth stays on FS/net/creds/clone/recovery/reduce — this table is the *frame*, not a biology keynote.

| Domain | Proposal Δ | Isolate (fork body) | Measure (oracle) | Keep / revert | Promote tip (scarce & singular) |
|---|---|---|---|---|---|
| **Auto software** | agent patch / Cell | sandbox / worktree | tests, types, eval harness | merge gate | merge to `main` |
| **RL post-training** | rollout / preference sample | rollout env | reward model, win-rate, KL | checkpoint gate | policy checkpoint release |
| **Simulation science** | mesh / timestep / constitutive param | sim cell | residual, conservation, validation suite | publishable-run gate | “publishable run” |
| **Computational biology** | sequence / docking / pipeline knobs | compute campaign | binding score → wet assay | assay booking gate | wet lab / animal / clinic hour |
| **HIL / Physical AI** | controller candidate from sim | sim / synthetic / teleop cell | sim metrics → human + arm | scarce hardware slot | **robot hour** (ladder tip) |
| **Auto research** | hypothesis + experiment script (+ harness rewrite) | disposable experiment sandbox | pre-registered metric + reproduction | claim gate | **paper / grant / Nature tip** |

**Spoken:** “Biology doesn’t need a different sandbox story. It needs a more expensive oracle and a stricter tip. HIL is the extreme of the same ladder: burn a million sim forks before you spend the arm.”

**Law carried from UNIVERSAL-HILLCLIMB:** Search may be stochastic. The objective digest, the parent snapshot id, and the promote bit may not.

---

## 2. Harness RSI vs claim-promote sociology (the fork in the road)

Two loops get conflated in auto-research discourse. SRG should keep them **architecturally separate**.

### 2.1 Loop H — Harness RSI (systems-amenable)

**Object of optimization:** the *harness* around a frozen backbone (prompts, control flow, tools, memory, search policy) — **not** the scientific claim, **not** the wet assay, **not** the paper.

| System | What it hill-climbs | Keep/revert mechanism | What stays frozen |
|---|---|---|---|
| **AIDE²** (2609.26457) | Inner research agent’s code under outer meta-rewrite | Private grade \(g(a)\) on held-out; keep only if \(g\) rises; fixed \$ budget | Backbone models per loop; selection tasks’ private splits |
| **RRSI** (2609.24972) | Component-wise harness edits | Annealed edit budget + critic/pruner; noise floor \(\delta\); cost–gain Ridge-style rule | Backbone weights; evolve-set ≠ OOD eval |
| **Darwin Gödel Machine** (2505.22954) | Agent codebase (tools, workflows) | Empirical benchmark accept into archive; open-ended parent sampling | FM weights; sandbox + human oversight |
| **GEAR** (2605.13874) | Training-script elites + (Evolve) search controller | Population frontier promote/discard vs single incumbent | Training env, 5-min GPU budget, evaluator |

**Systems reading:** this is outer-loop hillclimb on the *search policy / agent Hamiltonian* (PARALLEL-WORLDS §5). It still needs: disposable forks, frozen eval contract, singular promote of the *harness checkpoint*, burn of runners. AIDE²’s \(r^{\mathrm{pub}}\) vs \(r^{\mathrm{priv}}\) split is Search≠Authority for RSI. RRSI’s regularizers are Search≠Authority *for harness evolution* — constrain proposal cardinality and selection so evolve-set fit does not mint a permanent control plane.

**Claim-safe cite use:** BACKUP / speaker-notes for Act II isomorphism + Act III “accept boundary.” Do **not** put “first evidence of RSI” as a solved SRG claim — med–high overclaim risk (PAPERS §2 #11–12).

### 2.2 Loop C — Claim / paper / grant promote (sociology + process)

**Object of promotion:** a scientific *claim* (or paper, grant, clinic tip) that will be treated as authority outside the factory.

| System | What it produces | Tip that is scarce | Systems gap |
|---|---|---|---|
| **AI Scientist / v2** | Ideate → experiment → paper | Workshop/Nature-class publication | Pipeline ≠ honest keep/revert; overclaim risk high (PAPERS #10) |
| **AutoResearchClaw** | End-to-end research + 7 HITL modes | Human gate at high-leverage decision points | Positions as *amplifier* not PI replacement — cite for HITL tip design |
| Manual science | Lab notebook → peer review | PI / journal / IRB | Tip is social; runtime can only make the *bit* auditable |

**G’s question answered (systems only):** yes — runtime should expose a **two-phase promote**:

1. **Compute Epoch promote** — accept harness rewrite / experiment artifact into the archive under frozen `obj_digest` (AIDE² keep, RRSI admit, DGM archive add, GEAR frontier slot). This is fully in the factory API.  
2. **Scarce-tip Epoch promote** — paper claim / grant / wet booking / robot hour. Same fence shape (singular, auditable, no worker credentials), but the *decision* is sociology + process. Runtime owns the bit and the evidence digest; humans (or IRB/clinic policy) own the tip spend.

**Do not say:** auto-research has replaced PIs. **Do say:** AutoResearchClaw-class HITL is the tip design pattern — CoPilot at high-leverage gates beats Full-Auto *and* Step-by-Step (their ablation); that is Search≠Authority with a human as the scarce tip.

### 2.3 Where they couple (and must not leak)

| Coupling | Safe pattern | Failure |
|---|---|---|
| Harness rewrite uses same machine as claim draft | Separate sandboxes; harness promote ≠ claim promote | Experiment and scorekeeper share writable FS → theater |
| Outer RSI grade \(g(a)\) | Held-out private; fixed budget | Optimize public proxy → reward hacking (AIDE² measures decline along lineage — cite as emergent, not solved alignment) |
| Objective digest change mid-run | **Epoch bump** (authority act; B’s β / G’s Obj) | Child edits metric script → Rebound-class oracle capture |
| Population / archive (GEAR, DGM) | Many elites = search diversity; one promote bit | Twenty control planes if every elite can publish |

**Punch for Yossi:** *The systems problem of auto-research is not generating hypotheses — it’s making keep/revert and promote honest at scale.* Harness RSI is the amenable half; claim-promote is where the tip stays scarce on purpose.

---

## 3. Paper digest → loop slots (BACKUP cites)

### AIDE² — recursive self-improvement of research agents (2609.26457)
- **Bi-level:** inner = optimize code vs measurable objective; outer = rewrite the inner agent; keep if private \(g(a)\) improves.  
- **8-day / 100-node run:** 7 accepted rewrites (search policy → bandit+fork; context compression; robustness).  
- **Transfer:** ALE / MLE / FML / WeatherBench-2 (OOD physics) match or beat human-engineered `AIDE_human`.  
- **Systems gold:** fixed eval budget; pub≠priv signal; ignition test inconclusive (noise compounds across loops) — reinforces “promote under noise” as open.  
- **Fence:** harness RSI evidence with caveats; not “AGI scientist.”

### RRSI — Regularized Recursive Self-Improvement (2609.24972)
- **Problem:** unregularized harness RSI overfits evolve set; OOD gains vanish.  
- **Proposal side:** annealed edit budget (\(L_0\)-style); evidence-aware credit; structured exploration on stall.  
- **Selection side:** leakage critic; noise floor \(\delta\); cost–gain rule; structural prune.  
- **Numbers (theirs):** up to +14.1 ID / +4.7 OOD; ~30% fewer policy tokens vs unregularized.  
- **Systems gold:** regularization = Search≠Authority for RSI; critic is a pre-eval gate (C-adjacent).

### AI Scientist / v2 (2408.06292 → Nature 2026)
- Factory metaphor: ideate→experiment→paper.  
- **Use:** promote-to-claim is the scarce tip.  
- **Fence:** high overclaim risk on stage; BACKUP only; never “solved science.”

### GEAR — Genetic AutoResearch (2605.13874)
- Replaces single-incumbent AutoResearch hillclimb with population frontier (mutation + crossover).  
- **Maps to:** pstack local hillclimb vs swarm multi-path (PARALLEL-WORLDS).  
- GEAR-Evolve mutates the *controller* — outer loop on search policy (same family as AIDE²/DGM).

### Darwin Gödel Machine (2505.22954)
- Archive of self-modifying coding agents; empirical keep (not proofs); open-ended parent sampling.  
- SWE-bench 20%→50%, Polyglot 14.2%→30.7% (authors’).  
- **Systems gold:** archive = stepping stones; sandbox + oversight; open-ended exploration ≠ always branch from best (beats greedy ablation).  
- **Fence:** self-improving *coding agents*, not wet-lab AGI; safety section = sandboxing, not a product claim.

### AutoResearchClaw (2605.20025) — HIL tip design
- Pivot/Refine; verifiable registry; 7 HITL modes; CoPilot ≫ Full-Auto and Step-by-Step on accept rate.  
- **Positioning they claim (reuse):** research *amplifier*, not PI replacement — aligns our fence.  
- **HIL lesson for talk:** tip placement > tip volume; SmartPause ≈ uncertainty-gated promote to human.

---

## 4. Scarcity ladder (HIL as tip — Act III #5)

```
cheap & plural                          scarce & singular
─────────────────────────────────────────────────────────
patches / rollouts / sim cells          merge / checkpoint / robot hour
harness RSI candidates                  harness checkpoint promote
experiment forks / paper drafts         claim / grant / clinic tip
forked sandbox                          controller acceptance
     SEARCH  ─────────────────────────►  AUTHORITY
```

- Million compiles (or rollouts, or sim forks) = search.  
- One robot hour (or one merge, or one wet assay, or one Nature tip) = authority you can burn.  
- Forkable sandboxes make the left column real. They must **not** become the right column.  
- Auto-research fails the day the experiment and the scorekeeper share a writable machine.

---

## 5. Open problems (systems — for Act III / Q&A)

1. **Two-phase promote API** — name compute-Epoch vs scarce-tip-Epoch explicitly (answer to G); avoid collapsing paper/grant into `promote(best_of_N)`.  
2. **Objective digest as epoch bump** — changing metric / β / held-out split must invalidate in-flight children (hand to B + G).  
3. **Harness RSI under fork ρ** — AIDE²/RRSI/DGM fan candidates; CoW siblings sharing weights/prompts are not independent confirmations (B Eq. 1). Need lineage-aware reduce before outer keep.  
4. **Oracle outside the body** — Rebound/SpecBench: agents rewrite evaluators; AIDE² pub/priv helps but does not authenticate \(n_k\) (C).  
5. **Noise across bi-level loops** — AIDE² ignition inconclusive; false accept derails outer incumbent — statistical keep gates (SGM-class) as open.  
6. **HITL tip scheduling** — when does SmartPause / CoPilot fire as promote-to-human vs Full-Auto; systems contract for human leases (not vibes).  
7. **Cross-oracle ladders** — sim→HIL, compute→wet: promote of cheap epoch becomes \(S_0\) of scarce epoch without credential leak (G open #6).  
8. **Population ≠ authority** — GEAR/DGM archives are search state; singular promote bit remains one.

---

## 6. Challenges to A / B / G

### → A (Fork / CoW / shared fabric)
1. **Harness RSI needs nested fork semantics.** Outer rewrite of agent code must fork a *fresh* body that cannot see sibling eval artifacts or parent publish keys. Does your fabric expose `fork(epoch, obj_digest)` so children inherit immutable `(S₀, Epoch, Obj)` and cannot CoW-dirty the metric script?  
2. **Archive / population fan-out (DGM, GEAR) ≠ independent evidence.** Warm-parent CoW for N harness candidates will share pages/prompts — B’s ρ floor applies. Can snapshot lineage \(\mathcal{L}\) distinguish “same harness parent” from “same eval gold” so reduce can abstain?  
3. **Side-effect honesty for claim tips.** Paper upload, grant portal, wet-lab booking are Shepherd-*irreversible*. Fabric must refuse to put those capabilities inside the forked worker — even if FS+mem C/R is perfect.

### → B (Reduce / StatPhys / objective digests)
1. **Objective digest change = epoch bump — confirm wire.** When AIDE²-style private grade or RRSI evolve-set changes, is that a new `Obj` → hard reject of in-flight \((P,q)\) merges, or a soft β anneal? D needs: **hard epoch bump**; soft anneal only inside a declared Epoch.  
2. **Outer-loop keep is a reduce, not best-of-N.** AIDE² `arg max g(a)` and DGM archive adds should consume a *reduced posterior* over noisy eval seeds (structured \(r_k\)), not a naked scalar — else cold-liar harnesses mint incumbents. Will your worker contract wrap harness grades the same as SWE scores?  
3. **Population archives as correlated ensembles.** GEAR elites / DGM tree share ancestry — treat as replicas with \(\mathcal{L}\) overlap, not \(K\) i.i.d. samples when voting for promote-to-claim.

### → G (Factory API / promote-once)
1. **Answer your Q with a named split:** `Promote.compute(Epoch, Evidence)` vs `Promote.tip(Epoch, TipKind, Evidence)` — tip ∈ {merge, checkpoint, robot_hour, wet_slot, paper_claim}. Same fence; different scarcity. API must make tip kind first-class so auto-research cannot smuggle claim-promote through compute-promote.  
2. **Harness RSI as first-class factory mode.** Outer loop should be `World.fork` of *agent codebases* under frozen `Obj=g(·)`, not ad-hoc scripts. Cell/epoch must fence “editing the searcher” separately from “editing the subject.”  
3. **HITL tip as capability lease.** AutoResearchClaw CoPilot gates ≈ human holding the tip lease. API: `lease.tip(human_id, stages, ttl)` — workers never hold paper/clinic credentials; SmartPause returns evidence + uncertainty to the lease holder.

---

## 7. Deck placement & spoken lines

**Deck:** one isomorphism slide (table §1); speaker-notes for AIDE²/RRSI/GEAR/DGM; HITL as Act III tip line; no AGI-scientist pitch.

**Spoken (SRG-safe):**
1. “Hill-climbing is not a coding trick. It’s the shape of every closed-loop improvement system.”  
2. “AIDE² and RRSI hill-climb the *harness*. Publishing the paper is a different tip — same fence, scarcer burn.”  
3. “GEAR keeps a frontier; DGM keeps an archive — both are search. Authority is still promote-once.”  
4. “Auto-research fails the day the experiment and the scorekeeper share a writable machine.”  
5. “HIL is not a robotics digression — it’s the scarcity ladder with the tip on fire.”  
6. “CoPilot beats Full-Auto and Step-by-Step: tip placement beats tip volume.”  
7. “We are not replacing PIs. We are making keep/revert and promote honest so PIs spend the tip once.”

---

## 8. Do-not-say list

- ❌ Replaced Principal Investigators / wet-lab AGI / “science is solved.”  
- ❌ AIDE² “first RSI” as uncontested fact on a MAIN slide.  
- ❌ AI Scientist Nature result as proof of end-to-end scientific autonomy.  
- ❌ OpenClaw drives actuators; IB is a robot OS; we rewrote HIL-SERL.  
- ❌ Fork guarantees statistical independence of auto-research runs.  
- ❌ Every swfactory path already launches N candidate sandboxes per issue.  
- ❌ Claiming Shepherd / DeltaBox / AIDE² / GEAR / DGM as prior work you own.

---

*Researcher D pass · 2026-09-27 17:13 IDT (Asia/Jerusalem) · sources: arXiv 2609.26457, 2609.24972, 2605.13874, 2505.22954, 2605.20025, 2408.06292 + UNIVERSAL-HILLCLIMB / STORY-SPINE claim fence.*
