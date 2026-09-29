# Forkable Sandboxes: The Runtime Layer for AI Software Factories

**Yossi Eliaz**: Principal Engineer, Incredibuild; islo.dev; Associate Professor, Holon Institute of Technology (HIT).

Cambridge Computer Laboratory Systems Research Group seminar, 15 October 2026, 15:00–16:00 BST, FW11 + Microsoft Teams. [Event listing](https://www.talks.cam.ac.uk/talk/index/273181).

- **[Seminar PDF](dist/forkable-sandboxes-cambridge-40.pdf)** (28 main slides + backups; the file name is kept for old links)
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
- Every agent told the truth. The gate still approved an untested change.

The talk walks the seven advertised surfaces roughly in the order they bit across that day's runs. It then places fork in its Xen-era lineage (SnowFlock, Potemkin, Remus, Firecracker, the 2026 agent-checkpoint papers).

It ends on the contribution: sibling results are correlated evidence. The statistics for correlated evidence exist, and they need cluster labels. The runtime holds some of those labels (shared parent, seed, test, fixture) and today throws them away. A worker/reducer contract hands them over. Turning them into a dependence model is still open.

*Fork the machine, not the trust. Count evidence, not executions.*

## Structure

| Slides | Act | Time |
|---|---|---|
| 1–4 | The hook: one real run; what I claim and don't | 5:15 |
| 5–12 | The wall: networking, filesystem state, build/test, credentials, recovery, observability, reproducibility, fast cloning | 10:40 |
| 13–18 | The fork: lineage, clone hazards, held effects, where fork loses, isolation, architecture | 9:05 |
| 19–24 | The count: adaptivity, execution vs evidence multiplicity, cluster labels, the receipt contract | 7:50 |
| 25–28 | Test and agenda: the pre-registered test, the redesigned run, open problems | 4:55 |

The cues are derived from the script at about 105 wpm plus reading pauses: 37:45 in total. That leaves room for interruptions and about 20 minutes of questions. Replace them with stopwatch times after rehearsal.

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
