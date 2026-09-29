# AI (SW) Factories*

## Forkable Sandboxes as a Runtime for Automated Search and Development

**Yossi Eliaz** — Principal Engineer, Incredibuild / islo.dev; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group · 15 October 2026 · 15:00–16:00 BST · FW11 + Microsoft Teams.

*Factory understood as an atelier: a workshop for exploration, experimentation, and refinement.*

- **[Download the 40-slide seminar PDF](dist/forkable-sandboxes-cambridge-40.pdf)**
- **[Standalone LaTeX source with speaker notes](talk.tex)**
- **[Presenter guide and full slide notes](PRESENTER-GUIDE-40.md)**
- **[Claim boundaries and result provenance](CLAIM-FENCE.md)**
- [Cambridge event listing](https://www.talks.cam.ac.uk/talk/index/273181/)

## The argument

How can a system preserve a useful computational state, explore alternatives, and turn their results into justified decisions?

Forkable sandboxes provide a runtime mechanism. Search and reinforcement learning allocate computation. Evidence, communication, and joint validation determine which results can be accepted. The talk follows eight candidate changes from isolated trials to a documented integration decision.

The motivating applications are computational biology, scientific computing, model post-training, and development and maintenance of large software systems. These applications require different evaluation criteria and state boundaries.

## Seminar structure

| Slides | Topic | Planned time |
|---|---|---|
| 1–5 | Eight candidates, applications, and the systems hypothesis | 4:30 |
| 6–15 | State, continuation contracts, mechanisms, costs, and architecture | 10:25 |
| 16–22 | Stochastic search, evolution, biology, RL, and compute allocation | 7:55 |
| 23–32 | Scientific verification, dependence, communication, and composition | 13:05 |
| 33–40 | Implementation evidence, proposed experiments, and research questions | 8:50 |

Speaker cues total **44:45**, leaving time for questions in the one-hour slot. The presenter guide is generated from the canonical source; it includes a shorter pacing route.

## Contributions and scope

The runtime and promotion architecture are proposals. The reported implementation evidence consists of a reference numerical reducer, synthetic checks, and a four-worker named-snapshot integration trace. The talk does not report a controlled end-to-end speedup, a general dependence model, or deployments in the motivating open-source projects.

The biological connection concerns how local branching mechanisms shape global network structure. The three-body paper with Ori Chamo illustrates testing connectivity behind an apparent split in a projected representation. The examples have distinct roles and do not imply quantum interference or statistical independence between software forks.

Selected sources:

- [Eliaz, Evidence-Aware MapReduce for Forkable Compute](https://arxiv.org/abs/2607.09689), preprint, 2026.
- [Chamo and Eliaz, Continuation Geometry Resolves Apparent Branch Splitting in Unequal-Mass Three-Body Orbits](https://ai.vixra.org/abs/2608.0069), preprint, 2026.
- [Eliaz et al., Insights from Graph Theory on the Morphologies of Actomyosin Networks with Multilinkers](https://arxiv.org/abs/2006.06503), Physical Review E, 2020.
- [Liman et al., The role of the Arp2/3 complex in shaping the dynamics and structures of branched actomyosin networks](https://www.pnas.org/doi/10.1073/pnas.1922494117), PNAS, 2020.

Other primary references are linked on the relevant slides.

## Build and publication

`make academic` compiles the standalone canonical source. `make short` builds the separate historical 30-minute cut. `make dist` builds both PDFs. GitHub Actions checks that the canonical PDF contains exactly 40 pages, builds both cuts, and publishes the PDFs under `dist/`.

The canonical presentation is `talk.tex` and its 40-slide PDF. The earlier `talk-30min.tex`, `slides/`, `academic/`, `swarm/`, and research notebooks remain as historical background; their claims and numbering may differ from this revised seminar. They are not additional slides in the canonical talk.
