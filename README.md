# Forkable Sandboxes: The Runtime Layer for AI Software Factories

**Yossi Eliaz**: Principal Engineer, Incredibuild; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, 15 October 2026, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- **[Seminar PDF](dist/forkable-sandboxes-cambridge.pdf)** (50 story slides, then end matter: detail pages, research record, references)
- **[LaTeX source](talk.tex)**: the root file. Each slide is one file in [acts/](acts/), and its speaker note is inside it.
- **[Presenter guide, generated from the notes](PRESENTER-GUIDE.md)**
- **[Claim boundaries and provenance](CLAIM-FENCE.md)**
- **[Pre-registered experiment](PREREGISTRATION.md)**

## Advertised abstract

> As coding agents move from autocomplete to autonomous software engineering, they need an execution substrate designed for non-human developers. This talk will explore the systems challenges behind forkable, isolated environments, including filesystem state, networking and credentials, reproducibility, fast cloning, build/test execution, recovery, and observability. The focus will be on the underlying architecture, trade-offs, and open systems problems.

## Research question

How many independent observations do $N$ forks of one agent sandbox provide, and can the runtime measure that number?

**Thesis.** $N$ forks give $N$ executions but $N_{\rm eff} = N/(1+(N-1)\rho)$ independent observations, where $\rho$ is the correlation between sibling verdicts. Hedging (Dean and Barroso, CACM 2013) works when failures are independent. Forks of one snapshot share code, model, prompt and tests, so their failures may not be independent. The runtime sees what forks share, so it is where $\rho$ can be measured.

**Contributions.** (1) A receipt contract, built, in which reused evidence stops the merge and each result carries its lineage. (2) Two measured experiments with a self-evolving loop. (3) Two pre-registered, refutable hypotheses: H1, snapshot restore beats a warm build cache by more than 10 s; H2, siblings from one snapshot fail together more than strangers ($\Delta\rho > 0.05$).

**Not claimed.** A new estimator, a controlled speedup, a ranking of platforms, a loop that forks today, or physics and biology as evidence about forks.

## Structure

| Section | Slides | Content | Time |
|---|---|---|---|
| 1 Introduction | 1–10 | Hedging and its assumption, repeated sampling, runtime numbers with the missing correlation row, the review-gate case, the question across six fields, method and scope, intelligence as choice, research question, claims and outline | 9:05 |
| 2 Case study | 11–20 | Two experiments across the seven advertised surfaces (networking and credentials, filesystem state, build and test, recovery, observability, reproducibility, fast cloning), with six findings | 6:55 |
| 3 Design | 21–32 | Related work from Xen and SnowFlock to training-scale sandboxes, what a fork copies, held effects, a cost model, isolation, the runtime interface, the architecture, a promotion gate to model-check | 10:15 |
| 4 Analysis | 33–42 | Dependent reviews, reused graders, one formula in three fields, $N_{\rm eff}$ as Kish's design effect and Amdahl's law, cluster labels, common random numbers, gelation, patch interaction, receipts, misreported precision | 9:00 |
| 5 Evaluation | 43–47 | Test 1 (restore against a warm cache), the declared prior, Test 2 (sibling coupling), threats to validity, the redesigned run | 3:55 |
| 6 Conclusion | 48–50 | Limitations and open problems, future work (a canary for correlation), conclusions | 2:25 |
| End matter | after 50 | Untimed: detail pages (4), research record (3), references (3) | — |

Every evidence slide carries a tag: MEASURED (our run records), BUILT (implemented and tested, or a synthetic check), PROPOSED (designed, not run), PUBLISHED (other people's work) or ANALOGY (borrowed vocabulary, never evidence). The cues total 41:35 at about 100 words per minute, which leaves time for questions in the hour. Replace them with stopwatch times after rehearsal.

The speaker's own papers appear where they are used: OffRisk (slide 14), the ENCODE pipelines (slides 7 and 18), the 2021 CRISPR screen (slides 33, 40 and 45), Poolkeh (slide 35), the Bitcoin and iScience studies (slides 7 and 37), arXiv:2607.09689 (slides 4, 28, 30, 41 and 42) and the actomyosin papers (slides 7 and 44). The physics papers motivate Test 2 and are not evidence for it.

## Evidence status

- **Measured:** the SELFHOST-2 and SELFHOST-3 run records, and paper Table 2.
- **Built:** the reference reducer and its synthetic checks.
- **Proposed:** the fork contract and the experiment in `PREREGISTRATION.md`.
- **Not claimed:** see above.

`CLAIM-FENCE.md` lists every figure and its source.

## Repository layout

```
talk.tex                    root file: document class, preamble, the section indexes
preamble/
  packages.tex              packages, TikZ libraries, Beamer options
  theme.tex                 colours and Beamer theme
  macros.tex                frame-title strip, evidence tags, text helpers, fork-tree symbol
  tikz-styles.tex           shared node and arrow styles
  metadata.tex              title, author, PDF metadata
acts/
  1-introduction/           slides 1-10: motivation, the case, research question, claims and outline
  2-case-study/             slides 11-20: two experiments across seven runtime surfaces (the wall)
  3-design/                 slides 21-32: related work, what a fork copies, cost, isolation, interface (the fork)
  4-analysis/               slides 33-42: how many independent observations N forks give (the count)
  5-evaluation/             slides 43-47: two pre-registered tests, threats to validity, the redesigned run
  6-conclusion/             slides 48-50: limitations, future work, conclusions
  7-endmatter/              untimed: detail pages, research record, references
    index.tex               the order of the slides in the section, and the section number
    NN-name.tex             one slide: one frame, with its speaker note as the last item
tools/                      presenter_guide.py, slide_index.py, texflat.py
```

To edit a slide, open its file in `acts/` and change the text. To move a slide, move its `\input` line in the section's `index.tex`. To add a slide, create a file and add an `\input` line. File names carry the position within the section, so rename them after a reorder if the order should show in a directory listing. `python3 tools/slide_index.py` prints the global slide numbers, files, titles and planned times. Cross-references written in the text as "slide N" must be updated by hand after a move.

## Build

- `make deck` builds `talk.pdf` and regenerates the presenter guide. It fails if any slide's notes exceed 125 wpm.
- `make dist` copies the deck to `dist/forkable-sandboxes-cambridge.pdf`.
- CI checks the page count and pacing, and that `PRESENTER-GUIDE.md` is current.

## Historical material

`archive/` holds the research notebooks, earlier outlines and an earlier 30-minute cut (`talk-30min/`, `academic/`, `swarm/`, `scratch/` and the older notes files). None of it is built or published. Their claims and numbering differ from the canonical deck, and they are not part of it.
