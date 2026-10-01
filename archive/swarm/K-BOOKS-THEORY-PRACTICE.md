# Researcher K — Books + classic papers bridging theory ↔ practice
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Scope:** Curated biblio Yossi can *nod to* — systems · algorithms · stat phys / non-eq · RL · coding-agent sandboxes  
**Fence:** Everett / MWI is **NOT** a physics cite for the talk (prefer Feynman path-integral *pedagogy* OR many-worlds as *engineering ontology* already in `PARALLEL-WORLDS-STATPHYS.md`). Physics = interpretation with teeth. No vendor ms as Yossi benchmarks. Prefer primary sources.

**Legend (every entry):**
- **MAIN** — safe on a deck slide (within max-5 cite budget; usually footnote / “see also”)
- **speaker-note** — say in notes / Q&A; not a slide bullet
- **do-not-cite-on-stage** — know it; do not name on stage (cosplay risk, wrong room, or overclaim)

**Deck max-5 reminder:** Firecracker · DeltaBox∨Crab · Shepherd · 2607.09689 · SWE-bench∨Rebound. Everything else here is depth for notes / ROUNDTABLE / post-talk.

---

## A. Top 25 books (theory ↔ practice for THIS talk)

| # | Work | Why it matters for THIS talk | Stage |
|---|---|---|---|
| 1 | **Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau** — *Operating Systems: Three Easy Pieces* (OSTEP; free) | Canonical **fork / address space / CoW / virtual memory** pedagogy. Spoken “fork = copy the process, share until write” lands because SRG already knows this book. | **MAIN** (concept; book title optional footnote) |
| 2 | **Andrew S. Tanenbaum & Herbert Bos** — *Modern Operating Systems* | Broader OS survey; process creation, isolation walls, VMs vs containers framing for Act I trade-off. | speaker-note |
| 3 | **Robert Love** — *Linux Kernel Development* (3e) | `fork`/`clone`, mm, page tables — grounding when Q&A goes kernel-deep on CoW fan-out. | speaker-note |
| 4 | **Daniel P. Bovet & Marco Cesati** — *Understanding the Linux Kernel* | Classic deep dive; use only if a systems person asks “which pages are shared.” | do-not-cite-on-stage (too deep for slides) |
| 5 | **Mendel Rosenblum et al. lineage via** **James E. Smith & Ravi Nair** — *Virtual Machines* | VM / VMM mental model behind Firecracker-class microVMs. | speaker-note |
| 6 | **Martin Kleppmann** — *Designing Data-Intensive Applications* (DDIA) | **MapReduce / batch / replication / consensus** as the *distributed* fork-join mental model. Best bridge from agent fan-out → “we already had map then reduce.” | **MAIN** (mental model; title in notes) |
| 7 | **Leslie Lamport** — *Specifying Systems* (TLA+) | Spec-as-contract cousin of G’s capability contract; promote/epoch as state machine. | speaker-note (Q&A if formal methods) |
| 8 | **Maurice Herlihy & Nir Shavit** — *The Art of Multiprocessor Programming* | Futures, work-stealing intuition, linearizability — vocabulary for split/merge without claiming CRDT≡promote. | speaker-note |
| 9 | **R. K. Pathria & Paul D. Beale** — *Statistical Mechanics* (3e) | Standard equil. toolkit (ensembles, Z, free energy). Nod only: algebra of Z, **not** “sandboxes are canonical ensembles.” | speaker-note (light nod) |
| 10 | **Mehrān Kardar** — *Statistical Physics of Fields* / *Statistical Physics of Particles* | Field/particle view; useful for path-integral *language* without Everett. | speaker-note (light) |
| 11 | **L. D. Landau & E. M. Lifshitz** — *Statistical Physics* (Course of Theoretical Physics Vol. 5) | Classic authority if a physicist asks “which Z.” Prefer Pathria for pedagogy. | do-not-cite-on-stage (intimidation, not talk content) |
| 12 | **N. G. van Kampen** — *Stochastic Processes in Physics and Chemistry* | Master equations / Langevin — cousin of SGD-noise and driven factories (I). | speaker-note |
| 13 | **Crispin Gardiner** — *Stochastic Methods* | Same lane as van Kampen; Fokker–Planck Q&A only. | do-not-cite-on-stage (Fokker–Planck on stage forbidden) |
| 14 | **Udo Seifert** — *Stochastic thermodynamics…* (Rep. Prog. Phys. 2012 review — treat as book-length) | **Non-eq** standard: entropy production, fluctuation theorems, driven systems. Name carefully: toolkit for “promote = irreversible sink,” **not** second-law-for-CI. | speaker-note (name carefully) |
| 15 | **Spinney & Ford** — *Fluctuation relations: A pedagogical overview* (or equiv. intro chapters) | Gentler on-ramp to FT language than Seifert full review. | speaker-note |
| 16 | **J. Schnakenberg / later NESS textbooks** (e.g. **Tânia Tomé & Mário J. de Oliveira** — *Stochastic Dynamics and Irreversibility*) | NESS vocabulary for “steady swarm ≠ equilibrium.” | speaker-note |
| 17 | **Richard P. Feynman & A. R. Hibbs** — *Quantum Mechanics and Path Integrals* (emended ed.) | **Preferred** pedagogy for “sum over histories → sample paths by fork.” Euclidean/stat twin = e^{−βE}. | speaker-note (**prefer over Everett**) |
| 18 | **R. P. Feynman** — *Statistical Mechanics: A Set of Lectures* | Path-integral ↔ stat mech bridge in Feynman’s own voice. | speaker-note |
| 19 | **Hugh Everett III** — *“Relative State” formulation…* (Rev. Mod. Phys. 1957) / DeWitt MWI popularizations | **Engineering ontology already covered** in PARALLEL-WORLDS. **Not** a physics proof for sandboxes. | **do-not-cite-on-stage** |
| 20 | **David J. C. MacKay** — *Information Theory, Inference, and Learning Algorithms* (free) | β, free energy, MCMC, Occam — precision-weighted pooling cousins without Gibbs-of-nature. | speaker-note |
| 21 | **Christopher M. Bishop** — *Pattern Recognition and Machine Learning* | Gaussian pooling / precision matrices mental model for 2607.09689 reduce. | speaker-note |
| 22 | **Richard S. Sutton & Andrew G. Barto** — *Reinforcement Learning: An Introduction* (2e) | **THE** RL cite: episodes, returns, exploration temperature. Rollout = path sample; checkpoint = tip. | **MAIN** (RL factory isomorphism) |
| 23 | **Csaba Szepesvári** — *Algorithms for Reinforcement Learning* | Compact algorithms view if Q&A goes MDP-formal. | speaker-note |
| 24 | **Ian Goodfellow, Yoshua Bengio & Aaron Courville** — *Deep Learning* | SGD / noise / generalization — Act II½ cousin table, not a DL talk. | speaker-note (one breath) |
| 25 | **Tom Mitchell** — *Machine Learning* (1997) or **Bishop** already above; alt: **Russell & Norvig** — *AIMA* (search / agents chapters) | Classical search vs modern agent bodies; AIMA “agent” ≠ MicroVM body — use to *contrast*. | speaker-note |

**Books deliberately omitted as stage cites:** popular MWI books (Carroll *Something Deeply Hidden*, etc.); pop-sci annealing metaphors; vendor whitepapers-as-books.

---

## B. Top 40 papers / primary articles (clustered)

### B1. OS / fork / CoW / CRIU pedigree (1–8)

| # | Paper | Why for THIS talk | Stage |
|---|---|---|---|
| 1 | **Bach & Ritchie lineage / Unix process model** — Thompson/Ritchie Unix papers; modern restatement in OSTEP Ch. on `fork` | Historical *fork* API — the metaphor every SRG person shares. | speaker-note |
| 2 | **The CRIU Project** — Checkpoint/Restore In Userspace (docs + papers; primary: criu.org) | Process C/R substrate DeltaBox/Crab lean on. | speaker-note |
| 3 | **Laadan & Nieh** — *Transparent Checkpoint-Restart of Multiple Processes on Commodity Operating Systems* (USENIX ATC’07) and related Zap/CR work | Academic C/R pedigree before agent sandboxes. | speaker-note |
| 4 | **Dougan / Linux soft-dirty / userfaultfd docs** (kernel docs as primary) | Crab/DeltaBox change-tracking substrate. | do-not-cite-on-stage (mechanism Q&A) |
| 5 | **OverlayFS / union mounts** — Linux kernel docs; early unionfs papers | FS CoW upper layers = DeltaFS cousin. | speaker-note |
| 6 | **KSM / memory dedup papers** (e.g. Arcangeli et al. KSM) | **Side-channel density** foil for F — warmth as wire. | speaker-note (security Q&A) |
| 7 | **vmgenid / virtualization entropy** — Microsoft/Hyper-V & Linux virtio-rng/vmgenid docs | forkd-class CRNG reseed; **≠ WIRE lease revoke** (E fence). | speaker-note |
| 8 | **Xu & Kaffes** — *Toward Systems Foundations for Agentic Exploration* [arXiv:2510.05556](https://arxiv.org/abs/2510.05556) | Names open agenda: fork semantics, side-effects, native CoW. Talk *answers* this. | speaker-note → MAIN if “foundations” slide |

### B2. MicroVMs / serverless snapshot ancestry (9–16)

| # | Paper | Why for THIS talk | Stage |
|---|---|---|---|
| 9 | **Agache et al.** — *Firecracker: Lightweight Virtualization for Serverless Applications* (NSDI’20) | **Pedigree wall** for ESCAPE + snapshot. | **MAIN** |
| 10 | **Kata Containers / Clear Containers** design docs (primary engineering) | Container-in-VM middle wall. | speaker-note |
| 11 | **gVisor** — Singh et al. / Google gVisor paper & docs | Isolation thickness vs fork latency trade-off (Act I). | speaker-note |
| 12 | **Du et al.** — *Catalyzer: Sub-millisecond Startup for Serverless Computing…* (ASPLOS’20) | `sfork` ancestry of warm restore economics. | speaker-note (pedigree) |
| 13 | **Ustiugov et al.** — *REAP* [arXiv:2101.09355](https://arxiv.org/abs/2101.09355) | Prefetch / working-set for restore. | speaker-note |
| 14 | **Ao et al.** — *FaaSnap* (EuroSys’22) | Concurrent paging / snapshot lineage. | speaker-note |
| 15 | **Wang / Firecracker snapshot docs** (AWS primary docs) | Productized snapshot API; eng only for latency. | do-not-cite-on-stage (no vendor ms) |
| 16 | **Cloud Hypervisor** project docs | Tensorlake’s other MicroVM backend (docs). | speaker-note (landscape) |

### B3. MapReduce → Spark → Dryad → CIEL → Ray (17–24)

| # | Paper | Why for THIS talk | Stage |
|---|---|---|---|
| 17 | **Dean & Ghemawat** — *MapReduce* (OSDI’04) | **Canonical map→reduce.** Agent fork = map; trustworthy pool = reduce. | **MAIN** (mental model) |
| 18 | **Isard et al.** — *Dryad: Distributed Data-Parallel Programs…* (EuroSys’07) | DAG generalization beyond flat map/reduce. | speaker-note |
| 19 | **Yu et al.** — *DryadLINQ* (OSDI’08) | High-level DAG; lineage of “plan then execute.” | speaker-note |
| 20 | **Zaharia et al.** — *Spark: Cluster Computing with Working Sets* (HotCloud’10) / RDD paper (NSDI’12) | **RDD lineage** = recompute from parent — cousin of snapshot lineage + world-diff. | speaker-note → MAIN if lineage slide |
| 21 | **Murray et al.** — *CIEL: A Universal Execution Engine for Distributed Data-Flow Computing* (NSDI’11) | Dynamic task graphs — closer to agent-time DAG mutation. | speaker-note |
| 22 | **Moritz et al.** — *Ray* (OSDI’18) [arXiv:1712.05889](https://arxiv.org/abs/1712.05889) | **Actors + tasks** — RL sim+train; dynamic graphs MapReduce lacks. | speaker-note |
| 23 | **Power & Li / Naiad** — *Naiad: A Timely Dataflow System* (SOSP’13) | Timely/differential dataflow; static-graph foil to Ray. | do-not-cite-on-stage (unless Q&A) |
| 24 | **Eliaz et al.** — *Evidence-Aware / Boltzmann MapReduce* [arXiv:2607.09689](https://arxiv.org/abs/2607.09689) | **THIS talk’s reduce.** β≡n, cold liar, abstain. | **MAIN** |

### B4. MCMC / SA / SGD classics (25–30)

| # | Paper | Why for THIS talk | Stage |
|---|---|---|---|
| 25 | **Metropolis et al.** — *Equation of State Calculations by Fast Computing Machines* (JCP 1953) | **MH accept/reject** = keep/revert in a fork. | speaker-note (Act II½) |
| 26 | **Hastings** — *Monte Carlo Sampling Methods…* (Biometrika 1970) | MH generalization. | speaker-note |
| 27 | **Kirkpatrick, Gelatt & Vecchi** — *Optimization by Simulated Annealing* (Science 1983) | **T schedule** = liquid factory: hot explore → cool → promote. | speaker-note (**MAIN** if anneal slide) |
| 28 | **Geman & Geman** — *Stochastic Relaxation…* (IEEE PAMI 1984) | Annealing + Bayesian image models; pedigree. | do-not-cite-on-stage |
| 29 | **Robbins & Monro** — *A Stochastic Approximation Method* (1951) | SGD ancestor. | speaker-note |
| 30 | **Welling & Teh** — *Bayesian Learning via Stochastic Gradient Langevin Dynamics* (ICML’11) | Langevin–SGD cousin for I/H table. | speaker-note |

### B5. Non-equilibrium / stochastic thermo (31–34)

| # | Paper | Why for THIS talk | Stage |
|---|---|---|---|
| 31 | **Seifert** — *Stochastic thermodynamics, fluctuation theorems and molecular machines* (Rep. Prog. Phys. **75** 126001, 2012) [arXiv:1205.4176](https://arxiv.org/abs/1205.4176) | Standard non-eq review. **Nod:** driven systems, entropy production. **Refuse:** Jarzynski derivation for CI. | speaker-note (name carefully) |
| 32 | **Jarzynski** — *Nonequilibrium Equality for Free Energy Differences* (PRL 1997) | Famous FT — **Q&A only**; never “we proved second law for merge.” | **do-not-cite-on-stage** |
| 33 | **Crooks** — *Entropy production fluctuation theorem…* (PRE 1999) | Same fence as Jarzynski. | **do-not-cite-on-stage** |
| 34 | **Spinney & Ford** — pedagogical FT overview (contemporary reviews) | Safer spoken pointer than proving FT on stage. | speaker-note |

### B6. RL post-training / envs / verifiable rewards (35–40)

| # | Paper | Why for THIS talk | Stage |
|---|---|---|---|
| 35 | **Schulman et al.** — *Proximal Policy Optimization* (PPO) [arXiv:1707.06347](https://arxiv.org/abs/1707.06347) | Workhorse policy gradient; KL / clip ≈ dissipative regularizer (I). | speaker-note |
| 36 | **Shao et al. / DeepSeek** — GRPO (DeepSeekMath / R1 lineage; e.g. [DeepSeek-R1](https://arxiv.org/abs/2501.12948)) | Group rollouts = fork fan-out; advantage from group — **ρ caution** under shared snapshot. | speaker-note |
| 37 | **Jiménez et al.** — *SWE-bench* [arXiv:2310.06770](https://arxiv.org/abs/2310.06770) | Isolated coding oracle; why sandboxes became inevitable. | **MAIN** (or Rebound) |
| 38 | **Liu / Xia et al. Agentless; OpenHands; related scaffolds** (pick one primary) | Harness vs body split. | speaker-note |
| 39 | **Rebound→Remedy** [arXiv:2604.01476](https://arxiv.org/abs/2604.01476); **SpecBench** [arXiv:2605.21384](https://arxiv.org/abs/2605.21384) | Oracle must leave the fork; held-out gaps. | **MAIN** (pick vs SWE-bench) |
| 40 | **SandboxEscapeBench** [arXiv:2603.02277](https://arxiv.org/abs/2603.02277) | Container escape → Firecracker wall. | speaker-note |

### B7. Peer fork systems for agents (extra depth — still within “40+” talk set; cite as A’s MAIN)

These are **already** deck-budget peers — listed so K’s biblio is self-contained:

| Paper | Role | Stage |
|---|---|---|
| **DeltaBox** [2605.22781](https://arxiv.org/abs/2605.22781) | ms coupled FS+mem C/R | **MAIN** (xor Crab) |
| **Crab** [2604.28138](https://arxiv.org/abs/2604.28138) | semantics-aware C/R | **MAIN** (xor DeltaBox) |
| **Shepherd** [2605.10913](https://arxiv.org/abs/2605.10913) | fork-as-value / Tree-GRPO | **MAIN** |
| **OpenRath** [2606.19409](https://arxiv.org/abs/2606.19409) | Session as runtime value | speaker-note |

### B8. Coding agents / auto-research / HIL (speaker-note cluster — solid only)

| Work | Why | Stage |
|---|---|---|
| **AIDE²** [2609.26457](https://arxiv.org/abs/2609.26457); **RRSI** [2609.24972](https://arxiv.org/abs/2609.24972); **DGM** [2505.22954](https://arxiv.org/abs/2505.22954); **GEAR** [2605.13874](https://arxiv.org/abs/2605.13874) | Outer harness RSI under frozen eval — D’s beat | speaker-note |
| **AI Scientist** / AutoResearchClaw-class | Paper tip = scarce sociology tip | speaker-note (no AGI claim) |
| **Ouyang et al.** — InstructGPT / RLHF (NeurIPS’22) | Post-training survey anchor if asked “where RL entered LLMs” | speaker-note |
| **Bai et al.** — Constitutional AI; **Rafailov et al.** — DPO | Prefer RLHF/DPO only if Q&A; not Act II core | speaker-note |
| **Mnih et al.** — DQN (2015); **Silver et al.** — AlphaGo/AlphaZero | Tree search / MCTS pedigree for Tree-GRPO analogy | speaker-note |
| **Coulom / Kocsis & Szepesvári** — MCTS / UCT | Tree search ↔ Shepherd Tree-RL | speaker-note |

---

## C. Parallel-worlds metaphor — citation rule (hard)

| Allowed | Forbidden on stage |
|---|---|
| Feynman path-integral *pedagogy* (sum over histories → fork samples paths) | “Everett proves sandboxes” / MWI as physics warrant |
| Many-worlds as **engineering ontology** (branch / decoherence≈isolate / world-selection=promote) — already in `PARALLEL-WORLDS-STATPHYS.md` | DeWitt / Deutsch / Carroll popular MWI as deck cites |
| β≡n from **2607.09689** LAN/Wald reduce | Agent forks are Gibbs ensembles of nature |
| Non-eq: driven / NESS / promote=sink (Seifert *vocabulary*) | Jarzynski equality for CI merges |

---

## D. Quick “nod lines” (≤6)

1. “OSTEP fork — then Firecracker made the *machine* forkable.”  
2. “Dean/Ghemawat gave us map→reduce; we still owe an evidence-aware reduce after CoW.”  
3. “Kirkpatrick’s T schedule is the liquid factory — explore hot, promote as sink.”  
4. “Sutton & Barto: the rollout is a path; the checkpoint is a tip.”  
5. “Seifert for vocabulary of drive and dissipation — not a second-law slide.”  
6. “Feynman path sums — not Everett — for the parallel-worlds diagram.”

---

## E. Challenges → J / L / B / H / I

- **→ J:** Product MEMORY clone makes worlds cheap; which *three* book/paper nods keep SRG from hearing a vendor pitch?  
- **→ L:** MapReduce→Ray lineage must contrast CRDTs vs promote-once and Git merge vs world-diff without sliding into distributed-systems TED talk.  
- **→ B/H/I:** Confirm Seifert/Kirkpatrick stay speaker-note; 2607.09689 + Firecracker stay MAIN.

---

*Researcher K deep biblio · 2026-09-27 IDT · Top 25 books + Top 40 papers (+ peer fork extras). Prefer USENIX/ACM/arXiv primary over SEO lists.*

---

## F. Primary URL cheatsheet (prefer these)

| Work | URL |
|---|---|
| Firecracker NSDI’20 | https://www.usenix.org/conference/nsdi20/presentation/agache |
| MapReduce OSDI’04 | https://www.usenix.org/conference/osdi-04/mapreduce-simplified-data-processing-large-clusters |
| Dryad EuroSys’07 | ACM / Isard et al. (EuroSys 2007) |
| Spark HotCloud’10 | https://www.usenix.org/conference/hotcloud-10/spark-cluster-computing-working-sets |
| Spark RDD NSDI’12 | https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia |
| CIEL NSDI’11 | https://www.usenix.org/conference/nsdi11/ciel-universal-execution-engine-distributed-data-flow-computing |
| Ray OSDI’18 | https://www.usenix.org/conference/osdi18/presentation/moritz · arXiv:1712.05889 |
| Catalyzer ASPLOS’20 | ACM DL |
| REAP | https://arxiv.org/abs/2101.09355 |
| FaaSnap EuroSys’22 | ACM DL |
| Seifert 2012 | https://arxiv.org/abs/1205.4176 · https://iopscience.iop.org/article/10.1088/0034-4885/75/12/126001 |
| Kirkpatrick SA 1983 | Science 220:671 |
| Metropolis 1953 | J. Chem. Phys. 21:1087 |
| Sutton & Barto 2e | http://incompleteideas.net/book/the-book-2nd.html |
| OSTEP | https://ostep.org/ |
| DDIA | https://dataintensive.net/ |
| Evidence-Aware MR | https://arxiv.org/abs/2607.09689 |
| DeltaBox | https://arxiv.org/abs/2605.22781 |
| Crab | https://arxiv.org/abs/2604.28138 |
| Shepherd | https://arxiv.org/abs/2605.10913 |
| Xu–Kaffes | https://arxiv.org/abs/2510.05556 |
| SWE-bench | https://arxiv.org/abs/2310.06770 |
| Rebound→Remedy | https://arxiv.org/abs/2604.01476 |
| SpecBench | https://arxiv.org/abs/2605.21384 |
| EscapeBench | https://arxiv.org/abs/2603.02277 |
| DeepSeek-R1 | https://arxiv.org/abs/2501.12948 |
| PPO | https://arxiv.org/abs/1707.06347 |
| SGLD | Welling & Teh ICML 2011 |
| Feynman & Hibbs | Path Integrals (emended Dover/emended eds.) |
| Pathria/Beale | Academic Press Statistical Mechanics 3e |
| Kardar | CUP Statistical Physics of Particles / Fields |
| MacKay ITILA | https://www.inference.org.uk/mackay/itila/ |
| PARALLEL-WORLDS (repo) | scratch/PARALLEL-WORLDS-STATPHYS.md |

---

## G. Extra ranked papers (41–55) — still speaker-note / Q&A depth

| # | Work | Cluster | Stage |
|---|---|---|---|
| 41 | **Blumofe & Leiserson** — *Scheduling Multithreaded Computations by Work Stealing* (JACM’99) | work-stealing | speaker-note |
| 42 | **Halstead** — *Multilisp* / futures (1985) | futures | speaker-note |
| 43 | **Valiant** — *A Bridging Model for Parallel Computation* (BSP, CACM’90) | barrier foil | speaker-note |
| 44 | **Shapiro et al.** — *Conflict-Free Replicated Data Types* (SSS’11 / tech reports) | CRDT≠promote | speaker-note |
| 45 | **Lamport** — *Time, Clocks…* (1978); **Paxos** papers | authority / consensus Q&A | do-not-cite-on-stage |
| 46 | **Hajek** — *Cooling Schedules for Optimal Annealing* (Math OR 1988) | SA theory | do-not-cite-on-stage |
| 47 | **Bertsimas & Tsitsiklis** — *Simulated Annealing* (Stat Sci 1993) | SA survey | speaker-note |
| 48 | **Ghemawat et al.** — *Google File System* (SOSP’03) | map substrate | speaker-note |
| 49 | **Hindman et al.** — *Mesos* (NSDI’11); **Vavilapalli et al.** — *YARN* | cluster schedulers (Nomad cousin lane) | speaker-note |
| 50 | **Verma et al.** — *Large-scale cluster management at Google with Borg* (EuroSys’15) | scheduler pedigree | speaker-note |
| 51 | **Barham et al.** — *Xen and the Art of Virtualization* (SOSP’03) | VMM pedigree | speaker-note |
| 52 | **Young et al. / Firecracker snapshot deep-dives** (AWS eng blogs) | eng only | do-not-cite-on-stage |
| 53 | **OpenAI** — *Gym* / **Towers et al.** — Gymnasium; **Bellemare et al.** — Arcade Learning Environment | RL env abstraction vs MicroVM body | speaker-note |
| 54 | **Christiano et al.** — *Deep RL from Human Preferences* (2017) | RLHF root | speaker-note |
| 55 | **Ouyang et al.** — *Training language models to follow instructions with human feedback* (NeurIPS’22) | InstructGPT / modern post-training | speaker-note (solid) |

**Count check:** Books 1–25 · Core papers 1–40 · Peer fork extras (DeltaBox/Crab/Shepherd/OpenRath) · Depth 41–55. Deck still max-5.

---

## H. Per-act citation routing (speaker cheat)

| Act | Pull from K | Avoid |
|---|---|---|
| **0 Hook** | OSTEP fork metaphor (no title needed) | Everett |
| **I Execution contract** | Firecracker; CRIU/Catalyzer pedigree; Xu–Kaffes gaps | Vendor ms |
| **II Factories** | MapReduce; Sutton/Barto; Shepherd Tree-GRPO | “Spark=agent OS” |
| **II½ Boltzmann+anneal** | 2607.09689; Kirkpatrick; Metropolis; Seifert *vocab* | Jarzynski proof |
| **III Open problems** | WIRE/CRDT contrast; world-diff; abstain | AGI scientist |
| **Q&A** | Ray; DDIA; Feynman paths; EscapeBench; Rebound | Fokker–Planck lecture |

