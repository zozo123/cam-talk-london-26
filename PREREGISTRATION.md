# Pre-registration: fork cost and sibling coupling in an AI software factory

Written before any run. **The timestamp is the public push of tag `prereg-v1`** to github.com/zozo123/cam-talk-london-26. Any later change is a separate commit, with its reason, and a new tag.

Slides 27–28 of `talk.tex` present this protocol. Results, each prediction marked held or failed, go in `RESULTS.md` in this repository. If the runs finish before 15 Oct 2026, the talk shows them.

## Question

Does restoring sibling work cells from one snapshot:

1. reduce the time to a ready, tested cell compared with a warm cached template (H1), and
2. couple their test outcomes more than cells that merely run at the same time (H2)?

Also: does forking the factory's repair loop produce correlated edits?

## Workload

- Repository: `zozo123/ariflow-swfactory` at public commit `c07bc4a`, the parent of repair 1's delivered commit `2b1aa7c` on PR #2351.
  - `b77afa9` is the in-cell SHA that `workgraph-execution.json` records as `repairs[0].input_head`, and it is not recoverable.
  - The two are treated as equivalent because of the delivered commit order, not because a tree-hash comparison was made.
  - Before running, push a tag (`prereg/selfhost-2-pre-repair`) at `c07bc4a`.
- Test: `tests/test_dispatch_strand.py::test_two_replicas_pumping_the_same_outbox_dispatch_once`. It is a four-thread race. It failed in SELFHOST-2 ("0 runs from 4 replicas").
- Dependencies: `uv sync --group dev` against the committed `uv.lock`. One recorded base image digest.
- Record the platform CLI version and server region for every run.

## Gate 0: snapshot semantics (before anything else)

Find out whether an islo named snapshot includes guest memory and running processes.

**Probe:**
1. A process keeps a random 128-bit nonce in RAM.
2. Take a named snapshot.
3. Restore 3 children.
4. Record whether the process is running in each child and still holds the same nonce.

**If the nonce does not survive:**
- every report says **restore fan-out**, not fork;
- the memory-uniqueness probes are reported as not applicable.

The code suggests the snapshot is a disk archive (`.tar.zst` via bear-agent), but that is not a result.

## Fidelity gate

Before any child counts in Phase A or B, run the deterministic part of the suite twice: once directly on the parent, and once in a restored child. The outputs must be identical. A mismatch voids that arm until it is explained.

## Pilot (at most 2 hours)

Run 3 cells × 50 executions of the race test and estimate its failure rate p.
- Phase B sets runs per cell to ⌈10 / p⌉, so each cell expects at least 10 failures.
- If p < 1%, pin cells to 1 vCPU and pilot again.
- If it is still under 1%, the outcome becomes "any failure in the full suite".

## Phase A: cost, H1 (no model calls)

**Question:** does restoring a reached state beat a warm, cached template?

**Arms:**
- **Cached template:** dependencies baked in; source fetched at the pinned commit.
- **Restore:** a named snapshot taken after clone, `uv sync` and one warm test run.
- **Cold** (no cache): a reference only. H1 is not tested against it.

**Design:**
- N ∈ {3, 6, 12} concurrent cells.
- 20 repetitions per (arm, N), interleaved in random order, with the seed recorded.

**Measure:** time from the request to the first test result, using server-side timestamps where exposed and client-side ones otherwise (labelled as such). Also record capture time H and the uniqueness probe (`boot_id`, `machine-id`, IP/MAC, guest-minus-host clock, a userspace random value).

**Analysis:** gain = cached median − restore median, at each N, with a 95% bootstrap CI over repetitions.

**Decision:**
- **Supports H1** if the lower CI bound is above 10 s at every N.
- **Rejects H1** if the upper CI bound is below 10 s at any N.
- Anything else is inconclusive.

## Phase B: coupling, H2 (no model calls)

**Question:** do siblings restored from one snapshot fail together more than strangers that ran at the same time?

**Design:**
- 12 snapshot families, each built independently from the same commit.
- Each family has 3 restored siblings, paired with 3 cold "strangers" started in the same slot on the same host.
- The three cells of a triple run the race test in lockstep rounds (round k starts in all three at once), for ⌈10 / p⌉ rounds.
- Record the binary outcome and the failure class.

**Statistic:**
- For a triple, ρ is the mean pairwise phi (Pearson) correlation of its three cells' binary outcome sequences over rounds. This is the ρ of the variance-floor formula on slide 22.
- For pair i, Δρ_i = ρ(siblings) − ρ(strangers).
- Δρ is the mean over the 12 pairs.
- Because host and timing are matched within a pair, Δρ isolates shared ancestry.

**Test:** a sign-flip permutation test over the 12 pairs (all 4,096 sign patterns), plus a 90% bootstrap CI for Δρ.

**Decision:**
- **Supports H2** if p < 0.05 and Δρ > 0.05.
- **Rejects H2** if the 90% CI lies within ±0.05, which is equivalence with no coupling.
- Anything else is **inconclusive**.

**Why 0.05:** at N = 9 siblings, ρ = 0.05 gives N_eff = 9 / 1.4 ≈ 6.4.

## Phase C: the repair loop (model calls, about $26; descriptive)

Re-sample repair 1 of SELFHOST-2 nine times from its recorded input, on the pre-repair state. Keep the same prompt, the same tool policy (no shell) and the same model endpoint.

**Outcome per sample:** did it edit `src/swfactory/backend/service.py`, which is outside the plan? Also record the diff digest.

**Analysis:** the count k of 9, and the number of distinct diffs. Phase C is descriptive only:
- the hosted model's sampling is not part of any guest snapshot, so a within-family vs across-family contrast would be empty by design;
- a real contrast needs a second model or a paraphrased prompt, and is future work.

## Predictions

- **H1 (Phase A):** restore beats the cached template by more than 10 s at every N ∈ {3, 6, 12}.
- **H2 (Phase B):** siblings fail together more than co-scheduled strangers: Δρ > 0.05 with permutation p < 0.05.
- **Loop (Phase C, descriptive):** at least 5 of 9 samples repeat the out-of-plan edit.

## What rejects the thesis on this workload

- **H1:** the upper CI bound of the gain is below 10 s at some N. The warm cache is the better mechanism here.
- **H2:** the 90% CI of Δρ lies within ±0.05. Shared ancestry did not couple test outcomes.

Every result is reported, including inconclusive ones and failures to finish within budget. Excluded runs are listed with reasons: a failed restore is excluded from timing but counted as a failure.

## Scope

- Phases A and B measure correlation induced by the environment.
- Phase C describes how repeatable one model's behaviour is. It does not estimate a correlation.
- If Gate 0 shows the snapshot is disk-only, every result is about restore fan-out, not fork.
- None of the phases compares vendors.
- The cold arm is labelled "no cache". It is not presented as the build-system baseline; the cached template is.
