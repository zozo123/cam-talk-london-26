# AGGRESSIVE spine — Cambridge SRG · locked direction
**Lock:** 2026-09-28 (IDT) · Yossi · **AGGRESSIVE**  
**Primary:** **A chassis** (fork substrate / six surfaces) **+ C payload** (evidence-aware reduce · 2607.09689)  
**Format:** 45 min + 15 Q&A · **≤20** NSDI/SOSP-workshop slide titles  
**Repo:** zozo123/cam-talk-london-26 · **Do not rewrite** `talk.tex` / `academic/*.tex` from this file yet

---

## Direction (one line)

Own the hour as a **systems substrate seminar** that turns mid-talk into **your falsifiable reduce contract**. Cite the **full MAIN paper stack on stage**. World models / annealing / bio = **Q&A only**. Search≠Authority appears **only** as the client-rely / Promote-once invariant table — not as TED mantras.

---

## Minute map (45+15)

| Min | Block | Slides |
|---|---|---|
| 0–3 | Thesis + threat/TCB | 1–2 |
| 3–18 | Six surfaces · isolation · peer fork table · warm heat · recovery | 3–9 |
| 18–22 | Parallel worlds · Xu–Kaffes agenda bridge | 10–11 |
| 22–35 | Evidence wall: fork≠independence · worker record · sealed oracle | 12–15 |
| 35–42 | Promote-once invariants · open problems | 16–17 |
| 42–45 | Close / three SRG questions | 18 |
| 45–60 | Q&A (Dreamer, anneal, bio, vendor ms, HIL tip) | — |

Optional backup (not in spoken path): slides 19–20.

---

## ≤20 slide titles (workshop tone)

| # | Slide title | MAIN cite on slide | Abstract / beat job |
|---|---|---|---|
| 1 | **Forkable Sandboxes as an Execution Substrate for Agents** | — | Thesis: cheap CoW fork ≠ independent evidence; contract needed |
| 2 | **Threat Model & TCB: Untrusted Shell + Search Fan-Out** | — | Escape wall + authority boundary; what is *in* vs *out* of child |
| 3 | **Six Surfaces the Abstract Promised** | — | FS · net/creds · repro · fast clone · build/test · recovery/obs |
| 4 | **Isolation Walls: Namespaces / gVisor / Firecracker-Class** | Firecracker (NSDI’20) | Pedigree wall; density vs escape trade-off |
| 5 | **Filesystem, Credentials, Named \(S_0\)** | — | Snapshot object; remint on fork; restore fidelity (compress Act I FS/WIRE/repro) |
| 6 | **Peer Latency Table: How Fast Is Fork?** | DeltaBox (2605.22781) · Crab (2604.28138) · Shepherd (2605.10913) | **Attributed only:** ~10.83 ms ckpt / ~1.86 ms restore (DeltaBox); ≤1.9% overhead (Crab); ~134–143 ms fork (Shepherd) |
| 7 | **Fork Taxonomy: FS · Mem · VM · Delta · Effect-Trace** | DeltaBox · Crab · Shepherd | Cousins: how-fast / what-when / programmable value — not yours |
| 8 | **Warm Factory Beside the Fork (Heat ≠ Authority)** | — | Build/test cache lives *beside* trust boundary |
| 9 | **Recovery: Crash the Runner, Keep the Receipt** | — | Observability outlives child; crash ≠ promote |
| 10 | **Diagram: Shared Past, Divergent Futures, One Promote** | — | Must-hit: \(S_0\) → fork \(N\) → reduce → promote-once → burn |
| 11 | **Systems Agenda: Native CoW Fork Still Missing** | Xu–Kaffes (2510.05556) | Position paper names the gap this talk answers |
| 12 | **Execution Independence ≠ Evidence Independence** | Evidence-Aware / Boltzmann (2607.09689) | Shared ancestor ⇒ variance floor; Best-of-N on siblings is false precision |
| 13 | **Worker-Record Algorithm + Reduce + Abstain** | Evidence-Aware (2607.09689) | Estimate · precision · evidence IDs · lineage; overlap reject; cold liar; abstain first-class |
| 14 | **Sealed Oracle: RUN ≠ EVAL** | Rebound→Remedy (2604.01476) | Scorer outside writable child; peer foil for reward-hacking via env rewrite |
| 15 | **Oracle Pedigree: Why Isolated Eval Exists** | SWE-bench (ICLR’24) | Isolated-repo verdict made sandboxes inevitable (one cite, not a benchmark sermon) |
| 16 | **Promote-Once Invariants a Client May Rely On** | Evidence-Aware (2607.09689) *(cross-ref)* | Immutable \(S_0\); frozen Obj/Epoch; remint creds; sealed oracle; structured \(r_k\) or reject; one promote bit; burn-after-promote; abstain |
| 17 | **Open Problems: ρ under CoW · WIRE Leases · Warm Channels · Promote-Once API** | — | Research close, not sales |
| 18 | **Three Questions for SRG** | — | API object? Price shared ancestry? Where may warm state live? |
| 19 | *(backup)* **Peer Number Appendix — Authors’ Tables Only** | DeltaBox · Crab · Shepherd | Cut room / hallway; never invent ms |
| 20 | *(backup)* **Claim Fence Card** | — | What we are **not** claiming (capability contract ≠ shipped inventory) |

**Spoken count target:** **18** main path. Use 19–20 only if challenged on numbers / overclaim.

---

## MAIN paper stack — must appear on stage

| Paper | Slide(s) | Attribution rule |
|---|---|---|
| Firecracker · Agache et al., NSDI’20 | 4 | Pedigree, not “we invented VMs” |
| DeltaBox · 2605.22781 | 6, 7 | Authors’ ckpt/restore ms only |
| Crab · 2604.28138 | 6, 7 | Authors’ ≤1.9% overhead; semantics-aware skip |
| Shepherd · 2605.10913 | 6, 7 | Authors’ ~134–143 ms fork; effect-trace value |
| Evidence-Aware MapReduce / Boltzmann · 2607.09689 | 12, 13, 16 | **Your** payload — worker record, cold liar, abstain |
| Rebound→Remedy · 2604.01476 | 14 | Sealed-oracle foil |
| SWE-bench · Jimenez et al., ICLR’24 | 15 | Oracle/eval pedigree (MAIN benchmark) |
| Xu–Kaffes · 2510.05556 | 11 | Foundations agenda (promoted MAIN for this AGGRESSIVE lock) |

**Speaker-notes / Q&A only (claim-fence):** AIDE² · GEAR · RRSI · OpenRath · EscapeBench · vendor eng (forkd / E2B / Daytona / Tensorlake / islo marketing ms). One verbal cite of AIDE²/GEAR allowed if asked about harness RSI — **no slide**.

---

## Explicit DO NOT (stage)

| Forbidden | Why |
|---|---|
| **Dreamer / world-model Act** | Category error for SRG; Q&A bridge only |
| **Annealing / SA / MH / Langevin cousin table** | Physics cosplay; schedule language → Q&A |
| **Bio / wet-lab isomorphism slides** | Zenity/SRE color, not CompLab proof |
| **\\law / mantra stack as load-bearing argument** | “Burn the runner…” once max in spoken close — never a slide of slogans |
| **Empty eval sermon** (“a claim needs a benchmark…”) with no numbers | Either peer+paper numbers (slides 6, 13) or cut |
| Vendor / eng ms as “ours” | Verbal landscape only |
| Gibbs-of-nature / detailed balance / “we proved CI thermodynamics” | CLAIM-FENCE |
| AIDE² / GEAR numbers on slides | Claim-fence BACKUP; speaker-notes only |

---

## Number fence (peer-only, attributed)

**On-slide OK:** Firecracker pedigree; DeltaBox ~10.83 ms ckpt / ~1.86 ms restore; Crab ≤1.9% overhead; Shepherd fork ~134–143 ms; **your paper’s** four-worker / overlap-reject / forged-precision illustrations from 2607.09689.

**Never on slide:** forkd · E2B · Daytona · Tensorlake · islo demo economics · invented ms · thermalization times.

---

## Q&A reserve (ready lines, no slides)

- **World models:** “World models make imagination cheap; forks make executable interaction cheap; for code the world is often the model — crossover cost is open, not today’s claim.”  
- **Annealing / NESS:** “Schedule cousins of Epochs; promote is a sink under drive, not an equilibrium free-energy proof.”  
- **Bio / HIL tip:** scarcity ladder one sentence — million sim forks before the assay / arm.  
- **AIDE² / GEAR:** harness RSI as outer-loop hill-climb under frozen eval — Search≠Authority for the harness, not a Cambridge result.

---

## Pre-TeX status

| Lock question | Answer (2026-09-28) |
|---|---|
| Primary | **A+C** (AGGRESSIVE) |
| World models | **Q&A only** |
| Physics | **≤1 slide equivalent** folded into 12–13 (variance floor + cold liar in words); no anneal table |
| Contribution sentence | Falsifiable thesis from DEEP-MEMO §1 — not the mantra |
| Eval clusters | Peer fork table (slide 6) + paper worker-record artifact (slide 13) |

**Next:** rewrite `talk.tex` / `academic/*.tex` only after parent confirms this spine. This file is the stage map, not the deck.

---

*AGGRESSIVE lock · scratch/AGGRESSIVE-SPINE.md · 2026-09-28 IDT*
