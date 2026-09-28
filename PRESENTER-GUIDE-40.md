# Presenter guide: Cambridge SRG, 15 October 2026

The canonical deck is [`talk.tex`](talk.tex): **40 slides, about 48 minutes of talk and 12 minutes for discussion**. Each frame contains a `\note{...}` paragraph with its speaking point. The compiled slides hide those notes. This guide gives the pacing and claim boundaries for a live delivery.

| Slides | Time | Story to tell |
|---|---:|---|
| 1–5 | 5 min | Define the software factory as a search loop. Ask what eight forked parser trials actually duplicate, then state the conditional hypothesis, current evidence, and workload contract. |
| 6–14 | 11 min | Define environment, sandbox, reset, continuation state, and observational fidelity. Use the parser patch to explain what a fork can reuse and what each candidate must rebuild. Derive the break-even condition. |
| 15–23 | 11 min | Compare branch mechanisms and their isolation/cost tradeoffs. Show the proposed controller–snapshot–worker–evaluator–gate architecture and walk the parser campaign through its API-shaped operations. |
| 24–30 | 8 min | Show hill climbing, genetic search, automated research, and coding RL as search procedures that consume executable branches. Keep evaluator authority separate. Use simulation and biology to show where the sandbox boundary ends. |
| 31–37 | 9 min | Explain shared error and the 100-test retry example. Introduce the worker receipt and reducer assumptions. Present the synthetic checks and one named-snapshot integration trace with their actual scope. Close with the promotion gate. |
| 38–40 | 4 min | Propose the controlled benchmark, state the research questions, and finish on the distinction between exploring futures and certifying them. |

Opening line: “Suppose eight agents propose fixes for one parser failure. We can clone the prepared machine eight times. Have we also cloned the experiment, the evidence, or the right to accept a fix?”

Core claim: **When alternatives share an expensive, valid prefix, a forkable runtime may lower full-workload search cost. Its API must also specify continuation fidelity, external effects, evidence lineage, and promotion authority.**

Three questions carry the talk: **What state did the fork preserve? What does each result count as? Who may promote it?** Return to the same parser experiment at the branch lifecycle (12), work-cost model (14), architecture and API (22–23), sealed evaluation (28), evidence-ID example (32), and gate (37).

Keep four boundaries explicit on stage:

1. **Environment vs. sandbox.** An environment defines observations, actions, feedback, and termination. A sandbox captures and isolates some of its executable state.
2. **Measured vs. proposed.** DeltaBox and Shepherd numbers belong to their authors and setups. The cost model and runtime contract are hypotheses to test. The evidence-aware reducer has synthetic checks and one four-worker integration trace, without a controlled speedup baseline.
3. **Execution vs. evidence.** A fork can isolate a process while its result still shares data, model error, fixture error, or selection history with its siblings.
4. **Simulation vs. world.** A software simulator may be forked; a robot, remote service, or biological assay is outside the local snapshot unless a separate mechanism controls it.

Closing line: “Fork the machine. Keep the evidence. Promote through one explicit gate.” Invite the Cambridge systems audience to challenge the continuation boundary, the dependence model, and the placement of shared warm state.
