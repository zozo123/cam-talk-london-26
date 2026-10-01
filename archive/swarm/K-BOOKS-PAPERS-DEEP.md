# K — Deep bibliography (books + papers)

**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026 · FW11  
**Speaker:** Yossi Eliaz · curated 2026-09-27 (Asia/Jerusalem)  
**Companion:** `PAPERS-AND-SOURCES.md` (deck-facing), swarm A–I, `CLAIM-FENCE.md`  
**Repo:** https://github.com/zozo123/cam-talk-london-26

**Thesis this bib supports:** forkable sandboxes are the *execution substrate* for a universal hill-climb loop `(propose → isolate → measure → keep/revert → promote)`. Firecracker is **pedigree, not sufficiency**. The talk’s systems agenda lives in **next-gen** fork/C/R (DeltaBox, Crab, Shepherd, Cloud Hypervisor / Tensorlake, forkd/Mitos, libkrun) + evidence-aware reduce + sealed oracle + driven/non-eq schedule language.

---

## Claim fence (read before citing on stage)

| DO | DO NOT |
|---|---|
| Firecracker NSDI’20 = **ancestry** of microVM isolation + snapshot economics | “Firecracker solves agent fork” / “we invent VMs” |
| Peer ms only, attributed (DeltaBox / Crab / Shepherd tables) | Vendor / forkd / Tensorlake / E2B / islo ms as **Yossi benchmarks** |
| Physics = **algebra + schedule** (β≡n, SA/MH cousins, driven/NESS) | Everett MWI as physics proof; Gibbs-of-nature; closed Hamiltonian CI |
| Shepherd / DeltaBox / Crab / AIDE² = **related systems** | Owned prior work |
| Tensorlake / Mitos / forkd = **practice landscape** (BACKUP) | Peer lease model or peer latency |
| Promote = absorbing sink under drive | Equilibrium free-energy minimum |

**Deck cite budget (≤5):** (1) DeltaBox **or** Crab · (2) Shepherd · (3) 2607.09689 · (4) SWE-bench **or** Rebound→Remedy · (5) Firecracker *only as pedigree footnote* **or** Xu–Kaffes foundations. Prefer next-gen on slides; Firecracker verbally as “where the wall came from.”

---

## 0. Beyond Firecracker (priority frame)

Firecracker (NSDI’20) made **hardware-isolated microVMs cheap enough for serverless**. That is necessary pedigree for Escape — it is **not** the agent-fork research frontier.

| Gap Firecracker leaves | Who advances it | Route |
|---|---|---|
| Change-based FS+mem C/R for *stateful* agent trees | **DeltaBox** (2605.22781) | MAIN |
| Semantics-aware *when* to checkpoint (skip idle turns) | **Crab** (2604.28138) | MAIN |
| Agent+env as reversible effect-trace / Tree-RL | **Shepherd** (2605.10913) | MAIN |
| Named fork semantics + side-effect agenda | **Xu–Kaffes** (2510.05556) | BACKUP→MAIN foundations |
| Multi-hypervisor product substrate (FC **and** Cloud Hypervisor) | **Tensorlake** docs | BACKUP practice |
| Warm-parent CoW fan-out / live BRANCH | **forkd** · **Mitos** | BACKUP eng (high claim-risk) |
| Library VMM, KVM+HVF, local-first agents | **libkrun** (containers/libkrun) | BACKUP eng |
| Lightweight alternative VMM (rust-vmm family) | **Cloud Hypervisor** | BACKUP landscape |
| Container→VM / nested wall options | gVisor · Kata · QEMU snapshot | BACKUP Escape ladder |

**Spoken bridge (Act I):** “Firecracker taught the industry the microVM wall. The talk is about what comes *after* — fork as API, lineage as evidence, oracle outside the child.”

**Number fence:** peer tables only on slides. Eng landscape (forkd ~100 kids / ~100 ms; BRANCH ~150 ms; Tensorlake sub-second resume marketing) = **hallway / speaker-note**. Never equalize with DeltaBox/Crab/Shepherd peer figures.

---

## 1. Canon books (≤20)

| # | Book | Edition | Why for this talk | Stage use | Route |
|---|---|---|---|---|---|
| 1 | **Tanenbaum & Bos — Modern Operating Systems** | 4th ed. (2015) or later | `fork` / process / address-space CoW ancestry; “machine you can fork like a process” hook | Act 0 verbal pedigree (1 breath) | MAIN book |
| 2 | **Kerrisk — The Linux Programming Interface** | 1st (2010) | `fork`/`clone`/`mmap` MAP_PRIVATE; userland twin of microVM CoW story | Speaker notes / Q&A on CoW mechanics | MAIN book |
| 3 | **Kleppmann — Designing Data-Intensive Applications** | 1st (2017); watch 2nd | MapReduce contract, lineage, batch vs stream, “runtime owns fan-out” | Act II½ reduce pedigree slide | MAIN book |
| 4 | **Sutton & Barto — Reinforcement Learning: An Introduction** | 2nd (2018) | Rollout / reward / policy; why sealed oracle + forkable env matter | RL Act verbal; not a slide | MAIN book |
| 5 | **MacKay — Information Theory, Inference, and Learning Algorithms** | 2003 (CUP; free PDF) | β, evidence, Occam; bridges 2607.09689 β≡n without Gibbs cosplay | Act II½ / Q&A on β | MAIN book |
| 6 | **Kirkpatrick, Gelatt, Vecchi — Optimization by Simulated Annealing** | *Science* 220:671–680 (1983) — treat as **canon paper-book hybrid** | SA schedule = liquid factory (hot explore → cool → T→0 promote) | Act II½ anneal table | MAIN (paper) |
| 7 | **Barroso, Hölzle, Ranganathan — The Datacenter as a Computer** | **3rd ed.** (2018, Morgan & Claypool / Springer) | Warehouse-scale density, blast radius, why microVMs exist *at all* (Firecracker *context*) | Act I Escape density (1 breath); **not** “FC is enough” | BACKUP book |
| 8 | **Seifert — Stochastic thermodynamics…** | Rep. Prog. Phys. **75** 126001 (2012) | Driven trajectories, entropy production, NESS language for factories | Q&A non-eq only; **never** claim FT for CI | BACKUP review |
| 9 | **Kardar — Statistical Physics of Fields** | 2007 (CUP) | Light touch: path measure / replicas vocabulary for parallel-worlds dictionary | Speaker notes only; skip derivations | BACKUP light |
| 10 | **Feynman & Hibbs — Quantum Mechanics and Path Integrals** | Emended ed. (2005) or classic | **Pedagogy only** for ∑paths ↔ fork fan-out diagram | Claim-fence hard: Euclidean twin e^{−βE}, **not** MWI proof | BACKUP pedagogy |
| 11 | **Dean & Ghemawat — MapReduce** | OSDI’04 paper (also “book” of the contract) | Small interface; runtime owns topology — ancestor of Evidence-Aware MapReduce | Pedigree cite via Kleppmann + your paper | MAIN (paper) |
| 12 | **Pathria & Beale — Statistical Mechanics** | 3rd/4th | Skip as primary; Kardar+MacKay cover stage needs | — | **SKIP** — heavier than Kardar for SRG; no stage ROI |
| 13 | **Spinney & Ford — Fluctuation relations…** | Contemp. Phys. / reviews | Alternate to Seifert; redundant if Seifert kept | — | **SKIP** — Seifert is enough; avoid double non-eq stack |
| 14 | **Russinovich et al. — Windows Internals / Azure cloud books** | various | Low signal for Linux microVM + KVM fork agenda | — | **SKIP** — wrong stack; Barroso covers WSC |
| 15 | **Love — Linux Kernel Development** | 3rd | Optional deepen on mm / CoW pages | Pre-talk personal only | optional |
| 16 | **Cormen et al. — Introduction to Algorithms** | 3rd/4th | Hill-climb / greedy / local search vocabulary | Verbal only if challenged | optional |
| 17 | **Bishop / Murphy — Probabilistic ML** | various | Softmax / temperature / Bayesian evidence cousins | Prefer MacKay for β | optional |

**Must-consider audit**

| Item | Verdict |
|---|---|
| Tanenbaum/Bos | **INCLUDE** (#1) |
| Kerrisk LPI | **INCLUDE** (#2) |
| Kleppmann DDIA | **INCLUDE** (#3) |
| Dean/Ghemawat MapReduce | **INCLUDE** (paper cluster + #11) |
| Sutton & Barto | **INCLUDE** (#4) |
| MacKay ITILA | **INCLUDE** (#5) |
| Kardar / Pathria | **Kardar light INCLUDE** (#9); **Pathria SKIP** |
| Seifert **or** Spinney & Ford | **Seifert INCLUDE** (#8); Spinney SKIP |
| Kirkpatrick SA 1983 | **INCLUDE** (#6 / MCMC cluster) |
| Feynman/Hibbs | **INCLUDE pedagogy-only** (#10) — claim fence: no Everett MWI |
| Barroso datacenter | **INCLUDE** (#7) as FC *context*, not sufficiency |
| Russinovich / cloud books | **SKIP** — low signal for this room |

**Working set for Yossi (books):** #1–#8 + Feynman pedagogy skim. That is ≤10 active titles.

---

## 2. Canon papers (≤40) — clustered

### 2.A FORK / C/R / snapshot / microVM (**next-gen first**)

| # | Paper / system | Year | Venue / id | Why | Slot | Route |
|---|---|---|---|---|---|---|
| 1 | **DeltaBox** — Dong et al. | 2026 | arXiv 2605.22781 | OS-level change-based C/R (DeltaFS+DeltaCR); ~11 ms ckpt / ~2 ms restore peer tables; MCTS+RL fan-out | FORK | **MAIN** |
| 2 | **Crab** — Wu et al. | 2026 | arXiv 2604.28138 | Semantics-aware C/R; eBPF skip ≤87% turns; turn-aligned LLM-wait; RL branch | FORK | **MAIN** |
| 3 | **Shepherd** — Yu et al. | 2026 | arXiv 2605.10913 | Reversible agent+env effect trace; fork ~5× docker commit; Tree-GRPO | FORK / REDUCE | **MAIN** |
| 4 | **Toward Systems Foundations for Agentic Exploration** — Xu, Zhou, Wu, **Kaffes** | 2025 | arXiv 2510.05556 | Names fork semantics, side-effects, native CoW as open agenda — *your talk answers this* | FORK | BACKUP→MAIN foundations |
| 5 | **OpenRath** — Wen, Wang, Xu | 2026 | arXiv 2606.19409 | Session as branchable/replayable runtime value | KEY / FORK | BACKUP |
| 6 | **Catalyzer** — Du et al. | 2020 | ASPLOS | `sfork` / checkpoint-image boot; ancestor of agent fork latency | FORK | BACKUP pedigree |
| 7 | **REAP** — Ustiugov et al. | 2021 | ASPLOS / arXiv 2101.09355 | Working-set prefetch via userfaultfd; SnapStart economics | FORK | BACKUP pedigree |
| 8 | **FaaSnap** — Ao, Porter, Voelker | 2022 | EuroSys | Concurrent paging for VM snapshots | FORK | BACKUP |
| 9 | **Firecracker** — Agache et al. | 2020 | **NSDI’20** | Canonical microVM wall + snapshot pedigree — **ancestry, not the fork API** | ESCAPE / FORK | **MAIN pedigree only** |
| 10 | **QEMU** snapshot / migration literature (selective) | — | — | Classical C/R substrate; SaMOSA HIL uses QEMU | FORK / HIL | BACKUP |
| 11 | **gVisor** (Google) | 2018+ | OSDI’ish / docs | Syscall interception middle wall | ESCAPE ladder | BACKUP |
| 12 | **Kata Containers** | 2017+ | docs / papers | Containers-as-VMs; density vs isolation ladder | ESCAPE ladder | BACKUP |

### 2.B MapReduce / lineage / evidence reduce

| # | Paper | Year | Venue / id | Why | Slot | Route |
|---|---|---|---|---|---|---|
| 13 | **Evidence-Aware MapReduce (Boltzmann MapReduce)** — Eliaz | 2026 | arXiv **2607.09689** | Core: fork≠indep; precision-weighted reduce; evidence IDs + lineage; β≡n | REDUCE | **MAIN** |
| 14 | **MapReduce** — Dean & Ghemawat | 2004 | OSDI | Contract ancestor: small API, runtime owns fan-out | REDUCE | MAIN pedigree |
| 15 | **Resilient Distributed Datasets (Spark)** — Zaharia et al. | 2012 | NSDI | Lineage / recomputation — systems twin of \(\mathcal{L}\) | REDUCE / KEY | BACKUP |
| 16 | **Dryad** — Isard et al. | 2007 | EuroSys | DAG execution; topology ≠ evidence independence | REDUCE | BACKUP |
| 17 | **CIEL** — Murray et al. | 2011 | NSDI | Dynamic task graph + memoization / lineage | REDUCE | BACKUP |
| 18 | **Ray** — Moritz et al. | 2018 | OSDI | Actor/task runtime for RL + distributed python — factory cousin | FORK / ORACLE | BACKUP |
| 19 | **Self-Consistency** — Wang et al. | 2023 | ICLR | Naive majority-vote reduce — **foil** your paper upgrades | REDUCE | BACKUP |
| 20 | **Proof-of-Use** | 2025 | arXiv 2510.10931 | Evidence IDs in agent RL — cousin of \(\mathcal{E}_k\) | REDUCE | BACKUP |

### 2.C MCMC / SA / optimization schedules

| # | Paper | Year | Venue / id | Why | Slot | Route |
|---|---|---|---|---|---|---|
| 21 | **Metropolis et al.** | 1953 | J. Chem. Phys. | Propose / accept ancestry | ORACLE dynamics | BACKUP classic |
| 22 | **Hastings** | 1970 | Biometrika | MH ratio; accept lives outside proposal | ORACLE dynamics | BACKUP classic |
| 23 | **Geman & Geman** | 1984 | IEEE PAMI | Gibbs sampling / annealing for images — schedule pedigree | ORACLE dynamics | BACKUP classic |
| 24 | **Kirkpatrick et al. SA** | 1983 | Science | Liquid-factory T schedule dual | ORACLE / Epoch | **MAIN schedule** |
| 25 | *(optional)* Černý SA | 1985 | J. Optim. Theory Appl. | Parallel SA invention claim | — | BACKUP if historian Q |

### 2.D Non-equilibrium / stochastic thermo (claim-fenced)

| # | Paper / review | Year | Venue / id | Why | Slot | Route |
|---|---|---|---|---|---|---|
| 26 | **Seifert** stochastic thermodynamics review | 2012 | Rep. Prog. Phys. 75:126001 | Driven trajectories, entropy production, NESS vocabulary | non-eq ontology | BACKUP Q&A |
| 27 | *(light)* Crooks / Jarzynski primary papers | 1999–2000 | — | **Names only in Q&A**; irreversible work at tip | tip metaphor | **DO NOT USE** on slides |
| — | Everett / MWI | — | — | — | — | **DO NOT USE** as physics proof |

### 2.E RL / agents / software factories / oracles

| # | Paper | Year | Venue / id | Why | Slot | Route |
|---|---|---|---|---|---|---|
| 28 | **SWE-bench** — Jimenez et al. | 2024 | ICLR / arXiv 2310.06770 | Isolated-repo coding oracle pedigree | VERDICT | **MAIN** |
| 29 | **From Rebound to Remedy** | 2026 | arXiv 2604.01476 | Reward hacking via env manipulation; oracle must leave the fork | ORACLE / ESCAPE | **MAIN**-adjacent |
| 30 | **OpenHands** — Wang, Neubig et al. | 2024–25 | ICLR’25 / 2407.16741 | Docker/runtime abstraction for coding agents | FOLDER | BACKUP |
| 31 | **Large Language Monkeys** — Brown et al. | 2024 | arXiv 2407.21787 | Best-of-N / coverage motivates fan-out before reduce | FORK / REDUCE | BACKUP |
| 32 | **AI Scientist / v2** — Lu / Sakana et al. | 2024–26 | arXiv 2408.06292 · Nature 2026 | Auto-research factory metaphor; promote-to-claim scarce | PROMOTE | BACKUP (overclaim risk) |
| 33 | **AIDE²** | 2026 | arXiv 2609.26457 | Outer-loop harness RSI under frozen eval | ORACLE | BACKUP |
| 34 | **RRSI** | 2026 | arXiv 2609.24972 | Regularized harness evolution; annealed edit budget | ORACLE | BACKUP |
| 35 | **ProRL Agent** (rollout-as-a-service) | 2026 | arXiv 2603.18815 | Decoupled sandbox rollout service | FORK / WIRE | BACKUP |

### 2.F Security / escape / isolation walls

| # | Paper / system | Year | Venue / id | Why | Slot | Route |
|---|---|---|---|---|---|---|
| 36 | **SandboxEscapeBench** | 2026 | arXiv 2603.02277 | Frontier LLMs escape container misconfigs; nested VM measurement | ESCAPE | BACKUP |
| 37 | **Balkanization of Execution-Security…** | 2026 | arXiv 2607.05743 | Isolation vs access-control vs TOCTOU survey | ESCAPE | BACKUP |
| 38 | **gVisor / Kata** (see 2.A #11–12) | — | — | Middle / nested walls on Escape ladder | ESCAPE | BACKUP |
| 39 | **SpecBench** (reward hacking long-horizon) | 2026 | arXiv 2605.21384 | Visible vs held-out tests | VERDICT | BACKUP |
| 40 | **School of Reward Hacks** | 2025 | arXiv 2508.17511 | Harmless hacks → misalignment caution | ORACLE | BACKUP |

**Count check:** numbered entries ≈40 including classics; surplus go to speaker notes, not deck.

---

## 3. Beyond Firecracker — engineering / product landscape (BACKUP only)

**Rule:** name once in Act I / hallway. **Never** put demo ms on slides as peer evidence.

| System | Public surface | Role in story | Claim risk |
|---|---|---|---|
| **Cloud Hypervisor** | github.com/cloud-hypervisor | rust-vmm alternative VMM; Tensorlake runs FC **and** CH | med (eng) |
| **Tensorlake Sandboxes** | docs.tensorlake.ai/sandboxes | Productized microVMs; `FILESYSTEM` vs `MEMORY` snapshot; restore/clone API | **high** if ms quoted |
| **forkd** | github.com/deeplethe/forkd | Warm-parent CoW fan-out; live BRANCH; still FC-based but *fork API* is the point | **high** |
| **Mitos** | github.com/mitos-run/mitos | K8s CRDs + live CoW fork; `secretInheritance: reissue` = WIRE existence proof | **high** |
| **libkrun** | github.com/containers/libkrun | Library VMM (KVM + macOS HVF); local-first agent isolation path | med |
| **islo.dev** | islo.dev/sandboxes | Named snapshot/restore substrate used in boltzmann-mapreduce artifact | high if ms |
| E2B / Daytona / Modal | vendor docs | API-exposed sandboxes; landscape only | **high** — verbal |

**Framing line:** *Firecracker/CH/libkrun are walls and monitors. DeltaBox/Crab/Shepherd/forkd/Mitos/Tensorlake are trying to make **fork the API**. Your paper makes **reduce** honest after that API exists.*

---

## 4. Tensorlake practice pointer (BACKUP)

| Fact | Source | Use |
|---|---|---|
| **Diptanu Gon Choudhury** — founder / CEO (public) | LinkedIn · tensorlake.ai/blog (“CEO / Co-founder”) | Hallway credit if asked who builds product forks |
| Sandboxes = isolated Firecracker **or Cloud Hypervisor** microVMs | docs.tensorlake.ai/sandboxes/introduction | Escape ladder + multi-VMM = Beyond-FC evidence |
| Snapshot types: filesystem (cold) vs memory (warm restore) | docs.tensorlake.ai/sandboxes/snapshots | Parallel-worlds diagram (BACKUP) |
| Restore / clone from `snapshot_id` | docs.tensorlake.ai/api-reference/v2/sandboxes/restore | Fork-as-API practice |
| Homepage / FAQ latency & scale claims | tensorlake.ai · /faq | **Verbal landscape only** — not Yossi benchmarks |

**Fence:** product docs ≠ peer review. Cite as *demand existence proof* for forkable sandboxes, never as measured science. No second co-founder claim without public source (founding-engineer titles ≠ co-founder).

---

## 5. Reading order for Yossi — 2 weeks pre-talk (before Thu 15 Oct 2026)

Assume ~10 focused hours/week. Prefer primary PDFs/HTML.

### Week −2 (systems spine + next-gen fork)

| Day | Read | Goal |
|---|---|---|
| D1 | **Xu–Kaffes** 2510.05556 (skim) + your field manual | Own the *agenda* slide |
| D2 | **DeltaBox** 2605.22781 (intro + tables) | How-fast C/R twin |
| D3 | **Crab** 2604.28138 (intro + skip/%) | What/when twin |
| D4 | **Shepherd** 2605.10913 (§fork + Tree-GRPO) | Meta-agent + RL branch |
| D5 | **Firecracker** NSDI’20 *skim only* + Barroso ch.1–2 | Pedigree / density — then stop |
| D6–7 | Landscape skim: Tensorlake sandbox docs · forkd README/DESIGN · Mitos README · libkrun README | Beyond-FC vocabulary; **no ms memorization** |

### Week −1 (reduce + schedule + oracle + fence)

| Day | Read | Goal |
|---|---|---|
| D8 | **Your** 2607.09689v3 (Evidence-Aware) end-to-end | Own β≡n, cold liar, Δ |
| D9 | Dean/Ghemawat MapReduce + Kleppmann MapReduce/lineage chapters | Pedigree without reinventing |
| D10 | Kirkpatrick SA 1983 + Metropolis 1953 / Hastings 1970 (skim abstracts+ratios) | Anneal / MH keep-revert lines |
| D11 | Sutton & Barto ch.1–3 + **Rebound→Remedy** 2604.01476 | Oracle outside fork |
| D12 | SWE-bench + SandboxEscapeBench (skim) | Verdict + Escape ladder |
| D13 | MacKay ch. on Evidence / Occam (select) + Seifert §1–2 *light* | β language + driven/NESS fence |
| D14 | `CLAIM-FENCE.md` + deck ≤5 cites rehearsal + Top-10 below | Stage discipline |

**Optional stretch:** Catalyzer + REAP (pedigree), Spark RDD paper (lineage), Feynman/Hibbs *one diagram only*.

---

## 6. Top-10 must-reads (summary card)

| # | Item | Why must |
|---|---|---|
| 1 | **2607.09689** Evidence-Aware MapReduce (yours) | Owns REDUCE / Search≠Authority |
| 2 | **DeltaBox** 2605.22781 | Best peer *how-fast* fork/C/R |
| 3 | **Crab** 2604.28138 | Best peer *what/when* fork/C/R |
| 4 | **Shepherd** 2605.10913 | Fork-as-object + Tree-RL |
| 5 | **Xu–Kaffes** 2510.05556 | Names the open systems agenda |
| 6 | **SWE-bench** 2310.06770 **or** **Rebound→Remedy** 2604.01476 | Oracle / verdict door |
| 7 | **Kirkpatrick SA** Science 1983 | Anneal = liquid factory schedule |
| 8 | **Dean/Ghemawat MapReduce** OSDI’04 | Reduce contract ancestor |
| 9 | **Firecracker** NSDI’20 | Pedigree wall — *not* the contribution |
| 10 | **Kleppmann DDIA** (+ MacKay β chapters) | Lineage + evidence language for SRG ears |

**Honorable next:** Sutton & Barto · Seifert 2012 (Q&A) · Catalyzer/REAP · Tensorlake docs (practice) · forkd/Mitos (eng landscape) · SandboxEscapeBench · Self-Consistency (foil).

---

## 7. Cross-links inside cam-talk repo

| Need | File |
|---|---|
| Deck-facing paper table | `../PAPERS-AND-SOURCES.md` |
| Stage claim fence | `../repo-scratch/CLAIM-FENCE.md` (or root CLAIM-FENCE) |
| Fork systems deep | `A-FORK-SYSTEMS.md` |
| Reduce / β | `B-REDUCE-STATPHYS.md` |
| Oracle / escape | `C-ORACLE-RL-ESCAPE.md` |
| Anneal / MH / SGD | `H-ANNEALING-MCMC-SGD.md` |
| Non-eq / Hamiltonian fence | `I-NONEQUILIBRIUM-HAMILTONIAN.md` |
| Tensorlake people notes | `_notes-tensorlake-people.md` |

---

*K deep bibliography · 2026-09-27 IDT · Firecracker = pedigree; research mass = next-gen fork + evidence-aware reduce + sealed oracle + driven schedules.*
