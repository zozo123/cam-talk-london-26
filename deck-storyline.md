# Story and slide map for the Cambridge seminar

The main deck has **50 slides / 37:10 planned narration**, with no appendix or overlays. [DECK-REVIEW.md](DECK-REVIEW.md) preserves the original 57-slide numbering and explains each editorial decision. The source indexes and timed notes determine the final order.

The story proceeds from personal motivation and executable alternatives to concrete examples, then **run → evidence → acceptance**. Useful state enables trials; identified external checks support an exact result; controller-held authority determines what may continue or be published.

## Six acts

| Act | Slides | Question |
|---|---|---|
| Motivation | 1–15 | Why this problem, what state, and which execution abstraction? |
| Examples | 16–31 | What do reuse, evaluated search and separate acceptance look like? |
| Runtime | 32–39 | How are state, resource cost, external effects and authority bounded? |
| Evidence | 40–46 | What justifies selection, composition and measurement pooling? |
| Acceptance | 47–49 | Which executed checks and decision rules authorize a result? |
| Conclusion | 50 | What contract must every useful continuation satisfy? |

## Canonical slide map

| # | Full sentence title | Cue | Source comments |
|---|---|---|---|
| 1 | Forkable sandboxes let computers explore executable alternatives. | 0:25 | [Source](acts/1-introduction/01-title.tex) |
| 2 | My work connects self-organizing matter to systems that choose their next action. | 0:45 | [Source](acts/1-introduction/02-research-path.tex) |
| 3 | Twistlock learned container behavior and enforced the resulting model. | 0:30 | [Source](acts/1-introduction/02-container-security.tex) |
| 4 | Graph measures link protein binding to actomyosin self-organization. | 0:50 | [Source](acts/1-introduction/03-physics-origin.tex) |
| 5 | POSSUMM computed 500-bp chromosome compartments with 23 GB of RAM. | 0:40 | [Source](acts/1-introduction/04-genome-algorithms.tex) |
| 6 | ENCODE linked reproducible execution to identifiable outputs. | 0:45 | [Source](acts/1-introduction/05-encode-pipelines.tex) |
| 7 | CRISPR-IL fed measured outcomes into the next design round. | 0:45 | [Source](acts/1-introduction/05-crispr-design.tex) |
| 8 | A drug combination preserved cell killing while reducing PD-L1 induction. | 0:45 | [Source](acts/1-introduction/05-immune-response.tex) |
| 9 | A self-driving computer closes a feedback loop around its own actions. | 0:35 | [Source](acts/1-introduction/06-self-driving-systems.tex) |
| 10 | Forkable computation lets us try different futures from the same state. | 0:50 | [Source](acts/1-introduction/02-executable-search.tex) |
| 11 | The forkable API prepares once and runs alternatives in private children. | 0:40 | [Source](acts/1-introduction/02-control-comparison.tex) |
| 12 | Reusing build artifacts reduced a reported Tokio compile from 46 to 13 seconds. | 0:45 | [Source](acts/1-introduction/07-build-reuse.tex) |
| 13 | An agent changes the environment that executes its next experiment. | 0:40 | [Source](acts/1-introduction/08-agent-execution.tex) |
| 14 | A sandbox is a policy boundary; VMs and containers are implementation choices. | 0:40 | [Source](acts/1-introduction/08-runtime-layers.tex) |
| 15 | A fork creates private continuations from one captured execution state. | 0:30 | [Source](acts/1-introduction/10-fork-definition.tex) |
| 16 | AFL++ tests mutated inputs for bugs while reusing initialized state. | 0:45 | [Source](acts/2-case-study/01-fuzzing-state.tex) |
| 17 | AFL++ reports 10–20 times faster execution in persistent mode. | 0:30 | [Source](acts/2-case-study/02-fuzzing-speed.tex) |
| 18 | 250 samples raised SWE-bench Lite coverage from 15.9% to 56%. | 0:45 | [Source](acts/2-case-study/03-sampling-coverage.tex) |
| 19 | Autoresearch kept 23 experiments and lowered validation bits per byte. | 1:00 | [Source](acts/2-case-study/04-autoresearch.tex) |
| 20 | AlphaEvolve recovered 0.7% of Google's worldwide compute. | 0:50 | [Source](acts/2-case-study/05-alphaevolve.tex) |
| 21 | A genome-scale screen ranked candidates for sensitivity to SI-12. | 0:40 | [Source](acts/2-case-study/06-genomics-screen.tex) |
| 22 | Six of eight combinations improved killing in MCF-7 cells. | 0:45 | [Source](acts/2-case-study/07-genomics-assay.tex) |
| 23 | We tested whether projected three-body orbit branches connect. | 0:45 | [Source](acts/2-case-study/08-three-body-question.tex) |
| 24 | All 26 selected links connected by bidirectional continuation. | 0:45 | [Source](acts/2-case-study/09-three-body-verification.tex) |
| 25 | The installer fix added two missing hosts across a six-file plan. | 0:50 | [Source](acts/2-case-study/10-installer-task.tex) |
| 26 | The factory run took 43:44 and cost $10.33 in model calls. | 0:45 | [Source](acts/2-case-study/11-workflow-time.tex) |
| 27 | Two repairs and two reviews used 59% of time and 75% of cost. | 0:45 | [Source](acts/2-case-study/12-review-cost.tex) |
| 28 | The repair agent diagnosed a split between cell and dispatch ownership. | 0:45 | [Source](acts/2-case-study/13-dispatch-race.tex) |
| 29 | The green suite left same-owner adoption without a direct test. | 0:45 | [Source](acts/2-case-study/14-adoption-obligation.tex) |
| 30 | Three delivery refusals preceded cleanup that erased an approved patch. | 0:45 | [Source](acts/2-case-study/15-durable-delivery.tex) |
| 31 | CyberGym validated 22 zero-days after a 56-crash campaign. | 0:50 | [Source](acts/2-case-study/16-security-discovery.tex) |
| 32 | Forkable execution separates running, evidence collection and acceptance. | 0:45 | [Source](acts/3-design/00-three-jobs.tex) |
| 33 | The next action determines which state a continuation needs. | 0:45 | [Source](acts/3-design/01-state-choice.tex) |
| 34 | A sandbox create batch completed 256 calls at a 3.44 s median. | 0:45 | [Source](acts/3-design/04-create-trace.tex) |
| 35 | Reuse saves resources when avoided preparation exceeds its overhead. | 0:45 | [Source](acts/3-design/05-resource-rule.tex) |
| 36 | A warm cache reverses the same fork's resource advantage. | 0:45 | [Source](acts/3-design/06-warm-alternative.tex) |
| 37 | Restoring a guest cannot undo a completed remote model request. | 0:45 | [Source](acts/3-design/07-external-effects.tex) |
| 38 | The controller holds the credential that publishes a child's candidate. | 0:45 | [Source](acts/3-design/08-controller-authority.tex) |
| 39 | The controller rejects an old epoch after replacing a worker. | 0:45 | [Source](acts/3-design/10-restore-epochs.tex) |
| 40 | Evidence must identify what ran and what the runs shared. | 0:30 | [Source](acts/4-analysis/00-evidence-boundary.tex) |
| 41 | Selecting, composing, and pooling results require different checks. | 0:45 | [Source](acts/4-analysis/01-result-decisions.tex) |
| 42 | Passing every pair does not establish that all three patches pass. | 0:45 | [Source](acts/4-analysis/02-exact-composition.tex) |
| 43 | The reducer rejects a repeated evidence ID and retains distinct evidence. | 0:45 | [Source](acts/4-analysis/06-reducer-identity.tex) |
| 44 | A forged precision report moved the synthetic pooled estimate from 5 to 17. | 0:45 | [Source](acts/4-analysis/08-precision-stress.tex) |
| 45 | At correlation 0.1, 100 measurements have the mean precision of about nine. | 0:35 | [Source](acts/4-analysis/09-mean-precision.tex) |
| 46 | Success after reaching a checkpoint does not measure success from task start. | 0:45 | [Source](acts/4-analysis/12-checkpoint-population.tex) |
| 47 | A receipt must describe the operation that actually executed. | 0:55 | [Source](acts/5-evaluation/01-receipt-semantics.tex) |
| 48 | Publication must follow a passing check of the exact artifact. | 0:55 | [Source](acts/5-evaluation/02-publication-obligation.tex) |
| 49 | Two preregistered tests can reject the proposed reuse and dependence claims. | 1:15 | [Source](acts/5-evaluation/03-two-tests.tex) |
| 50 | A useful continuation returns its artifact, evidence, and authority context. | 1:00 | [Source](acts/6-conclusion/01-final-contract.tex) |

## Material retained for Q&A

RAM-only nonce/fidelity probe; operation-specific published latencies; repeated cases and Bitcoin source identity; full information-sharing graph; honest pooling check; higher-order cofailure and paired comparisons; overlapping-family analysis; nine-repair repeatability plan. These remain in source files and in relevant main-frame Q&A comments, without expanding the spoken PDF.

## Component status

The serial factory digest gate, recorded creation/API workflows and numerical reducer are exercised components. The private-continuation API, external artifact checker, dependence-aware abstention and generation-fenced acceptance are integration design requirements. The combined experiments are not yet run. The original PREREGISTRATION.md is unchanged.
