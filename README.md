# Forkable Sandboxes: The Runtime Layer for AI Software Factories

**Yossi Eliaz**: Principal Engineer, Incredibuild; islo.dev; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, 15 October 2026, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- **[Seminar PDF](dist/forkable-sandboxes-cambridge-40.pdf)** (33 main slides + backups; the file name is kept for old links)
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

The talk then covers the seven advertised surfaces, the fork (SnowFlock's 2009 Figure 1, what forks copy, when fork pays, the runtime interface) and the count. The count covers execution vs evidence multiplicity, the cluster labels only the runtime holds, and the receipt contract (arXiv:2607.09689). Two pre-registered tests follow, and the talk closes with *Hedging works when failures are independent. Fork the machine, not the trust.*

The speaker's own papers appear where they are used:
- **ENCODE pipelines:** reproducibility.
- **Bitcoin (2022) and iScience (2026):** recovering hidden cluster labels.
- **PRE and PNAS (2020):** branching networks, as motivation for the coupling test.

The full research record is in the backups.

## Structure

| Slides | Act | Time |
|---|---|---|
| 1–8 | The question: hedging, forks vs checks, numbers, where 43 minutes went, the run, the map, the claims | 8:45 |
| 9–16 | The wall: seven surfaces, numbered on each slide | 9:45 |
| 17–23 | The fork: SnowFlock Fig. 1, what forks copy, held effects, cost, isolation, the interface | 10:25 |
| 24–28 | The count: adaptivity, multiplicity, cluster labels, the receipt, precision | 7:25 |
| 29–33 | Test and agenda: two pre-registered tests, the redesigned run, open problems, close | 6:40 |

The cues are derived from the script at about 105 wpm plus reading pauses: 43:00 in total, leaving about 15 minutes for questions. Replace them with stopwatch times after rehearsal.

## Evidence status

- **Measured:** the SELFHOST-2 and SELFHOST-3 run records, and paper Table 2.
- **Built:** the reference reducer and its synthetic checks.
- **Proposed:** the fork contract and the experiment in `PREREGISTRATION.md`.
- **Not claimed:** a controlled speedup, a vendor ranking, or a factory that forks today.

`CLAIM-FENCE.md` lists every figure and its source.

## Build

- `make academic` builds `talk.pdf` and regenerates the presenter guide. It fails if any slide's notes exceed 125 wpm.
- `make dist` builds both PDFs.
- CI checks the page count and pacing, and that `PRESENTER-GUIDE.md` is current.

## Historical material

`talk-30min.tex`, `slides/`, `academic/`, `swarm/`, `scratch/` and the older outline files are research notebooks and earlier cuts. Their claims and numbering differ from the canonical deck, and they are not part of it.
