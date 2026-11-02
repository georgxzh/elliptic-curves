#!/usr/bin/env python3
"""Compare exact sums with candidate profiles, checking counts and symmetry.

Usage: python analyze_direct_extended.py input.csv pmax output.json
The input must cover all eligible primes from 7 through pmax, with K=24.
Diagnostics are descriptive and correlated, not calibrated tests.
"""
import csv
import json
import math
import sys
from collections import defaultdict
import numpy as np
from analyze_law import C
from check_theory import coefficients


def profile_grid(K=24, cutoff=10**18):
    b,c = coefficients(cutoff)
    out = {}
    # Reduce integer frequencies modulo K BEFORE conversion to floating point.
    # Forming a floating-point angle of size 1e18 would lose grid accuracy.
    for k in range(1,K):
        sinb = math.fsum(v/a*math.sin(2*math.pi*((a*k)%K)/K) for a,v in b.items())
        sinc = math.fsum(v/a*math.sin(2*math.pi*((a*k)%K)/K) for a,v in c.items())
        cosb = math.fsum(v/a*2*math.sin(math.pi*((a*k)%K)/K)**2 for a,v in b.items())
        cosc = math.fsum(v/a*2*math.sin(math.pi*((a*k)%K)/K)**2 for a,v in c.items())
        out[1,k] = -(sinb+sinc)/math.pi
        out[7,k] = -(cosb-cosc)/math.pi
    out[1,K//2] = 0. # Exact symmetry, avoiding sin(pi) roundoff.
    bound = 2*C*(1+2/math.sqrt(3))*cutoff**(-5/6)*((1+math.log(cutoff)/4)/(5/6)+.25/(5/6)**2)
    return out, dict(cutoff=cutoff,b_terms=len(b),c_terms=len(c),
                     tail_F1=bound/math.pi,tail_F7=2*bound/math.pi,
                     note='Proved truncation bounds; floating-point roundoff is not included.')


def main(path,pmax,output):
    rows = list(csv.DictReader(open(path)))
    K=24
    table={}
    for r in rows:
        assert int(r['K'])==K
        key=tuple(int(r[q]) for q in ['bin','p_mod_12','k'])
        assert key not in table
        table[key]=[int(r['count']),float(r['sum']),float(r['sum2'])]
    sieve=np.ones(pmax+1,dtype=bool); sieve[:2]=False
    for q in range(2,math.isqrt(pmax)+1):
        if sieve[q]: sieve[q*q::q]=False
    primes=np.flatnonzero(sieve)
    primes=primes[(primes>=7)&(primes%3==1)]
    expected=defaultdict(int)
    for p in primes:
        expected[int(p).bit_length()-1,int(p%12)]+=1
    assert len(table)==len(expected)*(K-1)
    for (bin_,res),count in expected.items():
        for k in range(1,K):
            n,s,t=table[bin_,res,k]
            assert n==count
            n1,s1,t1=table[bin_,res,K-k]
            assert n1==n
            assert abs(s1-(-s if res==1 else s))<1e-12*max(1,abs(s))
            assert abs(t-t1)<1e-12*max(1,t)
        if res==1: assert table[bin_,res,K//2][1:]==[0.,0.]
    pred,tail=profile_grid(K)
    output_rows=[]; diagnostics=[]
    ranges=[('pooled',16,pmax.bit_length()-1)]
    ranges += [('dyadic',b,b) for b in range(16,pmax.bit_length())]
    for tag,lo,hi in ranges:
        for res in [1,7]:
            selected=[]
            for k in range(1,K):
                triples=[v for (b,r,j),v in table.items() if lo<=b<=hi and r==res and j==k]
                if not triples: continue
                n=sum(t[0] for t in triples)
                s=math.fsum(t[1] for t in triples); t=math.fsum(t[2] for t in triples)
                mean=s/n
                se=math.sqrt(max(t-s*s/n,0)/(n*(n-1))) if n>1 else 0.
                value=pred[res,k]
                row=dict(range=tag,lo=2**lo,hi_exclusive=min(2**(hi+1),pmax+1),residue=res,
                         k=k,K=K,u=k/K,primes=n,mean=mean,stderr=se,predicted=value,
                         residual=mean-value,z=(mean-value)/se if se else None)
                output_rows.append(row)
                if k<=K//2 and not (res==1 and k==K//2): selected.append(row)
            if selected:
                denominator=math.fsum(r['predicted']**2 for r in selected)
                diagnostics.append(dict(range=tag,lo=2**lo,hi_exclusive=min(2**(hi+1),pmax+1),residue=res,
                    primes=selected[0]['primes'],nonmirrored_grid_points=len(selected),
                    sum_squared_standardized_residuals=math.fsum(r['z']**2 for r in selected),
                    max_abs_z=max(abs(r['z']) for r in selected),
                    descriptive_amplitude_ratio=math.fsum(r['mean']*r['predicted'] for r in selected)/denominator,
                    rms_residual=math.sqrt(math.fsum(r['residual']**2 for r in selected)/len(selected))))
    result=dict(pmax=pmax,primes=len(primes),aggregate_rows=len(table),K=K,
                prime_counts_checked=True,mirror_symmetries_checked=True,profile=tail,
                diagnostics=diagnostics,rows=output_rows,
                note='Correlated diagnostics; amplitude ratio describes drift and is not fitted into the predictions. No covariance data or calibrated significance claims.')
    with open(output,'w') as f: json.dump(result,f,indent=2); f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))


if __name__=='__main__': main(sys.argv[1],int(sys.argv[2]),sys.argv[3])
