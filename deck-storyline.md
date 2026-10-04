# Story and slide map for the Cambridge seminar

The main deck has **54 slides / 39:05 planned narration**, with no appendix or overlays. [DECK-REVIEW.md](DECK-REVIEW.md) reviews all original slides 1–57 and maps every later screenshot/comment to its final destination. The source indexes and timed notes determine the order.

The story follows **reuse useful state → fan out changed trials → gather new information → select, compose or pool → check the exact result → continue**. Physical self-organization, laboratory assays and numerical search illustrate related patterns; their mechanisms remain distinct. Cheap execution creates opportunities. The return path makes them useful.

## Six acts

| Act | Slides | Question |
|---|---|---|
| Motivation | 1–15 | Why this problem, what state, and which execution abstraction? |
| Examples | 16–32 | How do changed trials, reuse and checks lead to useful discoveries? |
| Runtime | 33–41 | How do we run, preserve and price private continuations? |
| Evidence | 42–50 | How do we combine new information without counting shared errors twice? |
| Acceptance | 51–53 | Which checks and merge rules authorize the exact output? |
| Conclusion | 54 | What makes the full feedback loop useful? |

## Canonical slide map

| # | Full sentence title | Cue | Source comments |
|---|---|---|---|
| 1 | Forkable sandboxes let computers explore executable alternatives. | 0:25 | [Source](acts/1-introduction/01-title.tex) |
| 2 | My work led from securing software and modeling cells to self-driving compute. | 0:45 | [Source](acts/1-introduction/02-research-path.tex) |
| 3 | Twistlock learned container behavior and enforced the resulting model. | 0:30 | [Source](acts/1-introduction/02-container-security.tex) |
| 4 | Graph measures link protein binding to actomyosin self-organization. | 0:50 | [Source](acts/1-introduction/03-physics-origin.tex) |
| 5 | POSSUMM computed 500-bp chromosome compartments with 23 GB of RAM. | 0:40 | [Source](acts/1-introduction/04-genome-algorithms.tex) |
| 6 | ENCODE linked reproducible execution to identifiable outputs. | 0:45 | [Source](acts/1-introduction/05-encode-pipelines.tex) |
| 7 | CRISPR-IL fed measured outcomes into the next design round. | 0:45 | [Source](acts/1-introduction/05-crispr-design.tex) |
| 8 | Ten drugs led to a pair with lower PD-L1. | 0:45 | [Source](acts/1-introduction/05-immune-response.tex) |
| 9 | Millions of cars build Mobileye's Roadbook. | 0:35 | [Source](acts/1-introduction/06-self-driving-systems.tex) |
| 10 | Forkable computation lets us try different futures from the same state. | 0:50 | [Source](acts/1-introduction/02-executable-search.tex) |
| 11 | The forkable API prepares once and runs alternatives in private children. | 0:40 | [Source](acts/1-introduction/02-control-comparison.tex) |
| 12 | Caching lets repeated experiments reuse their expensive build work. | 0:45 | [Source](acts/1-introduction/07-build-reuse.tex) |
| 13 | An agent changes the environment that executes its next experiment. | 0:40 | [Source](acts/1-introduction/08-agent-execution.tex) |
| 14 | A sandbox is a policy boundary; VMs and containers are implementation choices. | 0:40 | [Source](acts/1-introduction/08-runtime-layers.tex) |
| 15 | A fork creates private continuations from one captured execution state. | 0:30 | [Source](acts/1-introduction/10-fork-definition.tex) |
| 16 | Different fields use the same pattern: explore alternatives, then check the results. | 0:40 | [Source](acts/2-case-study/00-examples-overview.tex) |
| 17 | AFL++ finds bugs by changing inputs and reusing the initialized program. | 0:45 | [Source](acts/2-case-study/01-fuzzing-state.tex) |
| 18 | AFL++ reports 10–20 times faster execution in persistent mode. | 0:30 | [Source](acts/2-case-study/02-fuzzing-speed.tex) |
| 19 | 250 samples raised SWE-bench Lite coverage from 15.9% to 56%. | 0:45 | [Source](acts/2-case-study/03-sampling-coverage.tex) |
| 20 | Autoresearch kept 23 experiments and lowered validation bits per byte. | 1:00 | [Source](acts/2-case-study/04-autoresearch.tex) |
| 21 | AlphaEvolve recovered 0.7% of Google's worldwide compute. | 0:50 | [Source](acts/2-case-study/05-alphaevolve.tex) |
| 22 | A pooled gene-editing screen tested 19,050 genes to find drug partners. | 0:45 | [Source](acts/2-case-study/06-genomics-screen.tex) |
| 23 | Six of eight drug combinations improved killing of breast cancer cells. | 0:45 | [Source](acts/2-case-study/07-genomics-assay.tex) |
| 24 | We tested whether apparently separate orbit families actually connect. | 0:45 | [Source](acts/2-case-study/08-three-body-question.tex) |
| 25 | All 26 selected connections survived checks in both directions. | 0:45 | [Source](acts/2-case-study/09-three-body-verification.tex) |
| 26 | The installer failed because its download destinations were blocked. | 0:45 | [Source](acts/2-case-study/10-installer-task.tex) |
| 27 | Installing uv led to a 44-minute repair loop costing $10.33. | 0:40 | [Source](acts/2-case-study/11-workflow-time.tex) |
| 28 | Repairs and reviews consumed most of the recorded time and model cost. | 0:40 | [Source](acts/2-case-study/12-review-cost.tex) |
| 29 | One worker owned the workspace; another had permission to run. | 0:40 | [Source](acts/2-case-study/13-dispatch-race.tex) |
| 30 | The suite had zero failures, but the new recovery path still needed a test. | 0:40 | [Source](acts/2-case-study/14-adoption-obligation.tex) |
| 31 | Cleanup erased an approved patch before it was safely exported. | 0:45 | [Source](acts/2-case-study/15-durable-delivery.tex) |
| 32 | CyberGym validated 22 zero-days after a 56-crash campaign. | 0:50 | [Source](acts/2-case-study/16-security-discovery.tex) |
| 33 | A forkable runtime must preserve state, gather evidence and control acceptance. | 0:40 | [Source](acts/3-design/00-three-jobs.tex) |
| 34 | The next action determines which state a continuation needs. | 0:45 | [Source](acts/3-design/01-state-choice.tex) |
| 35 | Our paper recorded 256 sandbox creates with a 3.44-second median. | 0:40 | [Source](acts/3-design/04-create-trace.tex) |
| 36 | Isorun led the October 2 sandbox startup benchmark at a 73 ms median. | 0:45 | [Source](acts/3-design/04-current-startup.tex) |
| 37 | Reusing state pays off when it avoids more setup than it adds. | 0:45 | [Source](acts/3-design/05-resource-rule.tex) |
| 38 | Restoring wins against cold setup but loses against this warm cache. | 0:45 | [Source](acts/3-design/06-warm-alternative.tex) |
| 39 | Restoring a sandbox does not undo an API call or its bill. | 0:40 | [Source](acts/3-design/07-external-effects.tex) |
| 40 | Workers propose patches; the controller holds the key to publish them. | 0:40 | [Source](acts/3-design/08-controller-authority.tex) |
| 41 | Once a worker is replaced, it can no longer publish results. | 0:40 | [Source](acts/3-design/10-restore-epochs.tex) |
| 42 | Combining branch results should add information while accounting for overlap. | 0:40 | [Source](acts/4-analysis/00-evidence-boundary.tex) |
| 43 | Choosing a result, merging code and pooling measurements are different operations. | 0:45 | [Source](acts/4-analysis/01-result-decisions.tex) |
| 44 | Code changes that pass in pairs can fail when all three are merged. | 0:45 | [Source](acts/4-analysis/02-exact-composition.tex) |
| 45 | Set union keeps shared observations once; mutual information describes dependence. | 0:45 | [Source](acts/4-analysis/03-information-overlap.tex) |
| 46 | Our reducer catches duplicate observation IDs and keeps their source history. | 0:45 | [Source](acts/4-analysis/06-reducer-identity.tex) |
| 47 | For estimates of one quantity, covariance guides the pooling weights. | 0:50 | [Source](acts/4-analysis/07-covariance-pooling.tex) |
| 48 | A worker that exaggerates its precision can dominate a weighted average. | 0:50 | [Source](acts/4-analysis/08-precision-stress.tex) |
| 49 | With shared errors, 100 estimates can reduce noise like about nine independent ones. | 0:50 | [Source](acts/4-analysis/09-mean-precision.tex) |
| 50 | If 50 of 100 tasks reach a checkpoint and 40 finish, overall success is 40%. | 0:45 | [Source](acts/4-analysis/12-checkpoint-population.tex) |
| 51 | A check record must say what ran, who ran it and which files it checked. | 0:45 | [Source](acts/5-evaluation/01-receipt-semantics.tex) |
| 52 | The code we publish must be the same code that passed the required check. | 0:45 | [Source](acts/5-evaluation/02-publication-obligation.tex) |
| 53 | Each use case needs a merge rule and a check matched to its output. | 0:55 | [Source](acts/5-evaluation/03-two-tests.tex) |
| 54 | Self-driving compute tries alternatives, combines what they teach us and continues. | 0:50 | [Source](acts/6-conclusion/01-final-contract.tex) |

## Material retained for Q&A

RAM-only nonce/fidelity probe; operation-specific published latencies; repeated cases and Bitcoin source identity; higher-order cofailure and paired comparisons; full protocol rejection thresholds, overlapping-family analysis and nine-repair repeatability plan. These remain in source files and relevant main-frame Q&A, without adding appendix pages.

## Component status

The serial factory code-hash gate, recorded creation/API workflows and numerical reducer are exercised components. Full covariance pooling, dependence-aware refusal, the private-continuation API, integrated external artifact checking and generation-fenced acceptance are design requirements. The planned experiments have not started. PREREGISTRATION.md is unchanged.
