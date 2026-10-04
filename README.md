# Forkable Sandboxes Cambridge seminar

This academic talk connects reusable execution with the evidence and authority needed to accept a result. It follows a personal path through container security, biological physics, genomics, immune-related combination assays, automotive perception and execution systems.

- [Seminar PDF](dist/forkable-sandboxes-cambridge.pdf): **50 main slides, 37:10 planned narration, no appendix or overlays**.
- [Presenter guide](PRESENTER-GUIDE.md): timed spoken cues and retained Q&A detail.
- [Review of all original 57 slides](DECK-REVIEW.md): argument, keep/rewrite/merge decisions and final locations.
- [Story and canonical slide map](deck-storyline.md).
- [References](REFERENCES.md), [claim boundaries](CLAIM-FENCE.md), [QA](QA.md) and [preregistration](PREREGISTRATION.md).

## The story

State and feedback recur across the speaker's work. Twistlock learned container behavior and enforced an image model. Cytosim and graph measures quantified biological self-organization. POSSUMM kept genome-contact computation sparse; ENCODE made execution traceable. CRISPR-IL/GoGenome with Noam Barkai used measured editing outcomes for subsequent designs. PD-L1 combination assays checked both cell killing and induced expression; adaptive immunotherapy is a research direction. Mobileye perception supplies the observe/action connection. These are thematic relationships across overlapping work.

Forkable compute organizes private alternative executions from a useful reached state. The proposed API is expressed in Python. Build caches, worktrees, snapshots and replay preserve different state. A warm reconstruction is a serious comparison, and copied guest state does not rewind remote effects or grant publication authority.

Published examples attach mechanisms to values: AFL++ persistent mode reports typical **10–20×** speedups; SWE-bench Lite sampling raises coverage from **15.9% to 56%**; autoresearch validation bits per byte fall from **0.997900 to 0.969686**; AlphaEvolve reports **0.7%** average fleet compute recovery. Coauthored examples retain separate assays and **26** checked three-body links with Ori Chamo. The factory's **43:44 / $10.33** repair, missing direct test, and later teardown loss show what acceptance needs. CyberGym distinguishes **56 crashes** from **22 confirmed zero-days**.

The technical spine is **run → evidence → acceptance**. Runtime reuses state and starts continuations. Evidence names the exact artifact, executed check and shared observations. Acceptance selects, composes or pools under the appropriate checks, with publication authority outside the child. Duplicate rejection is implemented; dependence-aware refusal and the integrated external checker remain design requirements. The two preregistered tests are not yet run.

## Six acts

| Act | Slides | Purpose |
|---|---|---|
| Motivation | 1–15 | Personal mechanisms, Python API and execution vocabulary |
| Examples | 16–31 | Reuse, evaluated search and checked outcomes across fields |
| Runtime | 32–39 | State choice, resource tradeoffs, effects and current authority |
| Evidence | 40–46 | Selection, composition, identities and justified precision |
| Acceptance | 47–49 | Exact checks, durable bytes and preregistered decisions |
| Conclusion | 50 | Reuse state, run alternatives, check outside the child, accept once |

## Build and edit

`talk.tex` is canonical. The act indexes order active frames; other source files are retained research/Q&A records. `make dist` compiles the PDF and regenerates the presenter guide. CI verifies **50 pages**, displayed content and a 35–45 minute cue window. Every active frame has a spoken note and hidden Q&A detail. Secondary mathematics and probes remain outside the main narration. PREREGISTRATION.md is preserved unchanged.
