# Claim boundaries for the 40-slide Cambridge seminar

This document applies to the canonical `talk.tex`. Earlier notebooks and the separate 30-minute cut are historical material.

## Definitions and proposed contract

An environment defines interaction semantics. A sandbox constrains an execution. A snapshot captures declared state. A fork creates a separately evolving continuation under supported restoration semantics.

The full runtime architecture, evidence-routing policy, promotion protocol, maintenance campaign, benchmark, and ablations are proposals. The fidelity expression specifies a task-dependent observational test; it is not a universal guarantee about a shipped runtime.

The main performance hypothesis is lower total resources to a fixed quality target when useful preparation can be reused. Capture, restore, divergence, inference, failures, communication, evaluation, and external effects all belong in the comparison. The cost plot on slide 14 is an analytic illustration with declared hypothetical units.

## Reported implementation evidence

Source: Eliaz, arXiv:2607.09689, linked on slides 28–29 and 33–34.

- The numerical reducer exercises the stated precision-weighted algebra, metadata, and exact evidence-overlap checks.
- The unequal-size logistic comparison reports distance to centralized MLE across eight fixed seeds: information pooling 0.0083 ± 0.0042 versus equal coefficient average 0.177 ± 0.090. Error bars are standard deviations, not confidence intervals.
- The integration example starts from a 141 MB named snapshot. Four concurrent restore–run–capture round trips take 6.70 s in total at the client-observed boundary. This is not per-worker restore latency or a speedup.
- The trace's pooled mean is 4.9422 versus the seed-pinned full-sample mean 4.9450.
- The precision-forgery stress motivates a trust problem. Its heuristic response provides no Byzantine-robustness theorem.

No new controlled runtime benchmark is claimed by this slide revision.

## Statistical scope

Precision pooling requires a common parameter, calibrated information, and independent evidence under the stated Gaussian or local Wald approximation. Disjoint evidence identifiers and distinct processes do not establish independent errors.

The variance-floor formula assumes equal marginal variances and common pairwise correlation; the plotted curves are analytic examples. Positive covariance can improve paired differences under a valid coupling. Lineage alone is not a covariance estimator.

Shannon mutual information, Fisher information, verifier utility, and objective-score interactions are distinct quantities. The XOR example demonstrates information synergy. The patch equation measures objective non-additivity. Pairwise tests do not rule out higher-order effects.

## Biological and physical examples

The biological work motivates attention to local rules and global network structure. It does not establish a branching threshold, optimization law, or performance theorem for agents. The biological diagram is a schematic.

Chamo and Eliaz, ai.viXra:2608.0069, is a preprint. It reports verified continuation connecting apparent branches within a sampled periodic-orbit component. The two slide diagrams are conceptual schematics, not replotted numerical data. The result does not establish global topology of every orbit family, sandbox speedup, or autonomous discovery. Connectivity and dynamical stability are separate properties.

## Applications and commitment

Spark, OpenClaw, Airflow, and Linux are motivating maintenance settings, not validated deployments of this runtime. The Airflow-style campaign is explicitly proposed.

A local restore does not rewind external services or physical experiments. Protecting evaluator writes does not eliminate adaptive overfitting through feedback. Composed changes require a new identified artifact and fresh joint validation. Current authority and fencing are required for commitment; workers do not inherit release or merge authority.
