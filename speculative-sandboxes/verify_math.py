#!/usr/bin/env python3
"""Numerical sanity checks for illustrations in main.tex; standard library only."""
from math import erf, exp, sqrt
from itertools import combinations


def phi(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0


def rising(x, n):
    out = 1.0
    for i in range(n):
        out *= x + i
    return out


def tv(p, q):
    assert len(p) == len(q)
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q))


p, q = [0.7, 0.2, 0.1], [0.4, 0.4, 0.2]
assert abs(1 - tv(p, q) - sum(min(x, y) for x, y in zip(p, q))) < 1e-12
residual = [max(a - b, 0.0) / tv(p, q) for a, b in zip(p, q)]
for a, b, r in zip(p, q, residual):
    assert abs(min(a, b) + tv(p, q) * r - a) < 1e-12

u, v, K = 0.45, 1.05, 8
p_any = 1.0 - rising(v, K) / rising(u + v, K)
print(f"beta-binomial at least one: {p_any:.9f}")
print(f"independent at least one: {1 - 0.7 ** K:.9f}")
print(f"next success after four fails: {u / (u + v + 4):.9f}")
assert abs(p_any - 0.6575) < 0.003
assert abs(u/(u+v) - 0.3) < 1e-12
assert abs(1/(u+v+1) - 0.4) < 1e-12
assert abs(K / (1+(K-1)*0.4) - 2.1052631578947367) < 1e-12

coverage = phi(1.96) ** 100 - phi(-1.96) ** 100
print(f"coverage of selected-max interval: {coverage:.9f}")
assert 0.079 < coverage < 0.081

for Delta in (0, 0.5, 2.0, 8.0):
    acceptance = 2 * phi(-sqrt(Delta/2))
    print(f"Delta={Delta:g}, equal-cov Gaussian overlap={acceptance:.9f}")

# A fixed-set monotone-submodularity check with arbitrarily dependent events.
# Enumerate equally likely elementary worlds; each branch succeeds in its event subset.
worlds = 12
success_sets = [{0,1,4,5}, {0,1,4,5}, {6,8,10}, {1,7,9}]
def f(chosen):
    return len(set().union(*(success_sets[i] for i in chosen))) / worlds if chosen else 0.0
for j in range(len(success_sets)):
    other = [i for i in range(len(success_sets)) if i != j]
    subsets = [tuple(s) for r in range(len(other)+1) for s in combinations(other, r)]
    for S in subsets:
        for T in subsets:
            if set(S).issubset(T):
                assert f((*S, j)) - f(S) >= f((*T, j)) - f(T) - 1e-12
print("all numerical checks passed")