# Final deck — Cambridge SRG · 30-minute version

`talk.tex` is the stage source of truth. Research depth stays in `OUTLINE.md`, `DECK-BEATS.md`, `scratch/`, `swarm/`, `QA-BANK.md`, and `CLAIM-FENCE.md`.

## The 13-slide stage path

1. **Forkable Sandboxes** — title, affiliations (Incredibuild / islo.dev + HIT), mantra.
2. **100 agents. One laptop. What could possibly go wrong?** — funny cold open; shared state/credentials/tests make fake parallelism.
3. **Why I ended up here** — computational science → production ML/build reuse → coding agents; state changes from optimization to trust boundary.
4. **Search can be plural. Authority must be singular.** — patches/rollouts/sim are cheap; merge/checkpoint/robot hour is scarce.
5. **The primitive is a machine you can fork** — S0 → fork N → run → reduce → promote once → burn; DeltaBox/Shepherd/Firecracker as related systems.
6. **What actually has to fork?** — state, speed, authority, evidence; copy enough state to resume, not enough authority to become dangerous.
7. **Coding RL turns reset into a training primitive** — episode = S0 + task + tools + verifier + reset; cold provisioning versus fork/reset.
8. **The student cannot grade their own exam** — RUN ≠ EVAL; sealed oracle / reward integrity.
9. **Copy the machine, not the keys** — credentials remint, explicit network capability, warm caches beside trust boundary.
10. **Four clones do not make four witnesses** — fork ≠ independence; evidence needs lineage/precision; cold-liar failure mode.
11. **Three factories. Same loop.** — software, RL training, HIL/science as the same runtime contract with different scarce tips.
12. **Fork / Reduce / Promote** — capability contract; durable intent, disposable execution, singular authority, deterministic convergence.
13. **What I want from this room** — four research questions + mantra close.
14. **Appendix only** — selected sources and Q&A claim fence.

## Timing: 27 minutes + 3 minutes slack

- 0:00–1:00 — title + one-sentence promise.
- 1:00–3:00 — 100-agents cold open.
- 3:00–5:00 — personal path into the problem.
- 5:00–7:00 — Search vs Authority / scarcity ladder.
- 7:00–10:00 — forkable-machine API.
- 10:00–13:00 — what actually has to fork.
- 13:00–16:00 — coding-RL reset.
- 16:00–18:30 — sealed oracle / reward integrity.
- 18:30–21:00 — credentials + warm state.
- 21:00–23:30 — fork ≠ independence.
- 23:30–25:00 — three factories.
- 25:00–26:30 — Fork / Reduce / Promote.
- 26:30–28:30 — open problems + close.
- 28:30–30:00 — buffer / one audience question / transition.

## Why this version is more fun

- Starts with a relatable failure, not a taxonomy.
- Every technical section has a stage line:
  - “We call this a swarm. The operating system calls it roommates.”
  - “The student cannot grade their own exam.”
  - “Copy the machine, not the keys.”
  - “Four clones do not make four witnesses.”
- One equation total, on the RL episode slide.
- Statistical mechanics moved to Q&A; no annealing detour in the core 30 minutes.
- Literature is evidence for the story, not the story itself.

## Stage claim fence

- Say: forkable environments are a capability contract for controlled search and resettable coding-RL episodes.
- Say: verifier integrity, credentials, lineage, reset fidelity and isolation are separable properties.
- Do not claim universal setup bottlenecks or universal speedups without benchmark evidence.
- Do not claim fork implies independent evidence.
- Do not claim Gibbs equilibrium / detailed balance for the factory.
- Do not let worker-owned state define the verifier, schedule, confidence or promote bit.
