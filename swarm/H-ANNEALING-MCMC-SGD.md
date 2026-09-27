# Researcher H — Annealing / MCMC / SGD / Stochastic Simulation
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Lens:** schedule language that systems already speak — SA, MH, Langevin/SGD, MC particle, RL rollouts — mapped onto software factories & Tree-RL  
**Companion reads:** B’s `B-REDUCE-STATPHYS.md` (§4 annealing↔liquid factory; β≡n from [2607.09689](https://arxiv.org/abs/2607.09689)), G’s `G-FACTORY-API.md` (Epoch / Objective.digest / Search≠Authority), `PARALLEL-WORLDS-STATPHYS.md`, `UNIVERSAL-HILLCLIMB.md`, C on RL escape, A on Shepherd Tree-RL  
**Inspiration (methodology, not peer review):** ariflow-swfactory Cell/epoch; liquid-methodology entropy create/destroy; pstack one-Δ hillclimb

---

## Claim fence (non-negotiable)

| Say | Do not say |
|---|---|
| Physics / MC is the **algebra and schedule language** for hill-climb systems: propose, accept/reject, cool, promote. | Agent populations *are* Ising / spin glasses / Gibbs ensembles of nature. |
| Simulated annealing, MH, Langevin, SGD, and RL temperature are **useful duals** of factory epochs and fork fan-out. | Equilibrium thermodynamics already holds for sandboxes; detailed balance is “proven” in production. |
| β from 2607.09689v3 is **sample size / information weight** (\(β_k=n_k\)); factory \(T\) is a **policy knob** owned by Epoch. | Workers may mint their own temperature, energy function, or \(n_k\) to “cool themselves.” |
| Tree-RL / Shepherd branching ≈ **branching MCMC on traces** (path algebra), not a free-energy theorem. | We derived a partition function of the lab that decides merges. |
| Search≠Authority = **don’t let the worker set \(T\) or \(E\)**. | swfactory already ships full MH+anneal on every Airflow path. |

**One sentence for SRG:** *We borrow the *schedules* of annealing and MCMC — not a claim that agents equilibrate like magnets.*

---

## 1. Why this lens (between B’s reduce and G’s API)

B owns the **algebra**: \(β≡n\), \(Z_g\), \(Δ\), cold liar, precision-weighted pool.  
G owns the **capability contract**: `fork` / `reduce` / `promote`, `Objective.digest` → Epoch bump, Search≠Authority.  
**H owns the dynamics:** how proposals are generated, accepted, cooled, and burned — the *path-sampling schedule* that makes liquid factories look like SA/MH/SGD without cosplay.

Without H, “annealing” is a metaphor slide. With H, SRG hears: *temperature is an Epoch field; proposals are MH moves in Cells; learning rate / batch / rollout-temp are the same family of knobs; scarce tips are importance-sampled before spend.*

---

## 2. Simulated annealing ↔ liquid-methodology entropy create/destroy

Classical SA: start hot (accept uphill freely) → cool (accept rare) → \(T→0\) (greedy / mode).

| SA schedule | Factory / parallel-worlds schedule |
|---|---|
| High \(T\) | Wide `fork(n=K)`; diverse Cell proposals; swarm / GEAR population; high exploration entropy |
| Cool (raise \(β\) or tighten gates) | Precision-weighted reduce; fewer survivors; RRSI-style annealed edit budget (BACKUP cite only) |
| \(T→0\) | Singular **promote** — merge / checkpoint / wet-lab / robot hour / paper tip |
| Quench / burn | Dispose runners; receipts outlive machines (B §4; G burn invariant) |

**Teeth:** high \(T\) does *not* mint independent evidence (B Eq. 1: \(ρ>0\) floors variance). Cooling is **entropy destroy at the authority gate**, not “the swarm thermalized.” Liquid-methodology law restated: *create entropy where exploration pays; destroy entropy before promotion.*

**Cite B:** annealing ↔ liquid factory table is already in `B-REDUCE-STATPHYS.md` §4 — H deepens the *proposal / accept / schedule ownership* story so it is not only reduce rhetoric.

**Cite 2607.09689:** \(β_k=n_k\). Raising effective \(β\) in the pool = giving colder (larger-\(n\)) workers more shout — not dialing a thermostat on the microVM.

---

## 3. MCMC / Metropolis–Hastings ↔ Cell proposals + oracle energy

Metropolis–Hastings sketch (systems reading):

1. **Propose** \(Δ\) from current state \(S\) (patch, tool trace, hyperparam, controller Δ).  
2. Evaluate oracle energy \(E(S')\) under a **frozen** harness (tests, reward, assay).  
3. **Accept** with \(\min(1,\, e^{-β\,ΔE}\cdot\) Hastings ratio\()\); else **reject** = revert.  
4. **Detailed balance** (when it holds) ≈ a *frozen* energy + proposal kernel — not a property of CoW alone.

| MH object | Factory object |
|---|---|
| Proposal \(q(S→S')\) | Child sandbox run of proposal \(Δ\) (Cell / one-Δ / Shepherd BRANCH) |
| Energy \(E\) | Controller-owned oracle / `Objective.digest` (C’s sealed scorer; G’s Obj) |
| Accept | Keep artifact set / advance local tip inside Epoch |
| Reject | Revert = burn child; immutable \(S_0\) unchanged |
| Detailed balance | Frozen harness for the Epoch — mid-flight metric rewrite = Epoch bump or Rebound-class cheat |

**Invariant (Search≠Authority):** the worker proposes; the **controller** owns \(E\) and \(β\). If the child can rewrite `run_tests()` (Rebound→Remedy) or inflate \(n_k\), MH is theater — accept/reject follows a forged energy (hand to C + B cold liar).

**Detailed balance ≈ frozen harness:** we do **not** claim production factories satisfy balance. We claim the *systems twin* of “balance requires fixed \(E\)” is G’s invariant 3: mutating Obj bumps Epoch. That is the fence with teeth.

---

## 4. Langevin / SGD ↔ noisy gradients, batch = fork fan-out

Langevin / SGD intuition (claim-fenced):

- **Noisy gradient** ≈ stochastic oracle on a minibatch / subset of tests / stochastic sim seed.  
- **Learning rate \(η\)** ≈ proposal step size (how far a Cell may jump per move).  
- **Batch size** ≈ fork fan-out \(K\) — *path samples*, not i.i.d. evidence (again B ρ).  
- **KL / weight decay / trust region** ≈ free-energy-style regularizer: trade task reward vs distance from a reference policy / prior checkpoint.

| SGD / Langevin | Factory / RL binding |
|---|---|
| Minibatch noise | Stochastic eval seeds; partial suites; sim RNG |
| \(η\) schedule | Proposal amplitude / edit budget / Tree-RL branch width |
| Temperature in SGLD | Epoch policy field — not worker-writable |
| KL to ref | Free-energy dual of “don’t drift the promote tip silently” |

**Do not say:** SGD *is* Langevin dynamics of the agent Gibbs measure.  
**Do say:** the *same knobs* — step, noise, batch, regularizer — reappear as factory Epoch policy and RL post-training schedules.

---

## 5. Stochastic simulation (MC particle / Gillespie, lightly)

Monte Carlo particle / rare-event intuition for **scarce tips**:

- Many cheap trajectories in compute / sim (fork fabric).  
- One expensive tip: wet-lab slot, robot hour, clinic, Nature claim (D’s ladder).  
- **Importance sampling before scarce tip:** concentrate measure on high-value regions *before* spending the tip — do not bill \(K\) CoW siblings as \(K\) independent wet assays.

Gillespie-style continuous-time jump intuition (one breath, Q&A only): event rates ≈ oracle cost tiers; promote is the rare jump you budget, not the continuum of Cell retries.

**Hand to D/G:** `Promote.compute` vs `Promote.tip` — H’s rare-event story is why tip kinds must be first-class on the API (importance sample in compute Epoch; burn tip Epoch once).

---

## 6. RL post-training ↔ path samples + temperature

| RL object | Parallel-worlds / factory object |
|---|---|
| Rollout | Path sample from \(S_0\) under policy |
| Reward | \(-E\) (oracle energy; sealed outside fork — C) |
| PPO / GRPO temperature / top-\(p\) | Softmax sharpness over actions or preference pairs — **Epoch policy**, not child-editable |
| Advantage / KL penalty | Free-energy-style tradeoff vs reference |
| Tree-RL (Shepherd) | **Branching MCMC on traces**: fork the effect graph; commit survivors; lineage \(\mathcal{L}\) for reduce |

**Shepherd (2605.10913) — cite as related systems, not owned prior work:** agent+env as Git-like effect trace; fork ~134–143 ms peer table (A owns numbers). H’s reading: branching search on traces is MH/tree-sampling *algebra*, then B’s reduce pools structured evidence; G’s promote is zero-\(T\) authority.

**GRPO / Rebound caution (C):** temperature and reward only mean something if the grader is outside the fork. Hot exploration + in-fork oracle capture = fast self-hacking, not annealing.

---

## 7. SW factories (ariflow-swfactory) as MH + cooling schedule

Methodology map (capability contract, **not** inventory claim that every path already does this):

| swfactory / liquid concept | MC / SA dual |
|---|---|
| **Cell** proposal | MH move \(Δ\) in a sandboxed body |
| **Epoch** | Temperature rung / cooling stage / Obj pin — schedule ownership |
| Search≠Authority | Worker never sets \(T\) or \(E\) (nor promote keys) |
| Evidence → promote | Accept into authority tip; burn unsuccessful Cells |
| Liquid entropy create/destroy | Hot fan-out → cool reduce → \(T→0\) promote |

**G’s API binding H needs named:**

```text
Obj     = Objective.digest(..., anneal_schedule_id, beta_policy, ...)
Epoch   = Authority.epoch(Obj, policy)   # schedule change ⇒ Epoch bump
W       = World.fork(S0, n=K, epoch=Epoch, T=Epoch.T)
# children propose Δ; cannot mutate anneal_schedule_id or E
Pool    = Reduce(E_1…E_K, Obj)           # β≡n from 2607.09689
S0'     = Authority.promote(Pool.mode, Epoch)  # T→0 act
```

**B’s challenge already filed (B §→G #4):** “If Obj carries an anneal / β schedule id, bumping schedule = Epoch bump. Do not let workers cool themselves by inflating \(n_k\).” H **affirms** and asks G to put `T` / `anneal_schedule_id` on the wire as authority fields (see ROUNDTABLE →G).

---

## 8. Unified dictionary (one slide worth)

| Physics / MC / ML | Systems API (SRG should hear) | Owner |
|---|---|---|
| Configuration / microstate | Sandbox after restore from \(S_0\) | A |
| Proposal \(Δ\) | Cell / one-Δ / BRANCH | H + A |
| Energy \(E\) | Frozen Obj / sealed oracle | C + G |
| \(β\) / \(T\) | \(n_k\) in reduce; Epoch schedule for exploration | B + H + G |
| Accept / reject | Keep / revert child | H + G |
| Anneal schedule | Epoch rung / liquid cool-down | H + B |
| Path measure / rollouts | `fork(n=K)` | A + G |
| Reduce / \(Z_g\), \(Δ\) | Precision pool + abstain | B |
| Zero-\(T\) / mode | `Authority.promote` | G + D |
| Burn measure | Dispose runners; scrub leases | G + E |
| Importance sample | Compute Epoch before scarce tip | H + D |

---

## 9. Open problems (Act III bait — H-owned)

1. **Schedule as first-class Obj field:** canonical `anneal_schedule_id` + `T` / exploration budget in `Objective.digest`; false-positive Epoch bumps vs silent schedule drift.  
2. **Worker-inflated \(n_k\) = fake cooling:** attestation of \((n,J)\) (C) so MH accept probabilities cannot be gamed by cold-liar precision.  
3. **Tree-RL + reduce:** Shepherd lineage → B’s \(\mathcal{L}\); when is branching MCMC’s “survivor set” a correlated ensemble that must abstain?  
4. **η vs fork economics:** when does larger proposal step beat more CoW siblings under ρ floor? (Joint A+B+H; no invented ms.)  
5. **Rare-event tip budgets:** explicit importance-sampling API before `Promote.tip` (wet / robot / claim).  
6. **Do not pretend detailed balance:** document which Epoch invariants are necessary for MH *rhetoric* to stay honest (frozen \(E\), sealed \(β\)), without claiming balance holds.

---

## 10. Spoken lines (SRG — six)

1. “Annealing is the liquid factory in schedule clothes: explore hot, cool the gate, promote at zero \(T\), burn the runners.”  
2. “A Cell proposal is a Metropolis move; accept or revert — but only if the energy function lives *outside* the child.”  
3. “In Yossi’s reduce, \(β\) is sample size. Factory temperature is an Epoch policy — workers do not get the thermostat.”  
4. “SGD and Langevin are the same family of knobs: step size, batch-as-fork, noise, KL as free-energy regularizer — not a claim the swarm equilibrated.”  
5. “Tree-RL is branching MCMC on traces; Shepherd gives the path algebra, Boltzmann MapReduce asks what you measured and who else saw it.”  
6. “Search≠Authority means: never let the worker set temperature or the energy function. That is the whole fence.”

---

## 11. Deck placement

- **Half-slide / speaker bridge after B’s anneal table:** MH = Cell; Epoch = cooling rung; Search≠Authority = no worker \(T\)/\(E\).  
- **One spoken breath in Act II½:** β≡n (paper) vs factory \(T\) (Epoch) — two related but distinct knobs.  
- **Do not** derive MH ratios or Langevin SDEs for SRG. Schedule language only.  
- Point to B for \(Z/β/Δ\); to G for Epoch wire; to C for sealed \(E\); to A for Shepherd branch numbers; to D for scarce-tip importance sampling.

---

## 12. Do-not-say list

- ❌ “Agents *are* Ising / spin-glass / equilibrium Gibbs.”  
- ❌ “Detailed balance holds in our factory.”  
- ❌ “\(Z_g\) is the free energy of the lab / Bayes evidence.”  
- ❌ Workers may anneal themselves by editing metrics or inflating \(n\).  
- ❌ Vendor fork latencies or invented thermalization times.  
- ❌ Claiming Shepherd / PPO / GRPO / Gillespie as results you own — related duals only.  
- ❌ “swfactory already implements full MH+SA on every path” — methodology inspiration only.

---

## 13. Peer handoffs

| To | Ask / offer |
|---|---|
| **B** | Affirm β≡n vs factory \(T\) as *two* knobs; joint ownership of anneal↔liquid table; ask for schedule→effective-\(n\) policy guidance |
| **G** | Name `T` / `anneal_schedule_id` on Obj; Epoch bump on schedule change; refuse worker writes to thermostat |
| **C** | Sealed \(E\) is MH’s honesty condition; GRPO temp worthless if grader is in-fork |
| **A** | Tree-RL branch = proposal kernel; emit lineage for B’s ρ-abstain |
| **D** | Rare-event / importance sample before `Promote.tip` |
| **E** | Burn after reject/promote — leases die with the measure |

---

*Researcher H pass · 2026-09-27 (Asia/Jerusalem) · claim fence aligned with B/PARALLEL-WORLDS; β≡n from arXiv 2607.09689v3; Epoch/Search≠Authority from G; liquid/swfactory methodology as inspiration only.*


---

## Addendum — Non-equilibrium drive (open systems)

**Claim fence (restated):** this is schedule / systems language for *driven* factories — **not** a claim that agent sandboxes obey non-equilibrium statistical mechanics of nature, Onsager reciprocity, or a measured entropy-production theorem.

### Driven open systems, not closed Gibbs boxes

Liquid factories continuously inject work: new issues, fresh `S0` snapshots, oracle evaluations, human/HITL tips, GPU hours. They dump heat by burning runners and expiring leases. That is an **open, driven** picture — closer to a continuously forced Markov process than to a closed canonical ensemble relaxing to equilibrium.

| Closed / equilibrium rhetoric (avoid) | Open / driven systems reading (prefer) |
|---|---|
| Swarm “thermalizes” to \(\pi\propto e^{-\beta E}\) | Controller keeps pumping proposals + oracles; measure never sits still |
| \(Z\) is the lab’s free energy | \(Z_g\) stays B’s **pool diagnostic** only |
| Detailed balance as shipped invariant | Frozen Obj ≈ *local* honesty condition for MH rhetoric; global drive breaks balance by design |
| Equilibrium replicas | Correlated CoW siblings under ongoing Epoch policy |

**Spoken:** “Our factories are open systems under continuous drive — not a magnet cooling in a fridge.”

### Promote = absorbing sink

In the path picture, **promote** is an **absorbing** authority transition: once the tip is spent (merge / checkpoint / wet slot / robot hour / paper claim), sibling worlds are archival; runners burn; the control plane does not keep sampling as if the mode were still in the bulk.

- Search measure = transient / recurrent exploration under Epoch \(T\).  
- Promote = sink: probability mass that hits authority stays there (one bit, G invariant 4).  
- Reject / abstain / burn = other exits that do *not* mint a tip.  
- Two-phase promote (D/G): `Promote.compute` may still be reversible archival keep; `Promote.tip` is the scarce absorbing burn.

This is why zero-\(T\) language is useful **at the gate** without claiming the whole swarm equilibrated: absorption is an authority act, not a thermodynamic limit of \(K\to\infty\) forks.

### Hamiltonian only as proposal generator

If a “Hamiltonian” / energy appears in factory talk, treat it as a **proposal and scoring device**, not as the conserved generator of real-time dynamics:

- \(E\) / reward / loss = oracle score under frozen Obj (C + G).  
- Proposal kernel (Cell Δ, SGD step, Tree-RL branch, Langevin noise) may be *inspired* by \(-\nabla E\) or by a heuristic Hamiltonian Monte-Carlo story — but the runtime’s job is **sample → measure → reduce → promote**, not integrate symplectic equations on the guest.  
- Do **not** say microVMs evolve under a Hamiltonian flow; do say “Hamiltonian / energy is how we *name* the oracle the proposal is aiming at.”

Matches H §3–4: MH needs \(E\) for accept/reject; Langevin/SGD need noisy gradients — both are **generators of proposals and weights**, not claims of microscopic energy conservation in the sandbox.

### Entropy production ≈ lineage (algebra, not Clausius)

B’s ledger already carries fork lineage \(\mathcal{L}\) and evidence IDs \(\mathcal{E}\). H’s non-eq reading: **irreversible history is the systems twin of entropy production**.

| Non-eq intuition | Factory ledger |
|---|---|
| Forward path vs time-reverse | BRANCH / commit / promote record that has no cheap undo once tip I/O fired |
| Entropy production along a trajectory | Append-only \(\mathcal{L}\) + sealed oracle receipts + burn events |
| Housekeeping heat | Dispose runners, revoke leases (E), scrub warm CoW credential surface |
| Drive strength | Epoch exploration budget / \(T\) / fan-out \(K\) set by authority |

**Teeth:** we do **not** compute a numerical \(\dot{S}\) for SRG. We say: *lineage + burn + absorbing promote are how the factory makes irreversibility auditable* — the algebraic cousin of entropy production, owned jointly with B’s \(\mathcal{L}\) and G’s burn invariant.

### Tie-back to β / Epoch (B + G)

- Reduce \(\beta\equiv n\) (2607.09689) remains an **information weight**, not a thermostat of a closed system.  
- Factory \(T\) / `anneal_schedule_id` remains an **Epoch drive knob** (H→G wire ask).  
- Cooling toward promote = shrinking the transient measure into an absorbing tip — liquid entropy destroy — under continuous external drive, not equilibration.

**Do-not-say extras:** ❌ “we measured entropy production of the swarm”; ❌ “promote is the thermodynamic arrow of time in nature”; ❌ “Hamiltonian Monte Carlo is what Firecracker runs.”

---

*Addendum · Researcher H · 2026-09-27 (Asia/Jerusalem) · non-equilibrium drive / absorbing promote / Hamiltonian-as-proposal / lineage≈entropy-production — claim-fenced.*
