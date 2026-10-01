# Researcher B — Reduce / Statistical Physics
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Owner:** Yossi Eliaz · arXiv [2607.09689](https://arxiv.org/abs/2607.09689) (v3 Evidence-Aware framing) · artifact [zozo123/boltzmann-mapreduce](https://github.com/zozo123/boltzmann-mapreduce)  
**Companion reads:** `PARALLEL-WORLDS-STATPHYS.md`, `PAPERS-AND-SOURCES.md` §E, `STORY-SPINE.md` Act II½  
**Claim fence (non-negotiable):** physics is an *interpretation with teeth* of precision-weighted pooling under LAN / Wald kernels — **not** “agent forks are Gibbs ensembles of nature.” Say: *the algebra systems people need already looks like statistical mechanics.*

---

## 1. One-slide physics → systems dictionary

| Physics | Systems API (what SRG should hear) |
|---|---|
| Microstate / configuration | Sandbox state: FS + mem + processes after restore |
| Trajectory / path | One child rollout / agent trajectory |
| Path measure / ∑ histories | Fan-out `fork(n=K)`; later **reduce** |
| Energy \(E\) | Loss, residual, assay score, reward cost |
| Inverse temperature \(\beta\) | Sample size / information weight \(n_k\) (paper: \(\beta_k = n_k\)) |
| Partition function \(Z\) | Normalizer of the product of worker kernels |
| Free-energy drop | Promote only when evidence says the gain is real |
| Equilibrium / anneal | Entropy collapse at the authority gate |
| Replicas | CoW siblings — *correlated* unless evidence proves otherwise |

**Operational path integral (agentic twin, Euclidean form):**

\[
Z \approx \int \mathcal{D}[\mathrm{path}]\; \exp\!\big(-\beta\, E(\mathrm{path})\big)
\]

1. Snapshot \(S_0\) = shared past (boundary condition).  
2. Fork \(N\) children = sample paths (Tensorlake / islo / DeltaBox / Crab / Shepherd).  
3. Each child returns **structured evidence**, not a naked scalar.  
4. Reduce ≈ approximate the integral / pool natural parameters.  
5. Promote = mode / zero-\(T\) authority decision; keep finite-\(T\) uncertainty in the ledger.

Without (2) you cannot sample the path measure. Without (4) you average liars. Without (5) every path becomes a control plane.

---

## 2. Equations as systems API (from 2607.09689v3)

### 2.1 Why fork ≠ independence (Eq. 1 — open the Act II½ slide with this)

If \(K\) estimates share equal marginal variance \(\sigma^2\) and exchangeable pairwise correlation \(\rho\):

\[
\operatorname{Var}(\bar\theta)=\sigma^2\!\left[\rho+\frac{1-\rho}{K}\right]
\]

Independence reports \(\sigma^2/K\). For fixed \(\rho>0\), variance floors at \(\rho\sigma^2\) no matter how many CoW siblings you spawn. **Execution isolation ≠ evidence independence.** Shared model, prompt, repo, tests, or ancestor → common-mode error.

**Spoken:** “A million forks with \(\rho>0\) still leave a variance floor. Cheap branches do not mint independent evidence.”

### 2.2 Worker wire record (Eq. 2 — the contract)

\[
r_k = \big(\hat\theta_k,\; J_k,\; n_k,\; \mathcal{E}_k,\; \mathcal{L}_k,\; m_k\big)
\]

| Field | Meaning | Why systems care |
|---|---|---|
| \(\hat\theta_k\) | Estimate | What the child claims |
| \(J_k\) | Per-observation information | Calibrated precision shape |
| \(n_k\) | Literal sample count | **\(\beta_k\)** — how loud the child may shout |
| \(\mathcal{E}_k\) | Evidence IDs | Duplicate-ID reject; Proof-of-Use cousin |
| \(\mathcal{L}_k\) | Fork lineage | Shared-root signal for future \(\rho\) model |
| \(m_k\) | Execution metadata | Placement / retry / speculative tag |

**Invariant natural parameters (Eq. 3):**

\[
P_k = n_k J_k,\qquad q_k = P_k\hat\theta_k,\qquad c_k = \hat\theta_k^{\!T} P_k\hat\theta_k
\]

**Associative merge (Eq. 4)** — flat, streaming, or tree; runtime owns fan-out topology:

\[
(P,q,c,N)=\bigoplus_k (P_k,q_k,c_k,n_k)
\]

Provenance has *separate* semantics: evidence IDs = set union + exact-overlap reject; lineage = order-preserving dedup. Numeric state is \(O(p^2)\); ledger can grow with \(|\mathcal{E}|+|\mathcal{L}|\).

### 2.3 Gibbs / Wald kernel ↔ \(\beta\) naming (Eqs. 6, 10)

Local unnormalized kernel:

\[
g_k(\theta)=\exp\!\Big\{-\tfrac12(\theta-\hat\theta_k)^{\!T} P_k(\theta-\hat\theta_k)\Big\}
\]

Rewrite with energy / temperature:

\[
E_k(\theta)=\tfrac12(\theta-\hat\theta_k)^{\!T} J_k(\theta-\hat\theta_k),\qquad \beta_k=n_k
\quad\Rightarrow\quad
g_k=\exp\{-\beta_k E_k\}
\]

**Teeth:** \(\beta\) is not mystic. In the Gaussian reduce it is the sample size. Colder (larger \(n\)) workers dominate the pool. A global \(\beta=N=\sum n_k\) with weighted-average energy is the same product. This is a *naming convention* for systems APIs, not a claim that sandboxes thermalize.

### 2.4 Pooled center, residual \(\Delta\), partition \(Z_g\) (Eqs. 7–9)

\[
\hat\theta = P^{-1}q,\qquad \Sigma_g=P^{-1}
\]

\[
\Delta = \sum_k(\hat\theta_k-\hat\theta)^{\!T}P_k(\hat\theta_k-\hat\theta)
= c - q^{\!T}P^{-1}q \ge 0
\]

- Scalar \(p=1\): \(\Delta\) = Cochran’s \(Q\).  
- Under independent \(N_p(\theta_0,P_k^{-1})\) with known \(P_k\): \(\Delta\sim\chi^2_{p(K-1)}\) (plug-in \(P_k\) → asymptotic).  
- Small \(\Delta\) is *compatible with* dependence / duplicated evidence — do not read “agreement” as “independent confirmation.”

Product-integral / partition normalizer (unit-height kernels):

\[
Z_g = (2\pi)^{p/2}\,|P|^{-1/2}\,\exp(-\Delta/2)
\]

So \(\Delta/2\) is both minimized summed quadratic energy **and** the heterogeneity term in \(-\log Z_g\). Magnitude of \(Z_g\) alone is **not** a model-evidence score — SRG should not treat it as Bayes factor cosplay.

### 2.5 Cold liar / forged precision (Eq. 11 + artifact stress)

Influence of worker \(o\) (precisions held fixed):

\[
\frac{\partial\hat\theta}{\partial\hat\theta_o}=P^{-1}P_o
\]

Distance does not dampen leverage — **fabricated high \(P_o\)** does. Artifact check (forged precision): unprotected pool → \(17.0004\); determinant/MAD clip → \(4.9566\). Clip is a **diagnostic heuristic**, not Byzantine robustness (paper §5). Stage line: *“A cold liar hijacks the pool unless you clip or authenticate precision.”*

### 2.6 Self-consistency as the foil

Wang et al. ICLR’23 (arXiv 2203.11171): majority vote over sampled CoT paths — classical **naive reduce**. Multiagent debate / MoA likewise erase evidence identity. Boltzmann upgrades the contract: precision + \(n\) + \(\mathcal{E}\) + \(\mathcal{L}\) + \(\Delta\). **Cite self-consistency as BACKUP foil, not as prior work you own.**

---

## 3. Replica correlation & fork-DAG reducer (open problem you own)

| What systems have today | What reduce still lacks |
|---|---|
| CoW mem/FS sharing (DeltaBox, forkd, Tensorlake) | Measured \(\rho\) across siblings |
| Shepherd commit graph / OpenRath Session / your \(\mathcal{L}\) | Mapping ancestry → covariance / shared latent factors |
| Exact nonempty \(\mathcal{E}\) overlap reject | Relabeling, empty IDs, shared noise, adaptive selection |

**Agenda (paper §5 → talk Act III):**  
1. Record parent branch IDs, immutable evidence manifests, model/prompt/tool hashes, evaluator versions, selection events.  
2. Map known overlap → shared factors / conservative evidence groups.  
3. **Abstain** when dependence is unresolved — withhold the narrow interval.  
4. Winner’s curse: if the same evidence selects survivors *and* builds factors, ledger must record that reuse.

**Replica method (Q&A only):** correlated replicas ≠ \(N\) i.i.d. samples. Shepherd lineage + your overlap checks are the systems twin of replica overlap \(q_{ab}\).

---

## 4. Annealing ↔ liquid factory

Liquid-methodology / swfactory law: *create entropy where exploration pays; destroy entropy before promotion.*

| Stat-phys schedule | Factory schedule |
|---|---|
| High \(T\) / small \(\beta\) | Wide fan-out, diverse proposals, swarm / GEAR population |
| Cool / raise \(\beta\) (or raise effective \(n\)) | Tighten gates, precision-weighted reduce, fewer survivors |
| \(T\to 0\) / promote mode | Singular authority: merge / checkpoint / wet-lab slot |
| Burn measure | Dispose runners; receipts outlive machines |

Matches SGD / simulated-annealing *intuition* without claiming equilibrium thermodynamics. RRSI’s annealed edit budget and AIDE²’s frozen eval budget are outer-loop cousins — cite BACKUP only.

**Spoken bridge:** “Annealing is the liquid factory in physics clothes: explore hot, promote cold, burn the runners.”

---

## 5. Platform fit (physics role — one table, don’t overclaim)

| System | Role in the path picture |
|---|---|
| **islo / Tensorlake / Firecracker pedigree** | Durable configuration space; named snapshot = \(S_0\) |
| **DeltaBox / Crab / forkd** | Cheap propagator of the measure |
| **Shepherd** | Formal path algebra + Tree-RL; lineage sibling to \(\mathcal{L}\) |
| **swfactory / Airflow** | Thermostat + fence: Cell/epoch; Search≠Authority |
| **Your reduce paper** | Partition / pool for worker factors |
| **pstack hillclimb** | Local ascent on one path; swarm = multi-path |

Artifact numbers (own tables only): four-worker islo named-snapshot restore–run–capture ~6.70 s; unequal-size logistic pool gap \(0.0083\pm0.0042\) vs equal average \(0.177\pm0.090\). Do **not** quote Daytona/Tensorlake vendor create latencies as your fork benchmarks.

---

## 6. Deck placement (keep physics lean)

- **One slide:** parallel worlds — \(S_0\) → forks → reduce → promote → burn.  
- **One slide:** \(\beta/Z\) / cold liar — Eq. (1) variance floor + worker record + influence Eq. (11). Minimal latex.  
- **Speaker notes:** \(Z_g\), \(\Delta\sim\chi^2\), self-consistency foil, replica Q&A.  
- **Do not** derive path integrals for 15 minutes. Physics = lens; SRG cares about API, isolation, open problems.

Suggested MAIN cite #4 on the five-cite deck: **Evidence-Aware MapReduce (2607.09689)**.

---

## 7. Spoken lines (SRG-safe, claim-fenced)

1. “A fork is a parallel world with a shared past. A promote is world-selection.”  
2. “Path integrals taught us to sum over histories. Agent factories finally have a machine that can *sample* them.”  
3. “\(\beta\) is not mystic — in the Gaussian reduce it’s the sample size. Cold workers shout louder.”  
4. “Statistical physics gave us the *reduce*. Systems still owe us the *fork* and the *fence*.”  
5. “Tensorlake and friends make worlds cheap. The open problem is making the partition function trustworthy.”  
6. “Self-consistency votes. Evidence-aware MapReduce asks: *what did you measure, how hard, and who else already saw it?*”  
7. “A cold liar with forged precision hijacks the pool. Isolation does not authenticate \(n\).”  
8. “Annealing is the liquid factory: create entropy to search, destroy it before authority.”

---

## 8. Peer handoffs

| To | Need from them |
|---|---|
| **A (Fork / CoW)** | Measured or estimated \(\rho\) under shared pages / warm parent; whether CoW mem sharing changes effective independence beyond \(\mathcal{L}\) |
| **C (Oracle / Escape)** | How oracle digests / held-out tests sit *outside* the forked body so forged \(J_k,n_k\) and Rebound-class test rewrites cannot mint cold liars |
| **D (Promote / Factory)** | Epoch bump when \(\beta\) or objective digest changes; promote consumes reduced posterior, not raw best-of-N |

---

## 9. Do-not-say list

- ❌ “Agent forks *are* a Gibbs ensemble / thermodynamic equilibrium.”  
- ❌ “\(Z_g\) is Bayesian model evidence / free energy of the lab.”  
- ❌ “Majority vote / self-consistency already solves reduce.”  
- ❌ Vendor fork latencies as *your* numbers.  
- ❌ Byzantine-robust reduce as a solved claim (clip = heuristic).  
- ❌ Claiming Shepherd / DeltaBox / Crab as prior work you own — related systems only.

---

*Researcher B pass · 2026-09-27 (Asia/Jerusalem) · equations from arXiv 2607.09689v3 + PARALLEL-WORLDS-STATPHYS claim fence.*

---

## Challenges to A/C/G

**Claim fence restated:** these challenges ask for *measurement contracts and API teeth*, not for declaring forks a thermodynamic ensemble.

### → A (Fork / CoW) — measure ρ, don’t invent it

1. **Empirical ρ protocol:** Can you ship a sibling-pair assay — same `S0`, fixed Obj, two CoW children with *disjoint* RNG/evidence tokens vs *shared* warm pages only — that reports pairwise correlation of \(\hat\theta\) (or of oracle residuals) across ≥30 seeds? Without numbers, reduce must treat shared root \(\in\mathcal{L}\) as **unresolved ρ** and abstain from \(\Sigma_g \propto 1/K\).
2. **What CoW actually couples:** Is the dominant channel (a) shared model weights / prompt cache, (b) shared FS gold/tests, (c) CoW mem pages / TLB, or (d) scheduler placement? Name which your stack can *instrument* vs which is opaque — B needs a typed overlap tag on \(\mathcal{L}\), not a hope that Firecracker isolation ⇒ ρ=0.
3. **Replica billing:** Will fork schedulers expose `effective_n ≤ K` (or refuse to advertise K independent samples) when lineage overlap exceeds a threshold you define? If A only sells “K worlds in 100 ms,” reduce will keep being lied to by the API surface.

### → C (Oracle / Escape) — authenticate (n, J), don’t trust the child

1. **Precision authority:** Who signs \((n_k, J_k)\)? If the worker process that can rewrite Rebound-class tests also emits \(n,J\), the cold-liar attack is *in contract*. Demand: oracle binary + fixture digests live in controller Epoch; child may *invoke* a sealed scorer and receive a signed receipt `(θ̂, n, J, ℰ, obj_digest)` — never mint precision itself.
2. **Held-out vs visible:** SpecBench-style split — visible validation inside the fork, held-out compare outside. Does your escape story guarantee the held-out harness is unreachable from the child’s net/FS capability set? If not, forged \(J\) is the least of our problems.
3. **Retry / speculative duplicates:** Paper requires identical evidence tokens for retries. Can C’s oracle lease layer *key-admit* one result per `(ℰ, obj_digest)` so fault-tolerance cannot double-count into fake β?

### → G (Factory API) — wire Z_g without cosplay

1. **Reduce return type:** Propose `Pool = {θ̂, Σ_g, Δ, logZ_g, N, ℰ, ℒ, verdict∈{keep,revert,abstain}, reasons[]}` — is `logZ_g` a **diagnostic field** (heterogeneity + volume) with documented non-semantics (“not Bayes evidence”), or will path-integral CI UX misuse it as a green-score? Prefer exposing `Δ` + `df` + `abstain` as the human-facing triple; keep `Z_g` in speaker notes / ledger.
2. **Abstain first-class:** Confirm `verdict=abstain` when (i) shared nonempty \(\mathcal{L}\) without A’s ρ model, (ii) `obj_digest` ≠ Epoch Obj, (iii) cold-liar / precision-clip fired, (iv) Δ vs \(\chi^2_{p(K-1)}\) fails calibration gate. Promote must hard-fail on abstain — no silent best-of-N fallback.
3. **obj_digest binding:** Treat mismatch as **hard reject before** \(\bigoplus(P,q,c,N)\). That is *joint* G+C: G names the field on the wire; C authenticates the oracle bytes behind the digest. B will not merge natural parameters across Epochs.
4. **Annealing as Epoch policy:** If Obj carries an anneal / β schedule id, bumping schedule = Epoch bump (your invariant 3). Do not let workers “cool themselves” by inflating \(n_k\).

---

## Spoken Act II½

Fork makes workers cheap. It does **not** make them independent — shared ancestors leave a variance floor no matter how large \(K\) is.  
Self-consistency votes; we ask each child for estimate, precision, evidence IDs, and lineage.  
In the Gaussian reduce, \(\beta\) is just sample size: cold workers shout louder.  
A cold liar forges that coldness — isolation does not authenticate \(n\).  
\(Z\) and \(\Delta\) are diagnostics of the pool, not proof the lab thermalized.  
Annealing is the liquid factory: explore hot, reduce with teeth, promote once, burn the runners.  
Open problem: a reducer over the fork DAG that can abstain when correlation is unresolved.  
Physics here is an algebra systems people already need — not a claim that agent forks are nature’s Gibbs ensemble.
