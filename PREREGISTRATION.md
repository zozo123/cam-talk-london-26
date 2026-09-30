# Pre-registration: fork cost and sibling coupling in an AI software factory

Written before any run. **The timestamp is the public push of tag `prereg-v1`** to github.com/zozo123/cam-talk-london-26. Any later change is a separate commit, with its reason, and a new tag.

Slides 29–30 of `talk.tex` present this protocol. Results, each prediction marked held or failed, go in `RESULTS.md` in this repository. If the runs finish before 15 Oct 2026, the talk shows them.

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

Run 3 restored cells × 50 executions of the race test and estimate its failure rate p.
- If p is below 0.01 or above 0.99, pin cells to 1 vCPU and pilot again.
- If it is still outside [0.01, 0.99], Phase B uses another flaky test from the same suite whose piloted p is inside that range. It is chosen and named from pilot data alone, before any Phase B run.
- Phase B then runs T = max(300, ⌈10 / min(p, 1 − p)⌉) rounds per cell. That gives each cell at least 10 of the rarer outcome, and a per-triple standard error of ρ of about 0.014 or less.

## Phase A: cost, H1 (no model calls)

**Question:** does restoring a reached state beat a warm, cached template?

**Arms:**
- **Cached template:** dependencies baked in; source fetched at the pinned commit.
- **Restore:** a named snapshot taken after clone, `uv sync` and one warm test run.
- **Cold** (no cache): a reference only. H1 is not tested against it.

**Design:**
- N ∈ {3, 6, 12} concurrent cells.
- 20 repetitions per (arm, N), interleaved in random order, with the seed recorded.

**Outcome per repetition:** makespan, the time from the batch request until the last of the N cells reports its first test result.
- Both arms at a given N use the same clock source: server-side timestamps where exposed for both, otherwise client-side for both, labelled as such.
- Also record capture time H and the uniqueness probe (`boot_id`, `machine-id`, IP/MAC, guest-minus-host clock, a userspace random value).

**Analysis:**
- gain_N = median makespan (cached) − median makespan (restore), over the 20 repetitions of each arm.
- CI: 10,000 bootstrap resamples of repetitions drawn separately within each arm, percentile method, seed recorded.
- Secondary (not a decision input): the amortised gain, gain_N − H/N.

**Decision:**
- **Supports H1** if the lower bound of the 95% CI is above 10 s at every N.
- **Rejects H1** if the upper bound of a 98.3% CI (Bonferroni over the three N) is below 10 s at any N.
- Anything else is inconclusive.
- Why 10 s: a round number fixed before any data, not derived from it.

## Phase B: coupling, H2 (no model calls)

**Question:** do siblings restored from one snapshot fail together more than strangers that ran at the same time?

**Design:**
- 12 snapshot families, each built independently from the same commit.
- Each family has 3 restored siblings.
- Its 3 strangers are restores from other families' snapshots: pair i uses families i+1, i+2 and i+3 (mod 12). They start in the same slot on the same host.
- Both arms are therefore restored. Only shared ancestry differs.
- The three cells of a triple run the race test in lockstep rounds (round k starts in all three at once), for T rounds (see Pilot).
- Record the binary outcome and the failure class.

**Statistic:**
- For a triple, ρ = mean over cell pairs (j, j′) and rounds k of (Y_jk − p̄)(Y_j′k − p̄) / (p̄(1 − p̄)).
  - p̄ is the pooled failure rate of that arm (siblings or strangers), not each cell's own mean.
  - This is the intraclass correlation of outcomes. It is the ρ of the variance-floor formula on slide 22.
  - It captures both co-failure within a round and a shared shift in failure rate.
  - It stays defined when one cell's sequence is constant.
- For pair i, Δρ_i = ρ(siblings) − ρ(strangers).
- Δρ is the mean over the 12 pairs.
- Because host and timing are matched within a pair, Δρ isolates shared ancestry.

**Test:**
- One-sided sign-flip permutation test: p = #{s ∈ {±1}^12 : mean(s_i Δρ_i) ≥ observed Δρ} / 4,096, counting the identity pattern. The smallest attainable p is 1/4,096.
- CI: a 90% t-interval over the 12 pair differences, mean ± 1.796 · s / √12.
- A failed restore is replaced by a new restore of the same family and listed. If pairs are lost, the test runs over the n that remain (2^n patterns), and n is reported.

**Decision:**
- **Supports H2** if p < 0.05 and Δρ > 0.05.
- **Rejects H2** if the upper bound of the 90% CI is below 0.05: the data rule out a shared-ancestry excess of 0.05 or more.
- Anything else is **inconclusive**.

**Why 0.05:** an excess correlation of 0.05 from shared ancestry alone takes 9 siblings from 9 to 6.4 witnesses (9 / 1.4). Also report the siblings' absolute ρ with its CI. That value, not Δρ, feeds any N_eff bound.

## Phase C: the repair loop (model calls, about $26; descriptive)

Re-sample repair 1 of SELFHOST-2 nine times from its recorded input, on the pre-repair state. Keep the same prompt, the same tool policy (no shell) and the same model endpoint.

**Outcome per sample:** did it edit `src/swfactory/backend/service.py`, which is outside the plan? Also record the diff digest.

**Analysis:** the count k of 9, and the number of distinct diffs. Phase C is descriptive only:
- the hosted model's sampling is not part of any guest snapshot, so a within-family vs across-family contrast would be empty by design;
- a real contrast needs a second model or a paraphrased prompt, and is future work.

## Predictions

- **H1 (Phase A):** restore beats the cached template by more than 10 s in median makespan at every N ∈ {3, 6, 12}.
- **H2 (Phase B):** siblings fail together more than restored strangers: Δρ > 0.05 with one-sided permutation p < 0.05.
- **Loop (Phase C, descriptive):** at least 5 of 9 samples repeat the out-of-plan edit.

## What rejects the thesis on this workload

- **H1:** the upper bound of the 98.3% CI of the gain is below 10 s at some N. The warm cache is the better mechanism here.
- **H2:** the upper bound of the 90% CI of Δρ is below 0.05. Shared ancestry did not couple test outcomes by that much.

Every result is reported, including inconclusive ones and failures to finish within budget. Excluded runs are listed with reasons: a failed restore is excluded from timing but counted as a failure.

## Scope

- Phases A and B measure correlation induced by the environment.
- Phase C describes how repeatable one model's behaviour is. It does not estimate a correlation.
- If Gate 0 shows the snapshot is disk-only, every result is about restore fan-out, not fork.
- None of the phases compares vendors.
- The cold arm is labelled "no cache". It is not presented as the build-system baseline; the cached template is.
