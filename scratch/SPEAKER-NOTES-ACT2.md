# Speaker notes — Act II + optional Act II½

**Use with:** [`../OUTLINE.md`](../OUTLINE.md) (min 15:00–34:00) · [`../CLAIM-FENCE.md`](../CLAIM-FENCE.md)  
**Sources:** STORY-SPINE · B-REDUCE-STATPHYS (Spoken Act II½) · H-ANNEALING-MCMC-SGD · ROUNDTABLE · I-NONEQUILIBRIUM-HAMILTONIAN (driven/open/NESS)

---

## Act II — Three factories, one primitive (15:00–30:00)

**Stay systems-only.** Say *reduce evidence*, not β/Z, unless you have already committed to II½.

### Loop (draw once)

```
snapshot S₀ → fork N → run searchers → reduce evidence → promote once → burn runners
```

**Spoken:**
> “Same machine primitive three times. Different nouns. Same law: search may be plural; authority is singular.”

### Software factory (~16:30)

| Slot | Noun |
|---|---|
| Searchers | Agent patches in Cells |
| Reduce | Tests + evidence digests |
| Promote | Human / Airflow gate → main |
| Burn | Sandboxes |

**Gifts (one breath each):**
- **pstack:** fearless parallelism only when each arm has its *own* verifiable machine. Swarm without fork is theater.
- **OpenClaw:** agent = searcher; sandbox = body. Without fork+rollback, trial N contaminates N+1.
- **swfactory:** Cell + epoch fencing. Worker ≠ authority. Sibling forks reusing the same gold are not independent confirmation.

### RL post-training (~19:30)

| Slot | Noun |
|---|---|
| Searchers | Rollouts / preference samples |
| Reduce | Reward / preference / uncertainty-aware pool |
| Promote | Checkpoint / policy release |
| Burn | Rollout envs |

**Spoken:**
> “Rollouts are path samples from a shared past. The reward model is the energy function — and it must not live inside the child.”

If II½ is cut, add half-line: “Softmax temperature is an Epoch policy, not a worker dial.”

**Fence:** do not say we accelerate GPU RL; do not claim GRPO is solved; cite Shepherd as related Tree-RL path algebra only (`[CITE#3]`).

### HIL (~23:00)

| Slot | Noun |
|---|---|
| Searchers | Sim / synthetic / teleop proposals |
| Reduce | Graded evidence L0–Ln |
| Promote | Human + scarce hardware slot |
| Burn | Trial cells |

**Spoken:**
> “A million sim forks are search. One robot hour is authority you burn once. Don’t bill CoW siblings as independent tips.”

**Fence:** HIL as scarcity metaphor / upstream CI tax — not HIL-SERL rewrite, not robot OS.

### Isomorphism tease (~26:30)

One slide: SW / RL / sim / bio / auto-research share `propose → isolate → measure → keep/revert → promote`.  
Depth stays on FS / net / creds / clone / recovery / reduce — not six keynotes.

**Fail day (D):** experiment and scorekeeper share a writable machine.

### Bridge out of Act II (~29:00)

**If II½ will run:**
> “Fork makes workers cheap. Next: why that still isn’t independence — and why temperature is not the child’s to set.”

**If II½ is cut:**
> “Fork makes workers cheap. It does not make them independent. If siblings share a snapshot root, the honest reduce abstains instead of pretending \(1/K\).”

---

## Act II½ — Boltzmann reduce + anneal (30:00–34:00) — OPTIONAL

**Cut first if late.** Max two slides. Physics = lens; SRG wants API teeth.

### Spoken Act II½ (from B — deliver as continuous ~90–120 s)

Fork makes workers cheap. It does **not** make them independent — shared ancestors leave a variance floor no matter how large \(K\) is.  
Self-consistency votes; we ask each child for estimate, precision, evidence IDs, and lineage.  
In the Gaussian reduce, \(\beta\) is just sample size: cold workers shout louder.  
A cold liar forges that coldness — isolation does not authenticate \(n\).  
\(Z\) and \(\Delta\) are diagnostics of the pool, not proof the lab thermalized.  
Annealing is the liquid factory: explore hot, reduce with teeth, promote once, burn the runners.  
Open problem: a reducer over the fork DAG that can abstain when correlation is unresolved.  
Physics here is an algebra systems people already need — not a claim that agent forks are nature’s Gibbs ensemble.

### H weave — schedule cousins (next ~60–90 s)

> “Annealing is the liquid factory in schedule clothes. A Cell proposal is a Metropolis move: keep or full revert — but only if the energy lives *outside* the child.  
> SGD and Langevin are the same family of knobs: step, noise, batch-as-fork, KL as regularizer — not a claim the swarm equilibrated.  
> RL temperature is exploration policy on the Epoch; the checkpoint is zero-\(T\).  
> Search≠Authority means: never let the worker set temperature or the energy function.”

### I weave — driven / open (one breath)

> “If your factory never stops proposing and sometimes promotes, it is driven. Calling that equilibrium is the wrong default — even when the dashboard looks flat.”
>
> “Hamiltonian here means generator of proposals — what the searcher wants — not closed mechanical agents. Real factory = \(H\) plus oracle forces, dissipation, measurement, and an absorbing promote sink.”

### Slide checklist

| Slide | Must show | Must not show |
|---|---|---|
| A — Fork≠indep | Variance floor in words; worker record fields; cold liar | Full Eq wall; path-integral derivation |
| B — Anneal + sink | SA/MH/SGD/RL-T table; Epoch owns \(T\)/\(E\); promote=sink | “Detailed balance holds”; Ising; invented ms |

**Cite:** `[CITE#4]` 2607.09689 on Slide A. Shepherd numbers stay with A if asked.

### Recovery if a physicist pushes Gibbs

> “We borrow the schedules and the reduce algebra — β as sample size, anneal as Epoch policy, promote as sink under drive. We are not claiming sandboxes are magnets in equilibrium.”

### Recovery if a systems person wants API only

> “Wire contract: children return structured evidence; reduce may abstain; Obj digest + anneal schedule are Epoch-pinned; promote is singular and outside the CoW body.”

---

## Timing kill-switches

| Clock | Action |
|---|---|
| <2 min left before Act III | Skip Slide B; keep B’s eight spoken lines only |
| Already late at 29:00 | Skip all of II½; use cut-bridge above |
| Q&A hungry for physics | Re-open II½ dictionary; still no Fokker–Planck |

---

*Act II notes · 2026-09-27 (IDT) · Spoken II½ from B; schedule from H; driven/open sink coordinates with I (NESS / \(H\) = proposal generator).*
