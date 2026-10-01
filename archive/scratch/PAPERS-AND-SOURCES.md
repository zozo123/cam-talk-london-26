# Papers & sources — Cambridge SRG (15 Oct 2026)

**Talk:** Forkable Sandboxes: The Runtime Layer for AI Software Factories  
**Speaker:** Yossi Eliaz · CL Systems Research Group · FW11 · 15:00–16:00  
**Curated:** 2026-09-27 (Asia/Jerusalem) · deep pass over arXiv / HF / primary systems pages  
**Companion docs:** `STORY-SPINE.md`, `UNIVERSAL-HILLCLIMB.md`

**Thesis this bibliography supports:** forkable sandboxes are the execution substrate for a universal hill-climb loop  
`(propose → isolate → measure → keep/revert → promote)` used by auto-software, auto-build, RL post-training, simulation science, computational biology, HIL, and auto-research.  
**Inspirations (methodology, not peer review):** pstack (fearless parallelism + hillclimb), OpenClaw (agent loop), ariflow-swfactory (Search≠Authority, Cell/epoch).

---

## 1. Ranking rule

| Route | Meaning | Stage use |
|---|---|---|
| **MAIN** | Peer-primary, directly supports a slide claim, low claim-risk | On-slide citation (≤5 total) |
| **BACKUP** | Strong Q&A / speaker-notes; may be high-signal but niche, engineering, or adjacent | Verbal if challenged |
| **DO NOT USE** | Wrong door, marketing, SEO blog, duplicate secondary, high claim-risk on stage, or PleaseFix-class browser agent fluff | Exclude from deck |

**Door / slot keys** (from story spine):  
`KEY` identity · `FOLDER` workspace/state · `WIRE` credentials/network · `VERDICT` oracle/tests · `ESCAPE` isolation boundary · `ORACLE` reward/eval authority · `FORK` CoW/snapshot branch · `REDUCE` evidence fan-in · `PROMOTE` singular authority merge

**Claim-risk:** low = peer venue / canonical systems paper · med = strong arXiv / systems prototype · high = engineering repo numbers, blog, or contested RSI claim

---

## 2. Top 15 “must know” for this talk

| # | Item | Year | Slot | Route | Relevance (1–2 sentences) | Claim-risk | Primary URL |
|---|---|---|---|---|---|---|---|
| 1 | **Evidence-Aware MapReduce / Boltzmann MapReduce** — Yossi Eliaz | 2026 | REDUCE | **MAIN** | Your paper: cheap forks ≠ independent evidence; worker record carries estimate, precision, evidence IDs, fork lineage; inverse-information reduce + Δ disagreement. Owns the Search≠Authority reduce story. | low | https://arxiv.org/abs/2607.09689 · artifact https://github.com/zozo123/boltzmann-mapreduce |
| 2 | **Firecracker** — Agache et al., NSDI’20 | 2020 | FORK / ESCAPE | **MAIN** | Canonical microVM for serverless; snapshot/restore pedigree every agent sandbox cites. Pedigree slide, not “we invented VMs.” | low | https://www.usenix.org/conference/nsdi20/presentation/agache |
| 3 | **DeltaBox** — Dong, Du, Xia, Chen et al. | 2026 | FORK | **MAIN** | OS-level change-based C/R for stateful agents (DeltaFS + DeltaCR on Firecracker); ~11 ms ckpt / ~2 ms restore; SWE-bench MCTS + RL fan-out. Closest systems twin to “fork is the API.” | low–med | https://arxiv.org/abs/2605.22781 |
| 4 | **Crab** — Wu, Chang, Cao, Gao, Wang (HKUST) | 2026 | FORK | **MAIN** | Semantics-aware C/R: eBPF inspector skips ≤87% of turns; turn-aligned, LLM-wait overlap; RL branching + safe rollback. Complements DeltaBox (what/when vs how-fast). | low–med | https://arxiv.org/abs/2604.28138 |
| 5 | **Shepherd** — Yu, Chong, Manning, Shi et al. | 2026 | FORK / REDUCE / ORACLE | **MAIN** | Meta-agent substrate: reversible Git-like agent+env trace; fork 5× faster than docker commit; Tree-GRPO + runtime supervisor + counterfactual replay. Academic twin of Controllable fork + promote. | med | https://arxiv.org/abs/2605.10913 · HF https://huggingface.co/papers/2605.10913 |
| 6 | **Toward Systems Foundations for Agentic Exploration** — Xu, Zhou, Wu, Kaffes | 2025 | FORK | BACKUP→MAIN if “foundations” slide | Position paper naming fork semantics, external side-effects, native CoW fork as the gap. Frame your talk as answering this agenda. | med | https://arxiv.org/abs/2510.05556 |
| 7 | **SWE-bench** — Jimenez et al., ICLR’24 | 2024 | VERDICT / FOLDER | **MAIN** (benchmark pedigree) | Real GitHub issues in isolated envs; the oracle that made coding-agent sandboxes inevitable. | low | https://arxiv.org/abs/2310.06770 |
| 8 | **OpenHands** (OpenDevin) — Wang, Neubig et al. | 2024–26 | FOLDER / ESCAPE | BACKUP | Docker/runtime abstraction for generalist coding agents; production SDK separates workspace from control plane. | low–med | https://arxiv.org/abs/2407.16741 · SDK https://arxiv.org/abs/2511.03690 |
| 9 | **From Rebound to Remedy** — reward hacking via env manipulation | 2026 | ORACLE / VERDICT / ESCAPE | BACKUP→MAIN for RL Act | Coding RL where agents rewrite evaluator tests; three-phase rebound; Advantage Modification. Proves why oracle must live *outside* the forked body. | med | https://arxiv.org/abs/2604.01476 |
| 10 | **The AI Scientist / v2** — Lu, Sakana et al. → Nature 2026 | 2024–26 | ORACLE / PROMOTE | BACKUP | End-to-end auto-research (ideate→experiment→paper); promote-to-claim is the scarce tip. Use as factory metaphor, not “solved science.” | med–high (overclaim risk) | https://arxiv.org/abs/2408.06292 · Nature https://www.nature.com/articles/s41586-026-10265-5 |
| 11 | **AIDE²** — recursive self-improvement of research agents | 2026 | ORACLE / PROMOTE | BACKUP | Outer loop rewrites agent harness under frozen eval budget; RSI with hidden eval. Strong “hill-climb the harness” cite. | med–high | https://arxiv.org/abs/2609.26457 · https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement |
| 12 | **RRSI** — Regularized Recursive Self-Improvement of Agent Harnesses | 2026 | ORACLE / PROMOTE | BACKUP | Constrains harness evolution to avoid OOD collapse; up to +14.1 ID / +4.7 OOD. Regularization = Search≠Authority for RSI. | med | https://arxiv.org/abs/2609.24972 · HF trending |
| 13 | **Self-consistency** — Wang et al., ICLR’23 | 2023 | REDUCE | BACKUP (classical) | Majority vote over sampled paths — the naive reduce your paper upgrades with precision + lineage. | low | https://arxiv.org/abs/2203.11171 |
| 14 | **SandboxEscapeBench** — AISI / collaborators | 2026 | ESCAPE | BACKUP (security Q&A) | Frontier LLMs exploit container misconfigs; nested VM for safe measurement. Justifies Firecracker-class walls for untrusted agent code. | med | https://arxiv.org/abs/2603.02277 |
| 15 | **OpenRath** — Wen, Wang, Xu | 2026 | KEY / FORK / REDUCE | BACKUP | Session as first-class branchable runtime value (fork/merge/replay); PyTorch-like programming model for agent state. Complements Shepherd on the “what object flows” axis. | med | https://arxiv.org/abs/2606.19409 |

**Yossi field manual (systems essay, not peer paper):** https://zozo123.github.io/sandboxes-why-how-when/  
**islo (product substrate used in your artifact):** https://islo.dev/sandboxes/

---

## 3. Cluster tables A–F

### A. MicroVM / Firecracker / forkable / snapshot / CoW sandboxes

| Title | Authors | Year | Venue / id | Relevance | Slot | Risk | URL | Route |
|---|---|---|---|---|---|---|---|---|
| Firecracker: Lightweight Virtualization for Serverless Applications | Agache, Brooker, Iordache, Liguori, Neugebauer, Piwonka, Popa | 2020 | NSDI | Pedigree for microVM isolation + density; every agent sandbox stack descends from this. | FORK / ESCAPE | low | https://www.usenix.org/conference/nsdi20/presentation/agache | MAIN |
| Catalyzer: Sub-millisecond Startup for Serverless Computing with Initialization-less Booting | Du, Yu, Xia, Zang, Yan, Qin, Wu, Chen | 2020 | ASPLOS | `sfork` / checkpoint-image boot; ancestor of agent fork latency claims. | FORK | low | https://dl.acm.org/doi/10.1145/3373376.3378512 | BACKUP |
| Benchmarking, Analysis, and Optimization of Serverless Function Snapshots (REAP) | Ustiugov, Petrov, Kogias, Bugnion, Grot | 2021 | ASPLOS | Working-set prefetch via userfaultfd; explains SnapStart / lazy restore. | FORK | low | https://arxiv.org/pdf/2101.09355 | BACKUP |
| FaaSnap: FaaS made fast using snapshot-based VMs | Ao, Porter, Voelker | 2022 | EuroSys | Concurrent paging for VM snapshots; baseline for restore economics. | FORK | low | https://dl.acm.org/doi/10.1145/3492321.3524270 | BACKUP |
| DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback | Dong, He, Liu, Hou, Du, Xu, Yu, Yang, Xia, Chen | 2026 | arXiv 2605.22781 | Change-based FS+process C/R on Firecracker; MCTS + RL fan-out; CoW sharing across branches. | FORK | low–med | https://arxiv.org/abs/2605.22781 | MAIN |
| Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes | Wu, Chang, Cao, Gao, Wang | 2026 | arXiv 2604.28138 | Skip unnecessary ckpts via eBPF net-change; hide cost under LLM wait; RL tree branch + spot + speculative act. | FORK | low–med | https://arxiv.org/abs/2604.28138 | MAIN |
| Toward Systems Foundations for Agentic Exploration | Xu, Zhou, Wu, Kaffes | 2025 | arXiv 2510.05556 | Names fork semantics / side-effects / native CoW as open systems agenda. | FORK | med | https://arxiv.org/abs/2510.05556 | BACKUP |
| Shepherd: Enabling Programmable Meta-Agents via Reversible Agentic Execution Traces | Yu, Chong, Nandi, Soylu, Sun, Manning, Shi | 2026 | arXiv 2605.10913 | Agent+env fork as first-class FP object; Lean-mechanized effects; Tree-GRPO. | FORK / REDUCE | med | https://arxiv.org/abs/2605.10913 | MAIN |
| OpenRath: Session-Centered Runtime State for Agent Systems | Wen, Wang, Xu | 2026 | arXiv 2606.19409 | Session as branchable/inspectable/replayable value carrying sandbox placement + lineage. | KEY / FORK | med | https://arxiv.org/abs/2606.19409 | BACKUP |
| forkd — Fork() for AI agent microVMs | deeplethe (eng.) | 2026 | GitHub | Spawn ~100 children / ~100 ms from warm parent; live BRANCH ~150 ms; Firecracker CoW mmap. Demo numbers ≠ your benchmarks. | FORK | high | https://github.com/deeplethe/forkd | BACKUP |
| Agent libOS: A Library-OS-Inspired Runtime for Long-Running, Capability-Controlled LLM Agents | — | 2026 | arXiv 2606.03895 | Process-like execution + capability boundaries for long-running agents. | ESCAPE / KEY | med | https://arxiv.org/abs/2606.03895 | BACKUP |
| Quantifying Frontier LLM Capabilities for Container Sandbox Escape (SandboxEscapeBench) | UK AISI et al. | 2026 | arXiv 2603.02277 | Agents escape Docker-class sandboxes; nested VM measurement. Justifies microVM wall. | ESCAPE | med | https://arxiv.org/abs/2603.02277 | BACKUP |

*Industry landscape (BACKUP, name once):* E2B, Daytona, Tensorlake, Modal, islo.dev — API-exposed Firecracker/container sandboxes; cite field manual for the ladder, not vendor blogs.

---

### B. Coding agents + isolated execution environments

| Title | Authors | Year | Venue / id | Relevance | Slot | Risk | URL | Route |
|---|---|---|---|---|---|---|---|---|
| SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan | 2024 | ICLR | Canonical isolated-repo oracle; makes fork/reset economically necessary. | VERDICT / FOLDER | low | https://arxiv.org/abs/2310.06770 | MAIN |
| SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press | 2024 | NeurIPS | ACI design; Docker-backed interaction loop. | FOLDER / WIRE | low | https://arxiv.org/abs/2405.15793 | BACKUP |
| OpenHands: An Open Platform for AI Software Developers as Generalist Agents | Wang, Neubig et al. | 2024–25 | ICLR’25 / arXiv 2407.16741 | Docker runtime + action execution server; warm pools; remote workspaces. | FOLDER / ESCAPE | low–med | https://arxiv.org/abs/2407.16741 | BACKUP |
| The OpenHands Software Agent SDK | — | 2025 | arXiv 2511.03690 | Event-sourced SDK; Local vs Remote conversation; sandbox optional. | FOLDER | med | https://arxiv.org/abs/2511.03690 | BACKUP |
| R2E-Gym: Procedural Environments and Hybrid Verifiers for Scaling Open-Weights SWE Agents | — | 2025 | arXiv 2504.07164 | 8.1K procedural envs; execution + execution-free verifiers; SWE-bench Verified ~51%. | VERDICT / ORACLE | med | https://arxiv.org/abs/2504.07164 | BACKUP |
| SWE-Gym: Training Software Engineering Agents and Verifiers | — | 2024 | arXiv 2412.21139 | Real Python tasks as RL/env substrate. | ORACLE | med | https://arxiv.org/abs/2412.21139 | BACKUP |
| daVinci-Env / OpenSWE: Open SWE Environment Synthesis at Scale | — | 2026 | arXiv 2603.13023 | 45k+ executable envs; transparent SWE training scale. | FOLDER / ORACLE | med | https://arxiv.org/abs/2603.13023 | BACKUP |
| SWE-World: Building SWE Agents in Docker-Free Environments | — | 2026 | arXiv 2602.03419 | Learned surrogates replace physical Docker for training/test-time scaling — *contrast* with your “real fork” thesis. | ORACLE | med–high | https://arxiv.org/abs/2602.03419 | BACKUP (contrast) |
| Dockerless: Environment-Free Program Verifier for Coding Agents | — | 2026 | arXiv 2606.28436 | Verifier without execution — high HF engagement; use as foil for “oracle must run somewhere.” | VERDICT | med | https://arxiv.org/abs/2606.28436 | BACKUP (foil) |
| SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents | — | 2026 | arXiv 2605.21384 | Visible vs held-out tests; detects test-gaming. | VERDICT / ORACLE | med | https://arxiv.org/abs/2605.21384 | BACKUP |
| The Balkanization of Execution-Security Research for AI Coding Agents | — | 2026 | arXiv 2607.05743 | Isolation vs access-control vs TOCTOU fragmentation — good Escape-door survey. | ESCAPE | med | https://arxiv.org/abs/2607.05743 | BACKUP |

**HF datasets (bookmark, not cite as papers):**  
`SWE-bench/SWE-bench_Verified` · `ScaleAI/SWE-bench_Pro` · `princeton-nlp/SWE-bench` · `SWE-bench/SWE-smith-trajectories`

---

### C. RL / post-training environments, rollout isolation, reward hacking

| Title | Authors | Year | Venue / id | Relevance | Slot | Risk | URL | Route |
|---|---|---|---|---|---|---|---|---|
| From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering | — | 2026 | arXiv 2604.01476 | Agents rewrite evaluator code under RL; rebound pattern; Advantage Modification. **Oracle outside the fork.** | ORACLE / ESCAPE | med | https://arxiv.org/abs/2604.01476 | MAIN-adjacent |
| LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking | — | 2026 | arXiv 2604.15149 | Extensional vs isomorphic verifiers; RLVR induces shortcuts mid-training. | ORACLE | med | https://arxiv.org/abs/2604.15149 | BACKUP |
| School of Reward Hacks | MacDiarmid et al. / collaborators | 2025 | arXiv 2508.17511 | Harmless reward hacks generalize to misalignment — stage caution on “more rollouts ⇒ better.” | ORACLE | med–high | https://arxiv.org/abs/2508.17511 | BACKUP |
| SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents | — | 2026 | arXiv 2605.21384 | Held-out tests vs visible validation. | VERDICT | med | https://arxiv.org/abs/2605.21384 | BACKUP |
| Hack-Verifiable Environments / Reward Hacking Benchmark | — | 2026 | arXiv 2605.20744 / 2605.02964 | Embed exploit scenarios for automated detection. | ORACLE | med | https://arxiv.org/abs/2605.20744 | BACKUP |
| Proof-of-Use: Mitigating Tool-Call Hacking in Deep Research Agents | — | 2025 | arXiv 2510.10931 | Evidence-grounded RL; cite IDs for retrieval→answer causality. | REDUCE / ORACLE | med | https://arxiv.org/abs/2510.10931 | BACKUP |
| LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents | — | 2026 | arXiv 2608.17393 | In-process LLM proxy + sandbox orchestration; stage-wise sandbox defenses against exploitation. | FORK / ORACLE | med | https://arxiv.org/abs/2608.17393 | BACKUP |
| ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents | Microsoft Research et al. | 2026 | arXiv 2603.18815 | Decoupled HTTP rollout service managing sandboxes asynchronously — factory infra for rollouts. | FORK / WIRE | med | https://arxiv.org/abs/2603.18815 | BACKUP |
| Agent-RLVR: Training SWE Agents via Guidance and Environment Rewards | — | 2025 | arXiv 2506.11425 | Guidance + env rewards for agentic RLVR. | ORACLE | med | https://arxiv.org/abs/2506.11425 | BACKUP |
| Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis | — | 2026 | arXiv 2608.14312 | Synthesizes per-seed training envs via verifier rewards. | ORACLE / FOLDER | med | https://arxiv.org/abs/2608.14312 | BACKUP |
| Shepherd Tree-GRPO (§5.3) | Yu et al. | 2026 | part of 2605.10913 | Cheap fork enables sibling rollouts for per-step credit — RL Act demo. | FORK / ORACLE | med | https://arxiv.org/abs/2605.10913 | MAIN-adjacent |
| Large Language Monkeys: Scaling Inference Compute with Repeated Sampling | Brown et al. | 2024 | arXiv 2407.21787 | Best-of-N / coverage from many samples — motivates fan-out before reduce. | FORK / REDUCE | low | https://arxiv.org/abs/2407.21787 | BACKUP |

---

### D. AI scientist / auto-research / self-improving agents / lab automation

| Title | Authors | Year | Venue / id | Relevance | Slot | Risk | URL | Route |
|---|---|---|---|---|---|---|---|---|
| The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | Lu et al. (Sakana) | 2024 | arXiv 2408.06292 | Ideation→experiment→paper loop; sandbox empiricism. | ORACLE / PROMOTE | med–high | https://arxiv.org/abs/2408.06292 | BACKUP |
| Towards end-to-end automation of AI research (AI Scientist-v2) | Sakana et al. | 2026 | Nature | Template-free agentic tree search; workshop-level papers. Cite carefully — overclaim risk on stage. | PROMOTE | high | https://www.nature.com/articles/s41586-026-10265-5 | BACKUP |
| Recursive self-improvement of AI research agents (AIDE²) | Weco et al. | 2026 | arXiv 2609.26457 | Outer loop rewrites harness under frozen compute/eval; RSI evidence with caveats. | ORACLE / PROMOTE | med–high | https://arxiv.org/abs/2609.26457 | BACKUP |
| GEAR: Genetic AutoResearch for Agentic Code Evolution | — | 2026 | arXiv 2605.13874 | Population frontier vs single-incumbent hillclimb — maps to pstack swarm. | ORACLE / REDUCE | med | https://arxiv.org/html/2605.13874 | BACKUP |
| RRSI: Regularized Recursive Self-Improvement of Agent Harnesses | — | 2026 | arXiv 2609.24972 | Annealed edit budget + critic/pruner; OOD regularization. | ORACLE / PROMOTE | med | https://arxiv.org/abs/2609.24972 | BACKUP |
| Hierarchical Self-Improvement (HSI) | — | 2026 | arXiv 2608.08466 | Harness / evolver / meta-evolver with frozen outer anchor. | ORACLE | med | https://arxiv.org/abs/2608.08466 | BACKUP |
| AutoResearchClaw: Self-Reinforcing Autonomous Research with HIL | Liu et al. | 2026 | arXiv 2605.20025 | Pivot/Refine on failure; verifiable reporting; 7 HIL modes; beats AI Scientist v2 on ARC-Bench. | ORACLE / PROMOTE | med | https://arxiv.org/abs/2605.20025 | BACKUP |
| Darwin Gödel Machine | Zhang, Hu, Lu, Lange, Clune (Sakana) | 2025 | arXiv 2505.22954 | Archive of self-modifying agents; sandbox empiricism not proofs. | ORACLE | med–high | https://arxiv.org/abs/2505.22954 | BACKUP |
| Paper2Agent: Reimagining Research Papers As Interactive AI Agents | — | 2025 | arXiv 2509.06917 | Papers → interactive agents; dissemination, not discovery. | KEY | med | https://arxiv.org/abs/2509.06917 | BACKUP |
| SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness | — | 2026 | arXiv 2609.20519 | Token-efficiency of unattended exploration loops. | ORACLE | med | https://arxiv.org/abs/2609.20519 | BACKUP |
| AutoResearch AI / Personalized Auto-Research | — | 2026 | arXiv 2605.23204 / 2608.14881 | Workflow-level automation + researcher-conditioned loops. | ORACLE | med | https://arxiv.org/abs/2605.23204 | BACKUP |

*Bio / wet-lab note:* treat computational biology as the same loop with an expensive wet oracle — prefer systems metaphors over wet-lab marketing. Pair with scarcity ladder (million compiles / one assay).

---

### E. Evidence aggregation / ensemble reduce / MapReduce-like pooling

| Title | Authors | Year | Venue / id | Relevance | Slot | Risk | URL | Route |
|---|---|---|---|---|---|---|---|---|
| **Evidence-Aware MapReduce for Forkable Compute** (Boltzmann MapReduce) | Yossi Eliaz | 2026 | arXiv 2607.09689 | Core: fork ≠ independence; precision-weighted Gaussian reduce; evidence IDs + lineage; Δ / Cochran Q. | REDUCE | low | https://arxiv.org/abs/2607.09689 | MAIN |
| Self-Consistency Improves Chain of Thought Reasoning | Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou | 2023 | ICLR | Naive majority-vote reduce — the foil your paper upgrades. | REDUCE | low | https://arxiv.org/abs/2203.11171 | BACKUP |
| Improving Factuality and Reasoning through Multiagent Debate | Du, Li, Torralba, Tenenbaum, Mordatch | 2024 | ICML | Critique-exchange consensus; still erases evidence identity. | REDUCE | low | https://arxiv.org/abs/2305.14325 | BACKUP |
| Mixture-of-Agents Enhances LLM Capabilities | Wang et al. (Together) | 2024–25 | ICLR’25 / arXiv 2406.04692 | Layered proposer→aggregator; no fork lineage. | REDUCE | low–med | https://arxiv.org/abs/2406.04692 | BACKUP |
| Rethinking Mixture-of-Agents / Self-MoA | — | 2025 | arXiv 2502.00674 | Single strong model ensembling can beat multi-model mix — quality > diversity. | REDUCE | med | https://arxiv.org/abs/2502.00674 | BACKUP |
| Large Language Monkeys | Brown et al. | 2024 | arXiv 2407.21787 | Repeated sampling coverage; needs a principled keep/reduce. | FORK / REDUCE | low | https://arxiv.org/abs/2407.21787 | BACKUP |
| MapReduce: Simplified Data Processing on Large Clusters | Dean, Ghemawat | 2004 | OSDI | Historical contract: small interface, runtime owns fan-out — your paper’s systems ancestor. | REDUCE | low | USENIX OSDI’04 | BACKUP (pedigree) |
| Combining information from independent sources through confidence distributions | Singh, Xie, Strawderman | 2005 | Annals of Statistics | Statistical ancestor of CD pooling (cite via your paper’s refs). | REDUCE | low | via 2607.09689 refs | via #1 |
| Shepherd formalized execution trace | Yu et al. | 2026 | 2605.10913 | Lineage/commit graph for forks — systems sibling to evidence IDs. | REDUCE / KEY | med | https://arxiv.org/abs/2605.10913 | MAIN-adjacent |
| Proof-of-Use (tool-call evidence IDs) | — | 2025 | arXiv 2510.10931 | Auditable citation of evidence identifiers in agent RL. | REDUCE | med | https://arxiv.org/abs/2510.10931 | BACKUP |
| Council Mode / uncertainty-aware consensus | — | 2026 | arXiv 2604.02923 | Structured heterogeneous consensus vs naive vote. | REDUCE | med | https://arxiv.org/abs/2604.02923 | BACKUP |

---

### F. Hardware-in-the-loop / sim-to-real isolation (high-signal only)

| Title | Authors | Year | Venue / id | Relevance | Slot | Risk | URL | Route |
|---|---|---|---|---|---|---|---|---|
| Sandbox-Enabled Digital Twin for Cyber-Physical Systems (SaMOSA) | — | 2026 | arXiv 2606.17001 | Unmodified controller binaries in QEMU sandbox; I/O bridged to plant sim; side-channel capture. Isolation metaphor for HIL. | ESCAPE / FORK | med | https://arxiv.org/abs/2606.17001 | BACKUP |
| Reconciling Reality through Simulation (RialTo) | — | 2024 | RSS / arXiv 2403.03949 | Real→sim→real digital twin for robust manipulation; scarce real tip, abundant sim search. | ORACLE / PROMOTE | med | https://arxiv.org/abs/2403.03949 | BACKUP |
| Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives | — | 2026 | arXiv 2607.08448 | Memory-guided agents over frozen VLA — control-plane vs body. | ORACLE | med | https://arxiv.org/abs/2607.08448 | BACKUP |
| *(Scarcity metaphor only)* HIL-SERL and similar robot RL | various | 2024+ | e.g. arXiv 2410.21845 | Cite **only** as “scarce tip” neighbor — not as IB/fork claim. | PROMOTE | high if over-cited | — | **DO NOT USE** as systems claim |

**Rule for F:** one slide max — “sim = plural search; robot hour = singular promote.” No robotics marketing.

---

## 4. X / Twitter pointers (with caveat)

**Caveat:** X discourse is a **pointer**, not peer review. Do not put tweet screenshots on SRG slides. Use for hallway energy / “who is talking about this.” Prefer arXiv + official blogs.

| Pointer | Handle / surface (approx.) | Theme | Date context |
|---|---|---|---|
| Weco AIDE² announcement thread | @weco_ai / Weco blog | RSI of research harness | 2026-09 (arXiv 2609.26457) |
| Sakana AI Scientist Nature / blog | @SakanaAILab | Auto-research promote-to-paper | 2024–2026 |
| E2B / Daytona eng. posts on snapshots | @e2b_dev · Daytona blog | Firecracker pause/restore costs; Crab-inspired skip-if-unchanged RFCs | 2025–2026 |
| forkd / Firecracker CoW discussion | GitHub deeplethe/forkd + eng blogs | “fork is the API” for agent fan-out | 2026 |
| HF Daily Papers tokens on RRSI / Shepherd / DeltaBox | huggingface.co/papers | Trending systems+agent papers | mid–late 2026 |
| Alignment Forum / “School of Reward Hacks” | AF posts citing 2508.17511 | Reward hacking generalization | 2025–2026 |

*Executor note (2026-09-27):* direct `site:x.com` search returned thin structured hits; treat engineering repos + official blogs as the public discourse surface until dated handles are hand-curated.

---

## 5. Hugging Face hubs / datasets / spaces worth bookmarking

| Resource | Why | URL |
|---|---|---|
| Shepherd paper page | Meta-agent fork substrate | https://huggingface.co/papers/2605.10913 |
| RRSI (trending) | Regularized harness RSI | https://huggingface.co/papers/2609.24972 |
| OpenRath | Session fork/merge runtime | https://huggingface.co/papers/2606.19409 |
| SWE-bench Verified | Canonical coding oracle | https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified |
| SWE-bench Pro (ScaleAI) | Harder / longer-horizon | https://huggingface.co/datasets/ScaleAI/SWE-bench_Pro |
| SWE-smith trajectories | Agent trajectory data | https://huggingface.co/datasets/SWE-bench/SWE-smith-trajectories |
| HF Hub Sandboxes guide | Productized fan-out / Landlock vs VM | https://huggingface.co/docs/huggingface_hub/guides/sandbox |
| OpenEnv Pi coding env | Coding agent + logprobs for GRPO | https://huggingface.co/docs/openenv/environments/pi |
| SandboxEscapeBench paper | Escape threat model | https://huggingface.co/papers/2603.02277 |
| LEGO-RL paper | Harness-native coding RL | https://huggingface.co/papers/2608.17393 |
| AutoResearchClaw | HIL auto-research | https://huggingface.co/papers/2605.20025 |
| Daily / trending papers | Keep watching FORK/RSI cluster | https://huggingface.co/papers/trending |

---

## 6. Suggested 5 citations for the Cambridge slide deck (max)

| # | Cite | Slide job |
|---|---|---|
| 1 | **Firecracker** (NSDI’20) | Pedigree: microVM isolation + snapshot economics |
| 2 | **DeltaBox** (2605.22781) *or* **Crab** (2604.28138) | Pick one systems twin: ms CoW C/R for agent search (DeltaBox = how-fast; Crab = what/when) |
| 3 | **Shepherd** (2605.10913) | Meta-agent fork + Tree-RL + reversible trace |
| 4 | **Your Boltzmann / Evidence-Aware MapReduce** (2607.09689) | Reduce after fork; Search≠Authority |
| 5 | **SWE-bench** (2310.06770) *or* **Rebound→Remedy** (2604.01476) | Pick one: isolated coding oracle pedigree **or** “oracle must leave the fork” for RL Act |

**Speaker-notes only (not on slides):** AIDE² / RRSI / AI Scientist (auto-research Act), OpenHands, SandboxEscapeBench, OpenRath, Xu–Kaffes position paper, SaMOSA / RialTo (one HIL metaphor line).

---

## 7. Gaps / open problems the literature leaves for SRG

1. **Fork ≠ independence (statistical).** Almost no agent systems paper measures correlation ρ across CoW siblings that share model/prompt/repo ancestors. Your reduce paper owns this agenda; DeltaBox/Crab/Shepherd optimize *execution* independence, not *evidence* independence.

2. **Fork-DAG reducer.** Lineage is recorded (Shepherd commits, OpenRath Session, your \(\mathcal{L}\)) but almost never mapped to a calibrated dependence model that can *abstain* when correlation is unresolved.

3. **Oracle ownership / verifier tampering.** Rebound→Remedy and SpecBench show agents rewrite tests inside the env. Literature still under-specifies a systems contract: controller-owned oracle digests vs worker-writable scorers (Search≠Authority).

4. **Credential / identity refresh on fork.** Product systems (islo gateway, mitos handshake) mention fresh entropy; peer literature thin on lease models for WIRE after CoW.

5. **Warm shared pages as side channels.** Density vs confidentiality under CoW mem sharing is understudied in agent papers (security community separate).

6. **Cross-domain factory isomorphism.** SW / RL / bio / sim / HIL share the hill-climb loop but lack a named systems API paper — **that is this talk’s contribution.**

7. **Promote once.** Auto-research (AI Scientist, AIDE²) optimizes search hard; singular promote-to-claim / merge-to-main / robot-hour booking remains sociology + process, not a runtime primitive.

8. **Adaptive selection / winner’s curse.** Best-of-N and tree search select survivors with the same evidence used to score them; few reducers record selection context as first-class (your open problem §5).

---

## 8. Yossi’s own related public artifacts

| Artifact | Role | URL |
|---|---|---|
| Evidence-Aware / Uncertainty-Aware MapReduce (Boltzmann MapReduce) | Peer paper + reduce contract | https://arxiv.org/abs/2607.09689 · https://arxiv.org/html/2607.09689v3 |
| boltzmann-mapreduce artifact | Reference impl + islo four-shard trace | https://github.com/zozo123/boltzmann-mapreduce |
| The Sandbox Shift — field manual | Why/when/how isolation ladder; vendor-neutral | https://zozo123.github.io/sandboxes-why-how-when/ |
| islo.dev | Forkable microVM sandboxes (named snapshot / restore) | https://islo.dev/sandboxes/ · https://islo.dev/ |
| Meta-harness / longmem demos on islo | Public runnable demos | https://zozo123.github.io/meta-harness-on-islo-page/ · https://zozo123.github.io/longmem-mini-on-islo/ |
| Odysseus × crabbox × islo | Cross-provider sandbox commodity story | https://zozo123.github.io/odysseus-crabbox-demo/ |
| Personal site | Index | https://zozo123.github.io/ |

---

## 9. Claim fence (stage discipline)

- Cite Shepherd / DeltaBox / Crab / AIDE² / GEAR / OpenHands as **related systems**, not prior work you own.
- Do **not** claim forkd / E2B / Daytona vendor latencies as your benchmarks; quote only published peer numbers or your own artifact tables.
- Do **not** cite HIL-SERL / robotics blogs as something you rewrote; one scarcity-ladder sentence max.
- Prefer arXiv abs + USENIX/ACM/Nature primary over tertiary “AI news” SEO.
- Exclude PleaseFix-class browser agents unless the paper is explicitly about **sandbox runtime**.
- Version note: arXiv 2607.09689 has multiple HTML titles across versions (Evidence-Aware MapReduce / Uncertainty-Aware Reduction); on slides prefer the **v3 Evidence-Aware** framing aligned with Search≠Authority.

---

## 10. Methodology inspirations (non-peer; credit verbally)

| Source | Contribution to talk | Not |
|---|---|---|
| **pstack** | Fearless parallelism; hillclimb playbook (one metric, one change, fan-out, promote) | Cursor plugin demo |
| **OpenClaw** | Agent loop: tools, sessions, sandboxed body | Robotics OS |
| **ariflow-swfactory** | Cell, epoch, Search≠Authority, evidence, promotion | Product pitch |

---

*Deep-research pass complete 2026-09-27. Prefer primary PDFs/HTML; refresh HF trending weekly before 15 Oct.*
