> Written for an earlier draft, before the current `talk.tex`. Check each answer against `CLAIM-FENCE.md` before using it: the built reducer does not abstain, the epoch fence is proposed, and nothing forked in the recorded runs.

# QA bank — hard SRG questions from swarm ROUNDTABLE
**Talk:** Cambridge CL SRG · Forkable Sandboxes · 15 Oct 2026  
**Source:** Challenges A–G in `archive/swarm/ROUNDTABLE.md` + researcher packs  
**Use:** 2–4 sentence answers Yossi can say aloud · claim-fenced · no vendor ms

---

### Q1 — CoW siblings ≠ independent evidence (A ↔ B)
**Challenge:** DeltaBox/Shepherd make execution cheap — why isn’t \(K\) forks \(K\) i.i.d. samples?  
**Answer:** Because exchangeable correlation \(\rho>0\) floors \(\mathrm{Var}(\bar\theta)\) at \(\rho\sigma^2\) no matter how large \(K\) is — shared model, prompt, repo, or snapshot root is common-mode error. Systems optimize execution isolation; reduce must not bill CoW siblings as independent evidence. Until we have a measured overlap model, same snapshot root in lineage means unresolved \(\rho\): abstain from narrowing \(\Sigma_g\), don’t pretend Firecracker walls mint independence.

### Q2 — Abstain as first-class verdict (B ↔ G)
**Challenge:** Will the factory API let reduce refuse a narrow posterior?  
**Answer:** In the design, yes; today, no, and I will not claim it. Built: numeric summaries merge in any tree order, a repeated evidence ID stops the merge (it raises), and lineage travels with the result, but nothing consumes it yet. Proposed: abstaining when dependence is unknown, one execution per evidence ID, a controller-derived precision, and the bound on N_eff (slide 46). The gate built today binds approval to the artifact's sha256; the epoch fence is proposed.

### Q3 — Oracle digests outside the fork (C ↔ A/B)
**Challenge:** Rebound shows agents rewrite `run_tests()` inside the env — what stops forged \((J_k,n_k)\)?  
**Answer:** Content-address the oracle *before* fork; inject tests only in EVAL; never leave held-outs in a writable overlay. The child may invoke a sealed scorer and receive a signed receipt — it must not mint precision itself. Coupled C/R that restores a tampered scorer is an oracle-contract bug, not a DeltaBox feature; escape wall ≠ evidence wall.

### Q4 — Credential remint after CoW (E ↔ A)
**Challenge:** Fork copies memory — don’t children inherit API keys and cookies?  
**Answer:** Ambient credentials inside the snapshot become \(N\times\) blast radius. Default posture: treat the entire guest credential surface as dirty — drop sockets, scrub, remint opaque leases from a broker *outside* the fork. Heat (runtimes, compile caches, model weights) may share; secrets must not. vmgenid reseeds entropy; it does not revoke an inherited cloud key.

### Q5 — Warm CoW as side-channel (F ↔ A)
**Challenge:** Does density via shared pages create a confidentiality channel?  
**Answer:** Structural CoW, host page-cache, and prefetch profiles make the shared past observable via fault timing and residency. Pack by trust tier — tenant, template digest, threat tier, wire epoch — not by NUMA fill; disable KSM and cross-tenant file maps across tenants. Firecracker’s isolation guidance is the baseline, not an optional slide knob; density claims are not isolation claims.

### Q6 — Objective digest = epoch bump (D ↔ B/G)
**Challenge:** Can a searcher “improve” the metric mid-campaign?  
**Answer:** No — mutating `Objective.digest` is an authority Epoch bump, not a child patch. Soft \(\beta\) anneal only inside a declared Epoch; metric edits require promote-authority, or you get Rebound Phase III at paper scale. Mismatched `obj_digest` is a hard reject *before* any natural-parameter merge — joint G+C+B invariant.

### Q7 — Two-phase promote (D ↔ G)
**Challenge:** Is publish-a-paper the same bit as keep-an-experiment?  
**Answer:** Name them apart. `Promote.compute` accepts harness artifacts under a frozen digest; `Promote.tip` burns a scarce tip — merge, checkpoint, robot hour, wet slot, paper claim. Runtime owns the bit and the evidence digest; humans, IRB, or clinic own tip spend. Do not smuggle claim-promote through compute-promote.

### Q8 — Capability contract vs inventory (G)
**Challenge:** Does swfactory / Airflow already do N-way fork-merge?  
**Answer:** We claim a *capability contract* — what a hill-climb runtime must expose so Search≠Authority holds — not a factory that forks today: in the recorded runs nothing forked (`serial_fallback_missing_fork`). Forkable sandboxes are the body; objective digest, reduce, and promote are the spine. Bindings differ; invariants do not.

### Q9 — \(Z_g\) misuse (B ↔ G)
**Challenge:** Is the partition function Bayesian model evidence for CI?  
**Answer:** No. \(Z_g\) and \(\Delta/2\) are diagnostics of pool volume and heterogeneity under the Gaussian product kernel — useful on the ledger, dangerous as a green-score. Prefer exposing \(\Delta\), degrees of freedom, and abstain to reviewers. Physics naming here is algebra with teeth, not a claim that sandboxes thermalize.

### Q10 — Containers vs Firecracker for agents (C)
**Challenge:** Why not stay on dense containers if EscapeBench saturates?  
**Answer:** SandboxEscapeBench shows frontier models reliably escape Docker-class misconfigs; NCSC-aligned minimum for untrusted agent bodies is a hypervisor wall. Containers remain fine as an *inner* layer with dropped caps; they are not a substitute outer wall. EscapeBench measures escape — it does not authenticate evidence into reduce.

### Q11 — HIL / robot hour as tip (D)
**Challenge:** Is Physical AI a different systems story?  
**Answer:** Same fabric, scarcer tip. Million sim forks are search; one robot hour is authority you burn once. Tip *placement* beats tip volume — CoPilot-style gates beat both full-auto flood and step-by-step paralysis. Fail day: experiment and scorekeeper share a writable machine.

### Q12 — Promote tip outside the fork fabric (A/D ↔ G)
**Challenge:** Can perfect FS+mem C/R still leak authority into workers?  
**Answer:** Pin immutable \((S_0,\mathrm{Epoch},\mathrm{obj\_digest})\) into every child; refuse tip capabilities — publish keys, wet booking, promote tokens — inside the worker even when CoW is perfect. Singular promote stays outside the fork fabric; irreversible tip I/O is record-only or capability-refused. Children may outlive parents; authority must not.

### Q13 — Is it a fork at all? (Xen, SnowFlock)
**Challenge:** SnowFlock's VM_fork cloned a running VM's memory. Your islo snapshot may be a disk archive, and your factory runs forked nothing. Why call this fork?  
**Answer:** Until Gate 0 runs, I do not. Gate 0 keeps a random 128-bit nonce in a process's RAM, takes a named snapshot, restores three children and records whether the process still runs and holds the same nonce; the code suggests a `.tar.zst` disk archive, but that is not a result, so I say "restore fan-out". My 6.87 s is a public-API round trip (restore a 141 MB snapshot, run `true`, capture), not a mechanism latency. The factory runs used Docker's sandbox and nothing forked: the work graph recorded `serial_fallback_missing_fork`, and I wrote the fork contract before I had the fork.

### Q14 — Why not boot a minimal image, or hit the build cache? (Jitsu, LightVM, OBuilder, day10)
**Challenge:** Jitsu and LightVM boot minimal VMs in milliseconds; OBuilder snapshots every build step by hash. Your H1 baseline, dependencies baked in and source fetched, is weaker than either.  
**Answer:** Slide 27 concedes both: fork loses with one child, when the state is only files and the build cache is good, and when a minimal image boots faster. In my own run the parallel steps touched disjoint files, so two worktrees would have done. Fork pays only when (N−1)P > H + N(R+D), that is, when the reached state is expensive to rebuild; H1 tests that against the cached template the pre-registration names, with cold as a reference only. If the gain comes from state a better step cache would also hold, that is a point for the cache and for open problem 5; I do not claim fork beats a good build cache.

### Q15 — Every child talks to the model: what does Remus hold? (live migration, Remus)
**Challenge:** Remus holds network output until the checkpoint commits. Every one of your children sends bytes to a hosted model. Isn't that an unheld channel out of every fork?  
**Answer:** Yes, and slide 26 says so: the model API is the one exception, metered and logged, not held, and slide 11 notes the endpoint can carry arbitrary bytes out. What is structural today is narrower: children hold no credential that can publish, and the orchestrator delivers once, after the gate (in these runs, to a local git remote). Holding effects for remote services and for people is open problem 4.

### Q16 — Host identity is not a capability (Capsicum, CHERI, macaroons)
**Challenge:** You cite Capsicum and macaroons, then propose keying the gateway on a vsock CID or a tap device. That is identity-based authority. And whatever authority sits in guest memory, a fork copies.  
**Answer:** Agreed on both. Today the cell holds a placeholder, a bearer string in guest memory, and a fork copies it: eight forks of a VM holding a token are eight live tokens. The slide-11 proposal keys on identity the host assigns rather than on a string the guest holds, and a restore bumps a generation that voids the parent's lease; that is closer to a revocable lease (Gray and Cheriton) than to a Capsicum capability, it is proposed, and leases were not exercised in these runs. A capability that is re-minted on restore, revocable and never ambient is open problem 2, one of the two I asked for help with.

### Q17 — A receipt the child cannot write (CamFlow, PASS, in-toto)
**Challenge:** Whole-system provenance runs inside the machine the child controls. Where does your receipt come from, and why trust your receipts when slide 16 shows three of them were wrong?  
**Answer:** Do not trust them because they are mine; that is slide 16: a CI job green in 3 s with every real step skipped, `approvals.json` recording `"mode": "human"`, actor `admin`, when my harness answered, and status lines mixed into stdout. The receipt has to come from outside the guest: `evaluate(artifact, verifier)` runs outside the child and returns it, and that is proposed. What is built is the gate that binds approval to the artifact's sha256 and the receipt record the reducer checks; provenance captured inside the guest is useful for audit, but it sits in the child's trust domain, so I do not count it as the receipt.

### Q18 — Isn't this just set semantics? (provenance semirings)
**Challenge:** Green et al.'s provenance semirings already separate bag from set semantics. Isn't "executions, not evidence" just set semantics over evidence IDs?  
**Answer:** For exact reuse, yes: the built reducer canonicalises evidence IDs as a set and raises on a repeated ID, and that is the only dependence it handles today. Lineage travels with the result as annotation, but nothing consumes it yet, which is why slide 36 cites Green et al. What annotation does not give is how strongly two distinct evidence IDs that share a parent, a model or a test are correlated; that is ρ, and estimating it from lineage is open problem 1.

---

## Pre-registration and statistics (C2D3)

### Q19 — ρ is not identified from one parent (clustered errors)
**Challenge:** N_eff = N/(1+(N−1)ρ) with all nine forks from one parent is one cluster, and ρ cannot be estimated from one cluster. Where does ρ come from?  
**Answer:** Not from one parent. Test 2 builds 12 snapshot families of 3 siblings, each paired with 3 restored strangers in the same slot on the same host, and estimates the intraclass correlation from them; the siblings' absolute ρ with its CI, not Δρ, is what feeds any N_eff bound. Until that has run I count by evidence identity, not by execution: four re-runs of 100 tests are 400 executions and 100 evidence IDs, and 100 is only an upper bound until ρ is measured. The formula assumes equal variances and a common pairwise correlation; estimating ρ from lineage without running everything twice is open problem 1.

### Q20 — What do 29 greens confirm? (slide 34)
**Challenge:** 29 greens only show the new code probably ran once, and re-runs from one snapshot are not independent.  
**Answer:** Right, it is a coverage bound: if the race reaches the new code in 1 run of 10, 29 independent runs all miss it with probability 0.9^29 = 0.047. "Independent" is the hard word, because re-runs from one snapshot share whatever Test 2 measures. The better fix is the one review 2 asked for: a deterministic test that drives `cell_store.activate` to raise `CellBusy`, which beats any number of greens.

### Q21 — Two different tests on slide 44 (sign-flip vs t-interval)
**Challenge:** You support H2 with a sign-flip test against zero but reject with a 90% t-interval against 0.05. Why mix them, why 90%, and does support show the excess is above 0.05?  
**Answer:** The upper bound of a two-sided 90% interval is a one-sided 95% bound, so rejection is a one-sided 5% test that the excess is at least 0.05, at the same level as the one-sided support test. Support is the weaker rule: p < 0.05 is against Δρ = 0, plus a point estimate above 0.05, so it does not show the excess exceeds 0.05. The two rules cannot both fire, because rejection forces the estimate below 0.05; anything else is inconclusive. The sign-flip p is exact over the 4,096 patterns if the 12 pair differences are independent and symmetric under the null, the t-interval is the approximation, and both were fixed in prereg-v1 before any data.

### Q22 — Why 0.05, and why 10 s?
**Challenge:** 0.05 is both your correlation margin and your α. Is the margin just the α again, and where does 10 s come from?  
**Answer:** They are unrelated numbers that happen to match. The margin is practical: an excess correlation of 0.05 from shared ancestry alone takes 9 siblings from 9 to 6.4 witnesses (9/1.4); if strangers are coupled too, the siblings' absolute ρ is what matters, and the pre-registration reports it with its CI. The 10 s margin in Test 1 is, in the pre-registration's own words, a round number fixed before any data, not derived from it.

### Q23 — Multiplicity across N, H1 and H2
**Challenge:** Test 1 supports at an unadjusted 95% at every N but rejects at a Bonferroni 98.3%. Then there are H2 and Phase C. Where is the multiplicity control?  
**Answer:** The asymmetry is deliberate. Support needs all three N to pass, an intersection-union test, which keeps its level without adjustment; rejection fires on any one N, so each N uses a 98.3% interval (0.05/3). H1 and H2 are separate hypotheses, each reported as held, failed or inconclusive, with no joint claim across them, and Phase C is descriptive, with no test. Every result is reported, including inconclusive ones and failures to finish within budget.

### Q24 — Your standard error, and autocorrelated rounds
**Challenge:** The pre-registration says a per-triple standard error of ρ of about 0.014. I get 1/√(3·300) ≈ 0.033. And 300 lockstep rounds from one cell are not 300 independent draws.  
**Answer:** You are right on the arithmetic: with independent rounds, one triple's ρ has a standard error of about 0.033 at T = 300, and 0.014 is the standard error of Δρ, the mean over 12 pairs; the pre-registration now logs that correction. No decision rule uses it. The test and the interval take the 12 pair differences as the units, so autocorrelation within a cell widens the spread of the Δρ_i and the interval with it, rather than being assumed away; the pilot only fixes T so each cell sees at least 10 of the rarer outcome.

### Q25 — Cluster labels are known by design (Kish, Liang–Zeger, Kim et al.)
**Challenge:** In cluster sampling and longitudinal studies the design writes the labels too. What is new, and isn't a shared blind spot bias rather than variance?  
**Answer:** Nothing statistical is new; slide 36 says so. What the runtime adds is where the labels live: parent, seed, test, fixture and, through the egress gateway, the model each child called are known when it forks and lost if a worker returns a bare score, which is why the receipt carries lineage. Lineage names shared factors but does not estimate their strength, and it cannot label a shared model's blind spots; for one fixed model and test that is bias, which no re-run averages away (on one leaderboard, two models that are both wrong agree 60% of the time). Parent, model and test are crossed, so the analysis needs multiway clustering, and a wild-cluster bootstrap when clusters are few.

### Q26 — The closing line over-generalises Dean and Barroso
**Challenge:** Dean and Barroso hedge latency, where the first reply is as good as any. For correctness nothing is self-certifying. Isn't the closing line a false generalisation?  
**Answer:** It is a generalisation, and I say so. Their condition is a necessary one: the techniques are effective only when the cause of variability does not tend to hit several replicas at once. For correctness you also need a check (slide 3: without one, voting and reward models plateau), and that check must itself fail independently of the attempts. So independence is necessary, not sufficient, and partial independence buys a partial gain, which is what N_eff counts.

### Q27 — Isn't the 60% just question difficulty? (Jo, Garg & Raghavan)
**Challenge:** Hard questions fool everyone. Jo, Garg and Raghavan argue much of the "excess" agreement shrinks once the baseline accounts for difficulty. Isn't the 60% an artefact?  
**Answer:** Partly, and I would not defend the excess. Their 2026 preprint, with Kim et al.'s senior author, shows the measured monoculture depends on the baseline and on which models are compared; that errors are shared stands, how much is beyond difficulty is contested. For counting witnesses the split does not matter: what N_eff charges for is total shared failure, whatever its cause. Forks that all fail the same hard tasks are still fewer witnesses. And the 60% is a conditional agreement rate (both wrong, same wrong answer, against 33% by chance), not a ρ; I never plug it into the formula.

### Q28 — Those studies compare different models; your forks are one model. Does it transfer?
**Challenge:** Kim et al., Kohli and Bone et al. all compare different models. Your forks are one agent. Why should cross-model numbers say anything about forks?  
**Answer:** They do not measure forks, and I say so: none of these papers measures forks of one agent from a shared snapshot, or multi-step agent runs. My reasoning, not a result: forks share more than different models do (same weights, same prompt, same snapshot, same tools), so I expect the cross-model figures to be a floor on how much forks share, not a ceiling. That expectation is exactly what could be wrong, which is why Test 2 measures the fork case directly: sibling coupling against strangers, the blank row on slide 4.

### Q29 — Why not use a diverse panel of judges?
**Challenge:** If one grader shares the agent's blind spots, use a panel from many vendors and vote.  
**Answer:** Diversity helps less than it looks. Kohli's 2026 preprint finds 9 frontier judges from 7 model families carry about 2.2 independent votes (Kish n_eff 2.18), with a ceiling of about 2.6 however many are added; the panel never beat the best single judge beyond noise, and when all 9 agreed they were still wrong 9.1% of the time. Goel et al. (ICML 2025) find AI judges favour models similar to themselves, beyond accuracy, so a judge from the agent's family is not neutral. Same lesson as the forks: count witnesses, not judges, and keep the hidden test outside the search.

### Q30 — Is best-of-N safe if one fork is right?
**Challenge:** With pass@k, you only need one fork to be right. Doesn't correlation stop mattering?  
**Answer:** Only if something can tell which fork is right, and even then there is a ceiling. Chen's 2026 preprint shows that any vote, router or best-of-N that returns one member's answer is capped at 1 − β, where β is the rate at which all members are wrong together, and that average pairwise correlation cannot identify β. So record per-fork pass/fail, not just the winner (a proposal, not a built field): then the all-fail rate is measured rather than inferred from a correlation, and an imperfect verifier still caps the gain (slide 3).

---

## Staging

- Prefer **Q2, Q13, Q16, Q19, Q21** if time is short: they match the current deck. Q1–Q12 come from an earlier framing (Σ_g, Z_g, Promote.tip) that the talk no longer shows. Do not quote Q3's Rebound claim or Q10's SandboxEscapeBench and NCSC claims: none is in the deck or CLAIM-FENCE.md.  
- Keep **Q9** ready if someone hears “partition function” and smells Bayes cosplay.  
- Never invent forkd/E2B/Daytona latencies in answers; quote peer tables only when forced, attributed.
