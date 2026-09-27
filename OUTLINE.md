# Timed outline — Cambridge SRG · 45 + 15

**Slot:** Thu 15 Oct 2026 · **15:00–16:00 BST** (Cambridge) · **17:00–18:00 IDT** · FW11  
**Talk:** Forkable Sandboxes: The Runtime Layer for AI Software Factories  
**Spine:** systems contract through three factories; physics = schedule/algebra lens, not Gibbs-of-nature.

**Legend:** `[SYS]` = systems-only language · `[β/Z]` = allowed physics naming (minimal latex) · `[CITE#n]` = deck five

---

## Minute map

| Min | Block | Mode |
|---|---|---|
| 0:00–3:00 | Act 0 — Hook | `[SYS]` |
| 3:00–15:00 | Act I — Execution contract | `[SYS]` (+ peer ms only) |
| 15:00–30:00 | Act II — Three factories | `[SYS]` |
| 30:00–34:00 | Act II½ — Boltzmann + anneal *(optional; cut if late)* | `[β/Z]` lean |
| 34:00–42:00 | Act III — Open problems | `[SYS]` (name β only if II½ ran) |
| 42:00–45:00 | Close | `[SYS]` |
| 45:00–60:00 | Q&A | mix |

If clock is tight: **skip II½ entirely**; keep one spoken line (“fork ≠ independence; reduce needs lineage”) inside Act II reduce column. Do **not** cut Act I surfaces or Act III open problems.

---

## Act 0 — Hook (0:00–3:00) `[SYS]`

**Analogy (SW eng):** `fork(2)` / process clone — Docker:apps :: forkable sandbox:agent trajectories. Illuminates ≠ proves.
**Slide intent:** one title + one diagram of “machine you can fork like a process.”

**Beats (≈45 s each):**
1. Autocomplete wrote code → agents *run* code.
2. Missing OS layer ≠ another model → **forkable machine**.
3. Line: *Docker made apps portable. Forkable sandboxes make agent trajectories portable.*

**Cold-open alternate (if room is science-heavy):** Science = hill-climb; agents made proposals cheap; bottleneck moved to honest isolation + honest measurement.

**Cite:** none yet.  
**Don’t:** product pitch, vendor ms, AGI.

---

## Act I — The execution contract (3:00–15:00) `[SYS]`

**Analogies (per surface, prefer DL):** checkpointing≈S₀ · capability remint≈WIRE · ensemble≈fork fan-out · MoE≈fork experts · WAL/receipts≈recovery. Illuminates ≠ proves.
**Slide intent:** six surfaces (matches published abstract) + one trade-off slide.

| Min | Surface / beat | Slide | Cite | Analogy |
|---|---|---|---|---|
| 3:00 | Frame: substrate must expose these six | Checklist | — | — |
| 4:00 | **Filesystem state** — workspace as snapshotable object | FS as object | — | **DL** checkpointing ≈ S₀ |
| 5:30 | **Networking + credentials** — brokered WIRE; no ambient keys | Lease sketch | Xu–Kaffes BACKUP verbal | **SW** capability remint on spawn |
| 7:00 | **Reproducibility** — named snapshot → identical restore | S₀ badge | — | **DL** frozen weights + seed |
| 8:00 | **Fast cloning** — CoW microVM economics, not rebuild-from-Dockerfile | CoW fan-out | `[CITE#1]` Firecracker pedigree · `[CITE#2]` DeltaBox **or** Crab **peer tables only** | **DL** ensemble ≈ fork fan-out |
| 10:00 | **Build/test/rollout** — warm factory *beside* the fork | Factory-beside | — | **DL** MoE ≈ fork experts |
| 11:30 | **Recovery + observability** — crash ≠ authority; receipts outlive machine | Receipts | — | **SW** WAL / receipts outlive process |
| 12:30 | Trade-off: container vs gVisor vs Firecracker-class | Isolation × latency × density | EscapeBench → wall (BACKUP); no vendor ms | denser ≠ stronger evidence |

**Number fence (A):** quote DeltaBox ckpt/restore / Crab ≤1.9% / Shepherd 134–143 ms **as theirs**. forkd/Tensorlake/E2B = verbal landscape only.

**Spoken anchor:** “Parallel world with a shared past; promote is world-selection.”

---

## Act II — Three factories, one primitive (15:00–30:00) `[SYS]`

**Analogies (per factory):** batch≈siblings (SW) · RLHF reward model≈oracle outside policy (RL) · phenotype screen≈HIL tip (bio). Loop mnemonic: ckpt→ensemble→distill→early-stop→**dropout** burn. Illuminates ≠ proves.
**Slide intent:** one loop diagram, then three noun-swaps, then isomorphism tease.

```
snapshot → fork N → run searchers → reduce evidence → promote once → burn runners
```

| Min | Beat | Slide | Notes | Analogy |
|---|---|---|---|---|
| 15:00 | Draw the loop once | Loop | Stay `[SYS]` — say *reduce evidence*, not \(Z\) yet | DL loop mnemonic (see header) |
| 16:30 | **Software factory** | Patches / Cells / tests → main | pstack fearless parallelism needs *own* machine | **DL** batch ≈ siblings |
| 19:30 | **RL post-training** | Rollouts / preference → checkpoint | Reward sealed outside fork (preview C); soft temp = Epoch policy — don’t say β yet unless II½ confirmed | **DL** RLHF RM ≈ oracle outside policy |
| 23:00 | **HIL** | Sim fan-out → robot hour tip | Scarcity ladder; million sim ≠ N robot hours | **bio** phenotype screen |
| 26:30 | Isomorphism one-liner | SW/RL/sim/bio/auto-research table | Depth stays on FS/net/creds/clone/recovery | — |
| 28:00 | Three gifts | pstack / OpenClaw / swfactory | Worker ≠ authority; sibling reuse ≠ confirmation | sibling reuse ≠ confirmation (correlated batch) |
| 29:00 | Bridge to II½ or III | “Fork makes workers cheap…” | If skipping II½, add: “…not independent; lineage or abstain.” | — |

**Cite:** `[CITE#3]` Shepherd when saying Tree-RL / reversible trace (related, not owned).  
**Don’t:** HIL-SERL rewrite; “we accelerate GPU RL.”

---

## Act II½ — Boltzmann reduce + anneal (30:00–34:00) `[β/Z]` lean

**Analogies:** Slide A — **DDP ≠ evidence independence** (DL); Slide B — **LR schedule ≈ anneal T**, early stopping ≈ promote gate (DL). Illuminates ≠ proves. No Gibbs-of-nature.
**Cut priority:** first thing to drop if late.  
**Slide intent:** max **two** slides — (1) fork≠indep + worker record; (2) anneal schedule / driven sink.

### Slide A — Fork ≠ independence (≈90 s) `[β/Z]`

**Analogy (DL):** DDP ≠ evidence independence — shared init ⇒ variance floor; reduce needs lineage, not naked scalar.

- Open with B Eq. (1) in words: shared ancestor ⇒ variance floor; cheap branches ≠ independent evidence.
- Worker wire: \((\hat\theta, J, n, \mathcal{E}, \mathcal{L})\) — not a naked scalar. \(\beta_k \equiv n_k\).
- Cold liar: forged high precision hijacks pool; isolation does not authenticate \(n\).
- **Cite:** `[CITE#4]` Evidence-Aware MapReduce (2607.09689).
- Self-consistency = foil (BACKUP verbal).

**Say β/Z here.** Minimal latex. No path-integral derivation.

### Slide B — Annealing family + driven sink (≈90–120 s) `[β/Z]` + `[SYS]`

**Analogy (DL):** LR schedule ≈ anneal \(T\) (Epoch digest = schedule id); early stopping ≈ promote gate; promote = absorbing tip under drive, not equilibrium.

| Cousin | One line on stage |
|---|---|
| **SA** | Explore hot → cool gates → \(T\to0\) promote → burn |
| **MH** | Cell proposal; **keep = accept**, **revert = reject**; \(E\) outside child |
| **SGD / Langevin** | Step / noise / batch-as-fork; same knobs, not equilibration |
| **RL temperature** | Softmax / KL exploration = Epoch policy; checkpoint = zero-T tip |

- **Search≠Authority on the thermostat:** worker must not own \(\beta\), \(T\), or energy \(E\).
- **Driven / open / NESS:** proposals inject entropy; oracle+reduce dissipate; **promote = absorbing sink** (irreversible work), not closed equilibrium. \(H\) = proposal generator only (I).
- Anneal / schedule id lives in `Objective.digest` → schedule change = **Epoch bump**.

**Spoken Act II½ (from B, tightened):** see [`scratch/SPEAKER-NOTES-ACT2.md`](scratch/SPEAKER-NOTES-ACT2.md).

**Don’t:** Gibbs-of-nature; detailed balance holds; \(Z_g\) = Bayes evidence; derive MH ratios / Langevin SDEs; invent thermalization times.

---

## Act III — Open systems problems (34:00–42:00) `[SYS]`

**Analogies (per problem):** DDP≠indep · capability remint · heat/timing channel · RLHF oracle · distillation≈reduce · early-stop≈promote · Git/world-diff · capability contract. Illuminates ≠ proves. See [`OUTLINE-ANALOGIES.md`](OUTLINE-ANALOGIES.md).
**Slide intent:** 6–8 problem cards; leave 2 as questions you want back.

| Min | Problem | Owner lens | Stage tip | Analogy |
|---|---|---|---|---|
| 34:00 | **Fork ≠ independence** | A+B | Default abstain on shared root | **DL** DDP ≠ evidence independence |
| 35:00 | **WIRE leases** | E | Capability remint; lit thin | **SW** capability remint on fork |
| 36:00 | **Warm CoW channels** | F | Pack-by-trust; factory-beside | **physics** heat/timing side channel |
| 37:00 | **Sealed oracle** | C | `[CITE#5]` Rebound *or* SWE-bench pedigree | **DL** RLHF RM ≈ oracle outside policy |
| 38:00 | **Path-integral CI** | B+G | Merge = \((\hat\theta,\Delta,\mathrm{abstain})\), not green badge — say \(Z\) only if II½ ran | **DL** distillation ≈ reduce |
| 39:00 | **Promote-once API** | G+D | compute vs tip; tip = sink under drive | **DL** early stopping ≈ promote gate |
| 40:00 | **World-diff / β-as-Epoch** *(pick one if short)* | G / H | Conflict=evidence; no worker thermostat | **CS** Git conflict = evidence |
| 41:00 | Name the contribution | G | *Fork, Reduce, Promote* capability contract | **SW** capability contract (POSIX-shaped) |

**Literature gaps (Q&A ammo, not slides):** evidence ρ across CoW; reducers that abstain; credential-on-fork peer hole; warm pages as channels; winner’s curse in Best-of-N.

---

## Close (42:00–45:00) `[SYS]`

**Analogy (DL):** dropout ≈ burn runners — kill unused paths; keep the proof (tip + receipts). Illuminates ≠ proves.
**Mantra:** Burn the runner. Keep the proof. Fork the machine, not the trust.

**Three questions for SRG:**
1. Right API for “forkable machine” (FS, net, GPU, display)?
2. Where may warm state live so density ≠ side channel?
3. How do you fence authority when children outlive parents?

---

## Q&A (45:00–60:00)

| Likely ask | Mode | Point to |
|---|---|---|
| “Is this statistical mechanics?” | Fence | Algebra/schedule interpretation; driven/open; not Gibbs |
| “Your fork latency?” | Number fence | Peer tables only; eng = landscape |
| “Credentials after CoW?” | `[SYS]` | WIRE leases agenda (E) |
| “Reward hacking / Rebound?” | `[SYS]` | Oracle leaves fork (C) |
| “Auto-research / AGI scientist?” | Fence | Architecture of the loop, not replaced PIs (D) |
| “Detailed balance / Hamiltonian?” | `[β/Z]` lean | Frozen Obj ≈ honesty condition; \(H\)=proposal generator; promote=absorbing sink; NESS≠equilibrium (I) |
| “β vs temperature?” | `[β/Z]` | \(\beta\equiv n\) in reduce; factory \(T\) = Epoch policy — two knobs (B+H) |

---

## When to say β / Z vs stay systems-only

| Moment | Say | Avoid |
|---|---|---|
| Acts 0–II main path | reduce, precision, lineage, promote, burn | β, Z, partition, Gibbs |
| Act II½ Slide A | β≡n, cold liar, variance floor | path-integral derivation |
| Act II½ Slide B | T schedule, MH keep/revert, promote=sink | “equilibrated,” detailed balance holds |
| Act III path-integral CI | reduced measure / abstain; \(Z_g\) diagnostic **only if II½ ran** | \(Z_g\) as green-score |
| Q&A physics flex | free energy vs energy, replica correlation | Ising / spin glass / nature’s Gibbs |

---

## Deck five — when each appears

| # | Paper | First use |
|---|---|---|
| 1 | Firecracker NSDI’20 | Act I cloning / trade-off |
| 2 | DeltaBox **or** Crab | Act I fast cloning (peer ms) |
| 3 | Shepherd | Act II Tree-RL / path algebra |
| 4 | 2607.09689 Boltzmann / Evidence-Aware MR | Act II½ only |
| 5 | SWE-bench **or** Rebound→Remedy | Act III sealed oracle |

---

*Outline refined 2026-09-27 (IDT). Honor A’s peer-only number fence. Physics from B+H; driven/open/NESS from I; schedules from H; reduce from B. Analogies: [`OUTLINE-ANALOGIES.md`](OUTLINE-ANALOGIES.md) — illuminate ≠ prove; no Gibbs-of-nature.*
