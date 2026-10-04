# Forkable Sandboxes: Directing Executable Exploration

**Yossi Eliaz** — Principal Engineer, Incredibuild; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, **15 October 2026**, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- [Seminar PDF](dist/forkable-sandboxes-cambridge.pdf): **57 main frames in six acts; 44:00 of narration; no appendix or overlays**.
- [Source and slide comments](talk.tex), [presenter guide](PRESENTER-GUIDE.md), and [complete storyline](deck-storyline.md).
- [Claim boundaries](CLAIM-FENCE.md), [Q&A](QA.md), [bibliography](REFERENCES.md), and [experiment protocol](PREREGISTRATION.md).

## The story

**Self-driving computation chooses its next execution from observed results.** A programmer increasingly directs exploration: specify a goal and constraints, generate executable alternatives, run them, inspect the evidence, then choose the next execution. Ordinary Von Neumann processors and instruction sets remain underneath. The change concerns how a workflow chooses and verifies its work. IF, LOOP and CALL can implement both the orchestrator and its candidates; the proposed layer makes reached states, private continuations, returned evidence and acceptance explicit.

The opening uses a cinema analogy. A player follows a prescribed sequence. An agent can choose a reached computer state, create private alternatives, run a changed continuation, then keep or discard it from observed results. Saving and restoring computer state provides the rewind; completed remote requests and other external actions remain completed.

The main path is **state → evidence → authority**: supply useful state, establish what each returned result supports, and let the controller authorize the exact artifact. The examples explain those responsibilities at the point where they matter.

Forkable state supplies private continuations from a reached parent when that state remains valid and useful. Worktrees, warm files, process or VM checkpoints, and replay supply different state surfaces. Published examples put mechanisms beside values: AFL++ reports **10–20×** persistent-mode speedups; SWE-bench Lite sampling raises coverage from **15.9% to 56%**; autoresearch's keep/revert loop reduces validation bits per byte from **0.997900 to 0.969686**; AlphaEvolve reports **0.7%** average fleet compute recovery.

Our examples then show what acceptance requires: a separate functional assay in genomics, **26** checked three-body continuation links with Ori Chamo, a **43:44 / $10.33** factory repair with a missing direct behavior test, and an approved patch lost after delivery refusal. CyberGym distinguishes **56 crashes** from **22 confirmed zero-days**. These examples motivate concrete contracts; they do not collectively measure a fork benefit.

The implemented pieces are declared duplicate-evidence rejection, lineage carriage, numerical summary merging, and artifact-digest approval. The numerical stress example has known true target **μ = 5.0**. Separate designs address useful-state fidelity, backend choice, environmental co-failure, repair repeatability, and current publication authority.

## Personal motivation

The speaker's path is **biophysics → genomics → Mobileye perception → Incredibuild → self-driving computers**. Simulations exposed state and shared structure; genome algorithms exposed computational limits; ENCODE pipelines linked execution to identifiable outputs. Autonomous and build systems motivate directing exploratory work under constraints. This trajectory explains the research question; it is not the main argument or evidence of a fork benefit. Career context is the speaker's account, and coauthored findings retain team attribution.

## Six acts

| Act | Frames | Job in the argument |
|---|---:|---|
| 1 — Motivation | 1–12 | Adaptive execution choice, personal research trajectory, and private continuations |
| 2 — Examples | 13–28 | Fuzzing, AI research, genomics, physics, factory repair, and security validation |
| 3 — Runtime | 29–38 | Choose state, check fidelity, account for resources, and place authority outside the guest |
| 4 — Evidence | 39–50 | Separate selection, composition and pooling; show implemented evidence handling and numerical checks |
| 5 — Acceptance | 51–56 | Let defined behavioral and statistical experiments change a runtime decision |
| 6 — Conclusion | 57 | Connect useful continuations to checked evidence and authorized publication |

## Evidence and source record

The factory examples ran serially through Airflow and Docker Sandboxes, with hosted models through Databricks. Separate API traces measured creation or restore–run–capture. The integrated factory branching workflow, dependence calibration, and restore authority are designs. The state probe is unrun. Precise boundaries and source identities live in [CLAIM-FENCE.md](CLAIM-FENCE.md), [QA.md](QA.md), and hidden slide comments.

[PREREGISTRATION.md](PREREGISTRATION.md) is unchanged. H2 inference amendments for reused families and temporal dependence are proposed before collection. The public pre-repair substitute needs tree-equivalence verification. No experiment result is claimed.

## Editing and building

[talk.tex](talk.tex) is the canonical entry point; act indexes order the active frames. Use make deck and make dist. The canonical deck has **57 frames**. Each page has one semantic job, one main visual or a short list, and readable body text. Hidden qadetail comments retain secondary numbers and scope; spoken note comments set the narration cues. Historical files outside the active indexes are source records, not additional presentation pages. Their bibliography remains in [REFERENCES.md](REFERENCES.md).
