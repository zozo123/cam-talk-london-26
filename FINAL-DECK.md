# Final deck — Cambridge SRG · 15 Oct 2026

talk.tex is the stage source of truth. Planning documents (OUTLINE.md, DECK-BEATS.md, scratch/*, swarm/*) remain research and Q&A support.

## Final 18-slide main path + appendix

1. Forkable Sandboxes — title + mantra.
2. Why I ended up working on this — computational science → production ML/build systems → coding agents; state becomes the collision point between reuse and trust.
3. One-sentence talk — cheap forked machines for search; authority stays outside.
4. Scarcity ladder — cheap/plural search vs scarce/singular authority.
5. Execution substrate: six surfaces — FS, wire/credentials, reproducibility, fast cloning, execution, recovery/observability.
6. Outer wall — container/user-space-kernel/microVM isolation framing.
7. Fork becomes an OS primitive — DeltaBox + Shepherd as related systems.
8. Parallel worlds — S0 → fork N → evidence → reduce → promote once → burn.
9. Three factories, one loop — software, RL post-training, HIL/simulation.
10. Coding RL turns reset into a training primitive — training episode = S0 + task + tools + verifier digest + reset; forkable snapshots change the reset path.
11. Software factory: Cell and Epoch — attempt vs objective/authority lifetime.
12. RL factory: oracle leaves the fork — RUN ≠ EVAL; verifier tampering boundary.
13. HIL is the extreme of the same ladder — burn cheap simulation before robot/wet/human tip.
14. Fork ≠ independence: cold liar — structured worker record and precision/provenance integrity.
15. Annealing is schedule language — SA/MH/SGD/RL temperature as controller-owned schedules, not physical claims.
16. Capability contract: Fork / Reduce / Promote — named API.
17. Invariants: Search ≠ Authority — immutable S0, frozen objective, lineage, abstain, one promote bit.
18. Open problems for SRG — correlation, leases, warm channels, sealed oracle, world diff, promote-once.
19. Appendix: selected sources + claim fence.

## Timing

- Slides 1–4: 5 min
- Slides 5–8: 11 min
- Slides 9–13: 14 min
- Slides 14–17: 10 min
- Slide 18: 5 min
- Q&A: 15 min

If late, skip slide 15 (annealing) first. Never cut slide 8 (parallel worlds), slide 10 (training reset), slide 12 (oracle boundary), or slide 18 (open problems).

## Build

Run make, or run pdflatex twice on talk.tex. GitHub Actions builds talk.pdf and uploads it as an artifact.

## Stage claim fence

- Do say: forkable environments are a substrate/capability contract for controlled agent search and coding-RL episodes.
- Do say: reset/replay, verifier integrity, credential scoping and evidence lineage are separable systems properties.
- Do not claim universal setup bottlenecks or universal numeric speedups without the proposed benchmark.
- Do not claim fork implies statistical independence.
- Do not claim equilibrium thermodynamics, detailed balance, or Gibbs-of-nature.
- Do not claim the rollout worker owns the verifier, thermostat, schedule or promote bit.
