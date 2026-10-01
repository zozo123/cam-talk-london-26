# Forkable Sandboxes: The Runtime Layer for AI Software Factories

**Yossi Eliaz**: Principal Engineer, Incredibuild; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, 15 October 2026, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- **[Seminar PDF](dist/forkable-sandboxes-cambridge.pdf)** (50 story slides, then end matter: detail pages, research record, references)
- **[LaTeX source with speaker notes](talk.tex)**
- **[Presenter guide, generated from the notes](PRESENTER-GUIDE.md)**
- **[Claim boundaries and provenance](CLAIM-FENCE.md)**
- **[Pre-registered experiment](PREREGISTRATION.md)**

## Advertised abstract

> As coding agents move from autocomplete to autonomous software engineering, they need an execution substrate designed for non-human developers. This talk will explore the systems challenges behind forkable, isolated environments, including filesystem state, networking and credentials, reproducibility, fast cloning, build/test execution, recovery, and observability. The focus will be on the underlying architecture, trade-offs, and open systems problems.

## The argument

The talk opens with a result the room already trusts. In *The Tail at Scale* (Dean & Barroso, CACM 2013), hedged requests cut 99.9th-percentile latency from 1,800 ms to 74 ms for 2% more requests. It works because slowness is "often not inherent in the particular request". AI agents now hedge for correctness, but a wrong answer often *is* in the request.

- **Forks find answers.** Repeated sampling takes SWE-bench Lite from 16% to 56% (Brown et al. 2024).
- **Checks decide which answer is right.** An imperfect verifier caps the gain (Stroebl et al. 2024).
- **The numbers.** A Jeff Dean-style table of fork, checkpoint and restore numbers ends with the one nobody reports: how correlated two forks' verdicts are.
- **Where the time goes.** In the speaker's own factory run, sandbox setup was 0.8% of a 43-minute work order.

The talk is one story with no backup slides. It braids systems, software engineering, AI, RL training, statistics, physics and biology; physics and biology are vocabulary and motivation, never evidence about forks, and each borrowed link is labelled as an analogy, with an ANALOGY tag on screen or in the speaker note. After the hook, a journey slide shows the same question the speaker has met in actomyosin networks, genomes, Bitcoin, an agent factory and RL training: how many independent witnesses are there?

The wall covers the seven advertised surfaces where they bit in a real run, with reward hacking as the RL name for a gamed check. The fork covers SnowFlock's 2009 Figure 1, fork's lineage on Xen, training runs as sandbox factories (Kimi K3), how a reset changes the learning problem (Go-Explore), what forks copy, held effects, when fork pays, isolation, the interface, the architecture and a promotion gate small enough to model-check. The count covers the refrain *forks multiply executions, not evidence*: a reused grader, one formula in three fields (Dean's fan-out, Dorfman's pools, the run's race), the design effect as Amdahl's law, cluster labels, common random numbers, when a swarm gels, synthetic-lethal patches, the receipt contract (arXiv:2607.09689) and forged precision. Two pre-registered tests follow, then the redesigned run, open problems and a twist: the hedging paper's own canary requests. The talk closes with *Hedging works when failures are independent. Fork the machine, not the trust.*

The speaker's own papers appear where they are used:
- **OffRisk (2023):** the off-target analogy for an out-of-plan edit (slide 14).
- **ENCODE pipelines:** the replay bar (slides 7 and 18).
- **Commun. Biol. (2021):** technical replicates vs independent experiments, and synthetic lethality (slides 33, 40 and 45).
- **Poolkeh (2020):** pooled testing as a model, not a deployment (slide 35).
- **Bitcoin (2022) and iScience (2026):** dependence the co-authors had to uncover from outside, which a fork runtime could label itself (slides 7 and 37).
- **arXiv:2607.09689:** the receipt contract and forged precision (slides 41 and 42).
- **PRE, PNAS (2020) and JPCB (2021):** actomyosin linkers, branching and avalanches, as motivation (not evidence) for the coupling test (slides 7 and 44).

Detail pages for slides 22, 28, 31, 43 and 45, the full research record and the references are untimed end matter after the close.

The delivery follows Patrick Winston's *How to Speak* (MIT, 2018): an empowerment promise in the first minute, vision and done-something inside five minutes, the slogan cycled three times, a fenced claim, spoken act seams, two questions with a seven-second wait, one prop (nine photocopies of one page), one dense slide (slide 4), and a Contributions slide that mirrors slide 10 and stays up through questions. The talk ends on the refrain and a salute, not on "thank you".

## Structure

| Slides | Act | Time |
|---|---|---|
| 1–10 | The question: hedging, forks vs checks, numbers, where 43 minutes went, the run, the journey across fields, the map, intelligence and the agentic loop, the claims | 9:45 |
| 11–20 | The wall: seven surfaces, numbered on each slide, with reward hacking and the green-check receipt, then what our runs found | 7:45 |
| 21–32 | The fork: SnowFlock Fig. 1, Xen lineage, training runs, resets, what forks copy, held effects, cost, isolation, the interface, architecture, promotion | 11:15 |
| 33–42 | The count: the second review, reused graders, one formula in three fields, N_eff as Amdahl, cluster labels, common random numbers, gelation, synthetic lethality, the receipt, precision | 9:45 |
| 43–50 | Test and agenda: two pre-registered tests with the declared physics prior, what they cannot separate, the redesigned run, open problems, the canary twist, Contributions | 6:30 |
| after 50 | End matter (untimed): detail pages (4), research record (3), references (3) | — |

The cues are derived from the script at about 105 wpm plus reading pauses: 45:00 in total, leaving about 15 minutes for questions. Replace them with stopwatch times after rehearsal.

## Evidence status

- **Measured:** the SELFHOST-2 and SELFHOST-3 run records, and paper Table 2.
- **Built:** the reference reducer and its synthetic checks.
- **Proposed:** the fork contract and the experiment in `PREREGISTRATION.md`.
- **Not claimed:** a controlled speedup, a vendor ranking, or a factory that forks today.

`CLAIM-FENCE.md` lists every figure and its source.

## Build

- `make deck` builds `talk.pdf` and regenerates the presenter guide. It fails if any slide's notes exceed 125 wpm.
- `make dist` copies the deck to `dist/forkable-sandboxes-cambridge.pdf`.
- CI checks the page count and pacing, and that `PRESENTER-GUIDE.md` is current.

## Historical material

`archive/` holds the research notebooks, earlier outlines and an earlier 30-minute cut (`talk-30min/`, `academic/`, `swarm/`, `scratch/` and the older notes files). None of it is built or published. Their claims and numbering differ from the canonical deck, and they are not part of it.
