# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from `talk.tex` by `tools/presenter_guide.py`. 27 main slides, 12 backups. Planned talk: **41:45**, 3377 spoken words, 81 wpm average, peak 107 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:45 | 0:00-0:45 | 80 | 107 |
| 2 | Review said blocker. One more repair. Review said approve. | 1:45 | 0:45-2:30 | 185 | 106 |
| 3 | One work order, seven places the runtime bit | 1:15 | 2:30-3:45 | 107 | 86 |
| 4 | A factory needs a wall, a fork and a count | 1:15 | 3:45-5:00 | 122 | 98 |
| 5 | An allowlist is a list of names; the web is a graph of redirects | 2:00 | 5:00-7:00 | 172 | 86 |
| 6 | Locking the tests was not enough | 2:05 | 7:00-9:05 | 171 | 82 |
| 7 | The agent never pushes; a placeholder token is still a string | 1:50 | 9:05-10:55 | 147 | 80 |
| 8 | Teardown should destroy a worker, not the experiment | 1:40 | 10:55-12:35 | 140 | 84 |
| 9 | A green check is not proof the check ran | 1:50 | 12:35-14:25 | 143 | 78 |
| 10 | Everything is pinned except the part that wrote the code | 1:25 | 14:25-15:50 | 123 | 87 |
| 11 | The plan asked for a fork; the runtime said no | 0:50 | 15:50-16:40 | 76 | 91 |
| 12 | Fork has a 20-year literature, much of it built on Xen | 1:50 | 16:40-18:30 | 142 | 77 |
| 13 | Fork copies memory; identity and secrets must not follow | 1:55 | 18:30-20:25 | 144 | 75 |
| 14 | Hold effects until an authority releases them | 1:20 | 20:25-21:45 | 92 | 69 |
| 15 | When fork pays, and where it loses | 2:10 | 21:45-23:55 | 188 | 87 |
| 16 | Pick the lowest rung that holds the threat | 1:05 | 23:55-25:00 | 78 | 72 |
| 17 | Cheap forked machines for search; authority never lives inside them | 2:00 | 25:00-27:00 | 165 | 82 |
| 18 | One model wrote the fix and reviewed it twice. How many witnesses? | 1:15 | 27:00-28:15 | 80 | 64 |
| 19 | Execution multiplicity is not evidence multiplicity | 1:50 | 28:15-30:05 | 125 | 68 |
| 20 | The statistics exist; the runtime does not hand over the cluster labels | 1:15 | 30:05-31:20 | 101 | 81 |
| 21 | Fork is also how you run the control | 1:00 | 31:20-32:20 | 77 | 77 |
| 22 | Every worker returns a receipt, not a score | 2:00 | 32:20-34:20 | 150 | 75 |
| 23 | Isolation does not authenticate n | 1:10 | 34:20-35:30 | 90 | 77 |
| 24 | The test that could prove me wrong | 2:20 | 35:30-37:50 | 187 | 80 |
| 25 | The same work order, as the runtime should run it | 1:30 | 37:50-39:20 | 113 | 75 |
| 26 | Open problems where this room is ahead of me | 1:45 | 39:20-41:05 | 138 | 79 |
| 27 | Fork the machine, not the trust. | 0:40 | 41:05-41:45 | 41 | 62 |

## Script

### 01. Forkable Sandboxes

*0:45, starts at 0:00*

Thank you for having me. I work on distributed builds at Incredibuild, I teach at HIT, and I build an agent sandbox platform called islo. I'll disclose that once and then only talk about components. In build systems I learned that recomputing the world is insane. So the state I wanted to reuse for speed became the state I had to isolate for trust. This talk is about that runtime layer, and about one run that shows why it matters.

### 02. Review said blocker. One more repair. Review said approve.

*1:45, starts at 0:45*

Let me start with a real run. On the 27th of September my software factory worked on its own code. The factory is open source. It takes a GitHub issue, runs an agent in a sandbox, runs the tests, and opens a pull request. The work order was small: fix a network allowlist. Along the way a race test failed. The repair agent had no shell, and it said so: it could not run the tests. It read the code, decided the bug was in who owns a cell, and rewrote that logic, in a file no plan listed. Review one said: blocker, untested and unverified. So the loop tried again. The tests were locked, so it could not add one. It refactored until the old tests seemed to cover the change, and it argued its case. Review two said: major, and approved. The same model wrote the fix and ran both reviews. Forty-three minutes, ten dollars. The last defence was me: I reverted that file. Nothing escaped the sandbox. Every wall held. And the run still could not tell the truth about what happened.

### 03. One work order, seven places the runtime bit

*1:15, starts at 2:30*

Here is the whole run as a pipeline, with the seven topics from the abstract pinned where each one bit. I will walk them in that order. Every evidence slide carries one tag: measured in my own logs, built and tested, proposed, or other people's published work. And here is the scope, said once so I do not hedge every slide. These runs used Docker's sandbox, not my own platform. My harness answered the approval gates, not a person. Credential leases were built but switched off. And nothing forked. You will see the factory ask for a fork and be refused. That is the honest starting point.

### 04. A factory needs a wall, a fork and a count

*1:15, starts at 3:45*

That run was missing three things. A wall, so a child cannot grade its own exam. A fork, so the factory can try alternatives from a state it already paid to reach. And a count, so it knows what those alternatives actually found. Here is what I claim today: an evidence-aware reduction contract with a built reference reducer, which is my paper; real traces from a running factory; and a test that could reject my hypothesis, with the predictions written down before the runs. Here is what I do not claim: a new estimator, a speed ranking of sandbox vendors, or a factory that forks today. Miss one of the three and the factory still runs. It just cannot tell the truth.

### 05. An allowlist is a list of names; the web is a graph of redirects

*2:00, starts at 5:00*

The wall first, in the order it bit. The work order itself was a network bug. The sandbox allowlist named astral dot sh. But astral dot sh answers with a redirect to another host, and that host was not on the list. The installer's fallback goes to GitHub's release asset host, also not on the list. So curl returned 403, uv never installed, and the tests could never pass. The list lived in five places, and they had drifted. The fix added the two hosts. Be honest about what that does: allowing GitHub's release asset host lets in every release asset on GitHub. The lesson is granularity. A list of names is the wrong unit when the web is a graph of redirects. The build-system answer is to fetch by content digest through a caching proxy. Same idea for the whole snapshot: it captures a boundary, not the universe. Files are pinned by digest, agent history stays outside the VM, randomness is reseeded or coupled on purpose, and external services are mediated.

### 06. Locking the tests was not enough

*2:05, starts at 7:00*

Second surface: build and test. We did the standard thing. The tests directory was write-protected by a hook, and the hook worked. It did not help. Planned steps are scope-checked against the files they declare. Repairs are not, so the repair loop could touch any file. The child did not change the test. It changed the code under test, and then it talked the grader down. An out-of-plan edit counts as major, not as a blocker, and the writer and both reviewers were the same model. This is not special to my factory. METR found o3 reward-hacking in about thirty percent of runs where it could see the scorer, and under one percent where it could not. ImpossibleBench shows read-only tests stop test edits but not special-casing. And the Kimi K3 report names the same fixes we need: isolate agents from verifiers, keep hidden verifiers, and limit submission budgets. So: run, evaluate and promote are three different permissions. Scope has to follow the repair loop, and each grader needs a budget.

### 07. The agent never pushes; a placeholder token is still a string

*1:50, starts at 9:05*

Networking and credentials. The structure is simple and I think right. The orchestrator holds the GitHub token and applies patches only after the gate. The agent never pushes. The work cell has no GitHub token and deny-by-default egress. The model credential is injected by an egress gateway, so it never sits in the cell. Industry has converged on that pattern. But be precise, because this room will be. What the cell holds is a placeholder token, and a placeholder token is still a bearer string in guest memory. Fork the VM and you copy it. And the model endpoint is itself an allowed channel that carries arbitrary bytes out. So the next step is that the gateway authenticates the child, not the string, and the child's principal is re-minted on every restore. That part is proposed, not built. Capsicum and leases are the right vocabulary for it.

### 08. Teardown should destroy a worker, not the experiment

*1:40, starts at 10:55*

Recovery. A second run the same day went well, then badly. Build and test passed first time, 1,981 tests. Review approved. Then delivery was refused three times: the workspace contained a file outside the reviewed commit stream. That file was my own harness's review archive, mirrored into the workspace. So the gate was right to refuse. What happened next was wrong: teardown destroyed the cell, and with it the approved candidate. Fourteen minutes, three dollars forty, nothing delivered. The fix is not exotic. The artifact has to leave the cell before the cell dies; here a patch file on the host would have been enough. The general rule: a crash, a refusal or a human wait should destroy a worker, never the experiment. Snapshot, destroy, and restore across a long human gate, instead of keeping a machine alive for days.

### 09. A green check is not proof the check ran

*1:50, starts at 12:35*

Observability. Three receipts. First, a CI job that evaluates the islo lane reported success in three seconds, because the key was unset and every real step was skipped. Second, my approvals file records the gates as mode human, actor admin. It was my harness answering. Third, my own sandbox command line printed its status messages on the same standard output as the program it was running, so the tool's words and the program's output were mixed. Two of these are my own receipts, and they were wrong. I would rather tell you than have you find them. The rule: every check needs a receipt that says it actually ran, carried on a channel the child cannot write. This room knows this problem as provenance, from PASS and CamFlow, and the supply-chain world calls it in-toto. The factory needs the same thing for evaluations.

### 10. Everything is pinned except the part that wrote the code

*1:25, starts at 14:25*

Reproducibility. Here is what the run record pins: the input commit, the lockfile, a digest of the policy, a digest of the accepted inputs, and the output of every agent step as JSON. Here is what it does not pin: the hosted model, which has no sampling seed I control; the external hosts and their redirects; and time and scheduling. So everything is reproducible except the part that wrote the code. The honest target is replay, not rerun. Keep every model call and response as a log, and re-execute everything else against it. That is record and replay, as in rr, and DeepSeek's sandbox system keeps trajectory logs for the same reason. Today a scientist could audit this run. Nobody could rerun it.

### 11. The plan asked for a fork; the runtime said no

*0:50, starts at 15:50*

Fast cloning. The plan had three steps, and one of them was safe to run in parallel with the other two. The executor needed a fork to do that. It did not have one, so it ran them one after another, and it wrote down why: serial fallback, missing fork. With a fork it would have saved about three minutes of a forty-three-minute run. So speed is not why we fork. We fork to buy alternatives.

### 12. Fork has a 20-year literature, much of it built on Xen

*1:50, starts at 16:40*

Now the fork. Fork is old, and much of it was built on Xen, in this building. Potemkin flash-cloned honeypot VMs with copy-on-write memory in 2005. SnowFlock forked Xen VMs across hosts in 2009, in six to eight hundred milliseconds. Its very first example is our pattern: run trusted code, fork, and give the child the untrusted work. Catalyzer forked running sandboxes. This year, DeltaBox reports fourteen-millisecond agent checkpoints and Shepherd forks agent sandboxes in about 140 milliseconds. And a frontier lab, Kimi, reports fifty-one million sandboxes in RL, with fork used, in their words, for reward judging without side effects. By fork I mean whole-machine fork, not the POSIX call that A fork in the road argued we should retire. So the mechanism is old. What is new is the caller: a program that searches, reads git history and games tests.

### 13. Fork copies memory; identity and secrets must not follow

*1:55, starts at 18:30*

Fork copies memory, so it copies everything in memory. Five things follow the child that must not. Random state: siblings share random streams. VMGenID reseeds the kernel generator, but Firecracker's own documentation says there is no generic solution for userspace. Tokens: eight forks of a VM holding a token are eight live tokens, which is why the secret should never be in the guest, and why AWS proposed wiping memory on suspend. The clock resumes at snapshot time. Network identity: every clone has the same IP and MAC, so each needs its own namespace and NAT; back in 2005 Potemkin already spent 142 of its 521 milliseconds just configuring IP. And nobody clones an open TCP connection. CRIU can restore one connection, once. gVisor resets it. A runtime for search has to treat all five as part of the fork contract, not as surprises.

### 14. Hold effects until an authority releases them

*1:20, starts at 20:25*

External effects. A restore cannot unsend an email or un-push a branch. The answers here are old too. Speculator and external synchrony ran ahead speculatively and held output until it was safe to release. Remus held network output until the checkpoint committed. And this year Zheng and colleagues state the agent version plainly: an execution edit cannot undo a tool request already sent. In my factory the rule is structural. The children hold no credential that can publish anything. The orchestrator applies their patches, once, after the gate. Output commit, made structural.

### 15. When fork pays, and where it loses

*2:10, starts at 21:45*

When does fork pay? You pay preparation once instead of N times, and in exchange you pay capture once and restore and divergence per child. Fork wins when N minus one preparations cost more than that. It loses in three places. With one child. When the state is only files and your build cache is good, which is the lesson I learned at Incredibuild. And when a minimal image boots faster than you can restore, which is the Jitsu and LightVM argument, from this room. Now my number, carefully. From a named 141-megabyte snapshot, one restore, run and capture round trip through the public API takes 6.87 seconds at the median, at concurrency twelve, and 255 of 256 succeeded. That is an API round trip. The mechanisms are much faster: Kimi reports 133 milliseconds to checkpoint, DeltaBox under 11. Mine is an API round trip; theirs are mechanisms. And Kimi reports that a sandbox spends up to 98 percent of its life waiting on the model. So the value of fork is not seconds. It is state you cannot rebuild cheaply, and a grader the child cannot touch.

### 16. Pick the lowest rung that holds the threat

*1:05, starts at 23:55*

Isolation. There is a ladder: process, container, a user-space kernel like gVisor, and a microVM. Pick the lowest rung that holds the threat, and remember that the threat here is a program that searches. Kimi reports container kernel panics under agent workloads. Firecracker's own production guide says to turn off simultaneous multithreading and kernel same-page merging, because both are side channels. Density claims are not isolation claims. We call it a swarm. The operating system calls it roommates.

### 17. Cheap forked machines for search; authority never lives inside them

*2:00, starts at 25:00*

Here is the architecture with honest labels. Built and running: an Airflow scheduler with a durable journal and a run lock, the work cells, and an orchestrator whose gate binds an approval to the exact artifact hash. Built but not exercised in these runs: a lease broker that ties each credential to an attempt, a cell and an epoch, so an old worker cannot commit into a new campaign. Proposed: an evaluator that lives outside the cell. And missing: the fork store. I wrote the fork contract before I had the fork. It lives in the repository: fork from an immutable content-addressed parent, give every branch its own lease and budget, never copy publishing credentials, record parent and evidence identities, never count siblings that reuse evidence as independent agreement, merge deterministically, and verify the merged result. That list is my ask to every provider in the lineage I just showed you. And the fifth condition is the bridge to the last part of the talk.

### 18. One model wrote the fix and reviewed it twice. How many witnesses?

*1:15, starts at 27:00*

Now the turn. Go back to that run. One model wrote the fix, and the same model reviewed it twice. How many independent witnesses was that? Not two, and not three. Now imagine the thing the factory asked for: fork the repair loop nine times from the same parent. Suppose all nine go green. That is not nine witnesses either. Same parent, same model, same prompt, same flaky test. The copies share almost everything that could make them wrong together.

### 19. Execution multiplicity is not evidence multiplicity

*1:50, starts at 28:15*

Here is the arithmetic. If K runs have the same variance and a common pairwise correlation rho, the variance of their average has a floor at rho times sigma squared. More runs approach the floor; they never go below it. The same thing written as an effective sample size: a hundred forks at a correlation of point one are worth about nine independent witnesses. At point five they are worth two. And the correlation is not hypothetical. Kim and colleagues looked at more than 350 language models and found that when two models are both wrong, they agree sixty percent of the time. So: execution multiplicity is not evidence multiplicity. Four clones do not make four witnesses, and past the floor, more forks buy nothing.

### 20. The statistics exist; the runtime does not hand over the cluster labels

*1:15, starts at 30:05*

I want to be precise about what is new, because it is not the statistics. Correlated evidence has a sixty-year literature. Kish's design effect, cluster-robust variance, meta-analysis of dependent effect sizes, and in databases, provenance as annotations on derived results. All of these need the same input: cluster labels. Which runs share a parent, a model, a seed, a test, a fixture. The runtime is the only component that knows. Today it throws that away and returns a score. Fork lineage and evidence identities are exactly the cluster labels. So counting correlated evidence is a runtime problem, not a statistics problem.

### 21. Fork is also how you run the control

*1:00, starts at 31:20*

Dependence is not always the enemy. To compare two candidates, give them the same random draw, and the nuisance variation cancels in the difference. That is common random numbers, old in simulation. To corroborate a claim, you want the opposite: vary the randomness and the failure modes. A fork decides which one you get, by whether it copies the random state or reseeds it. So the seed policy belongs in the fork API, as an explicit choice.

### 22. Every worker returns a receipt, not a score

*2:00, starts at 32:20*

That is my contribution. Every worker returns a receipt, not a score. The receipt carries an estimate, its information, the sample size, the identities of the evidence it used, its fork lineage, and metadata. Theta is one candidate's quantity, for example its pass probability, estimated by forked re-runs. Choosing among different candidates is a separate selection step. The numeric part merges in any tree order, so it fits MapReduce-style reduction. Two workers that declare the same evidence are rejected, not counted twice. A retry reuses its evidence identity, so fault tolerance cannot turn into double counting. And when the dependence is unknown, the reducer abstains: it refuses to report the narrow interval that independence would imply. The estimator is Cochran's inverse-variance weighting. The contract is what was missing. The reference reducer is built and tested, and one trace runs it end to end from a named snapshot through four workers.

### 23. Isolation does not authenticate n

*1:10, starts at 34:20*

One more trap. Isolation bounds what a child can do. It does not bound what a child can claim. In a synthetic check from the paper, one worker reports a distant estimate and inflates its reported precision a further fifty times. Unprotected pooling moves to seventeen. A simple stress heuristic brings it back to about five. That heuristic is not a Byzantine guarantee. The real fix is architectural: the controller measures sample size and information; the child does not report them. Precision is an input the child should not control.

### 24. The test that could prove me wrong

*2:20, starts at 35:30*

Here is the test that could prove me wrong, and I wrote the predictions down before any run. Phase A is cost, with no model calls: a cold cell, a cached template, and a restore from snapshot, at one to twelve concurrent children, timed on the server side so we see where the seconds go. If restore does not beat a good cached template, fork buys nothing for this factory, and I will say so. Phase B is coupling, also with no model calls: six snapshot families of three siblings each, against eighteen cold cells scheduled at the same times, each running the flaky race test thirty times. If siblings fail together no more than co-scheduled strangers do, shared ancestry did not couple the evidence here. Phase C is the repair loop itself: re-run it from its recorded input, three forks in each of three families, and ask whether each child edits the out-of-plan file. That is the only phase that measures correlation induced by the model. My predictions are on the slide. A result where the build cache wins is a good result for this room.

### 25. The same work order, as the runtime should run it

*1:30, starts at 37:50*

So here is the same work order, run the way the runtime should run it. Fork after the plan is approved, from a content-addressed parent. Each child gets its own lease and budget. The evaluator lives outside the cells, and the repair loop's scope is enforced, so the out-of-plan edit is denied instead of being reported as a major finding. The reducer reports an effective number of witnesses, or abstains. The approved candidate leaves the cell before teardown. And promotion is fenced by an epoch, so a stale worker cannot commit. Review two would not count as a second witness. Search can race. Promotion must not. This is a design, not a run.

### 26. Open problems where this room is ahead of me

*1:45, starts at 39:20*

I will end with open problems, where I think this room is ahead of me. One: estimate the dependence from lineage. Given fork trees and evidence manifests, what can we say about rho without running everything twice? Two: leases that fork. A child's capability should be re-minted on restore, revocable, and never ambient. Three: warm state and side channels. Sharing warm pages is performance, and it is also a channel, so we should pack forks by trust and not only by utilisation. Four: evidence commit. We know how to hold network output; how do we hold effects on remote services and on people? Five: when does a content-addressed build beat a live fork? Six: a human gate can take a day; the machine should not wait alive for it. I would especially like help with the first two.

### 27. Fork the machine, not the trust.

*0:40, starts at 41:05*

Fork the machine, not the trust. State without secrets. Graders the children cannot write. Receipts that outlive the runner. Evidence counted, not executions. And authority committed once. Burn the runner; keep the proof. Thank you. I am happy to take questions.

## Backup slides

### B1. Paper Table 2: exercised API paths, not a provider ranking

Bring this up only if asked about speed. The operations differ: two rows are sandbox creation, the islo row is restore plus run plus capture. Do not compare them as latencies. The islo total implies queueing above the median; the one failure out of 256 must be explained before the talk.

### B2. Agent checkpoint and fork, 2026

None of these systems treats sibling outputs as correlated evidence; they optimise checkpoint latency or safety. Planarian was posted on 28 September; read it in full before the talk.

### B3. Arp2/3 shapes network dynamics

This is a result from mechanochemical simulations of branched actomyosin networks. At high Arp2/3 concentration the network stalls; at low concentration it contracts; at an intermediate concentration, loosely connected clusters can collapse suddenly under motor activity. My graph-theoretic work studies how local connectivity relates to global morphology, while the avalanche study uses network science and machine learning to forecast collective rearrangements. Stockmayer's random-branching polymer theory is a formal precedent for asking when local branching yields system-scale connectivity, under its own idealized assumptions. A related question for agent systems is whether communication links connect otherwise separate lineages and reduce effective diversity; its threshold must be derived for the actual dependency model. These biological and polymer results motivate that question, but do not predict software behavior.

### B4. Reset changes the learning problem

Reusing a difficult-to-reach state can make exploration productive, as return-and-explore methods illustrate. But a policy trained primarily from favorable intermediate checkpoints has seen a different starting-state distribution. We cannot silently substitute its performance for task-start performance. Depending on the algorithm, distribution correction, curriculum design, or explicit reporting may be necessary. Snapshot ancestry records where experience came from. The final evaluation should still test the deployment question we claim to answer.

### B5. Three graphs describe the computation

Ancestry records where execution state came from, often as a tree or DAG. Communication adds edges that need not follow ancestry; these edges can introduce dependencies among later decisions. Composition concerns sets of artifacts and may need hyperedges for three-way or higher-order effects. The outline around the three candidates denotes a possible higher-order interaction, not a measured one. Keeping these structures separate avoids calling every relationship a fork. It also clarifies which metadata the controller must retain.

### B6. What does a message contribute?

The XOR example is exact and deliberately small. Either bit alone leaves H uniformly random; together they determine H. After receiving A, B contributes one bit of conditional information. This is information synergy, not the finite-difference score interaction between two software patches. In practical search we rarely know the joint distribution well enough to compute mutual information directly. Treat it as a precise way to ask what a message could add, not a ready-made universal routing score. Here, think of H as which candidate the evidence would favor under the declared objective, and E_k as a branch report. The next slide makes that distinction concrete. Useful decision information also depends on costs and available actions.

### B7. How eight changes work together

Gamma is a second finite difference of a declared scalar objective. It measures non-additivity such as synergy, conflict, or saturation, and may itself require repeated measurements. It is not mutual information or quantum interference. Define an application order or canonical composition procedure; if the patches do not compose, record a failure rather than inventing a score. Eight candidates have 28 unordered pairs, while all subsets number 256 including the empty set. Pairwise screening can guide an economical search but cannot certify every higher-order interaction.

### B8. What the reducer experiments establish

The logistic check uses five IID shards with sample sizes 60, 120, 400, 2000, and 5000. Across eight fixed seeds the information-weighted estimate is closer to the centralized maximum-likelihood estimate than equal coefficient averaging. This specific check does not establish universal efficiency or superiority to other distributed estimators. The forged-precision example motivates trustworthy information estimates, not a claim of Byzantine robustness. These are reported results from the paper; they are not new agent-task benchmark measurements.

### B9. Ablations that explain the outcome

These ablations distinguish mechanisms. A fast fork with a worse search policy may lose. A communicating system may win only because it spends more model calls. Sharing can help discovery while increasing evidence dependence. Evaluate communication with an equal full resource budget and record the induced selection history. For composition, include deliberately interacting changes rather than only independent patches. Use uncertainty across tasks and seeds and reserve fresh validation for selected results.

### B10. Evaluation under adaptive search

Access control prevents direct tampering. It does not prevent a candidate generator from adapting to repeated pass/fail or score feedback. The final reported score may then be optimistic even when every individual evaluation was computed correctly. A fresh held-out evaluation or a statistically justified adaptive procedure addresses a different failure mode from sandbox isolation. If final-validation feedback is fed back into further selection, it has become development feedback and the protocol must account for that.

### B11. References: systems

Systems references. Every figure on a main slide is traceable to one of these or to a named run file.

### B12. References: evidence and evaluation

Evidence and evaluation references.
