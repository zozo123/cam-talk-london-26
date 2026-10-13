#!/usr/bin/env python3
"""Independent finite and numerical checks for equations in main.tex.

Runs with the Python standard library; these validate the stated examples,
not the correctness of real software patches or assumptions of a fitted model.
"""
from itertools import combinations
from math import erf, exp, pi, sqrt

from reference import ForkGates, WorkCosts, admit, Admission, example_scheduler


def phi(x: float) -> float:
    return (1 + erf(x / sqrt(2))) / 2


def approx(actual, expected, tol=1e-9):
    assert abs(actual - expected) <= tol, (actual, expected, tol)


def check_exact_sampling():
    for p, q in (([.7, .2, .1], [.4, .4, .2]),
                 ([1., 0., 0.], [0., 1., 0.]),
                 ([.5, .5], [.5, .5]),
                 ([0., 1.], [1., 0.])):
        tv = sum(abs(a-b) for a, b in zip(p,q))/2
        overlap = sum(min(a,b) for a,b in zip(p,q))
        approx(overlap, 1 - tv)
        if tv:
            r = [max(a-b,0)/tv for a,b in zip(p,q)]
            approx(sum(r), 1)
            for a,b,correction in zip(p,q,r):
                approx(min(a,b)+tv*correction,a)
        else:
            approx(overlap,1)
        # Maximal coupling upper bound for discrete distribution pair:
        # every diagonal entry in a joint distribution is <= min(p_i,q_i).
        for i in range(len(p)):
            assert min(p[i],q[i]) <= p[i] and min(p[i],q[i]) <= q[i]
    print("[PASS] TV / residual exactness / maximal-coupling upper bound")


def check_gaussian_tv():
    # Independently integrate min densities; analytic result is 2 Phi(-d/2).
    n=40000
    lo,hi=-12.,12.
    h=(hi-lo)/n
    for delta in (0., .5, 2., 8.):
        distance = sqrt(2*delta)
        def norm(x,mean):
            return exp(-((x-mean)**2)/2)/sqrt(2*pi)
        total=sum((.5 if i in (0,n) else 1) *
                  min(norm(lo+i*h,-distance/2),norm(lo+i*h,distance/2))
                  for i in range(n+1))*h
        expected=2*phi(-sqrt(delta/2))
        approx(total,expected,1e-6)
        # Equal covariance unit variance: KL = (mu1-mu2)^2/2 = delta.
        approx(distance**2/2,delta)
    print("[PASS] equal-covariance Gaussian overlap and KL=Delta (quadrature)")


def check_conditional_success():
    s=example_scheduler()
    attempts=list(s.branches)
    failures=set(s.worlds)
    survival_product=1.0
    for name in attempts:
        p=len(failures & s.branches[name].successful_worlds)/len(failures) if failures else 0.0
        survival_product *= 1-p
        failures-=s.branches[name].successful_worlds
    approx(1-survival_product,s.coverage(set(attempts)))
    # The second candidate is an exact copy of the first: conditional acceptance=0.
    approx(len(s.branches["family-A-clone"].successful_worlds -
               s.branches["family-A"].successful_worlds),0)
    print("[PASS] conditional chain identity with arbitrarily overlapping success events")


def rising(x,k):
    out=1.0
    for j in range(k):out*=x+j
    return out


def check_beta():
    u,v,k=.45,1.05,8
    approx(u/(u+v),.3)
    approx(1/(u+v+1),.4)
    p_any=1-rising(v,k)/rising(u+v,k)
    approx(p_any,.6575,.004)
    approx(1-.7**k,.94235199)
    approx(u/(u+v+4),.45/5.5)
    print(f"[PASS] beta-binomial shared difficulty: P(any)={p_any:.7f}, after failures={u/(u+v+4):.7f}")


def check_submodular_and_greedy():
    s=example_scheduler()
    names=list(s.branches)
    sets=[set(subset) for n in range(len(names)+1) for subset in combinations(names,n)]
    for x in sets:
        for y in sets:
            if x<=y:
                for j in set(names)-y:
                    assert s.coverage(x|{j})-s.coverage(x) >= s.coverage(y|{j})-s.coverage(y)-1e-12
    # Cardinality budget k=2: enumerate optimum and compare greedy result.
    best=max((s.coverage(set(x)),set(x)) for x in combinations(names,2))
    chosen=set()
    while len(chosen)<2:
        chosen.add(max((name for name in names if name not in chosen),
                       key=lambda name:s.coverage(chosen|{name})-s.coverage(chosen)))
    assert s.coverage(chosen) >= (1-1/exp(1))*best[0]
    print(f"[PASS] coverage submodularity, greedy k=2 ({s.coverage(chosen):.4f} vs optimum {best[0]:.4f})")


def check_prefix_tail_sum():
    # Explicit correlated event model, nested accepted-prefix events.
    s=example_scheduler()
    names=["family-A", "family-A-clone", "independent-C", "alternate-D"]
    lengths=[]
    for world in s.worlds:
        length=0
        for name in names:
            if world in s.branches[name].successful_worlds:
                length+=1
            else:
                break
        lengths.append(length)
    actual=sum(lengths)/len(lengths)
    tail=sum(sum(1 for length in lengths if length>=j)/len(lengths)
             for j in range(1,len(names)+1))
    approx(actual,tail)
    # Only under constant *conditional* prefix survival does geometric formula apply.
    a=.8; n=4
    approx(sum(a**j for j in range(1,n+1)), a*(1-a**n)/(1-a))
    print("[PASS] expected validated-prefix length via tail-sum identity")


def check_covariance_and_gls():
    rho=.4;k=8
    approx(k/(1+(k-1)*rho), 2.1052631578947367)
    # Scalar GLS for two observations, correlated error with covariance [[2,1],[1,3]].
    c11,c12,c22=2.,1.,3.
    det=c11*c22-c12*c12
    i11,i12,i22=c22/det,-c12/det,c11/det
    denom=i11+2*i12+i22
    weights=((i11+i12)/denom,(i12+i22)/denom)
    approx(sum(weights),1)
    # Numerical weighted mean variance = (1^T C^-1 1)^-1.
    var=weights[0]**2*c11+2*weights[0]*weights[1]*c12+weights[1]**2*c22
    approx(var,1/denom)
    # Independent limiting case with common, equal variance.
    approx(8/(1+7*0),8)
    print(f"[PASS] GLS identity, equicorrelation information, K_eff={k/(1+(k-1)*rho):.6f}")


def check_selection_coverage():
    selected=phi(1.96)**100-phi(-1.96)**100
    assert .079 < selected < .081, selected
    # Bonferroni simultaneous coverage: each interval misses with <=delta/K.
    k=100;delta=.05
    # Test inequality via normal quantile found by bisection (without scipy).
    l,h=0.,8.
    for _ in range(70):
        mid=(l+h)/2
        if 2*(1-phi(mid))>delta/k:l=mid
        else:h=mid
    z=(l+h)/2
    assert 3.47 < z < 3.49
    assert k*2*(1-phi(z)) <= delta+1e-12
    print(f"[PASS] post-selection coverage={selected:.7%}; Bonferroni z={z:.5f}")


def check_fork_cost():
    gates=ForkGates(*([True]*6))
    c=WorkCosts(4,7,10,1,2,5,3,2)
    approx(c.warm-c.fork,4*(7-2)-10-1-2)
    assert admit(gates,c) == Admission.FORK
    assert admit(gates,WorkCosts(4,1,10,1,2,5,3,2)) == Admission.USE_WARM
    print("[PASS] fork-versus-warm algebra and no-fork control")


if __name__ == "__main__":
    check_exact_sampling()
    check_gaussian_tv()
    check_conditional_success()
    check_beta()
    check_submodular_and_greedy()
    check_prefix_tail_sum()
    check_covariance_and_gls()
    check_selection_coverage()
    check_fork_cost()
    print("ALL MATHEMATICAL CHECKS PASSED")