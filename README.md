# Forkable Sandboxes Cambridge seminar

This academic talk connects reusable execution with the evidence and authority needed to accept a result. It follows a personal path through container security, biological physics, genomics, immune-related combination assays, automotive perception and execution systems.

- [Seminar PDF](dist/forkable-sandboxes-cambridge.pdf): **57 main slides, 41:25 planned narration, no appendix or overlays**.
- [Presenter guide](PRESENTER-GUIDE.md): timed spoken cues and retained Q&A detail.
- [Two-sentence slide takeaways](SLIDE-TAKEAWAYS.md): the point and practical lesson of every slide.
- [Review of all original 57 slides](DECK-REVIEW.md): argument, keep/rewrite/merge decisions and final locations.
- [Story and canonical slide map](deck-storyline.md).
- [References](REFERENCES.md), [claim boundaries](CLAIM-FENCE.md), [QA](QA.md) and [preregistration](PREREGISTRATION.md).

## The story

The dated overview follows early systems/security work (2010–2016), biological and genomic research (2016–2021), a published cancer-drug combination result (2019), NRGene gene-editing prediction (2020–2021), Mobileye junction perception (2021–2024), and Incredibuild/forkable compute (2025–2026). Its headings explain the work before naming tools. Career periods follow the speaker’s own website; projects overlap and the 2019 label is a publication event. The driving slide uses a credited official Mobileye photo and a concrete pedestrian/braking example, then connects it to repairing a failing test. The detailed science remains on the following slides.

Forkable compute organizes private alternative executions from a useful reached state. The proposed API is expressed in Python. Build caches, worktrees, snapshots and replay preserve different state. A warm reconstruction is a serious comparison, and copied guest state does not rewind remote effects or grant publication authority.

Published examples attach mechanisms to values: AFL++ persistent mode reports typical **10–20×** speedups; SWE-bench Lite sampling raises coverage from **15.9% to 56%**; autoresearch validation bits per byte fall from **0.997900 to 0.969686**; AlphaEvolve reports **0.7%** average fleet compute recovery. Coauthored examples retain separate assays and **26** checked three-body links with Ori Chamo. The factory's **43:44 / $10.33** repair, missing direct test, and later teardown loss show what acceptance needs. CyberGym distinguishes **56 crashes** from **22 confirmed zero-days**.

Section agendas introduce the examples and runtime, then the evidence bridge explains the return path. The technical spine is **run → evidence → acceptance**. Runtime reuses state and starts continuations. Evidence names the exact artifact, executed check and shared observations. Acceptance selects, composes or pools under the appropriate checks, with publication authority outside the child. Duplicate rejection is implemented; dependence-aware refusal and the integrated external checker remain design requirements. A set-union example explains duplicate observations; a covariance-weighted equation explains how a justified model can account for shared errors. The two planned experiments have not started.

ComputeSDK’s **2 October 2026** Burst TTI run places Isorun first at **72.77 ms median**, with 100/100 successful requests. Its create-to-first-command endpoint differs from our **3.44 s** create-only trace; the new slide updates the landscape without claiming a controlled speedup. The dated raw JSON is preserved in `evidence/`.

## Six acts

| Act | Slides | Purpose |
|---|---|---|
| Motivation | 1–15 | Personal mechanisms, Python API and execution vocabulary |
| Examples | 16–33 | Reuse, evaluated search and checked outcomes across fields |
| Runtime | 34–42 | State choice, resource tradeoffs, effects and current authority |
| Evidence | 43–52 | Selection, composition, identities and justified precision |
| Acceptance | 53–55 | Exact checks, durable bytes and applied merge rules |
| Conclusion | 56–57 | Reuse state, run alternatives, check outside the child, accept once |

## Build and edit

`talk.tex` is canonical. The act indexes order active frames; other source files are retained research/Q&A records. `make dist` compiles the PDF and regenerates the presenter guide. CI verifies **57 pages**, displayed content and a 35–45 minute cue window. Every active frame has a spoken note and hidden Q&A detail. Secondary mathematics and probes remain outside the main narration. PREREGISTRATION.md is preserved unchanged.
