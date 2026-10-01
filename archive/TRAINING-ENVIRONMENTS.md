# Training-grade coding environments — reset as a runtime primitive

This note incorporates the coding-RL / RLVR angle into the Cambridge story without turning the talk into a startup pitch.

## Core systems claim

A coding-training episode is a controlled experiment:

episode = (repo/start-state S0, task, tools, verifier digest, reset)

The environment is useful for training only if:

1. the repository and dependencies are real enough to exercise the capability,
2. the reward is executable/verifiable rather than merely stylistic,
3. the worker cannot rewrite or inspect protected verifier state,
4. repeated episodes can return to an authenticated starting state,
5. trajectories preserve evidence and lineage.

Forkable-snapshot thesis: prepare the expensive base once, snapshot the known-good state, fork a disposable child per episode, then burn the child and keep the evidence. This is the architectural proposal; do not present universal latency/speedup numbers without a benchmark.

## Evidence that the category is real

### SWE-smith

SWE-smith is a NeurIPS 2025 Datasets & Benchmarks Spotlight toolkit for turning GitHub repositories into software-engineering training environments and synthesizing executable tasks. Its public project describes large-scale task and environment generation.

- Paper: https://arxiv.org/abs/2504.21798
- Code: https://github.com/SWE-bench/SWE-smith

Talk relevance: environment construction and task/verifier generation are already recognized bottlenecks. Forkable reset is a complementary runtime question: how cheaply and faithfully can we replay the same starting state across many episodes?

### Meta Code World Model (CWM)

Meta FAIR’s CWM uses code-execution and agentic interaction data and is trained/evaluated in executable coding environments.

- Meta: https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models
- Code: https://github.com/facebookresearch/cwm

Talk relevance: executable environments are part of the model-training stack, not only evaluation infrastructure.

### Scale AI

Scale publicly offers RL Environments, including realistic system state, automated verifiers, parallel runs, trajectory capture, and environment reset/inspection.

- Product: https://scale.com/rlenvironments
- Launch article: https://scale.com/blog/rl-environments

### Surge AI

Surge publicly offers RL Environments and Agents and publishes work on training agents inside high-fidelity environments with designed verifiers.

- Product: https://surgehq.ai/products
- Research: https://surgehq.ai/research

### Mercor

Mercor’s research site describes RL environments as realistic data-rich worlds with tools/applications, tasks and verifiers.

- Research: https://www.mercor.com/research/

### Prime Intellect

Prime Intellect launched an Environments Hub for RL/evaluation, integrated it with prime-rl, and added hosted training/evaluation and sandbox support.

- Hub: https://www.primeintellect.ai/blog/environments
- Lab: https://www.primeintellect.ai/blog/lab
- prime-rl: https://github.com/PrimeIntellect-ai/prime-rl

## The wedge implied by this repo

Do not frame the value as generic sandbox hosting. The differentiated systems layer is:

real repo + verified reward + authenticated S0 + fork/reset + isolation + lineage

The execution contract is the same Cambridge contract:

snapshot → fork N → run → verify outside child → reduce evidence → promote/train → burn

For training, promote may mean consuming the trajectory/reward into an optimizer rather than merging a patch. The authority boundary still matters: a rollout may generate evidence; it must not rewrite the reward function that grades itself.

## What the current repo contributes

- swarm/A-FORK-SYSTEMS.md — fork/checkpoint primitives and related systems.
- swarm/C-ORACLE-RL-ESCAPE.md — sealed oracle, reward hacking and escape boundary.
- swarm/E-CREDENTIALS-WIRE.md — capability remint / credential inheritance.
- swarm/F-WARM-COW-SIDECHANNELS.md — warm-state and cross-tenant leakage risks.
- swarm/G-FACTORY-API.md — Fork / Reduce / Promote contract.
- swarm/H-ANNEALING-MCMC-SGD.md — exploration schedules.
- scratch/UNIVERSAL-HILLCLIMB.md — same loop across software, RL, simulation, biology and HIL.
- CLAIM-FENCE.md — prevents turning architecture hypotheses into benchmark claims.

## Claim fence for the RL-environment story

### Safe to say

- Coding-agent post-training uses executable/verifiable software environments.
- SWE-smith, Meta CWM, Scale, Surge, Mercor and Prime Intellect are direct evidence that RL environments are a real category.
- Reset/replay is a first-class requirement for controlled repeated episodes.
- Forkable snapshots are a plausible systems mechanism for making reset cheaper while preserving a known starting state.
- Reward/verifier integrity is a separate boundary from ordinary process isolation.

### Do not say without new evidence

- Environment setup is always the dominant cost.
- Forkable snapshots are 100x cheaper as a universal claim.
- Nobody else productizes snapshot-fork reset.
- Frontier labs all use this exact architecture.
- ariflow-swfactory PR merges prove training gains. They prove realistic execution/evaluation pressure, not that a model improves after training.
- SWE-smith is naive. It solves a different layer: environment/task synthesis and training-data generation.

## Benchmark that would convert the thesis into evidence

Compare identical repo/task/verifier episodes under:

1. cold environment build,
2. cached/prebuilt container restart,
3. snapshot restore,
4. snapshot fork fan-out.

Measure separately:

- time-to-ready for the episode,
- storage/write amplification,
- concurrency/density,
- reset fidelity (state digest before every episode),
- cross-episode leakage,
- verifier secrecy/integrity,
- task completion / reward distribution,
- total rollout throughput per host.

Only after that benchmark should the talk or company narrative attach numeric speedups to fork-reset.


## World models versus executable worlds

There are two different “CWM” references around this topic and they must not be conflated:

- **Contrastive World Models** — Bonnie Li, arXiv:2609.22175 (2026), a Dreamer-style latent-dynamics approach that replaces pixel reconstruction with a contrastive / InfoMax-style objective to retain future-predictive information and ignore visual nuisance factors.
- **Code World Model** — Meta FAIR (2025), a code-generation model trained on Python execution traces and agentic container trajectories and post-trained with RL in verifiable coding/software-engineering environments.

The Cambridge bridge uses **Contrastive World Models** for the representation argument and **Meta Code World Model** only as evidence that executable environments matter for code learning.

### The systems inversion

World-model methods make imagined rollouts cheap when direct interaction is costly, unsafe, or scarce. Forkable sandboxes attack the complementary term for software: make **real executable interaction** cheap enough to branch directly.

> World models make imagination cheap. Forkable sandboxes make interaction cheap.

A forked software rollout avoids learned transition-model error for the transition actually executed inside the captured boundary. This is not a claim that all external reality is captured. Network services, clocks, hardware, randomness, production state and incomplete tests may remain outside the snapshot.

### Benchmark extension

In addition to cold build / cached container restart / snapshot restore / snapshot fork, add a fifth axis where appropriate:

5. learned / predicted rollout used for proposal or pruning, followed by executable forked validation.

That hybrid benchmark would answer a more interesting question than “model or sandbox?”: **how should learned imagination choose branches, and how cheaply can executable forks ground them?**
