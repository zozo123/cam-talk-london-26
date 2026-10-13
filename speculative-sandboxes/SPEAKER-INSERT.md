# Optional Cambridge side-note (90 seconds, not part of timed 57-slide deck)

**Placement:** after “Reusing state pays off when it avoids more setup than it adds” (Runtime) or during Q&A following “Choosing a result, merging code and pooling measurements are different operations” (Evidence).

> A sandbox does not become useful merely because it boots fast. We need to know **what state it actually preserved**; whether a child can privately continue; whether its verifier and publication permissions remain outside the child; and whether restoring beats a realistic warm cache. Those are the gates for a useful fork.
>
> Speculative decoding offers a scheduling lesson, not a license to call test passes mathematically exact. Token decoding accepts drafts at a rate `1 - total variation` because it has both target and draft distributions, plus a correction sampler. For software, we instead measure the probability that an exact candidate passes a trusted, external verifier.
>
> When forks share a model, prompt or flawed assumption, their failures are correlated. A new worker's marginal value is the probability it succeeds **when the current workers fail**. That tells us when to go deeper, diversify, or stop.
>
> Finally, the work that passes is not necessarily independent evidence. We preserve the whole selection history, verify exact bytes, and let the controller accept once. **Speculate for speed; verify for correctness; reduce for defensible confidence.**

**One-sentence Q&A math:** `P(any accepted) = 1 - product_i (1 - P(A_i | all earlier failures, history))`; this needs no independence assumption, although accurate conditionals must be learned.

**Status:** proposal only; no measured speedup, new preregistered hypothesis, or claim that a live memory fork was observed.