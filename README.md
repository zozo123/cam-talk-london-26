# Forkable Sandboxes: The Runtime Layer for AI Software Factories

**Yossi Eliaz**: Principal Engineer, Incredibuild; islo.dev; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, 15 October 2026, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- **[Seminar PDF](dist/forkable-sandboxes-cambridge-40.pdf)** (27 main slides + backups; the file name is kept for old links)
- **[LaTeX source with speaker notes](talk.tex)**
- **[Presenter guide, generated from the notes](PRESENTER-GUIDE.md)**
- **[Claim boundaries and provenance](CLAIM-FENCE.md)**
- **[Pre-registered experiment](PREREGISTRATION.md)**

## Advertised abstract

> As coding agents move from autocomplete to autonomous software engineering, they need an execution substrate designed for non-human developers. This talk will explore the systems challenges behind forkable, isolated environments, including filesystem state, networking and credentials, reproducibility, fast cloning, build/test execution, recovery, and observability. The focus will be on the underlying architecture, trade-offs, and open systems problems.

## The argument

On 27 September 2026, the speaker's open-source software factory ([zozo123/ariflow-swfactory](https://github.com/zozo123/ariflow-swfactory)) ran a work order on its own code:
- A repair agent without a shell rewrote code outside the plan.
- The first review blocked it. After one more repair, the second review approved it.
- The same model wrote the fix and ran both reviews.
- Nothing escaped the sandbox, and the run still could not tell the truth about what happened.

The talk walks the seven advertised surfaces in the order they failed in that run. It then places fork in its Xen-era lineage (SnowFlock, Potemkin, Remus, Firecracker, the 2026 agent-checkpoint papers).

It ends on the contribution: sibling results are correlated evidence. The statistics for correlated evidence exist; what is missing is that the runtime never hands the reducer the cluster labels. Fork lineage and evidence identities are those labels.

*Fork the machine, not the trust. Count evidence, not executions.*

## Structure

| Slides | Act | Time |
|---|---|---|
| 1–4 | The hook: one real run; what I claim and don't | 5:00 |
| 5–11 | The wall: networking, build/test, credentials, recovery, observability, reproducibility, fast cloning | 11:40 |
| 12–17 | The fork: lineage, clone hazards, held effects, where fork loses, isolation, architecture | 10:20 |
| 18–23 | The count: execution multiplicity vs evidence multiplicity, the receipt contract | 8:30 |
| 24–27 | Test and agenda: the pre-registered test, the redesigned run, open problems | 6:15 |

That is 41:45 of planned speaking, leaving about 15 minutes for questions.

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
