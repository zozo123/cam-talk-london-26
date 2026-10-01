# Researcher I — Non-equilibrium Physics / Hamiltonian / Driven Systems
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Lens:** why *equilibrium* is the wrong default for agent factories; careful Hamiltonian metaphor; driven / open-system toolkit that systems people can stage-safely use  
**Companion reads:** B’s `B-REDUCE-STATPHYS.md` (β≡n, Z_g, Δ, cold liar), H’s `H-ANNEALING-MCMC-SGD.md` (SA/MH/Langevin schedule dual), `PARALLEL-WORLDS-STATPHYS.md`, G’s Epoch / Search≠Authority, C on sealed oracles, D on scarce tips  
**Owner framing:** Physics PhD license to *speak* the language — **not** a license to claim agent factories are closed Hamiltonian systems of nature.

---

## Claim fence (non-negotiable — HARD)

| Say | Do **not** say |
|---|---|
| Agent factories are **driven, open systems**: continuous proposal injection, budget flows, oracle measurements, promote sinks. | Agent factories *are* closed Hamiltonian systems / conservative mechanics of nature. |
| Steady search at fixed Epoch ≈ **non-equilibrium steady state (NESS)**, not thermodynamic equilibrium. | The swarm “equilibrates”; CoW siblings form a Gibbs ensemble; detailed balance is proven in CI. |
| \(H(q,p)\) is a **generator-of-proposals metaphor** — what the searcher *would* do if isolated. | We derived / proved a Hamiltonian (or second law) for the lab / for CI. |
| Promote is an **absorbing sink** — irreversible work / entropy destroy at the authority gate. | Promote is a free-energy *minimum of a closed system*. |
| Entropy production along evidence lineage = irreversibility *record* (useful ledger reading). | Fluctuation theorems / Jarzynski equalities hold for sandboxes; we measured them. |
| TUR intuition: precision costs dissipation — ties to β≡n / cold-liar *as interpretation*. | Thermodynamic uncertainty relations are theorems of your factory. |
| Physics PhD = fluency with fences. | “We proved the second law for continuous integration.” |

**One sentence for SRG:** *I use non-equilibrium language because factories are driven — continuous proposals in, promote sinks out — not because agents thermalize like magnets.*

---

## 1. Why equilibrium is the wrong default

Equilibrium statistical mechanics assumes a **closed** (or weakly coupled) system that has forgotten its drive and sits in a stationary Gibbs measure \(e^{-\beta H}/Z\). Agent factories violate that picture in four structural ways:

1. **Continuous proposal injection** — Cells / rollouts / patches keep arriving; the measure is fed, not left alone.  
2. **Budget / tip flows** — robot-hours, wet slots, merge tokens, compute Epochs are *expended*; energy-like resources cross the boundary.  
3. **Oracle measurements** — sealed scorers / held-outs / preference models are external apparatus (C); measurement is not internal to the child’s \(H\).  
4. **Promote sinks** — singular authority absorbs one mode into `main` / checkpoint / claim tip and **burns** the rest (G burn invariant; B anneal table). That is an **absorbing boundary**, not a free-energy minimum of a closed landscape.

**Steady search ≠ thermodynamic equilibrium.** A swarm running at fixed Epoch \(T\) with continuous `fork`/`burn` can look “steady” (constant fan-out, constant reduce rate) while producing entropy every cycle — classic **non-equilibrium steady state (NESS)** intuition, claim-fenced.

**Spoken bridge (Act II½):** “If your factory never stops proposing and sometimes promotes, it is driven. Calling that equilibrium is the wrong default — even when the dashboard looks flat.”

Hand to **H**: schedule language (hot → cool → \(T\to0\)) is the *protocol* on this drive. Hand to **B**: reduce algebra sits on the *evidence* that survives the drive; it does not make the drive Hamiltonian.

---

## 2. Hamiltonian intuition (careful — metaphor with teeth)

Use phase-space language as a **dictionary**, then immediately open the system:

| Symbol | Systems reading |
|---|---|
| Configuration \(q\) | Sandbox / world state after restore from \(S_0\) (FS + mem + processes) — A’s surface |
| Momentum / auxiliary \(p\) | Optimizer / agent internal state: policy logits, Adam moments, Tree-RL controller state, edit buffer |
| \(H(q,p)\) | **Generator of proposals** — what the isolated searcher *wants* to do next (prior dynamics, reference policy, one-Δ hillclimb bias) |
| Hamilton’s equations (metaphor) | Deterministic proposal flow if no reward, no oracle, no burn |
| Non-conservative force | Reward / human preference / test oracle / assay — **outside** \(H\) (C + G Obj) |
| Dissipation | Burn runners; KL / trust-region pull toward prior; learning-rate friction; lease revoke (E) |
| Measurement back-action | Oracle / EVAL injection; attestation \(a_k\); Epoch bump when Obj changes |

**Real factory = open driven system:**

\[
\underbrace{\dot q,\;\dot p}_{\text{proposal generator }H}
\;+\;
\underbrace{F_{\mathrm{oracle}}(q)}_{\text{non-conservative}}
\;+\;
\underbrace{-\gamma\,p}_{\text{dissipation / KL friction}}
\;+\;
\underbrace{\xi(t)}_{\text{noise / minibatch / sim RNG}}
\;+\;
\underbrace{\text{promote sink}}_{\text{absorbing boundary}}
\]

**RL / PPO reading (one breath):** policy-gradient / PPO updates ≈ **discrete dissipative dynamics** on \((q,p)\); the KL penalty toward a reference policy ≈ **friction** that dissipates “distance from prior.” That is why free-energy-style regularizers reappear in H’s SGD dictionary — not because the swarm is a Gibbs measure.

**Teeth:** \(H\) answers “what would this searcher propose if isolated?” Authority answers “what did the sealed oracle and Epoch allow?” Conflating them is Search=Authority cosplay.

**Refuse:** closed Hamiltonian = agents; symplectic integrators “prove” CI correctness; conjugate momenta of CoW pages.

---

## 3. Non-equilibrium toolkit for the talk (stage-safe picks)

Pick **three on-stage**, park the rest in Q&A. Do **not** derive.

### 3.1 Driven Langevin — underdamped vs overdamped (on-stage OK)

- **Underdamped** (inertia): momentum SGD / Adam-with-memory / agent carrying internal optimizer state across Cells — \(p\) persists.  
- **Overdamped** (no inertia): plain LR / small-step one-Δ / memoryless propose-revert — \(p\) slaved to force.  
- **Drive** \(\lambda(t)\): Epoch anneal schedule, exploration budget, tip scarcity — H’s schedule id on Obj.

**Say:** learning-rate and momentum are the same family as Langevin friction/inertia knobs.  
**Don’t say:** your factory *is* Langevin dynamics of a Gibbs density.

### 3.2 Entropy production along trajectories (on-stage OK, one slide breath)

Each fork→run→measure→keep/revert→burn cycle is typically **irreversible**: you cannot un-burn a runner or un-spend a robot hour from the ledger alone. **Evidence lineage \(\mathcal{L}\)** (B) + Shepherd effect traces (A) are the systems twin of an irreversibility *record* — who proposed, what oracle saw, what was promoted.

**Say:** “Lineage is how the factory remembers it produced entropy.”  
**Don’t say:** we computed \(\Sigma\) in nats for islo.

### 3.3 Fluctuation theorems — Q&A only, light touch

Crooks / Jarzynski relate work along driven trajectories to free-energy differences **in carefully prepared physical systems**. For the talk:

- **One line max if at all:** “Promote spends irreversible work — you don’t get the robot hour back by reversing the patch.”  
- **Better:** skip names; say *irreversible work at the tip*.  
- **Do not derive.** Do not claim Jarzynski for CI.

### 3.4 Non-equilibrium steady state (NESS) (on-stage OK)

Swarm at fixed Epoch \(T\) with continuous `fork(n=K)` / reduce / burn: fluxes in (proposals, budget) and out (burns, promote rare events) with roughly stationary statistics. That is **NESS intuition**, not \(e^{-\beta H}/Z\).

Liquid-methodology restated in non-eq clothes: *create entropy where exploration pays; destroy entropy before promotion* — destruction is the promote sink, not equilibration.

### 3.5 Thermodynamic uncertainty relations (TUR) — interpretation bridge to B

TUR folklore: **precision costs dissipation** — you cannot get arbitrarily tight estimates without paying irreversible cost (time, heat, tip spend).

**Systems twin with teeth (claim-fenced):**  
- B’s \(\beta_k=n_k\): colder (larger \(n\)) workers shout louder — precision is *bought* with sample count / oracle cost.  
- Cold liar: forged high \(P_o\) claims precision **without** paying dissipation / attestation — TUR intuition says that should be impossible; systems fix is C’s sealed receipts + B’s clip/abstain, not a physics theorem.  
- Scarce tip (D): one robot hour buys one high-stakes measurement; \(K\) CoW siblings do not mint \(K\) independent tips (B ρ floor).

**Say:** “Precision is not free — β≡n is how the reduce *prices* it; TUR is why forged precision smells wrong.”  
**Don’t say:** we proved a TUR for MapReduce.

---

## 4. Map to swfactory / RL / parallel worlds

| Non-eq object | Factory / RL binding | Owner |
|---|---|---|
| Time-dependent drive \(\lambda(t)\) | Epoch anneal schedule / exploration budget / tip ladder — **not** quasi-static fantasy | H + G |
| Protocol (non-eq annealing) | Hot fan-out → cool reduce → \(T\to0\) promote → burn — liquid schedule | H + B |
| External bath + measurement apparatus | Search≠Authority: sealed oracle + promote keys **outside** \(H\) / outside child | C + G + E |
| Path measure under protocol | \(\int\mathcal{D}[\mathrm{path}]\,e^{-\beta E}\) with \(\lambda(t)\) — fork measure under Epoch | B + PARALLEL-WORLDS |
| Dissipative policy update | PPO/GRPO step + KL friction; Tree-RL branch = driven path sample | H + C |
| Absorbing sink | `Authority.promote` / `Promote.tip` — singular, auditable | G + D |
| NESS at fixed \(T\) | Steady swarm density + continuous fork/burn without promote | A + F packing |
| Irreversible work at tip | Robot hour / wet slot / paper claim — importance-sample in compute Epoch first | D + H |

**Path-integral line (align with B / PARALLEL-WORLDS):**

\[
Z[\lambda] \approx \int \mathcal{D}[\mathrm{path}]\;\exp\big(-\beta\, E(\mathrm{path};\,\lambda(t))\big)
\]

Operationally: \(S_0\) boundary → fork samples paths under protocol \(\lambda\) (Epoch) → reduce pools structured \(r_k\) → promote is **not** “argmin of closed \(H\)” but selection under external authority after irreversible spend.

**Quasi-static fantasy to refuse:** pretending Epoch cool-down is infinitely slow equilibrium annealing so free-energy differences are path-independent. Real factories quench, gate, and burn — **finite-rate driven protocols**. H’s schedule language already says this; I names why physics people flinch at “equilibrium.”

---

## 5. Division of labor (I vs B vs H)

| Owner | Owns |
|---|---|
| **B** | Algebra: β≡n, \(Z_g\), Δ, cold liar, ρ floor, abstain |
| **H** | Schedule dual: SA / MH / Langevin-SGD knobs; Cell=MH move; Epoch owns \(T\) |
| **I** | **Why not equilibrium:** driven/open ontology; \(H\) as proposal generator only; NESS; irreversible promote sink; TUR↔precision cost bridge; fluctuation theorems Q&A fence |

I does **not** re-derive MH ratios or \(Z_g\). I supplies the **ontology fence** so Act II½ physics does not accidentally claim closed-system thermodynamics.

---

## 6. Six spoken SRG lines + deck placement

1. “Equilibrium is the wrong default — factories are driven: proposals in, promote sinks out.”  
2. “Hamiltonian here means generator of proposals — what the searcher wants — not a claim agents are closed mechanical systems.”  
3. “Real factory = open system: H plus oracle forces, dissipation, measurement, and an absorbing promote boundary.”  
4. “Steady swarm at fixed temperature with continuous fork and burn is a non-equilibrium steady state, not a Gibbs ensemble of CoW siblings.”  
5. “Promote spends irreversible work — you don’t un-burn a robot hour by reverting a patch.”  
6. “Precision costs dissipation: that is why β equals sample size in the reduce, and why a cold liar forging precision is physically *and* systems-wrong.”

### Where in the talk

| Line | Act | Role |
|---|---|---|
| 1, 4 | **Act II½** (after B’s anneal table / before or after H’s schedule breath) | Ontology correction — “driven, not equilibrium” |
| 2, 3 | **Act II½** speaker notes | Hamiltonian fence in one breath; point to sealed oracle (C) |
| 5 | **Act III** (HIL / scarce tip) or Q&A | Irreversible work ↔ D’s tip ladder |
| 6 | **Act II½** cold-liar beat **or** Act III open problem | TUR intuition → B β≡n / attestation |

**Do not:** spend slides on Jarzynski derivations, symplectic integrators, or “second law of CI.”  
**Do:** one bridge sentence so physicists in the room hear you refuse the closed-system trap.

---

## 7. Open problems (Act III bait — I-owned)

1. **Protocol as first-class drive:** name \(\lambda(t)\) / `anneal_schedule_id` on Obj (joint H+G); document finite-rate quench vs fantasy quasi-static cool.  
2. **Entropy-production ledger:** can \(\mathcal{L}\) + promote receipts expose a usable irreversibility audit (who spent what tip) without fake nats?  
3. **NESS vs promote rare events:** when is “steady swarm” actually waiting for a Poisson tip — scheduling implication for warm pools (F) and lease TTL (E)?  
4. **TUR-inspired attestation:** systems analogue of “precision requires dissipation” = sealed \((n,J)\) receipts (C) so reduce cannot be hijacked by costless cold liars (B).  
5. **Refuse closed \(H\):** keep any future “agent Hamiltonian” paper (AIDE²/GEAR outer loop on search policy) clearly labeled *driven policy dynamics*, not conservative mechanics.

---

## 8. Do-not-say list (repeat for ops)

- ❌ “We proved the second law / fluctuation theorem for CI.”  
- ❌ “Agent factories are closed Hamiltonian systems of nature.”  
- ❌ “CoW siblings are an equilibrium Gibbs measure.”  
- ❌ “Promote is the free-energy minimum of a closed landscape.”  
- ❌ Derive Jarzynski / Crooks on stage; quote invented entropy-production numbers.  
- ❌ “Detailed balance holds because Firecracker is isolating.”  
- ❌ Conflate factory exploration-\(T\) (Epoch) with reduce \(\beta\equiv n\) (B) — two knobs (H already split them; I keeps the drive outside both).

---

## 9. Peer handoffs

| To | Ask / offer |
|---|---|
| **B** | Affirm promote = sink/absorbing boundary in the physics↔systems dictionary (not closed FE min); TUR intuition as *interpretation* of why forged \(n\) is illicit — not a new theorem in 2607.09689 |
| **H** | Joint ownership: your SA/MH schedule = non-eq **protocol** \(\lambda(t)\); I supplies “driven/NESS not equilibrium” fence so annealing slides don’t sound quasi-static |
| **G** | Drive fields on Obj (`anneal_schedule_id`, exploration budget) stay authority-owned; promote sink remains singular |
| **C** | Oracle = external measurement apparatus — measurement back-action must not rewrite \(H\) inside the child |
| **D** | Irreversible work language for `Promote.tip` (robot/wet/claim) |
| **A/F** | NESS density under continuous fork/burn ≠ evidence independence (ρ still B’s) |

---

## 10. Challenges filed

**→ B (dictionary + TUR bridge):** Will you add “promote = absorbing sink / irreversible work” beside the anneal table in Act II½ notes, and accept TUR-only-as-intuition for “precision costs dissipation ↔ β≡n / cold-liar,” without importing fluctuation-theorem claims into 2607.09689?

**→ H (protocol vs equilibrium anneal):** Confirm on-stage wording: Epoch cool-down is a **finite-rate driven protocol** (non-eq), not quasi-static equilibrium annealing — and keep MH “detailed balance ≈ frozen \(E\)” as *honesty condition*, never “the factory equilibrated.”

---

*Researcher I pass · 2026-09-27 (Asia/Jerusalem) · claim fence aligned with B/H/PARALLEL-WORLDS; driven/open ontology; Hamiltonian = proposal generator only; no second-law-for-CI claims.*
