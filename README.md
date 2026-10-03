# Forkable Sandboxes: State, Evidence, and Authority

**Yossi Eliaz** - Principal Engineer, Incredibuild; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, **15 October 2026**, 15:00-16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- [Seminar PDF](dist/forkable-sandboxes-cambridge.pdf): **41 main frames in six acts; 39:30 of narration; no appendix, no overlays**.
- [Source and slide comments](talk.tex), [presenter guide](PRESENTER-GUIDE.md), and [complete storyline](docs/SEMINAR-STORYLINE.md).
- [Story map PDF](docs/forkable-sandboxes-story-map.pdf) and [editable vector map](docs/forkable-sandboxes-story-map.svg).
- [Claim boundaries](CLAIM-FENCE.md), [Q&A](QA-BANK.md), [bibliography](REFERENCES.md), and [experiment protocol](PREREGISTRATION.md).

## The story

A fork creates private continuations from a reached state. Reusing preparation lets an agent try alternatives and keep the result that passes the required checks. A published backup-request experiment reduced p99.9 latency from **1,800 ms to 74 ms**; repeated sampling raised SWE-bench Lite solution coverage from **15.9% to 56% at 250 samples**. The opening establishes the value of alternatives, then the cases explain how results become trustworthy.

Our software-factory cases lead with **43:44 / $10.33** for an installer repair and **about 26 min / $3.43** for a separate delivery incident. Genomics then follows **19,050 genes to eight tested combinations**, physics follows **26 successful bidirectional continuation links**, AI follows bounded experiments and deployed optimization, and security follows fast execution through confirmed vulnerabilities. Each case supplies a concrete workflow: input, method, decision and result.

The published AI cases include an autoresearch session's **0.997900 → 0.969686** validation score and AlphaEvolve's **0.7% fleet compute recovery**. AFL++ documents **10–20×** persistent-mode throughput gains; CyberGym's separate latest-code campaign reports **56 crashes and 22 confirmed zero-days** for OpenHands/GPT-5. The full source and denominators are in [REFERENCES.md](REFERENCES.md) and the slide comments.

We built a reducer that rejects repeated evidence IDs and carries lineage, plus an artifact-digest approval gate. The talk connects these components into a proposed state/evidence/authority contract. Selection and composition use exact artifact verification; numeric reduction combines measurements of one common target. Experiments then choose a preparation backend, assess environmental co-failure, resolve the behavioral test obligation, and describe repair repeatability.

## Six acts

| Act | Frames | Job in the argument |
|---|---:|---|
| 1 - Opportunity | 1-4 | Define private continuations; show published gains and our concrete run results |
| 2 - Concrete cases | 5-14 | Four software frames, genomics, physics, two AI cases and two security cases |
| 3 - Runtime contract | 15-23 | Choose state semantics, constrain authority, account for costs, verify publication |
| 4 - Evidence and implementation | 24-35 | Separate selection/pooling, interpret shared factors, show the built reducer and synthetic checks |
| 5 - Decisions from experiments | 36-40 | Test preparation cost, environmental co-failure, targeted coverage, and repair repeatability |
| 6 - Result | 41 | Return to the lifecycle and the runtime decisions the evidence supports |

## Evidence and source record

The factory cases ran serially through Airflow and Docker Sandboxes, with hosted models through Databricks. The API traces measured creation or restore-run-capture. Duplicate rejection, lineage carriage and digest binding are built; the integrated branching workflow, dependence calibration and restore authority remain proposed. Precise limits live in `CLAIM-FENCE.md` and slide comments.

`PREREGISTRATION.md` is unchanged. H2 inference amendments for reused families and temporal dependence are proposed before collection. The public pre-repair substitute needs tree-equivalence verification. No experiment result is claimed.

## Editing and building

`talk.tex` is the canonical entry point; act indexes order the active frames. Use `make deck` and `make dist`. Frame-count and no-overlay checks apply to the **41-frame deck**. Historical files in `acts/7-endmatter/` and `archive/` remain as source records, outside the presentation. Their complete bibliography is preserved in `REFERENCES.md`.
