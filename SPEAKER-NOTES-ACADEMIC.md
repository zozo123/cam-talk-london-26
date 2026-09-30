> Superseded: the canonical talk is `talk.tex` (33 main slides, 15 Oct 2026). These notes follow the earlier 38-slide draft in `academic/`; the notes for `talk.tex` are embedded in it and rendered in `PRESENTER-GUIDE.md`.

# Speaker notes — Full academic Cambridge talk

Target: **~45 minutes content + 15 minutes discussion**.

The deck should feel like a guided tour from first principles into a systems research agenda. Do not assume the audience knows reinforcement learning terminology, and do not assume the ML audience knows OS/security terminology.

The repeating structure is:

**define → motivate → show mechanism → show analogy → state boundary → state limitation.**

---

## Slides 1–2 — Thesis and map

Open:

> “I want to connect three worlds that are usually discussed separately: software engineering, reinforcement learning, and systems isolation.”

Then:

> “The recurring object is state. Science wants state reproducible. Build systems want state reusable. Agents make state active. World models learn futures from state. Forkable runtimes execute futures from state.”

The promise:

> “By the end, I want Fork / Reduce / Promote to feel like one coherent runtime contract rather than three unrelated features.”

---

## Slides 3–6 — The motivating systems problem

Slide 3:

> “We call this a swarm. The operating system calls it roommates.”

The joke is useful because the failure is intuitive: shared workspace, processes, tests, credentials, cache, and network.

Make one distinction:

- **parallel execution** means things happen concurrently;
- **independent experiments** means one attempt cannot contaminate or silently correlate another.

Slide 4 is the personal causal path, not biography.

Slide 5 is there to slow the talk down and define language. Do not rush it. The rest of the deck becomes much easier if the audience shares the terms.

Slide 6:

> “Search wants abundance. Authority wants scarcity.”

Explain that authority need not mean “human.” It means the narrow trusted path by which search changes durable state.

---

## Slides 7–11 — Reinforcement learning and world models

### Slide 7 — RL in one slide

Define:

- state $s_t$: what the agent knows about the current world,
- policy $pi$: rule for choosing actions,
- action $a_t$: intervention,
- environment: what evolves in response,
- reward $r_t$: feedback,
- rollout: a sequence of interactions.

Do not teach all of RL. The only purpose is to make later terms legible.

### Slide 8 — Three RL perspectives + executable forks

Model-free:
> “Learn from interaction without explicitly learning the world dynamics.”

Model-based:
> “Learn a transition model, then use it to reason about futures.”

World model:
> “Learn a compressed predictive state from rich observations.”

Forked executable world:
> “If the environment itself is software, sometimes I can execute the transition instead of learning it.”

Main question:

> “Which future is cheaper to trust?”

### Slide 9 — Dreamer / Contrastive World Models bridge

Say:

> “World models make imagination cheap. They trade interaction cost for approximation.”

For Contrastive World Models:

> “The representation should keep what predicts the future, not spend all its capacity reconstructing nuisance detail.”

Then pivot:

> “Software gives us another systems knob: reduce interaction cost itself.”

### Slide 10 — Executable counterfactuals

Point to the branches.

> “From one authenticated past, I can apply different interventions and observe different executable futures.”

Use the phrase **executable counterfactual**, but qualify it:

> “This is exact only for the software state and capabilities we actually captured. External services, clocks, GPUs, nondeterminism, or hidden production state can remain outside the boundary.”

### Slide 11 — Snapshot vs latent

This is an important precision slide.

Do not say the snapshot “is” the latent.

Say:

> “They answer related sufficiency questions with opposite engineering trade-offs. A latent is compressed and learned. A snapshot is explicit and usually overcomplete. One predicts; one resumes.”

---

## Slides 12–17 — Software engineering, RL environments, and security

### Slide 12 — What is the software world?

Make the audience notice that a repository alone is not an environment.

> “The world includes the repo, but also dependencies, compiler, processes, cache, tests, credentials, network, generated files, and authority.”

Then:

> “Software engineering begins to look like experimental science: patch as hypothesis, CI as oracle, merge as a claim.”

### Slide 13 — Reset as a training primitive

Point to:

`episode = (S0, task, tools, verifier, reset)`

Explain why reset belongs in the episode definition:

- hidden prior state changes the task;
- prior rollout residue contaminates training;
- a reward is only comparable if the experiment starts from a known state.

Do not quote universal speedups.

### Slide 14 — Verifiable reward

This slide explains why coding RL is special.

> “The world can answer back.”

Tests, type checks, benchmarks, linters, and hidden evals can create machine-checkable feedback.

Mention limitation:

> “Tests are not truth. They are an oracle with coverage and integrity assumptions.”

### Slide 15 — Student cannot grade own exam

Pause.

> “The student cannot grade their own exam.”

Then:

> “RUN is not EVAL.”

The worker may execute; the worker should not own hidden reward logic or the promotion key.

### Slide 16 — Non-escape escapes

Explain that “sandbox escaped” is too narrow a security question.

An agent can defeat the experiment without escaping the kernel boundary:
- inherited credential,
- writable mount,
- allowed exfiltration,
- verifier tampering.

### Slide 17 — Copy the machine, not the keys

This is the capability boundary.

Four verbs:
- copy,
- share carefully,
- remint,
- keep outside.

---

## Slides 18–20 — Operating systems and durable evidence

### Slide 18 — Isolation layers

Avoid absolutism.

> “There is no universal answer called ‘container bad, VM good.’ The boundary depends on threat model, compatibility, density, and capabilities.”

The key point:

> “Even a perfect VM wall does not automatically solve credential inheritance or verifier ownership.”

### Slide 19 — Warmth

Explain build/cache pressure.

> “A useful factory wants heat: compiled dependencies, package caches, immutable images, CAS artifacts.”

But:

> “Warmth can become a wire.”

Shared mutable caches, cross-tenant pages, and secret residue can become information channels.

### Slide 20 — Evidence

> “Burn the runner. Keep the proof.”

Explain durable evidence:
- logs,
- artifact hashes,
- objective digest,
- snapshot identity,
- lineage,
- method,
- evaluator result.

---

## Slides 21–24 — Computer science analogies and reduction

### Slide 21 — Translation dictionary

This slide is deliberately broad. Walk through only four examples unless asked.

Suggested:
- Git branch / merge,
- DB transaction / rollback,
- OS fork / checkpoint,
- statistics correlated samples.

Say:

> “These are not identical systems. The value is that each field already has a vocabulary for one part of the problem.”

### Slide 22 — Fork / Reduce / Promote

This is the named abstraction.

Fork:
> “Make worlds cheap.”

Reduce:
> “Make evidence honest.”

Promote:
> “Spend authority once.”

### Slide 23 — Reduce is not majority vote

A green score is not enough.

Structured evidence must include enough metadata to know:
- what was evaluated,
- against which objective,
- from which parent,
- with what method.

Explain `abstain`:

> “Sometimes the most correct reducer output is: I cannot honestly narrow this yet.”

### Slide 24 — Four clones ≠ four witnesses

Explain correlation by shared ancestry.

> “Execution isolation prevents direct contamination. It does not erase shared prompt, model, snapshot root, cache, hidden fixture, or systematic error.”

Cold liar:

> “If one worker can mint arbitrarily high confidence, it can hijack the pool.”

---

## Slides 25–27 — Cross-domain views

### Slide 25 — Same loop

Repeat slowly:

`snapshot → fork → search → verify → reduce → promote → burn`

Software:
patch → tests → merge.

RL:
trajectory → verifier → checkpoint.

HIL/science:
hypothesis → measurement → physical/scientific claim.

### Slide 26 — Scientific computing / biology

This is where the user’s scientific background becomes useful without turning into biography.

> “Expensive oracles make cheap safe branching even more valuable.”

Examples:
- sequence candidates before wet-lab assay,
- simulation parameters before a large production run,
- pipeline variants before publication.

### Slide 27 — Annealing analogy

Keep this disciplined.

> “I am using annealing as schedule language: explore broadly early, become selective later.”

Do not claim equilibrium thermodynamics.

If the audience is not interested, this slide can be cut with no loss.

---

## Slides 28–34 — Architecture and conclusion

### Slide 28 — Architecture blueprint

This is the end-to-end system.

Trace:
Objective digest → Snapshot → Fork → Run → Verifier → Reduce → Promote → Ledger → next objective/state.

Main sentence:

> “The child executes. The controller decides.”

### Slide 29 — Epochs and fencing

This is the distributed-systems correctness slide.

Define an **epoch** as the frozen experiment contract: objective digest, trusted parent snapshot, verifier identity, and schedule/policy.

> “A child is evidence for the epoch that created it — and nothing else.”

If any trusted part changes, increment the epoch. Old children may finish, but they are stale for promotion.

Then:

> “Search can race. Promotion must not.”

The important systems property is a single promotion linearization point guarded by the current epoch.

### Slide 30 — Evaluation methodology

This is where the talk becomes falsifiable.

> “A research claim needs a benchmark, not a slogan.”

Walk across the measurement families:
- latency/throughput,
- memory/storage/write amplification,
- reset fidelity,
- leakage and authority violations,
- evidence correlation/effective sample size,
- task success or validated candidates per hour.

The baseline ladder is:
cold build → cached container → snapshot restore → snapshot fork → learned proposal + fork validation.

Do not quote universal numbers before running this benchmark.

### Slide 31 — Failure checklist

Treat this as a design review checklist.

Ask:
- Can attempts contaminate each other?
- Does a child possess promotion credentials?
- Is the evaluator writable?
- Is evidence durable?
- Are correlated siblings overcounted?
- Can warmth become a channel?

### Slide 32 — What this is not

This protects the research claim.

The audience should leave knowing what you are **not** claiming.

### Slide 33 — Cambridge research agenda

Spend time here.

The strongest questions:

1. What exactly is a first-class executable state?
2. Where is the crossover between learned imagination and forked interaction?
3. How should shared ancestry affect reduction?
4. How should capability inheritance work on fork?
5. Where can warm state exist without becoming a wire?

### Slide 34 — Takeaways

Do not add a second conclusion after this.

End:

> “The runner is disposable. The proof is durable.”

Then:

> “Burn the runner. Keep the proof. Fork the machine, not the trust.”

---

# Appendix slides

## Slide 35 — Sources / claim fence

Use for citation questions and to recover from an overclaim.

## Slide 36 — Hybrid world models + forks

Key answer if asked “why not use both?”:

> “Exactly. Use imagination for breadth and executable forks for grounding.”

## Slide 37 — Minimal API

Useful for systems/API questions.

## Slide 38 — Why factory?

Explain:

> “A factory is a controlled path from disposable motion to durable matter.”

---

# Cut strategies

## 30 minutes

Use `talk-30min.tex`.

## 40 minutes

From the full deck, cut:
- slide 5 glossary if audience is expert,
- slide 11 snapshot-vs-latent,
- slide 19 warmth,
- slide 26 science/biology,
- slide 27 annealing,
- slide 31 checklist.

## 60 minutes

Use all 34 core slides and allow discussion during slides 11, 18, 24, 29, 30, and 33.

---

# Q&A anchors

## “Is this just checkpoint/restore?”

No. Checkpoint/restore is a mechanism for state. The contract also includes credentials, verifier ownership, evidence lineage, reduction, and promotion authority.

## “Is this just VMs?”

No. VM/microVM is one isolation mechanism. The talk is about the environment contract around it.

## “Why not world models?”

Use both when useful. A learned model can propose/prune; executable forks can ground candidate futures.

## “Does fork give independent samples?”

No. Shared ancestry can create correlated evidence.

## “Are tests truth?”

No. Tests are a verifier with coverage, integrity, and provenance assumptions.

## “How much faster is reset?”

Do not invent a universal multiplier. Compare cold build, cached container restart, snapshot restore, and fork under the same repo/task/verifier benchmark.


## “What prevents a stale child from winning later?”

Epoch fencing. Every child is bound to the objective/verifier/snapshot epoch that created it. Changing trusted experiment state increments the epoch; old children may finish but cannot promote.

## “How would you prove this architecture is better?”

Run the same repo/task/verifier workload across cold build, cached container restart, snapshot restore, snapshot fork, and hybrid model-propose/fork-validate. Measure cost, fidelity, isolation, effective evidence, and validated task throughput.
