# Concise deck — Cambridge SRG · 30-minute version

`talk-30min.tex` + `slides/` are the source of truth for this concise cut. The canonical full academic deck is `talk.tex` + `academic/`; see `FULL-ACADEMIC.md`. Research depth stays in `OUTLINE.md`, `DECK-BEATS.md`, `scratch/`, `swarm/`, `QA-BANK.md`, `CLAIM-FENCE.md`, and `WORLD-MODELS-BRIDGE.md`.

## The 13-slide stage path

1. **Forkable Sandboxes** — title, affiliations (Incredibuild / islo.dev + HIT), mantra.
2. **100 agents. One laptop. What could possibly go wrong?** — funny cold open; shared state/credentials/tests create correlated chaos.
3. **Why I ended up here** — computational science → production ML/build reuse → coding agents; state changes from optimization target to trust boundary.
4. **Search can be plural. Authority must be singular.** — patches/rollouts/sim are cheap; merge/checkpoint/robot hour is scarce.
5. **There are two ways to make futures cheap.** — learned world (Dreamer / Contrastive World Models) versus forked executable world; imagination cost versus interaction cost.
6. **For code, the best world model is often the world.** — executable counterfactuals from one snapshot; same past, different interventions, actual software transitions inside the captured boundary.
7. **A fork should copy state, not authority.** — copy state, share heat carefully, remint credentials/network identity, keep verifier/promote outside.
8. **Coding RL turns reset into a training primitive.** — episode = S0 + task + tools + verifier + reset; cold provisioning versus fork/reset.
9. **The student cannot grade their own exam.** — RUN ≠ EVAL; sealed oracle / reward integrity.
10. **Four clones do not make four witnesses.** — fork ≠ statistical independence; evidence needs lineage/precision; cold-liar failure mode.
11. **Three factories. Same loop.** — software, RL training, HIL/science as one runtime contract with different scarce tips.
12. **Fork / Reduce / Promote.** — capability contract; durable intent, disposable execution, singular authority, deterministic convergence.
13. **What I want from this room.** — executable-state boundary, model-vs-world crossover, correlation, authority inheritance; mantra close.
14. **Appendix only.** — selected sources and Q&A claim fence.

## Timing: 27–28 minutes + 2–3 minutes slack

- 0:00–0:45 — title + one-sentence promise.
- 0:45–2:30 — 100-agents cold open.
- 2:30–4:30 — personal path into the problem.
- 4:30–6:30 — Search vs Authority / scarcity ladder.
- 6:30–9:30 — learned-world vs executable-world inversion.
- 9:30–12:00 — executable counterfactuals / fork API.
- 12:00–14:30 — what crosses the fork boundary.
- 14:30–17:15 — coding-RL reset.
- 17:15–19:15 — sealed oracle / reward integrity.
- 19:15–21:30 — fork ≠ independence.
- 21:30–23:00 — three factories.
- 23:00–25:00 — Fork / Reduce / Promote.
- 25:00–27:30 — open problems + close.
- 27:30–30:00 — buffer / interruption / first question.

## The central intellectual arc

The talk is about **state** and **cheap futures**:

1. Science taught me that state must be reproducible.
2. Build systems taught me that state should be reused.
3. Agents made reused state a trust problem.
4. World models show one way to make futures cheap: learn approximate dynamics.
5. Forkable runtimes show the systems dual: make executable dynamics cheap enough to branch directly.
6. Once worlds are cheap, evidence and authority become the scarce resources.

The CWM bridge is not a side analogy. It is the elevation of the talk:

> **World models make imagination cheap. Forkable sandboxes make interaction cheap.**

and, for executable software worlds:

> **For code, the best world model is often the world.**

## Why the wording is claim-safe

Do **not** say forks eliminate all simulation or all model error. The precise claim is:

- A learned world model approximates environment transitions.
- A fork runs the actual program/environment transition **inside the executable state/capability boundary captured by the sandbox**.
- Therefore it avoids *learned transition-model error* inside that boundary.
- External services, hardware, wall-clock behavior, nondeterminism, hidden production state, and incomplete tests may remain outside the captured world.

Likewise, do not call a snapshot a minimal latent. It is the opposite trade-off: explicit, usually overcomplete, and executable. Both world models and snapshot systems nevertheless ask a sufficiency question: **what state must survive for the future to continue correctly?**

## Stage lines

- “We call this a swarm. The operating system calls it roommates.”
- “World models make imagination cheap. Forkable sandboxes make interaction cheap.”
- “For code, the best world model is often the world.”
- “Copy the machine, not the keys.”
- “The student cannot grade their own exam.”
- “Four clones do not make four witnesses.”
- “Fork makes search cheap. It does not manufacture evidence.”

## Hard cut rule

If behind at minute 20:

- compress slide 11 (three factories) to 35 seconds,
- state the three verbs on slide 12 without re-explaining earlier examples,
- never cut slides 5, 6, 8, 9, 10, or the closing question slide.

## Stage claim fence

- Say: forkable environments are a capability contract for controlled search and resettable coding-RL episodes.
- Say: world models and forked runtimes reduce different costs — imagination versus executable interaction.
- Say: a fork gives actual software transitions inside its captured boundary, not learned-transition predictions.
- Do not say: reality is *always* cheaper than a learned model.
- Do not say: no sim-to-real gap exists for external systems/hardware not represented by the sandbox.
- Do not say: a snapshot is a minimal learned latent.
- Do not say: fork implies independent evidence.
- Do not claim Gibbs equilibrium / detailed balance for the factory.
- Do not let worker-owned state define the verifier, schedule, confidence or promote bit.
