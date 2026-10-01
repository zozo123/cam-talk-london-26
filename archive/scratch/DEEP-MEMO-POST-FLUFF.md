# Deep memo — Cambridge SRG · after the fluff critique
**Audience:** Yossi Eliaz · CompLab systems researcher voice + his research identity  
**Slot:** Thu 15 Oct 2026 · 15:00–16:00 BST · FW11 · CL Systems Research Group  
**Constraint:** Think deeply. **Do not rewrite TeX yet.** Below P0 cut lists.  
**Sources used:** talks.cam/273181 abstract; `FULL-ACADEMIC.md` + `academic/*.tex`; CLAIM-FENCE / DECK-BEATS / OUTLINE; arXiv:2607.09689v3; swarm A–G; WORLD-MODELS-BRIDGE; TRAINING-ENVIRONMENTS; RustChinaConf + Zenity NYC venue notes.

---

## 0. Blunt diagnosis in one paragraph

The current academic deck is not “too long.” It is **three talks wearing one title**. The published SRG abstract promises a **systems substrate seminar** (FS, net/creds, repro, clone, build/test, recovery/obs). The deck delivers a **TED manifesto** (Search≠Authority mantras), a **world-models ML bridge**, a **cross-domain isomorphism sermon**, and only then, as garnish, the systems material SRG actually booked. Your real paper (2607.09689) is buried as Act II½ optional physics cosplay. Your real product surface (islo / fork economics) is fenced into “verbal landscape.” The capability contract (G) is asserted as the contribution while living in the appendix as an API sketch. That is contribution insecurity made visible.

---

## 1. What is the actual research claim?

### One falsifiable thesis sentence (recommended)

> **Cheap CoW fork of a prepared machine makes execution fan-out economically free, but does not increase independent evidence; a systems runtime for agentic search must therefore expose fork of authenticated \(S_0\), credential remint, sealed oracle outside the child, and a reduce that carries lineage/precision and can abstain — otherwise Best-of-N on siblings is false precision.**

That sentence is falsifiable: build two factories (lineage-aware reduce + abstain vs scalar majority vote on CoW siblings) under controlled shared-root ρ, and show overconfidence / wrong promote rate.

### Separate the three claims the deck currently conflates

| Layer | Claim | Falsifiable? | Stage role at Cambridge |
|---|---|---|---|
| **(a) Systems claim** | Agent sandboxes need Firecracker-class isolation + snapshot/fork primitives for FS+mem, with credentials and verifier **not** inherited by CoW; warm heat must live *beside* the fork. | Latency/fidelity/leakage benchmarks vs cold rebuild / cached container / restore / fork (your TRAINING-ENVIRONMENTS matrix). | **Primary. Own the hour.** |
| **(b) Methodological claim** | Search≠Authority / Fork→Reduce→Promote is the *control-plane contract* that makes (a) usable for SW factories and coding-RL episodes. | Can you name invariants a client may rely on (immutable \(S_0\), frozen Obj digest, one promote bit, structured evidence or reject, burn-after-promote) and show a failing system when any is dropped? | **Secondary spine language**, not the paper. |
| **(c) Physics analogy** | Under LAN/Wald, inverse-information pooling looks like a product of Gaussian kernels; \(\beta\equiv n\); \(\Delta\) = Cochran \(Q\); cold liar = forged \(P_o\). | Algebra identity + synthetic checks in 2607.09689 (already done). Does **not** falsify “CI is thermodynamics.” | **Off stage or ≤2 slides / Q&A.** Paper owns this; talk cites it. |

### Title / thesis conflation — name it

The published title *“Forkable Sandboxes: The Runtime Layer for AI Software Factories”* plus the academic deck currently tries to be **three talks**:

1. **SRG systems talk** (what talks.cam sold): isolation, FS, net/creds, repro, clone, build/test, recovery/obs.  
2. **Evidence-aware reduce talk** (what 2607.09689 actually contributes): fan-out ≠ evidence; worker record; abstain.  
3. **World-model / training-env / universal-hillclimb manifesto** (what FULL-ACADEMIC and FINAL-DECK elevated): Dreamer dual, coding-RL reset, SW≅RL≅HIL≅bio isomorphism, annealing cousins.

Until you pick one primary, every mantra (“Burn the runner…”) is covering for the missing decision.

---

## 2. Contribution boundary vs cousins

| System | Relationship | What they own | What you do **not** own |
|---|---|---|---|
| **Firecracker** (NSDI’20) | **Pedigree / reuse** | MicroVM isolation wall; snapshot restore culture | You did not invent the wall |
| **DeltaBox** (2605.22781) | **Cousin — how-fast** | Coupled FS+mem change-based C/R (~10.83 ms ckpt / ~1.86 ms restore, *their* tables) | Do not present as your numbers or “we built DeltaBox” |
| **Crab** (2604.28138) | **Cousin — what/when** | Semantics-aware skip; ≤1.9% overhead | Complementary, not yours |
| **Shepherd** (2605.10913) | **Cousin — API object** | Effect-trace / `scope.fork()` as meta-agent value (~134–143 ms) | Closest “fork as programmable value”; still not your system |
| **CRIU** | **Reuse / substrate** | Process C/R engine under Crab/DeltaCR | Commodity mechanism |
| **gVisor** | **Trade-off foil** | Density + syscall interception middle wall | EscapeBench-class threat → usually insufficient outer wall for untrusted shell agents |
| **E2B / Tensorlake / Daytona / forkd** | **Landscape / eng** | Product CoW fan-out; FILESYSTEM vs MEMORY snapshots | **Verbal only.** Never on-slide ms as “ours” |
| **islo + boltzmann-mapreduce** | **Yours** | Named-snapshot restore path; worker evidence contract; end-to-end four-worker trace; platform create/restore tables in the *paper* | Not a full OS paper; not Byzantine reduce; not shipped WIRE lease science |

### What can he uniquely own in 45 minutes?

Not another CoW microbenchmark. Not “we invented fork.”  

**Unique ownership window:**

> The **missing joint contract** between (i) forkable execution substrates that cousins already race on latency, and (ii) evidence-aware fan-in that your paper actually writes down: *fork makes workers; reduce must see lineage; promote is singular; credentials/oracle never ride the CoW.*

Spoken as systems, not manifesto:

- Cousins answer **how fast / what to checkpoint / what object a meta-agent holds**.  
- You answer **what the client may rely on after the fork returns** — especially when siblings share a root.

That is a Cambridge-shaped contribution: interface + failure modes + open problems, with 2607.09689 as the one artifact you personally authored.

---

## 3. Why the academic deck failed structurally

Not “too many slogans.” Five structural failure modes:

### 3.1 Teaching-for-mixed-audience as architecture

FULL-ACADEMIC explicitly designs for “mixed systems / ML / software-engineering” and burns Acts I–II on glossary, RL 101, Dreamer vs fork. SRG is not a freshman survey. Teaching breadth **displaced** the abstract’s six surfaces. When you teach everyone, you prove nothing to anyone who already knows Firecracker.

### 3.2 Isomorphism as proof

“Three factories, same loop” / universal hillclimb is an **illumination**, not a theorem. The deck treats SW≅RL≅HIL≅bio as if cross-domain noun-swap *establishes* the runtime claim. CompLab hears: “you haven’t measured fork, you’ve renamed MapReduce.” Isomorphism belongs as a **30-second bridge** or Q&A, not Act II of a systems seminar.

### 3.3 Mantra as substitute for invariant

“Burn the runner. Keep the proof. Fork the machine, not the trust.” / “Search can be plural. Authority must be singular.” / “The student cannot grade their own exam.”  

These are **compression of invariants**, useful once. The deck uses them as *load-bearing argument*. Invariants should appear as a **client-rely table** (immutable \(S_0\), remint on fork, sealed Obj digest, one promote bit, structured \(r_k\) or reject, abstain under shared \(\mathcal{L}\)). Mantras without that table are TED.

### 3.4 Empty eval slide as moralizing

Slide 30 (“A research claim needs a benchmark, not a slogan”) lists *questions to measure* and no numbers of yours. That is the talk confessing it has no eval while scolding the room for wanting one. Either:

- put **peer-attributed** DeltaBox/Crab/Shepherd + **your paper’s** Table 1/2 (islo four-worker 6.70 s; overlap reject; forged precision), or  
- cut the sermon.

An empty methodology matrix is worse than no eval slide.

### 3.5 Appendix API = contribution insecurity

G names *Fork, Reduce, Promote* as “the paper this talk contributes,” then the academic deck parks the API in appendix slide 35–37 while the main spine sells world models and mantras. If the contribution is the contract, it is **slide 8–12 material with invariants**, not appendix. Parking it in the appendix tells SRG you don’t believe it survives peer pressure.

---

## 4. The talk SRG actually wants

### Published abstract → obligations

> filesystem state · networking and credentials · reproducibility · fast cloning · build/test execution · recovery · observability · architecture, trade-offs, open systems problems.

Map → **minimal slide spine (≤20)** — systems titles only:

| # | Slide title (NSDI/SOSP workshop tone) | Abstract slot |
|---|---|---|
| 1 | Forkable sandboxes as agent execution substrate | title / thesis |
| 2 | Threat & workload: untrusted shell + fan-out search | why now |
| 3 | Capability checklist (six surfaces) | abstract map |
| 4 | Filesystem state as a first-class snapshot object | FS |
| 5 | Networking & credentials: remint on fork | net/creds |
| 6 | Reproducibility: named \(S_0\) → identical restore | repro |
| 7 | Isolation trade-off: namespaces / gVisor / Firecracker-class | architecture |
| 8 | Fast cloning: CoW / delta C/R (peer tables) | fast cloning |
| 9 | Fork taxonomy: FS · mem · VM · delta · effect-trace | architecture |
| 10 | Warm factory *beside* the fork (heat ≠ authority) | build/test |
| 11 | Recovery & receipts that outlive the child | recovery/obs |
| 12 | Parallel worlds diagram: shared past, divergent futures | synthesis |
| 13 | Fork ≠ independent evidence (Eq. 1 in words) | **2607 sits here** |
| 14 | Worker record + reduce + abstain (your artifact) | **2607 sits here** |
| 15 | Sealed oracle / RUN≠EVAL (peer: Rebound) | trust boundary |
| 16 | Invariants a client may rely on | contribution |
| 17 | Open problems: ρ under CoW · WIRE leases · warm channels · promote-once | open problems |
| 18 | Agenda + three questions for SRG | close |
| 19–20 | (optional) peer number appendix / claim fence | backup |

**Where 2607.09689 sits:** slides 13–14 as the **systems consequence of cheap fork**, not as Act II½ physics theatre. Cite the paper for the worker contract + cold liar + abstain agenda. One equation in words: shared ancestor ⇒ variance floor.

**Where world-models bridge sits:** **Q&A only** (or one appendix slide if someone asks “isn’t this Dreamer?”). Line ready: *World models make imagination cheap; forks make executable interaction cheap; for code the world is often the model — and that is a research question about crossover cost, not today’s claim.* Do not build Act II around Bonnie Li / Dreamer 4.

**Where training-env reset sits:** one spoken bridge under build/test or recovery (“coding-RL episode = \(S_0\) + task + tools + verifier + reset”), not a Scale/Surge/Mercor market slide.

---

## 5. Intellectual honesty risks

| Risk | How it shows up now | Honest fix |
|---|---|---|
| **Overclaiming factory API** | G’s “paper this talk contributes” + appendix API + “path-integral CI” language | Say **capability contract / research agenda**. Explicitly: not shipped N-way fork-merge everywhere; not production path-integral CI. |
| **Under-selling 2607.09689** | Optional Act II½; Boltzmann branding; “physics with teeth” instead of “systems reduce contract” | Lead with **Evidence-Aware MapReduce** as *your* artifact. Boltzmann/Gibbs naming is the paper’s own fence (“interpretation, not new estimator”) — on stage prefer **evidence-aware reduce**. |
| **Physics cosplay** | Partition function, anneal family, NESS, Hamiltonian-as-proposal, promote=absorbing sink as if proved | Keep \(\beta\equiv n\), cold liar, \(\Delta\). Drop SA/MH/Langevin table from main path. Driven/NESS = Q&A if a physicist bites. |
| **“Universal hillclimb” as rhetoric** | Cross-domain table as proof of systems depth | One slide max: “same slots, different oracles” — then return to FS/creds/clone. Biology/HIL tip scarcity is Zenity/SRE color, not CompLab proof. |
| **World-model elevation** | FINAL-DECK: “CWM bridge is not a side analogy; it is the elevation” | For SRG that elevation is a **category error**. Elevation for Cambridge is Xu–Kaffes agenda + your reduce contract. |

---

## 6. Emotional / career read — punchline by venue

| Venue | Date | Audience | Punchline that belongs there | What to **strip** |
|---|---|---|---|---|
| **Cambridge SRG** | 15 Oct · 45+15 | OS/distributed/systems faculty & students (Xen/Unikernel lineage in the room’s memory) | *Fork is cheap; evidence is not. Here is the contract and the open ρ/WIRE problems.* | Escape-door thriller; wet-lab AGI; Rust cargo poetry; Dreamer Act |
| **RustChinaConf** | 17 Oct · ~25+10 | Rust/production/AI-infra engineers | *Disposable runners, warm Cargo factory* — concrete cache/isolation/engineering takeaways | StatPhys; world models; HIL robot hour |
| **Zenity NYC** | 21 Oct · security summit | Agent security practitioners | *Your agent escaped without escaping the sandbox* — KEY/FOLDER/WIRE/VERDICT doors; isolation ≠ acceptance | Boltzmann algebra; factory API paper cosplay; universal hillclimb |

**Career rule:** Cambridge must stay **systems-hard**. If you spend FW11 sounding like Zenity (doors) or like a keynote (mantras), you burn the rare CompLab slot that legitimizes islo/2607 as research. Put the security punchline on Oct 21; put the Rust engineering punchline on Oct 17; put the **falsifiable substrate + reduce contract** on Oct 15.

Emotional temptation to watch: the academic deck’s humor (“100 agents, one laptop”) and mantra stack feel like confidence. At SRG, confidence without peer numbers + your artifact reads as **evasion**.

---

## 7. Recommended spine rewrite (outline only · no TeX)

**Format:** 45 min talk + 15 min Q&A · ≤18 slides · NSDI/SOSP workshop titles · peer numbers only where attributed · one open-problem close.

### Minute map

| Min | Block | Slides |
|---|---|---|
| 0–3 | Hook: agents run code; substrate missing | 1–2 |
| 3–18 | Six surfaces + isolation trade-off + peer fork | 3–11 |
| 18–28 | Evidence wall: fork≠independence + your reduce | 12–15 |
| 28–40 | Invariants + open problems | 16–17 |
| 40–45 | Close: three SRG questions | 18 |
| 45–60 | Q&A (world models, physics, vendor ms, HIL) | — |

### Slide titles (workshop tone)

1. **Forkable Sandboxes as an Execution Substrate for Agents**  
2. **Workload: Untrusted Shell + Search Fan-Out**  
3. **Six Surfaces the Abstract Promised**  
4. **Filesystem State Is a Snapshot Object**  
5. **Credentials Must Not Survive CoW**  
6. **Named \(S_0\) and Restore Fidelity**  
7. **Isolation Walls: Process, gVisor, MicroVM**  
8. **Fast Cloning: Peer Measurements (DeltaBox / Shepherd)** — *authors report…*  
9. **Warm Build/Test Heat Belongs Beside the Fork**  
10. **Recovery: Crash the Runner, Keep the Receipt**  
11. **Diagram: Shared Past, Divergent Futures, One Promote**  
12. **Execution Independence ≠ Evidence Independence**  
13. **Evidence-Aware Reduce (arXiv:2607.09689)** — worker record, overlap reject, cold liar  
14. **Sealed Oracle: RUN ≠ EVAL** (Rebound as peer foil)  
15. **Client-Rely Invariants (Search≠Authority without TED)**  
16. **Open Problems: ρ · WIRE Leases · Warm Channels · Promote-Once API**  
17. **What We Are Not Claiming**  
18. **Three Questions for SRG**

### Where peer numbers go

- **Slide 8 only (attributed):** DeltaBox ~10.83 ms ckpt / ~1.86 ms restore **or** Crab ≤1.9%; Shepherd fork ~134–143 ms; Firecracker as pedigree cite.  
- **Slide 13 (yours, from paper):** four-worker named-snapshot path; overlap reject; forged-precision clip as *vulnerability illustration*, not Byzantine solution.  
- **Never on slide:** forkd / E2B / Daytona / Tensorlake / islo marketing ms.

### Open-problem close (pick three, ask the room)

1. What is the right API object for a forkable machine (FS, mem, GPU, display, external side-effects)?  
2. How should a reducer price shared snapshot ancestry instead of pretending siblings are i.i.d.?  
3. Where may warm state live so density is not a covert channel — and how do credentials remint at fork latency?

---

## 8. Decision he must make before any TeX edit

Pick **ONE** primary contribution for the hour:

| Option | Primary | Fits abstract? | Owns 45 min? | Risk |
|---|---|---|---|---|
| **A. Fork substrate** | Architecture of FS/net/creds/clone/recovery; peer landscape; open OS problems | **Best fit** | Yes, if you bring sharp trade-offs + open problems | Looks survey-ish unless you add *your* evidence wall |
| **B. Search≠Authority control plane** | Factory/Cell/epoch/promote contract | Partial | Only if invariants + failure demos, not mantras | Overclaim / product cosplay |
| **C. Evidence-aware reduce** | 2607.09689 as the talk | Weak vs abstract wording | Strongest *personal* research claim | Feels like a paper talk; must still honor six surfaces in Act I |
| **D. Training-env reset thesis** | Coding-RL episode = reset primitive; SWE-smith/Scale landscape | Weak | Wrong room primary | Sounds like market category talk |

### Rank and recommend

1. **A as chassis + C as payload** *(recommended)*  
   - Hour promise matches talks.cam.  
   - Mid-talk turns to *your* falsifiable systems result: fan-out ≠ evidence.  
   - B’s language appears only as the invariant table (not the title claim).  
   - D and world-models → Q&A.

2. **C alone** — if you are willing to soft-retitle verbally (“with a focus on evidence-aware reduction”) and accept abstract mismatch risk with Yaman/SRG hosts.

3. **B alone** — only after you can show a client-rely table + a failing system when an invariant breaks. Currently under-instrumented; appendix API proves the gap.

4. **D** — last for Cambridge; better as LLMday/SRE color.

### Pre-TeX lock questions (answer in writing before touching `talk.tex`)

1. Primary = **A+C** or pure **C**?  
2. World models: **Q&A only** — yes/no?  
3. Physics: **≤1 slide** (cold liar + variance floor) or **zero + Q&A**?  
4. Contribution sentence on slide 1 — paste the falsifiable thesis from §1, not the mantra.  
5. Eval: which **two** number clusters appear (peer fork table + paper Table 1/2)?

Until those five are locked, any TeX rewrite will recreate the three-talk conflation under nicer fonts.

---

## Bottom line

SRG booked a **substrate and open-problems** seminar. You prepared a **manifesto with optional algebra**. The fix is not another P0 cut list. The fix is choosing **fork substrate as the hour’s chassis and evidence-aware reduce as the only net-new payload**, demoting Search≠Authority to invariants, demoting physics and world models to Q&A, and putting peer + paper numbers where the empty eval sermon currently moralizes.

**Do not rewrite TeX until §8 is decided.**
