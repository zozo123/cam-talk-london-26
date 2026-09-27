# Topic map — Cambridge SRG talk repo

This is the repo-wide map for Forkable Sandboxes: The Runtime Layer for AI Software Factories. It separates the final stage story from research depth and Q&A material.

## A. Final talk spine

1. Personal path into the problem — reproducible computational science → production ML/build reuse → coding agents; reusable state becomes both optimization and trust boundary.
2. Forkable sandbox thesis — cheap forked machines for search; authority stays outside them.
3. Search ≠ Authority — worker ≠ judge ≠ promote; durable intent, disposable execution, singular authority, deterministic convergence.
4. Scarcity ladder — cheap/plural search versus scarce/singular tips: merge, checkpoint, robot hour, wet-lab/human slot.
5. Universal hill-climb — propose → isolate → measure → keep/revert → promote once.
6. Execution contract — filesystem state, network/credentials, reproducibility, fast cloning, build/test/rollout, recovery/observability.
7. Fork / Reduce / Promote — the named capability contract for a controlled software/research factory.
8. Open problems — correlation, credential leases, warm-state channels, sealed oracles, world diff, promote-once semantics.

## B. Forkable execution systems

9. Firecracker-class isolation — microVM pedigree, density/isolation trade-offs, outer escape wall.
10. Checkpoint / restore and CoW — machine snapshots, memory/process/filesystem state, restore semantics.
11. DeltaBox / Crab / Shepherd — checkpoint/rollback research, semantics-aware checkpointing, reversible agent traces.
12. Fork as a first-class API — supervisor holds/replays/reverts machine trajectories rather than only text transcripts.
13. Parallel worlds — one shared past S0, many divergent child futures, world selection at promotion.
14. World diff — machine-level analogue of Git diff: filesystem + process + side effects + evidence lineage.
15. Next-generation sandbox substrate — what comes after today’s Firecracker-shaped stack.
16. Sandbox layers / Monty — execution-layer taxonomy and Pydantic Monty-related sandboxing ideas.
17. Tensorlake / fork fabric practice — operational fork fabrics and how an API maps onto real runtimes.

## C. Agent factories and training environments

18. Software factory Cells + Epochs — isolated attempts, frozen objectives, retries, budgets, evidence, singular promotion.
19. Agent swarm / pstack discipline — fearless parallelism only when each arm gets its own verifiable body; one change, one measurement, keep/revert.
20. OpenClaw loop — agent as searcher; sandbox as body; tools/sessions as execution surface.
21. Airflow / swfactory control plane — orchestration, Cell identity, epoch fencing, evidence and promotion.
22. Coding RL / RLVR environments — repo + task + tools + executable verifier + known start state + reset.
23. Reset as a training primitive — prepare/build once → snapshot → fork per rollout → discard child → preserve evidence/lineage.
24. Training-environment landscape — SWE-smith, Meta CWM, Scale RL Environments, Surge AI, Mercor, Prime Intellect Environments Hub.
25. Environment maintenance / rot — dependency drift, broken builds, repo evolution, verifier maintenance.
26. Training-grade reward integrity — worker cannot read/modify reward logic; reset must return to an authenticated S0.

## D. Oracle, reward and security boundary

27. Oracle outside the fork — RUN ≠ EVAL; child output is evidence, not authority.
28. Reward hacking / verifier tampering — tests, score files, reward scripts, hidden fixtures and telemetry as attack surfaces.
29. Rebound → Remedy / SpecBench / SWE-bench context — why coding agents need sealed evaluation boundaries.
30. Sandbox escape vs non-escape escape — inherited credentials, mounts, exfiltration and verifier tampering can defeat the system without kernel escape.
31. Acceptance boundary — trusted controller validates evidence and owns the final promote bit.

## E. Credentials, networking and warm state

32. WIRE capability model — networking and credentials are explicit capabilities, not ambient inheritance.
33. Credential leases — short-lived opaque handles, remint on fork, revoke on burn.
34. Secret inheritance — why CoW should copy process state but not production authority.
35. Warm CoW / cache sharing — compile heat, artifacts and shared pages versus isolation.
36. Side channels — timing/storage channels, KSM/cross-tenant pages, pack-by-trust policy.
37. Factory beside the fork — CAS/cache/build service can be warm while the child trust domain stays disposable.

## F. Reduce, evidence and statistical-physics lens

38. Evidence-Aware / Boltzmann MapReduce — worker records carry estimate, precision/sample size, evidence IDs and lineage.
39. Fork ≠ independence — shared roots create correlation; N cheap siblings are not N independent confirmations.
40. Cold-liar problem — forged precision/sample size can hijack a reduce; isolation does not authenticate n.
41. Abstain as a first-class verdict — digest mismatch, unresolved correlation or provenance gaps should withhold promotion.
42. Precision-weighted pooling — β ≡ n in the Gaussian/LAN interpretation; structured reduce rather than naked majority vote.
43. Path-integral / parallel-world interpretation — fan-out over trajectories and evidence reduction; analogy, not physical Gibbs claim.
44. β / Z / free-energy language — restricted algebraic interpretation with explicit claim fences.

## G. Search dynamics

45. Simulated annealing — hot exploration → cooling schedule → singular tip.
46. Metropolis-Hastings analogy — proposal in child; keep=accept, revert=reject.
47. SGD / Langevin analogy — local noisy ascent; schedule/noise outside worker authority.
48. RL temperature / KL — exploration temperature as controller/Epoch policy.
49. Driven / open / non-equilibrium system — proposals inject entropy; evaluation/reduction dissipates; promotion is an absorbing sink.
50. Hamiltonian / proposal generator — H as search proposal language only, not a closed-mechanics claim.
51. NESS framing — steady fork/run/burn throughput is not thermodynamic equilibrium.

## H. Beyond software

52. RL post-training factory — rollouts/preferences → sealed reward/evidence → checkpoint promotion.
53. HIL / physical AI — simulation fan-out before scarce robot/human time.
54. Computational biology — sequence/pipeline/assay proposals; expensive/noisy oracle; wet-lab tip.
55. Simulation science — mesh/timestep/parameter search with conservation/residual oracles.
56. Auto-research — hypothesis + experiment scripts under frozen evaluation; paper/claim as singular promotion.
57. Factory of factories — outer loop can evolve the harness, but only under a frozen higher-level objective.

## I. Theory ↔ practice / landscape

58. Split/merge algorithms and frameworks — fork-join, MapReduce, speculative execution and related patterns.
59. Books and papers bridge — systems, statistical mechanics, RL/search and distributed-systems concepts mapped to runtime design.
60. Frontier-lab landscape — DeepSeek / OpenAI / Anthropic research directions relevant to agent training and environments.
61. Solution levels 0–10 — catalog from lightweight process/container approaches through full fork/reduce/promote systems.
62. Papers and sources — ranked MAIN / BACKUP / DO-NOT-USE bibliography and number/claim fences.
63. Five-domain analogies — software engineering, CS theory, biology, physics and deep learning analogies for each talk beat.

## J. Stagecraft / repo support material

64. Timed outline (45 + 15) — minute map, cut priorities and systems-vs-physics language budget.
65. Deck beats — slide intent, spoken cue, citation budget and must-hit diagrams.
66. Speaker notes — especially Act II and physics transition.
67. Q&A bank — likely SRG objections: independence, latency, credentials, reward hacking, detailed balance, HIL, auto-research.
68. Claim fence — explicit DO / DO NOT say list; peer-only number policy.
69. Glossary — exhaustive terms across swarm A–P and the physics lens.
70. Factory API paper abstract — research-paper framing for Fork / Reduce / Promote.
71. Talk logistics — Cambridge date/time/room, DST note and event details.
72. October talk differentiation — Cambridge systems story vs Rust/CI and Zenity/security talks.

## Where the material lives

- README.md — unified notebook / master story.
- OUTLINE.md — timed 45+15 outline.
- OUTLINE-ANALOGIES.md — five-domain analogy matrix.
- DECK-BEATS.md — final slide intentions and citation budget.
- CLAIM-FENCE.md — hard stage guardrails.
- QA-BANK.md — Q&A material.
- talk.tex + slides/ — final Beamer deck.
- TRAINING-ENVIRONMENTS.md — coding-RL environment/reset landscape and systems thesis.
- scratch/ — story depth, bibliography, glossary, paper draft, speaker notes and timing.
- swarm/A–P — sixteen independent research lenses plus ROUNDTABLE.md synthesis.
