# Paper → stage map — Cambridge SRG · AGGRESSIVE lock
**Lock:** 2026-09-28 (IDT) · aligns `scratch/AGGRESSIVE-SPINE.md` + `CLAIM-FENCE.md` + `scratch/PAPERS-AND-SOURCES.md`  
**Primary:** A chassis + C payload · full MAIN stack on stage · peer ms attributed only

| Paper | Route | Slide # | Slide title (from AGGRESSIVE-SPINE) | One-sentence job on stage | Claim-fence note |
|---|---|---|---|---|---|
| **Firecracker** — Agache et al., NSDI’20 | MAIN | **4** | Isolation Walls: Namespaces / gVisor / Firecracker-Class | Anchor the outer escape wall every agent sandbox cites; pedigree, not invention. | DO say: related systems / pedigree. DO NOT: “we invented VMs.” |
| **DeltaBox** — Dong et al., arXiv 2605.22781 | MAIN | **6**, **7** | Peer Latency Table; Fork Taxonomy | How-fast twin: change-based FS+mem C/R makes checkpoint cheap under LLM wait — **authors’** ~10.83 ms ckpt / ~1.86 ms restore. | Cousin, not owned. Numbers attributed “authors report.” Never present as yours. |
| **Crab** — Wu et al., arXiv 2604.28138 | MAIN | **6**, **7** | Peer Latency Table; Fork Taxonomy | What/when twin: semantics-aware skip (≤1.9% overhead, authors) complements DeltaBox’s how-fast. | Cousin. On-slide under AGGRESSIVE (was verbal-only under old deck-five). Still not your system. |
| **Shepherd** — Yu et al., arXiv 2605.10913 | MAIN | **6**, **7** | Peer Latency Table; Fork Taxonomy | Fork-as-value: effect-trace a meta-agent can hold; authors’ ~134–143 ms fork — programmable object, not just restore path. | Cousin / academic twin of Controllable fork. DO NOT claim as prior work you shipped. |
| **Evidence-Aware MapReduce / Boltzmann** — Eliaz, arXiv 2607.09689 | MAIN (**your payload**) | **12**, **13**, **16** | Exec≠Evidence; Worker-Record Algorithm; Promote-Once Invariants | Own the hour’s net-new claim: cheap forks ≠ independent evidence; worker record + lineage reduce + abstain; cold liar / forged \(P_o\). | Prefer **evidence-aware reduce** wording on stage; Boltzmann/Gibbs = paper’s interpretation fence, not “CI is thermodynamics.” \(Z_g\) diagnostic only. |
| **From Rebound to Remedy** — arXiv 2604.01476 | MAIN (oracle foil) | **14** | Sealed Oracle: RUN ≠ EVAL | Peer proof that agents rewrite evaluator tests when reward is scarce — oracle digests stay controller-owned. | Cite as foil for sealed oracle, not as your RL result. DO NOT: “we rewrote HIL-SERL / accelerate GPU RL.” |
| **SWE-bench** — Jimenez et al., ICLR’24 | MAIN (benchmark pedigree) | **15** | Oracle Pedigree: Why Isolated Eval Exists | Isolated GitHub-issue envs made coding-agent sandboxes inevitable — oracle pedigree, not a scoreboard slide. | One cite. No empty “eval sermon.” No inventing your SWE-bench numbers. |
| **Toward Systems Foundations for Agentic Exploration** — Xu, Zhou, Wu, Kaffes, arXiv 2510.05556 | MAIN *(promoted for AGGRESSIVE foundations beat)* | **11** | Systems Agenda: Native CoW Fork Still Missing | Name the open agenda (fork semantics, side-effects, native CoW) that this talk answers with substrate + reduce contract. | Position paper — agenda cite, not a latency claim. Was BACKUP; AGGRESSIVE puts it on stage as foundations bridge. |

---

## Speaker-notes / Q&A only (not on slides)

| Paper / item | Why off-slide | If asked |
|---|---|---|
| **AIDE²** (2609.26457) | Claim-fence BACKUP; RSI overclaim risk | One verbal: outer loop rewrites harness under frozen eval — Search≠Authority for the harness |
| **GEAR** (2605.13874) | Claim-fence BACKUP | One verbal: population frontier vs single-incumbent hill-climb |
| **RRSI** · OpenRath · EscapeBench · Self-consistency | BACKUP | Verbal if challenged on RSI / session value / escape / naive majority vote |
| **forkd / E2B / Daytona / Tensorlake / islo ms** | Eng landscape · high claim-risk | Verbal only; never on-slide as benchmarks |
| **AI Scientist / wet-lab / HIL-SERL** | Wrong room / overclaim | Scarcity metaphor one sentence in Q&A |

---

## Slide coverage checklist (required beats)

| Required beat | Slide(s) | Covered? |
|---|---|---|
| Threat / TCB | 2 | yes |
| Six surfaces | 3 (+5 compress FS/creds/\(S_0\)) | yes |
| Peer latency table | 6 | yes |
| Worker-record algorithm | 13 | yes |
| Sealed oracle | 14 | yes |
| Promote-once invariants | 16 | yes |
| Open problems | 17 | yes |
| Every MAIN paper above | 4, 6–7, 11–16 | yes |

---

## Explicit non-mapping (DO NOT get slides)

| Temptation | Disposition |
|---|---|
| Dreamer / CWM / Bonnie Li Act | **No slide** — Q&A line in AGGRESSIVE-SPINE |
| Annealing / SA / MH / Langevin table | **No slide** — Q&A |
| Bio isomorphism / universal-hillclimb proof table | **No slide** — optional one spoken scarcity sentence |
| Mantra / \\law slide | **No slide** — spoken close once max |
| Empty eval sermon | **No slide** — numbers live on 6 + 13 |


---

## Flowchart gate map (companion)

Full annotated decision flowchart (per-gate systems meaning · papers · venue · claim-fence · HIS vs cousin · paper shapes):

→ [`FLOW-GATES-PAPERS.md`](FLOW-GATES-PAPERS.md)

| Flowchart gate cluster | AGGRESSIVE slides | Primary papers |
|---|---|---|
| START · stateful · \(S_0\) | 1–5 | Firecracker · Xu–Kaffes |
| cheap branch · FORK N | 6–7, 10–11 | DeltaBox · Crab · Shepherd · Xu–Kaffes |
| LEARN/SIMULATE (off spine) | Q&A only | Dreamer · CWM · ContrastiveWM |
| oracle seal | 14–15 | Rebound→Remedy · SWE-bench |
| independent evidence · REDUCE | 12–13 | **2607.09689** ★HIS |
| promote-once · REPEAT | 16–18 | **2607.09689** · G-contract |


---

*PAPER-STAGE-MAP · 2026-09-28 IDT · companion to AGGRESSIVE-SPINE + FLOW-GATES-PAPERS*
