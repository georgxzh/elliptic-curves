#!/usr/bin/env python3
"""Small independent arithmetic checks; no large-prime bias experiment.

Run with Python and mpmath. Finite character sums are the oracle.
The infinite-weight and analytic-tail conclusions require the written proofs.
"""
import json
import math
from fractions import Fraction
from pathlib import Path
import mpmath as mp


def primes(limit):
    return [p for p in range(5,limit) if all(p%q for q in range(2,math.isqrt(p)+1))]


def leg(a,p):
    v=pow(a%p,(p-1)//2,p)
    return 0 if v==0 else 1 if v==1 else -1


def main():
    mp.mp.dps=45
    error=mp.mpf(0); modes=0; fejer=0; sparse=0; null=0
    K=40
    for p in primes(150):
        trace=[-sum(leg(x**3+B,p) for x in range(p)) for B in range(p)]
        assert trace[0]==0 and sum(trace)==0
        if p%3==2:
            assert all(v==0 for v in trace)
            continue
        roots=[mp.exp(2j*mp.pi*t/p) for t in range(p)]
        cos=[z.real for z in roots]; sin=[z.imag for z in roots]
        G=[sum(roots[(a*x**3)%p] for x in range(p)).real for a in range(p)]
        norm=mp.mpf(p)**(mp.mpf(5)/6)
        h=lambda a: leg(a,p)*G[a%p]/mp.root(p,3)
        for a in [1,3,4,8,27,64,1728,p**6,27*p**6]:
            for trig,active in [(cos,p%12==1),(sin,p%12==7)]:
                actual=sum(trace[B]*trig[(a*B)%p] for B in range(p))/norm
                predicted=-h(a) if active else 0
                error=max(error,abs(actual-predicted)); modes+=1
        # Nonzero finite weights cancel in the specified progression.
        trig=cos if p%12==1 else sin
        sign=-1 if p%12==1 else 1
        value=sum(trace[B]*(trig[B]+sign*trig[27*B%p]) for B in range(p))/norm
        error=max(error,abs(value)); null+=1
        # Truncate the smooth infinite example; use its exact finite correction.
        grid=[sum(mp.mpf(2)**(-k)*(cos[pow(k,6,p)*B%p]+sin[pow(k,6,p)*B%p])
                  for k in range(1,K+1))-cos[B]-sin[B] for B in range(p)]
        actual=sum(t*w for t,w in zip(trace,grid))/norm
        correction=Fraction(1,2**K)+sum((Fraction(1,2**k) for k in range(p,K+1,p)),Fraction(0))
        predicted=G[1]/mp.root(p,3)*mp.mpf(correction.numerator)/correction.denominator
        error=max(error,abs(actual-predicted)); sparse+=1
        # Includes exact endpoints, p-divisible modes and frequencies above p.
        for u in [Fraction(0),Fraction(1,p),Fraction(1,7),Fraction(1,2),Fraction(3,5),Fraction(1)]:
            uu=mp.mpf(u.numerator)/u.denominator
            for M in [1,2,7,20]:
                alpha=[mp.sin(2*mp.pi*a*uu)/(mp.pi*a) for a in range(1,M+1)]
                beta=[(1-mp.cos(2*mp.pi*a*uu))/(mp.pi*a) for a in range(1,M+1)]
                q=[uu+sum((1-mp.mpf(a)/(M+1))*(alpha[a-1]*cos[a*B%p]+beta[a-1]*sin[a*B%p])
                          for a in range(1,M+1)) for B in range(p)]
                assert min(q)>-mp.mpf('1e-40') and max(q)<1+mp.mpf('1e-40')
                value=sum(t*w for t,w in zip(trace,q))/norm
                coeff=alpha if p%12==1 else beta
                rhs=-sum((1-mp.mpf(a)/(M+1))*coeff[a-1]*h(a) for a in range(1,M+1))
                error=max(error,abs(value-rhs)); fejer+=1
    assert error<mp.mpf('1e-35')
    witnesses=[]; principal=0
    for a in range(1,81):
        for j in [0,1]:
            expected=(math.isqrt(a)**2==a) if j==0 else (a%3==0 and math.isqrt(a//3)**2==a//3)
            witness=next((p for p in primes(1000) if p%3==1 and a%p and leg(a,p)*leg(-1,p)**j==-1),None)
            if expected:
                assert witness is None; principal+=1
            else:
                assert witness is not None
                witnesses.append(dict(a=a,j=j,prime=witness))
    result=dict(mode_checks=modes,fejer_checks=fejer,sparse_finite_checks=sparse,
                null_weight_checks=null,max_absolute_error=str(error),
                principal_character_cases=principal,nonprincipal_witnesses=witnesses,
                note='Finite checks support exact reductions only. No prime asymptotic or averaged-tail conjecture is numerically certified.')
    destination=Path(__file__).with_name('checks.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='nonprincipal_witnesses'},indent=2))


if __name__=='__main__': main()
