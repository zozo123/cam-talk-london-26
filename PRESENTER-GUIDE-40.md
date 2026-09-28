# Presenter guide: Cambridge SRG, 15 October 2026

The canonical deck is [`talk.tex`](talk.tex): **40 slides, about 48 minutes of talk and 12 minutes for discussion**. Each frame contains a `\note{...}` paragraph with its speaking point. The compiled slides hide those notes. This guide gives the pacing and claim boundaries for a live delivery.

| Slides | Time | Story to tell |
|---|---:|---|
| 1–5 | 5 min | Agents execute software. State interference makes parallel search hard to interpret. State the conditional systems hypothesis and the workload contract. |
| 6–14 | 11 min | Define environment, sandbox, reset, continuation state, and observational fidelity. Use the parser patch to explain what a fork can reuse and what each candidate must rebuild. Derive the break-even condition. |
| 15–23 | 11 min | Compare worktrees, process/container/VM mechanisms, and reversible traces. Discuss isolation, copy-on-write divergence, secrets, warm caches, crash recovery, and the fork–run–reduce–promote contract. |
| 24–30 | 8 min | Show hill climbing, genetic search, automated research, and coding RL as search procedures that consume executable branches. Keep evaluator authority separate. Use simulation and biology to show where the sandbox boundary ends. |
| 31–37 | 9 min | Explain why branches do not imply independent evidence. Introduce the worker receipt and reducer assumptions. Present the synthetic checks and the one named-snapshot integration trace with their actual scope. Close with the promotion gate. |
| 38–40 | 4 min | Propose the controlled benchmark, state the research questions, and finish on the distinction between exploring futures and certifying them. |

Opening line: “Agents now change a computational world, run it, and learn from the result. That makes the state of the computer part of the search problem.”

Core claim: **When alternatives share an expensive, valid prefix, a forkable runtime may lower full-workload search cost. Its API must also specify continuation fidelity, external effects, evidence lineage, and promotion authority.**

Keep four boundaries explicit on stage:

1. **Environment vs. sandbox.** An environment defines observations, actions, feedback, and termination. A sandbox captures and isolates some of its executable state.
2. **Measured vs. proposed.** DeltaBox and Shepherd numbers belong to their authors and setups. The cost model and runtime contract are hypotheses to test. The evidence-aware reducer has synthetic checks and one four-worker integration trace, without a controlled speedup baseline.
3. **Execution vs. evidence.** A fork can isolate a process while its result still shares data, model error, fixture error, or selection history with its siblings.
4. **Simulation vs. world.** A software simulator may be forked; a robot, remote service, or biological assay is outside the local snapshot unless a separate mechanism controls it.

Closing line: “Fork the machine. Keep the evidence. Promote through one explicit gate.” Invite the Cambridge systems audience to challenge the continuation boundary, the dependence model, and the placement of shared warm state.
