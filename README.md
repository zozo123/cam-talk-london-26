# Forkable Sandboxes: The Runtime Layer for AI Software Factories

**Yossi Eliaz**: Principal Engineer, Incredibuild; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, 15 October 2026, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- **[Seminar PDF](dist/forkable-sandboxes-cambridge.pdf)** (57 story slides, then end matter: decision rules, research record, references)
- **[LaTeX source](talk.tex)**: the root file. Each slide is one file in [acts/](acts/), and its speaker note is inside it.
- **[Presenter guide, generated from the notes](PRESENTER-GUIDE.md)**
- **[Claim boundaries and provenance](CLAIM-FENCE.md)**
- **[Pre-registered experiment](PREREGISTRATION.md)**

## Advertised abstract

> As coding agents move from autocomplete to autonomous software engineering, they need an execution substrate designed for non-human developers. This talk will explore the systems challenges behind forkable, isolated environments, including filesystem state, networking and credentials, reproducibility, fast cloning, build/test execution, recovery, and observability. The focus will be on the underlying architecture, trade-offs, and open systems problems.

## Research question

What counts as new evidence when an agent loop repeats work? A loop can generate a patch, run tests, repair it and review it several times. The talk asks which of those events adds evidence about the behaviour being changed, and what a forking runtime must record so that the answer can be computed.

**Story.** A small work order exposed failures in scope, validation, reporting and recovery. Forking reuses the state in which those failures arise. The runtime must preserve what each execution actually established. We have implemented part of that contract. The remaining claims require experiments.

**Thesis.** Repeated executions are not repeated evidence. Under a common correlation $\rho$, $N$ measurements of one candidate have the precision of $N_{\rm eff} = N/(1+(N-1)\rho)$, and shared bias remains. Choosing among candidates is a different question from pooling measurements of one candidate.

**Contributions.** (1) Two recorded work orders of a self-evolving loop, with the incident at the centre of the talk: a branch that combined `CellBusy` with same-owner adoption shipped without a direct deterministic test, after a green suite and two reviews. (2) A built reducer that rejects reused evidence IDs and carries lineage with each result. (3) A runtime contract for branches, of which parts are built and parts are proposed. (4) Two pre-registered experiments, unrun: restore against a warm cached template, and environmental co-failure of siblings.

**Not claimed.** A failure frequency, a fork speedup, a fork-induced correlation, a ranking of platforms, a loop that forks today, or physics and biology as evidence about forks.

## Structure

| Section | Slides | Content | Time |
|---|---|---|---|
| 1 Introduction | 1–6 | A backup request cut tail latency 24 times, more attempts found more solutions, the question across six fields, intelligence as choice, what this talk establishes | 4:30 |
| 2 Case study | 7–20 | The first work order step by step: redirect hosts, the plan, 43 minutes, the split-ownership race, the untested branch, repair scope, visible feedback; then the second work order, misleading receipts, the adapter source, snapshot scope, the computed parallel saving, and seven runtime requirements | 10:00 |
| 3 Design | 21–36 | Publication authority, isolation and authority, SnowFlock's API, related work, published latencies, training-scale forks, conditional success, the snapshot probe, inherited state, the commit path, a cost model, our API timings, the runtime calls, the architecture, the branch contract, promotion invariants | 11:00 |
| 4 Analysis | 37–49 | Selection versus pooling, adaptive feedback, reruns versus test cases, best-of-N coverage, the variance of a correlated average, $N_{\rm eff}$ in numbers, runtime manifests, the evidence graph, paired comparisons, composition failure, the reducer, synthetic checks, inflated precision | 9:30 |
| 5 Evaluation | 50–55 | Test 1 (restore against a warm template), Test 2 (environmental co-failure), families and rounds, repair resampling, the redesigned workflow, a pilot | 4:45 |
| 6 Conclusion | 56–57 | Two open problems, what counts as new evidence | 1:45 |
| End matter | after 57 | Untimed: pre-registered decision rules (1), research record (3), references (3) | — |

Every evidence slide carries a tag: MEASURED (our run records), BUILT (implemented and tested, or a synthetic check), PROPOSED (designed, not run), PUBLISHED (other people's work) or ANALOGY (borrowed vocabulary, never evidence). Illustrations and calculations are labelled as such. The cues total 41:30 at about 100 words per minute, which leaves time for questions in the hour. Replace them with stopwatch times after rehearsal.

The speaker's own papers appear where they are used: the actomyosin papers (slides 4 and 44), the ENCODE pipelines (slides 4 and 17), the Bitcoin and iScience studies (slides 4 and 43), OffRisk (slide 13), the 2021 CRISPR screen (slides 39 and 46), Poolkeh (slide 41) and arXiv:2607.09689 (slides 32, 47, 48 and 49).

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
  1-introduction/           slides 1-6: motivation, the question across fields, what this talk establishes
  2-case-study/             slides 7-20: two work orders and the runtime requirements they expose
  3-design/                 slides 21-36: authority, related work, fork semantics, cost, interface, contract
  4-analysis/               slides 37-49: what repeated executions can establish
  5-evaluation/             slides 50-55: two pre-registered experiments, repair resampling, the redesigned run
  6-conclusion/             slides 56-57: open problems, conclusions
  7-endmatter/              untimed: decision rules, research record, references
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
