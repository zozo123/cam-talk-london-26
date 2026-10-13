#!/usr/bin/env python3
"""Independent finite / numeric audits of the equations in main.tex.

These verify mathematical examples under stated assumptions, NOT sandbox security,
learned calibration, policy optimality or measured workload speedups.
"""
from __future__ import annotations
from itertools import combinations, product
from math import exp, isclose, prod


def close(x: float, y: float, tol: float = 1e-10) -> None:
    assert isclose(x, y, rel_tol=tol, abs_tol=tol), (x, y)


def audit() -> None:
    # Exact speculative token sampling (maximal overlap / TV / correction).
    p = (0.7, 0.2, 0.1)
    q = (0.4, 0.4, 0.2)
    tv = sum(abs(a - b) for a, b in zip(p, q)) / 2
    close(tv, 0.3)
    close(sum(min(a, b) for a, b in zip(p, q)), 1-tv)
    r = [max(a-b, 0)/tv for a, b in zip(p, q)]
    close(sum(r), 1.0)
    for a, b, rem in zip(p, q, r):
        close(min(a, b) + tv*rem, a)

    # Accepted-prefix tail-sum formula: direct enumeration of 3 Bernoulli chains.
    # The test does not assume identical conditional survival probabilities.
    probs = (0.8, 0.65, 0.5)
    distribution = [(bs, prod((pj if bj else 1-pj)
                     for pj, bj in zip(probs, bs)))
                    for bs in product((0, 1), repeat=3)]
    e_length = 0.0
    for bits, pr in distribution:
        length = 0
        for x in bits:
            if not x:
                break
            length += 1
        e_length += length*pr
    close(e_length, probs[0] + probs[0]*probs[1] + prod(probs))

    # Conditional success in exactly two mutually exclusive worlds.
    worlds = ({'A'}, {'B'})
    p_b = sum('B' in w for w in worlds)/2
    p_b_given_a_fail = sum(('B' in w and 'A' not in w) for w in worlds) / sum('A' not in w for w in worlds)
    close(p_b, 0.5)
    close(p_b_given_a_fail, 1.0)

    # Fixed-set coverage is submodular (including duplicates).
    sets = ({0, 1, 2}, {0, 1, 2}, {3, 4}, {2, 5})
    def coverage(I):
        return len(set().union(*(sets[i] for i in I))) / 8 if I else 0.0
    for j in range(len(sets)):
        others = [k for k in range(len(sets)) if k != j]
        subs = [set(s) for n in range(len(others)+1) for s in combinations(others, n)]
        for A in subs:
            for B in subs:
                if A <= B:
                    assert coverage(A | {j})-coverage(A) >= coverage(B | {j})-coverage(B)-1e-12

    # Critical path example and simplified expected crossover.
    da, v, d, vf = 10, 30, 20, 30
    close(da+v+d+vf, 90)
    close(da+max(v, d)+vf, 70)
    close(min(v, d), 20)
    accept = 0.8
    cB = d
    close(accept*min(v, d), 16)
    close((1-accept)*cB, 4)
    # Example with beta = 1 second-value unit and lambda = 0.2 per worker-sec.
    beta, lam, h, cf = 1.0, 0.2, 2.0, 3.0
    net = beta*accept*min(v, d) - beta*h - lam*((1-accept)*cB + cf)
    close(net, 12.6)
    # Break-even acceptance from the exact same symbolic inequality:
    threshold = (beta*h + lam*(cB+cf)) / (beta*min(v, d)+lam*cB)
    close(threshold, 6.6/24)
    assert accept > threshold

    # Committor/h-transform finite absorbing Markov chain: F=0, G=3.
    # P(1,0)=.3 P(1,2)=.7; P(2,1)=.4 P(2,3)=.6.
    h2 = .6/(1-.4*.7)
    h1 = .7*h2
    close(h1, .7*h2)
    close(h2, .4*h1+.6)
    close(.3*0/h1 + .7*h2/h1, 1.0)
    close(.4*h1/h2 + .6*1/h2, 1.0)
    close(h2, 5/6)
    close(h1, 7/12)

    # Pairwise common-random-numbers variance: matched = 2*sigma^2.
    tau2, sigma2 = 9.0, 1.0
    matched, independent = 2*sigma2, 2*(tau2+sigma2)
    close(matched, 2)
    close(independent, 20)
    close(independent/matched, 10)

    # Value-of-information, illustrative two-hypothesis decision problem.
    direct_cost = 10 + .5*10
    diagnostic_cost = 2+10
    close(direct_cost, 15)
    close(diagnostic_cost, 12)
    close(direct_cost-diagnostic_cost, 3)

    # Nested rare-event levels, and importance-sampling identity.
    close(.1**6, .000001)
    P = (0.8, 0.2)
    Q = (0.3, 0.7)
    G = (False, True)
    weighted = sum(qq*(pp/qq)*(1 if g else 0) for pp,qq,g in zip(P,Q,G))
    close(weighted, .2)

    # Equicorrelated estimation error / *not* binary patch success.
    K, rho = 8, 0.4
    close(K/(1+(K-1)*rho), 2.1052631578947367)

    # Extra guard against optimistic evaluation on repeatedly probed tests.
    false_pass = 1-(1-.01)**100
    close(false_pass, 0.6339676587267709)

    # Boltzmann policy normalization and preference for utility as T decreases.
    weights = (0.5, 0.5)
    Qs = (0., 1.)
    def gibbs(T):
        nums = [w*exp(q/T) for w,q in zip(weights,Qs)]
        return [x/sum(nums) for x in nums]
    for T in (0.2, 0.5, 2.0):
        close(sum(gibbs(T)), 1.)
    assert gibbs(.2)[1] > gibbs(2)[1]
    print('PASS: all algebraic and finite-model equation cross-checks')


if __name__ == '__main__':
    audit()
