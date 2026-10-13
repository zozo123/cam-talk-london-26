# Optional Cambridge speaker insert (approx. 90 seconds)

**Placement:** after the runtime -> evidence -> acceptance boundary, or in Q&A. Keep the canonical 57-slide narration unchanged.

> We have made it cheap to create possible futures, but that doesn't tell us which ones are worth running. The first question is whether a fork should exist at all. Can it replay the state we need? Are its writes private? Are the checker and publication authority outside it? Have we controlled external tool calls? And does it actually outperform the warm cache, rather than only looking fast against a cold start?
>
> This is where speculative decoding provides a useful mental model. A small model proposes; a stronger model verifies. The profound idea isn't simply parallelism, but budgeting guesses according to their probability of acceptance. Yet decoding has an exact correction theorem; software does not. A green test is not semantic correctness, and undoing a branch cannot unsend an API request.
>
> A fork controller should therefore predict whether a new branch succeeds **when the existing branches fail**. If four siblings all fail the same way, the fifth identical sibling is often a poor investment. Try a genuinely different hypothesis instead. But passing attempts are not independent evidence, either: their errors may share a cause, and choosing the most flattering result creates statistical selection bias.
>
> So our contract is: **admit only safe, useful forks; speculate to reduce expected cost; verify the exact bytes outside the sandbox; record failures and ancestry; and let one controller publish once.** We built a small executable model of that contract. The real-system speedup and statistical calibration remain experiments to run.

**Key equation for Q&A:**

\[
\Pr(\exists\text{ accepted}) = 1-\prod_{i=1}^K \left(1-\Pr(A_i\mid H,A_1^c,\ldots,A_{i-1}^c)\right).
\]

This is exactly the chain rule when every conditioning event has positive probability; it does **not** assume siblings are independent. Timeouts/cancellations should be recorded as unobserved, not fed into the model as failures.

**If pressed about what has shipped:** the earlier reducer handles declared duplicate evidence IDs; the new Python finite-world controller, receipts and failure tests are a mock demonstration, not a forked islo integration. If pressed about rigor: acceptance and correctness are different variables, and covariance/selection assumptions must be calibrated externally before reporting tighter confidence intervals.