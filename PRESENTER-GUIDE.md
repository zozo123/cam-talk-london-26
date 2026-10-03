# Presenter guide: Forkable Sandboxes

**The Runtime Layer for AI Software Factories.** Cambridge SRG, 15 October 2026, 15:00-16:00 BST, FW11 + Microsoft Teams.

Generated from the notes in `acts/` by `tools/presenter_guide.py`. 50 main slides, 10 end-matter pages. Planned talk: **41:35**, 4118 spoken words, 99 wpm average, peak 110 wpm. These are planned cues, not a measured rehearsal.

## Run of show

| # | Slide | Cue | Clock | Words | wpm |
|---|---|---|---|---|---|
| 1 | Forkable Sandboxes | 0:40 | 0:00-0:40 | 53 | 80 |
| 2 | Hedged requests reduce tail latency | 1:05 | 0:40-1:45 | 107 | 99 |
| 3 | Repeated sampling needs an automatic check | 0:45 | 1:45-2:30 | 81 | 108 |
| 4 | Latency and scale of agent runtimes | 1:10 | 2:30-3:40 | 119 | 102 |
| 5 | Where 43 minutes went | 0:50 | 3:40-4:30 | 81 | 97 |
| 6 | A review gate approved untested code | 1:25 | 4:30-5:55 | 143 | 101 |
| 7 | One question across six fields | 1:00 | 5:55-6:55 | 103 | 103 |
| 8 | Method: two experiments, seven surfaces | 0:40 | 6:55-7:35 | 65 | 98 |
| 9 | Intelligence as choice and action | 0:40 | 7:35-8:15 | 69 | 104 |
| 10 | Research question, claims and outline | 0:50 | 8:15-9:05 | 91 | 109 |
| 11 | Allowlists fail when hosts redirect | 0:40 | 9:05-9:45 | 66 | 99 |
| 12 | Forks copy cell memory, so keys stay outside | 0:40 | 9:45-10:25 | 69 | 104 |
| 13 | Filesystem state shared by a snapshot | 0:40 | 10:25-11:05 | 64 | 96 |
| 14 | Write-protected tests did not limit edits | 0:50 | 11:05-11:55 | 82 | 98 |
| 15 | Reinforcement learning calls it reward hacking | 0:45 | 11:55-12:40 | 70 | 93 |
| 16 | Teardown destroyed the approved patch | 0:40 | 12:40-13:20 | 68 | 102 |
| 17 | Three of our check records were wrong | 0:45 | 13:20-14:05 | 70 | 93 |
| 18 | What the run pins, and what it cannot | 0:40 | 14:05-14:45 | 63 | 94 |
| 19 | The parallel-safe steps had no fork available | 0:30 | 14:45-15:15 | 53 | 106 |
| 20 | Six findings from two experiments | 0:45 | 15:15-16:00 | 63 | 84 |
| 21 | SnowFlock described agent sandboxing in 2009 | 0:50 | 16:00-16:50 | 83 | 100 |
| 22 | Related work: fork systems since 2003 | 0:55 | 16:50-17:45 | 85 | 93 |
| 23 | Training runs create sandboxes at large scale | 1:00 | 17:45-18:45 | 105 | 105 |
| 24 | Reset changes the learning problem | 0:40 | 18:45-19:25 | 61 | 92 |
| 25 | Fork copies memory, secrets and identity | 0:50 | 19:25-20:15 | 61 | 73 |
| 26 | What each kind of fork copies | 0:55 | 20:15-21:10 | 86 | 94 |
| 27 | Hold effects until an authority releases them | 0:50 | 21:10-22:00 | 81 | 97 |
| 28 | When fork pays, and where it loses | 1:05 | 22:00-23:05 | 102 | 94 |
| 29 | Isolation has two axes, kernel and authority | 0:50 | 23:05-23:55 | 81 | 97 |
| 30 | The interface the runtime owes the loop | 0:50 | 23:55-24:45 | 79 | 95 |
| 31 | Work cells fork and the gate holds authority | 0:50 | 24:45-25:35 | 81 | 97 |
| 32 | Promotion is small enough to model-check | 0:40 | 25:35-26:15 | 66 | 99 |
| 33 | The second review was not independent | 1:00 | 26:15-27:15 | 104 | 104 |
| 34 | A reused grader becomes a training set | 0:45 | 27:15-28:00 | 74 | 99 |
| 35 | One formula, three fields | 0:55 | 28:00-28:55 | 93 | 101 |
| 36 | Extra forks add few witnesses | 1:50 | 28:55-30:45 | 186 | 101 |
| 37 | The runtime holds some of the cluster labels | 0:45 | 30:45-31:30 | 80 | 107 |
| 38 | A fork can supply the control run | 0:40 | 31:30-32:10 | 64 | 96 |
| 39 | When a swarm gels | 0:45 | 32:10-32:55 | 70 | 93 |
| 40 | Two passing patches can fail together | 0:40 | 32:55-33:35 | 73 | 110 |
| 41 | Workers return a receipt of evidence and origin | 0:50 | 33:35-34:25 | 89 | 107 |
| 42 | A sandbox cannot verify a claim | 0:50 | 34:25-35:15 | 88 | 106 |
| 43 | Test 1: restore versus a warm cache | 0:55 | 35:15-36:10 | 97 | 106 |
| 44 | Why siblings may fail together | 0:35 | 36:10-36:45 | 53 | 91 |
| 45 | Test 2: sibling failure coupling | 1:05 | 36:45-37:50 | 110 | 102 |
| 46 | Threats to validity | 0:35 | 37:50-38:25 | 60 | 103 |
| 47 | The same work order, run as designed | 0:45 | 38:25-39:10 | 82 | 109 |
| 48 | Limitations and open problems | 0:30 | 39:10-39:40 | 55 | 110 |
| 49 | Future work: a canary for correlation | 0:45 | 39:40-40:25 | 77 | 103 |
| 50 | Conclusions | 1:10 | 40:25-41:35 | 112 | 96 |

## Script

### 01. Forkable Sandboxes

*0:40, starts at 0:00*

A fork is a new sandbox started from a running sandbox's snapshot. In five minutes we ask how many independent observations nine passing forks provide, and by the end we answer it. We built a receipt contract, ran two experiments with a self-evolving loop, and defined two tests that could falsify our claim.

### 02. Hedged requests reduce tail latency

*1:05, starts at 0:40*

In 2013 Jeff Dean and Luiz Barroso published hedging. The client sends a request to one server. If no answer arrives within 10 milliseconds, it sends a copy to a second server and uses the first answer. In one benchmark, the slowest requests fell from 1,800 milliseconds to 74, for two percent more requests. Delays usually come from the server, and two servers rarely stall together. [click] Agents now hedge for correctness by running the task several times and keeping a passing run. When the flaw is in the task, every copy repeats it. Their paper gives a second technique for that case, presented at the end.

### 03. Repeated sampling needs an automatic check

*0:45, starts at 1:45*

Hedging for correctness works in part. Brown and colleagues sampled a coding model 250 times. It solved 56 percent of SWE-bench Lite, against 16 percent for one sample. This gain requires an automatic check. Without a check, voting and reward models stop improving. A check that accepts wrong answers caps the gain. When wrong answers cost more than none, Stroebl and colleagues find the best number of tries is often under ten. In model training, this check is called the reward.

### 04. Latency and scale of agent runtimes

*1:10, starts at 2:30*

Jeff Dean also gave us numbers everyone should know. This table gives them for agent runtimes. Checkpointing a sandbox, saving its state, takes eleven milliseconds. Forking one takes about a hundred and forty milliseconds. SnowFlock forked Xen VMs across hosts in 2009 in under a second. Through a public API, a fork takes seconds. One work order in our experiments takes forty-three minutes and costs ten dollars. One frontier model used fifty-one million sandboxes across training and evaluation. The row without a source is how correlated two forks' verdicts are. It decides how much independent evidence the other rows buy. Our claim is that the runtime sees what forks share, so it is where this value can be measured.

### 05. Where 43 minutes went

*0:50, starts at 3:40*

The forty-three-minute row is one work order of a self-evolving loop, an agent system that proposes, tests and merges changes to its own code. The analogy comes from two years on self-driving cars at Mobileye, where the rare case was hardest. The loop is self-driving software with the same hard part. Setup takes twenty seconds, under one percent. A hundredfold faster setup would make this run 0.8 percent faster. The minutes and the risk are in the agents and the checks.

### 06. A review gate approved untested code

*1:25, starts at 4:30*

A race test on four threads failed, and the loop sent a repair agent. It had no shell and rewrote code outside the plan. Review one blocked the change as untested and unverified. The tests were locked, so repair two restructured the code and argued it was covered. Review two downgraded untested to minor and approved. One model did all four steps. All 1,972 tests passed after each repair. The new code had no test of its own, and both repairs said they had not run the tests. The gate approved. [click] Suppose the loop had forked repair one nine times and all nine passed. We ask how many independent observations that provides. Type your number in the Teams chat. [wait seven seconds, silently, then read one or two numbers aloud for the recording] Keep your number. We check it when we count.

### 07. One question across six fields

*1:00, starts at 5:55*

We have met that question before, in six fields, which explains why a biological physicist forks sandboxes. In a PhD on protein filament networks, it was which links make parts move together. In genomics with co-authors, a new cell type or the same patient again. In Bitcoin, a decentralized network or sixty-four agents. At Mobileye, on self-driving perception, a million frames or one rare case. In agent loops, nine green forks or one parent. In reinforcement learning, which rollouts, or practice runs, shared a start. Five of these six fields are ours. Physics and biology give vocabulary here and no evidence about forks.

### 08. Method: two experiments, seven surfaces

*0:40, starts at 6:55*

We logged the experiments and the seven places the runtime mattered. Every evidence slide is tagged by kind, analogy included. The scope is two experiments with the loop in Docker Sandboxes through Airflow's sandbox toolset, with models served through Databricks. Two observations come from our own sandbox platform. Our harness answered the gates without a human, permission leases were off, and no run used forking.

### 09. Intelligence as choice and action

*0:40, starts at 7:35*

Intelligence comes from Latin intellegere, from inter, between, and legere, to choose or read, meaning choosing between. Since the twenty-ninth of September, US agencies must say Super Intelligence. We say intelligence. Our ladder is an analogy from self-driving cars to self-driving computers to self-driving intelligence, an agent in a loop. The loop reads, chooses between forks, acts inside a wall, and checks with a count that decides what counts.

### 10. Research question, claims and outline

*0:50, starts at 8:15*

Wall, fork and count structure the talk. We ask how many independent observations N forks provide, and whether the runtime can measure it. Section two studies the wall in two experiments. Section three designs the fork. Section four analyses the count. Section five gives two tests that could prove us wrong, and section six concludes. We claim a built receipt contract, two measured experiments and two rejectable hypotheses. We do not claim an estimator, a speedup, a ranking, a loop that forks today, or physics and biology as evidence about forks.

### 11. Allowlists fail when hosts redirect

*0:40, starts at 9:05*

Section two, a case study of the wall, starts with networking. The work order was a network bug on our sandbox platform that morning. The allowlist named astral dot sh, which redirects off the list. Curl returned 403 and uv failed. Five drifted copies held the list. The fix admits every GitHub release asset. We propose fetching by digest, the file's hash, through a caching proxy.

### 12. Forks copy cell memory, so keys stay outside

*0:40, starts at 9:45*

The GitHub token stays outside, with the orchestrator. The cell, the agent's sandbox, blocks outbound traffic, called egress, by default. A gateway injects the model credential. A placeholder token still sits in cell memory, which a fork copies. We propose keying each request on a host-assigned identity. Restore increments a generation number, voiding the parent's lease, its timed permission. Credentials must never reside in memory that a fork copies.

### 13. Filesystem state shared by a snapshot

*0:40, starts at 10:25*

Surface two is filesystem state. A snapshot, a saved copy of the sandbox, captures only state inside it. Each kind needs its own policy. Build outputs are pinned by digest, and OBuilder snapshots every step. The workspace disk is copy-on-write, and DeepSeek's DSec already chains such snapshots. Randomness and external services come later. A filesystem snapshot cannot share memory, which the forking section addresses.

### 14. Write-protected tests did not limit edits

*0:50, starts at 11:05*

Surface three is build and test. The wall here was a write-protected tests directory. The hook never fired, and all fifteen edits were allowed. Repairs were not scope-checked, and one edited code outside the plan. In biology, this is an off-target edit. Biologists label that risk before they cut, and we built a tool for it with our co-authors. A scope check does the same for code. The proposed scope check and blocker change only policy. A write-protected directory defines no scope.

### 15. Reinforcement learning calls it reward hacking

*0:45, starts at 11:55*

Others report the same failure. Reinforcement learning calls it reward hacking. METR reports o3 reward-hacked in thirty percent of RE-Bench runs and under one percent of HCAST. Their leading hypothesis is the visible scorer. ImpossibleBench reports read-only tests prevent test edits but not special-casing. Kimi K3 hides some verifiers. Its kernel-task hacking detector penalises input caching, which is also core to build acceleration. Running, evaluating and promoting are three permissions.

### 16. Teardown destroyed the approved patch

*0:40, starts at 12:40*

Surface four is recovery. A second work order that day passed tests and review, then failed. A stray file, our harness's review archive, blocked delivery three times. Teardown destroyed the sandbox and the approved patch. The run took twenty-six minutes, cost three dollars forty-three and delivered nothing. The artifact should leave the sandbox before teardown. During a long human wait, the sandbox should be snapshotted, destroyed and restored.

### 17. Three of our check records were wrong

*0:45, starts at 13:20*

Surface five is observability. Three of our own receipts, records of what ran, were wrong. A sandbox evaluation CI job passed in three seconds with every real step skipped. Our approvals file records mode human, but our harness answered. Our sandbox CLI mixed status into its output. Every check needs a receipt the sandbox cannot write. The literature calls this provenance. Kimi K3 grounds reward in the final environment state.

### 18. What the run pins, and what it cannot

*0:40, starts at 14:05*

Surface six is reproducibility, whether anyone can rerun the run. The record pins the commit, lockfile and digests. It omits the hosted model, external hosts, the clock, and our adapter's source. We propose replay, which logs every model response, fetch and clock read and re-executes the rest. Genomics set this standard in the ENCODE pipelines. This run can be audited but not rerun.

### 19. The parallel-safe steps had no fork available

*0:30, starts at 14:45*

Surface seven, the last, is fast cloning. The executor requested a fork. No provider offered one, so it ran in series and recorded the reason, serial fallback, missing fork. By our computation, excluding fork cost, a fork would have saved three minutes of forty-three. We propose forking to obtain alternatives from expensive state.

### 20. Six findings from two experiments

*0:45, starts at 15:15*

The runs gave six findings. Sandbox setup took under one percent of work order time. A locked test folder did not limit repair. Passing checks can test nothing. One model in all four steps gives one review. Teardown can destroy approved results. No provider offered a fork. Across the seven surfaces, trusted components belong outside the sandbox. Next we consider copying the sandbox.

### 21. SnowFlock described agent sandboxing in 2009

*0:50, starts at 16:00*

Section three designs the fork, starting from related work. SnowFlock (EuroSys 2009) forked Xen virtual machines, and Xen was built in this laboratory. In pattern (a), sandboxing, the parent forks a child to run untrusted code and waits. This is an agent sandbox, described seventeen years ago. In pattern (b), parallel work, the fork ID selects each child's slice. Nine forks of an agent's repair share state, tests and one slice. The mechanism is old, and the caller is a program that searches.

### 22. Related work: fork systems since 2003

*0:55, starts at 16:50*

SnowFlock continued a line begun here in 2003. Xen led to live migration with sixty milliseconds of downtime. Potemkin cloned honeypots. SnowFlock forked across hosts. Catalyzer forked a gVisor sandbox in under one millisecond, best case. MITOSIS forked over remote direct memory access. Fork means the whole machine, unlike the POSIX call Baumann and colleagues proposed to retire. The shaded band marks this year. One row is a training run. Each targets speed or safety. None counts what siblings share. That is the blank row.

### 23. Training runs create sandboxes at large scale

*1:00, starts at 17:45*

Model training is the largest reported use of fork. Kimi K3 created fifty-one million sandboxes for training and evaluation. It pauses a sandbox while the model thinks, up to ninety-eight percent of its life. It forks one, in their words, for reward judging without side effects. It snapshots for recovery. The trainer stops waiting once a fraction lambda of trajectories, meaning attempts, finishes, to mitigate the long-tail latency. This matches Dean and Barroso's good-enough approach of not waiting for stragglers. DeepSeek-V4 runs hundreds of thousands of sandboxes per cluster. In training, a sandbox is the environment, a fork a reset, and a verifier the reward.

### 24. Reset changes the learning problem

*0:40, starts at 18:45*

A fork used as a reset changes what the learner sees. Starting at the task start samples one distribution. Restoring a checkpoint samples another. Ecoffet and colleagues showed that returning to a state before exploring makes exploration productive. We propose recording each checkpoint's origin and reason, and evaluating on the intended task distribution. Each restore point selects the learner's training data.

### 25. Fork copies memory, secrets and identity

*0:50, starts at 19:25*

The child inherits all memory, even what it should not. Siblings share random streams, with no generic solution above the kernel. Eight forks holding a token are eight live tokens, so secrets stay outside the VM. Clocks resume at snapshot time. Clones share one IP and MAC address. Open TCP connections cannot be cloned. All five belong in the fork contract.

### 26. What each kind of fork copies

*0:55, starts at 20:15*

Each fork type copies different state at a different cost. Children share memory until they write. Kimi reports copy-on-write memory with page-cache optimisations allows up to 6.5 times overcommit. A worktree keeps files. CRIU keeps processes, but a connection survives in one copy at most. A microVM pays for pages each child touches. A restore that returns OK is not a faithful copy. As an analogy from physics, paths share a past and split at first write. Fork is cheap, and the cost appears at divergence.

### 27. Hold effects until an authority releases them

*0:50, starts at 21:10*

Memory can be copied or discarded, but a sent email cannot. Speculator, external synchrony and Remus held output until safe. Zheng and colleagues stated in Lean that no edit undoes a sent request. DeepSeek replays logged results, so an unrepeatable command never runs twice. Kimi forks to judge reward because judging produces no side effects. Prototype children hold no publishing credential. The orchestrator delivers once, after the gate. The model API is the one unheld channel. Output commit is structural here.

### 28. When fork pays, and where it loses

*1:05, starts at 22:00*

A safe fork pays when it trades N preparations for one capture, plus a restore and a divergence per child. It loses in three cases. The first is one child. The second is files-only state with a good build cache. The third is a faster-booting minimal image, as in Jitsu from Cambridge and LightVM from NEC Labs. Fork pays for state that cannot be rebuilt. The end matter lists API timings without ranking them. With teardown, a slot on the sandbox platform averaged 11.3 seconds. Until the snapshot is shown to hold memory, the platform's fork is restore fan-out from one snapshot.

### 29. Isolation has two axes, kernel and authority

*0:50, starts at 23:05*

Child isolation has two axes, and this laboratory built systems for both. A container shares one kernel. gVisor moves it to user space. A microVM stands on a hypervisor. An ordinary process names whatever its user can. Under Capsicum or CHERI, it uses only what it is handed. A build cache may be shared within one trust domain of equally trusted code. Scratch is never shared. Kimi saw kernel panics in early container runtimes. Firecracker advises disabling SMT and same-page merging.

### 30. The interface the runtime owes the loop

*0:50, starts at 23:55*

The runtime owes the loop six calls with stated status. Checkpoint names snapshots, memory unverified. Fork takes a lease, an egress policy and a seed policy, copy or reseed. Evaluate runs outside the child. Select picks one candidate on a fresh test. Reduce combines receipts into an estimate or abstains, with merge built and abstention proposed. Promote runs once, with the hash-bound gate built and the epoch fence, which blocks stale runs, proposed. Select and reduce are separate calls.

### 31. Work cells fork and the gate holds authority

*0:50, starts at 24:45*

The six calls rest on an architecture labelled by status. Solid boxes were built and ran: the scheduler with its journal and run lock, the work cells, and a gate bound to the artifact's hash. [click] Dashed gold marks the lease broker, built but unexercised, and the evaluator, only designed. [click] The fork store is missing. We wrote the fork contract before the fork store existed. Condition eight came from our second run. The rest of this talk concerns condition five.

### 32. Promotion is small enough to model-check

*0:40, starts at 25:35*

The promotion gate must never race. It is small enough to model-check every ordering. Evidence names only the frozen candidate. Approval needs that evidence. Publication needs all three in the current epoch. Six rules must hold, and no model-checker run exists yet. Dean and Barroso report that consistent updates use quorum protocols such as Paxos. A child's output cannot be model-checked, so it must be counted.

### 33. The second review was not independent

*1:00, starts at 26:15*

Section four analyses the count. Nine agent copies approve the fix. Belief depends on independence. Nine strangers giving one direction are probably right. Nine readers of one wrong map hold one opinion. Our reviews shared one map. Repair two answered review one's verdict, graded by the same model. The two reviews give at best one look. Choosing among nine patches needs a fresh test. Best-of-nine cannot beat one minus the chance all nine fail together, so record each fork's pass or fail. Confirming one patch is capped by what runs share. Biologists call these technical replicates. Nine forks of one parent are technical replicates.

### 34. A reused grader becomes a training set

*0:45, starts at 27:15*

In machine learning, a reused grader becomes a training set. Even a protected grader can let the search overfit its feedback. The candidate should be frozen and validated once. Reinforcement-learning labs do this. Kimi K3 gives feedback from public verifiers and scores with hidden ones. It caps answer length, so longer answers cannot win. Repair two argued past review one. Graders and reward models fail alike. Feedback that is optimised against stops being evidence.

### 35. One formula, three fields

*0:55, starts at 28:00*

One formula appears in three fields. Dean and Barroso report each server is slow one time in a hundred. Across a hundred servers, sixty-three percent of requests are slow. In 1943 Dorfman noted a pool is clean only if every swab is. In 2020 we modelled Poolkeh, pooling many swabs per tube for nine million people with under three hundred thousand tests. We run one patch in many sandboxes. If our race breaks one run in ten, it takes twenty-nine greens before a miss drops under five percent. All three assume independent draws.

### 36. Extra forks add few witnesses

*1:50, starts at 28:55*

Forks share starting code, model, prompt and tests. A mistake from a shared source appears in all nine. The sharing is one number, the correlation rho. A hundred forks at rho point one give about nine independent witnesses. Point five gives about two. Identical means one. Take nine green repairs. [hold up nine photocopies of one page, beside the screen, in camera] Nine sheets of one page give one witness. Their average's variance never drops below rho sigma squared. Two different models that both miss a question pick the same wrong answer sixty percent of the time, where chance would give a third. This agreement indicates nonzero rho. Nine frontier judges give about two independent votes. Reading rho as coupling and this result as bias is our interpretation. Systems people may recognise N over one plus N minus one times a fraction. [wait seven seconds, silently, repeat any answer aloud for the recording] [click] Statisticians call this Kish's design effect. Systems people call it Amdahl's law, with rho as the serial fraction of evidence. [pause] N forks give N executions, but fewer than N independent observations.

### 37. The runtime holds some of the cluster labels

*0:45, starts at 30:45*

The 1965 formula needs cluster labels, records of shared sources, that analysts rarely get. Only the runtime knows which copies share a parent, seed or test. Its egress gateway sees which model each copy calls. It can record this lineage with every result. It cannot see blind spots shared across models. We inferred clusters from outside, in Bitcoin and tumours. Malignant cells cluster by tumour, and forks by parent. Others must infer the clusters. A fork runtime can record them.

### 38. A fork can supply the control run

*0:40, starts at 31:30*

Positive correlation lowers the variance of a difference between candidates. Giving A and B the same draw, called common random numbers, cancels shared noise. Corroboration needs a different draw per copy, so a fork copies the seed or reseeds. Seed policy belongs in the fork API. Test two uses this, so only ancestry differs. Sharing the draw supports comparison and varying it supports corroboration.

### 39. When a swarm gels

*0:45, starts at 32:10*

Seeds couple copies deliberately, and exchanged information often couples them by accident. A swarm has three graphs: ancestry, evidence flow and composition. Only ancestry, who forked from whom, is a tree. Evidence edges can merge lineages, as cross-links join polymer chains. Stockmayer asked in 1943 when such links make one gel. Enough shared context makes a swarm one witness. This is an analogy, so the agent threshold must be derived.

### 40. Two passing patches can fail together

*0:40, starts at 32:55*

Composition hides a severe case: two patches pass alone but fail together. Gamma measures the pair's departure from additivity. Eight candidates give twenty-eight pair tests and two hundred and fifty-six subsets. Effects among three or more can pass every pair test. Genetics calls strongly negative gamma synthetic lethality, and we screened the genome for it. Each perturbation is survivable alone and lethal together. The shipped composition must be rebuilt and evaluated (condition seven).

### 41. Workers return a receipt of evidence and origin

*0:50, starts at 33:35*

A worker should return a receipt containing the result, the evidence it used and its origin. The built part merges summaries in any order and stops when evidence is used twice. We propose one evidence ID per execution. If the runtime cannot tell how much copies share, it should abstain. A hedged request is a speculative duplicate of an earlier request. DeepSeek's DSec replays cached results instead of re-running them. Such evidence should be counted once. The estimator is Cochran's. The proposed contract specifies how its inputs are counted.

### 42. A sandbox cannot verify a claim

*0:50, starts at 34:25*

Isolation cannot prevent a false receipt. A copy can claim more certainty than it has. Two synthetic checks come from our preprint. On the left, honest shards have unequal size. Information pooling gives a distance of 0.0083 against 0.177 for the equal average. On the right, one worker inflates its precision fifty-fold. It moves the pooled estimate from about five to seventeen. A heuristic restores it to about five but gives no Byzantine guarantee. The controller should set each child's precision, and children should not report their own.

### 43. Test 1: restore versus a warm cache

*0:55, starts at 35:15*

Section five evaluates the claim with two refutable tests. Both were written before any run. Test one measures cost. Gate zero snapshots a random RAM value and restores three children. If the value is lost, memory was not restored, so the operation is restore fan-out and not a fork. Fidelity requires matching restored and direct outputs. A cached template and a restore are compared over twenty alternating runs per size. Restore counts as better only if the whole confidence interval of the gain exceeds ten seconds at every size. A build cache win is a valid outcome.

### 44. Why siblings may fail together

*0:35, starts at 36:10*

Before test two, we state why siblings may fail together. We simulated branched actomyosin networks and observed this behaviour. At high Arp2/3 levels the networks stall, and at low levels they contract. In between, loose clusters may collapse in sudden avalanches. We described the avalanches as an analogy to cytoquakes observed in cells.

### 45. Test 2: sibling failure coupling

*1:05, starts at 36:45*

Test two asks whether siblings sharing a snapshot fail together more than strangers from other snapshots. Twelve families of three siblings each pair with three strangers on the same slot and host. The statistic is delta rho, the extra correlation among siblings. The hypothesis is supported if delta rho significantly exceeds point zero five, and rejected if its interval lies below point zero five. We chose point zero five because that excess reduces nine siblings to six point four independent witnesses. For the nine imagined repairs, we resample repair one nine times and predict at least five repeats of the out-of-plan edit. When it runs, it fills the blank row.

### 46. Threats to validity

*0:35, starts at 37:50*

A positive result on both tests would still not explain its cause. A fast fork with a worse search policy can still lose. Forks sharing notes may win only by spending more model calls. Each row therefore changes one factor at an equal full budget. Stroebl and colleagues report that the number of paid tries is part of the result.

### 47. The same work order, run as designed

*0:45, starts at 38:25*

This proposed design shows the intended work order. It forks after the plan into three children with their own leases. Stroebl reports that when a wrong answer costs more than none, the best number of tries is often under ten. The out-of-plan edit is denied. Another model family scores hidden tests once, as Kimi K3 hides its verifiers. The reducer groups results by lineage or abstains, and the artifact is exported before teardown. Search may run in parallel, but promotion may not.

### 48. Limitations and open problems

*0:30, starts at 39:10*

Section six concludes. The prototype has six open problems. We seek help with the first two. Problem one is estimating dependence from lineage and evidence edges without running everything twice. Problem two concerns forking leases. On restore, a child's capability should be newly issued, revocable, and never ambient. The other four are available for questions.

### 49. Future work: a canary for correlation

*0:45, starts at 39:40*

Next is the hedging paper's second technique, for request faults. The authors describe one request reaching an untested code path and crashing thousands of servers at once. They propose a canary sent to one or two leaf servers first. Our first run's new code had no test, so nine passing forks would share that gap. Kohli reports that nine agreeing frontier judges were still wrong 9.1 percent of the time. We therefore propose a canary for correlation.

### 50. Conclusions

*1:10, starts at 40:25*

To conclude, hedging works when failures are independent. The runtime must detect dependence. Recent work counts independent witnesses for models and judges. We know of no such count for forks of one agent. That is the blank row, and it stays blank until test two runs. In 2009 the parent ended with a wait call. Ours must count by grouping receipts by lineage, or abstain. [pause, let them read] In physics, genomics and Bitcoin, we had to infer the clusters. A fork runtime can record them. N forks give N executions, but fewer than N independent observations. [pause] We plan to report the completed row later. [Stop. Slide stays up through questions.]

## End matter (untimed)

### E1. Fork lineage, in full

Detail for slide 22.

### E2. Fork cost model and API timings

Detail for slide 28: the full cost model and the three API paths behind it.

### E3. The fork contract, in full

Detail for slide 31.

### E4. Pre-registered decision rules

Detail for slides 43 and 45. The protocol is PREREGISTRATION.md, tags prereg-v1 to prereg-v3.

### E5. Research record: biophysics

PhD work at the University of Houston and Rice: graph theory of actomyosin network shape (PRE 2020, linker valency), Arp2/3 branching and avalanches (PNAS 2020, JPCB 2021), protein folding and calcium binding. Used on slide 7 (the journey) and slide 44, the declared prior for Test 2. It motivates Test 2 and is no evidence for it. Team results with co-authors.

### E6. Research record: genomics

Genome architecture, bioinformatics and cancer genomics at Baylor, NRGene, HIT and Harvard. OffRisk appears on slide 14 (the off-target analogy). The 2021 CRISPR screen appears on slides 33, 40 and 45 (replicates, synthetic lethality). The per-patient tumour clustering (iScience) appears on slides 7 and 37 (cluster labels). The ENCODE pipelines, which set the replay bar on slide 18, are on the next page. Team results with co-authors.

### E7. Research record: preprints, systems and talks

Preprints, systems work and talks. Poolkeh appears on slide 35 as a model of a pooling scheme. arXiv:2607.09689 appears on slides 4, 7, 28, 30, 37, 41, 42 and 50 (timings, snapshots, receipts, forged precision). Bitcoin appears on slides 7 and 37 (team result). The ENCODE pipelines appear on slides 7 and 18. The three-body e-print is on an AI-assisted server and is not peer reviewed. Say so if asked.

### E8. References: systems

Systems references. Every figure on a story slide is traceable to these, to the slide's own source line, or to a named run file.

### E9. References: evidence and evaluation

Evidence and evaluation references. The shared-errors papers compare different models and do not study forks of one agent. The 2026 arXiv items are preprints.

### E10. References: own work and documentation

The speaker's own and co-authored work cited on story slides, the documentation behind slides 12, 13, 25, 26 and 29, and Go-Explore for slide 24.
