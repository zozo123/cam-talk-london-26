# Earlier modular academic draft — Cambridge SRG

This file documents an earlier 38-slide, teaching-oriented outline. The current canonical stage deck is the standalone 40-slide talk.tex; its complete speaker notes are embedded in that source. The earlier material below remains useful as background and Q&A reference, but its slide order and counts do not describe the current deck.

The concise conference cut remains talk-30min.tex plus slides/.

## Format

- **38 slides total**
- **34 core slides**
- **4 appendix / optional deep-cut slides**
- Designed for **~45 minutes of material + 15 minutes discussion**
- The first 34 slides form a complete academic narrative.
- Slides 35–38 are source/claim-fence and optional technical depth.

## Why this version exists

The 30-minute cut is a good conference-style argument. The academic version is designed to teach the whole idea from first principles to a mixed systems / ML / software-engineering audience.

It explicitly explains:

- what an agent, sandbox, snapshot, fork, rollout, verifier, authority, and evidence mean;
- reinforcement learning from state/action/reward/policy;
- model-free vs model-based RL vs learned world models;
- Dreamer / Contrastive World Models versus executable forked worlds;
- software engineering as an experimental system;
- verifiable rewards and coding RL;
- reward integrity, non-escape escapes, capabilities, credential remint;
- process/container/user-space-kernel/microVM isolation;
- warm caches, side channels, evidence ledgers;
- Git/database/OS/distributed-systems/security/statistics/science/RL analogies;
- structured Reduce, correlation, abstain, and the cold-liar failure;
- software/RL/HIL/science as the same abstract loop;
- scientific-computing / biology analogies;
- annealing / MH / SGD / RL-temperature analogies with a hard claim fence;
- the full Fork / Reduce / Promote architecture;
- open research questions.

## Six-act narrative

### Act I — Why state becomes the problem
Slides 1–6.

We begin with the motivating agent-swarm failure and the personal path:

**science:** state must be reproducible  
→ **build systems:** state should be reused  
→ **agents:** state becomes active and dangerous.

The act ends on the key separation:

> **Search can be plural. Authority must be singular.**

### Act II — Reinforcement learning and cheap futures
Slides 7–11.

We define RL accessibly, then compare:

- model-free RL,
- model-based RL,
- world models,
- executable forks.

The central inversion is:

> **World models make imagination cheap. Forkable sandboxes make interaction cheap.**

and:

> **For code, the best world model is often the world.**

The snapshot-vs-latent slide makes the relation precise: they are not identical objects, but they expose the same **state-sufficiency** question.

### Act III — Software engineering becomes an environment problem
Slides 12–17.

A coding agent’s “world” includes source, toolchain, processes, tests, credentials, network, caches, hidden verifier, and release authority.

Coding RL then becomes:

`episode = (S0, task, tools, verifier, reset)`

Verifiable rewards explain why code is unusually suitable for RL.

Then comes the core trust boundary:

> **The student cannot grade their own exam.**

followed by non-escape escapes and:

> **Copy the machine, not the keys.**

### Act IV — Operating systems, security, and durable proof
Slides 18–20.

We separate:

1. isolation wall,
2. capability / credential boundary,
3. evidence boundary.

We compare process namespaces, containers, user-space kernels, and microVMs without making a universal “containers are bad” claim.

Then:

> **Warmth is performance. Authority is a capability.**

and:

> **The runner is disposable. The proof is not.**

### Act V — Computer science translation + evidence reduction
Slides 21–24.

The same runtime idea is translated across fields:

- Git: branch / merge
- databases: transaction / commit / rollback
- distributed systems: MapReduce
- OS: fork / checkpoint
- security: capability
- statistics: correlated samples
- science: experiment / notebook
- RL: rollout / reward

This produces the API:

> **Fork → Reduce → Promote**

Then we explain why Reduce is not majority vote, why abstain is valid, and why:

> **Four clones do not make four witnesses.**

### Act VI — Cross-domain synthesis and research agenda
Slides 25–34.

Software, RL, HIL, scientific computing, and biology all instantiate:

`snapshot → fork → search → verify → reduce → promote → burn`

We use annealing only as carefully fenced schedule language.

The architecture blueprint then assembles the full system.

We close with:

- epoch fencing and stale-result rejection,
- falsifiable evaluation methodology,
- failure-mode checklist,
- “what this is not,”
- Cambridge research agenda,
- five takeaways.

## Core slide list

1. Forkable Sandboxes — title / thesis.
2. The whole talk in one picture.
3. Motivating failure: 100 agents, one laptop.
4. Why I ended up here.
5. Glossary: terms we will use carefully.
6. Search can be plural. Authority must be singular.
7. Reinforcement learning, in one slide.
8. Model-free, model-based, and world-model RL.
9. There are two ways to make futures cheap.
10. For code, the best world model is often the world.
11. Snapshot versus latent: the sufficiency question.
12. Software engineering view: what is the world?
13. Coding RL turns reset into a training primitive.
14. Why verifiable rewards matter.
15. The student cannot grade their own exam.
16. Non-escape escapes.
17. What actually has to fork?
18. Operating systems view: isolation layers.
19. Warmth is performance. Authority is a capability.
20. Evidence must outlive the child.
21. Computer science translation dictionary.
22. Fork, Reduce, Promote: the capability contract.
23. Reduce is not majority vote.
24. Four clones do not make four witnesses.
25. Three factories. Same loop.
26. Scientific computing and biology fit the same shape.
27. Search dynamics: annealing, without mysticism.
28. Architecture blueprint.
29. Epochs and fencing make promotion linearizable.
30. A research claim needs a benchmark, not a slogan.
31. Failure mode checklist.
32. What this is not.
33. Research agenda for Cambridge SRG.
34. Takeaways.

## Appendix / optional deep cuts

35. Selected sources / claim fence.
36. World models plus forks, not either/or.
37. Minimal API shape.
38. Why the title says “factory.”

## Suggested pacing — 45 minutes

- Slides 1–6: 7 minutes
- Slides 7–11: 8 minutes
- Slides 12–17: 8 minutes
- Slides 18–20: 5 minutes
- Slides 21–24: 6 minutes
- Slides 25–34: 13 minutes

The exact order can be shortened without breaking the story because every act has an explicit transition.

## Suggested 30-minute cut

Use the preserved `talk-30min.tex` for a polished short version.

If cutting the full academic deck live, keep:
1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 17, 20, 21, 22, 24, 25, 28, 29, 30, 33, 34.

## Accessibility rules used in the deck

1. Define terms before compressing them.
2. Show one abstraction per slide.
3. Give each abstraction a software example.
4. Translate the same idea across CS / RL / science.
5. Separate analogy from identity.
6. Separate mechanism from authority.
7. Keep claims fenced where the literature is incomplete.
8. Return repeatedly to the same simple loop.
9. Make correctness properties explicit: stale work is fenced, promotion linearizes once.
10. Make the central systems thesis falsifiable with an explicit benchmark matrix.

## Main stage lines

- “We call this a swarm. The operating system calls it roommates.”
- “Search can be plural. Authority must be singular.”
- “World models make imagination cheap. Forkable sandboxes make interaction cheap.”
- “For code, the best world model is often the world.”
- “Code is trainable because the world can answer back.”
- “The student cannot grade their own exam.”
- “Copy the machine, not the keys.”
- “The runner is disposable. The proof is not.”
- “Four clones do not make four witnesses.”
- “Search may be stochastic. Authority may not be ambient.”
- “Burn the runner. Keep the proof. Fork the machine, not the trust.”
