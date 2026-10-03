# Forkable Sandboxes: State, Evidence, and Authority

**Yossi Eliaz** - Principal Engineer, Incredibuild; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, **15 October 2026**, 15:00-16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- [Final seminar PDF](dist/forkable-sandboxes-cambridge.pdf): **45 main frames in six acts; no appendix, no overlays**.
- [Canonical LaTeX source](talk.tex), with slide sources and speaker notes in [acts/](acts/).
- [Presenter guide](PRESENTER-GUIDE.md).
- [Story map PDF](docs/forkable-sandboxes-story-map.pdf) and [editable vector map](docs/forkable-sandboxes-story-map.svg).
- [Claim boundaries](CLAIM-FENCE.md), [Q&A](QA-BANK.md), and [full bibliography](REFERENCES.md).
- [Original unrun experiment protocol](PREREGISTRATION.md), preserved unchanged.

## The story

An agent needs several continuations from a useful reached state. The execution mechanism must preserve what those continuations need: files and dependencies may only need worktrees or a warm template; live processes and RAM require proven checkpoint semantics. The recorded factory work orders did not demonstrate a valuable live-state workload or exercise a fork.

A small installer task instead exposed a precise validation gap: a repair changed exactly-once dispatch behavior, and the green suite plus successive reviews did not directly validate the new same-owner adoption path. A separate delivery refusal was followed by cleanup that lost the patch. These observations motivate explicit state, evidence, and authority contracts.

The built reducer rejects declared evidence reuse and carries lineage. It pools measurements of one common target; choosing or composing patches is a separate validation problem. Digest-bound approval is also built. Dependence calibration, fresh clone authority, an external evaluator, and epoch fencing remain proposed.

The proposed experiments have different jobs: preparation cost chooses the backend; environmental co-failure tests whether ancestry modeling is useful; a targeted test resolves the missing behavioral obligation; repair resamples describe repeatability. None has produced a claimed result.

## Six acts

1. **Useful reached state:** alternatives, mechanism choice, and the gap between cheap execution and reliable selection.
2. **Observed factory failures:** the actual task, dispatch race, missing direct test, misleading records, and artifact loss.
3. **Runtime contracts:** preserve or refresh state, constrain authority, verify exact artifacts, and retain recoverable results.
4. **Evidence handling:** selection versus pooling, shared factors, duplicate rejection, and uncalibrated dependence.
5. **Refutable experiments:** restore versus warm template, environmental coupling, targeted coverage, and descriptive repairs.
6. **The decision:** built enforcement, remaining uncertainty, and the next runtime choices.

The story map connects these acts. Ori Chamo / Three-Body Atlas provides a concrete example of candidate-to-screen-to-verified-claim admission, explicitly preliminary physics work rather than a fork result.

## Evidence status

**Observed:** two work orders using Airflow and Docker Sandboxes, with hosted models through Databricks; separate API-path measurements. **Built:** numeric merge, evidence-ID rejection, lineage carriage, and an artifact-digest gate. **Proposed:** branching architecture, dependence handling, child authority, and experiments. Published and illustrative results retain their own labels.

There is no claimed fork speedup, fork-induced agent correlation, platform ranking, completed dependence estimator, or self-authored merged PR from these work orders. The equal-variance/common-correlation formula describes precision of a mean, not candidate correctness or search accuracy.

`PREREGISTRATION.md` is unchanged. H2 analysis changes for reused families and temporal dependence are proposed before collection; the public pre-repair substitute also needs tree-equivalence verification. See the claim fence and Q&A.

## Editing and building

`talk.tex` is the canonical entry point. Act indexes determine frame order; each active slide contains its speaker note. Use `make deck` and `make dist` for the deck and distributable PDF. Repository tools generate the slide index and presenter guide. Frame-count and no-overlay checks apply to the **45-frame canonical deck**.

Historical files in `acts/7-endmatter/` and `archive/` are retained for source preservation and are not extra presentation pages. Their numbering and older claims do not govern this deck. The complete former bibliography is preserved in `REFERENCES.md`.
