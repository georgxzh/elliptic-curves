#!/usr/bin/env python3
"""Exact finite-lift checks for FRONTIER_ADDITIVE.md (requires SymPy)."""

from collections import Counter
import json
from pathlib import Path
import sympy as S

def vp(n,p):
    if n==0:return 1000
    v=0
    while n%p==0:n//=p;v+=1
    return v

def sqrtmod(n,p,N):
    M=p**N;n%=M;v=vp(n,p)
    if v>=N:return 0
    if v%2:return None
    e=v//2;u=n//p**v;L=N-v
    roots=[r for r in range(1,p) if (r*r-u)%p==0]
    if not roots:return None
    r=roots[0];m=p
    for j in range(1,L):
        r+=m*((u-r*r)//m*pow(2*r,-1,p)%p);m*=p
    return p**e*r

def actual(p,A,B,x,y,K):
    out=set()
    for k in range(1,K+1):
        pk=p**k
        for z in range(pk):
            f=z**4-6*x*z*z+8*y*z-3*x*x-4*A
            d=4*(z**3-3*x*z+2*y)
            if f%(pk*pk) or d%pk:continue
            # Taylor expansion in z -> z+pk*w, modulo p^(2k+1).
            quadratic=6*(z*z-x)
            if any((f//(pk*pk)+(d//pk)*w+quadratic*w*w)%p in squares[p] for w in range(p)):
                out.add((k,z))
    return out

def predicted(p,A,B,x,y,typ,K):
    mod=p**(K+1)
    if x%p:
        t=y*pow(x,-1,mod)%mod
        if typ in ('II','II*'):return set()
        if typ=='III':return {(1,t%p)}
        if typ in ('IV','IV*'):
            e=1 if typ=='IV' else 2
            return {(e,t%(p**e))} if (B//p**(2*e))%p in squares[p] else set()
        if typ=='III*':
            shift=(B//p**3)*pow(A//p**3,-1,p**3)*pow(t,-1,p**3)
            return {(3,(t-shift)%(p**3))}
        if typ=='I0*':
            roots=[w for w in range(p) if (w**3+(A//p**2)*w+B//p**3)%p==0]
            return {(2,(t+p*(w*pow(t,-1,p)%p))%(p*p)) for w in roots}
    else:
        if typ in ('II','II*'):raise AssertionError('impossible nonunit point')
        if typ in ('III','III*'):return set()
        if typ=='IV':return {(1,0)}
        if typ=='IV*':return {(2,((A//p**2)*pow(2*(y//p**2),-1,p**2))%(p**2))}
        if typ=='I0*':
            roots=[w for w in range(p) if (w**3+(A//p**2)*w+B//p**3)%p==0]
            return {(1,0)} if len(roots)==3 else set()

squares={p:{r*r%p for r in range(1,p)} for p in (5,7)}
counts=Counter(); models=Counter()
for p in (5,7):
    cases=[]
    for typ,a,b,dv in [('II',1,1,2),('II',3,1,2),('III',1,2,3),('III',1,4,3),('IV',2,2,4),('IV',4,2,4),('IV*',3,4,8),('IV*',5,4,8),('III*',3,5,9),('III*',3,7,9),('II*',4,5,10),('II*',6,5,10)]:
        for u in (1,2):
            cases.append((typ,p**a,p**b*u,dv//2))
    for a2 in range(p):
        for b3 in range(p):
            if (4*a2**3+27*b3*b3)%p:
                cases.append(('I0*',p*p*a2,p**3*b3,3))
    for typ,A,B,K in cases:
        models[p,typ]+=1;N=2*K+3
        xs=sorted(set([0]+[u*p**e for e in range(4) for u in range(1,p)]+[1+p*u for u in range(p)]))
        for x in xs:
            y=sqrtmod(x**3+A*x+B,p,N)
            if y is None:continue
            exactB=y*y-x**3-A*x
            got=actual(p,A,exactB,x,y,K);want=predicted(p,A,exactB,x,y,typ,K)
            assert got==want,(p,typ,A,exactB,x,y,got,want)
            counts[p,typ,'unit' if x%p else 'nonunit']+=1
print('MODEL COUNTS',dict(sorted(models.items())))
print('POINT COUNTS',dict(sorted(counts.items())))
print('TOTAL',sum(models.values()),'models,',sum(counts.values()),'local point samples; all exact finite-lift lattice counts agree')
z,t,h,x,A,B,s=S.symbols('z t h x A B s')
y=t*x
f=z**4-6*x*z*z+8*y*z-3*x*x-4*A
expr=f.subs(z,t+s)-(s**4+4*t*s**3+6*h*s*s+4*t*h*s+h*h+4*B/x)
expr=S.factor(expr.subs(h,t*t-x).subs(B,x*x*(t*t-x)-A*x))
assert expr==0,expr
print('SYMBOLIC: general unit-point expansion verified')

z,x,y,A,B=S.symbols('z x y A B')
f=z**4-6*x*z*z+8*y*z-3*x*x-4*A
disc=S.Poly(S.discriminant(f,z),y).rem(S.Poly(y*y-x**3-A*x-B,y)).as_expr()
assert S.factor(disc+4096*(4*A**3+27*B**2))==0
print('SYMBOLIC: disc(f_P)=2^8 Delta_E verified')

X,Y,q,d=S.symbols('X Y q d',nonzero=True)
def binary(U,V):
    return U**4-6*x*U*U*V*V+8*y*U*V**3-(3*x*x+4*A)*V**4
transformed=S.Poly(S.expand(binary(z*X+(z*d-q)*Y,X+d*Y)/q**2),X,Y)
coefficient=transformed.coeff_monomial(X**2*Y**2)
# First use monicity F(z)=q^2, then depression F'(z)=4qd.
remainder=S.factor(coefficient-(6*(z*z-x)-6*d*d))
identity=6*d*d*(f-q*q)/q**2-3*d*(S.diff(f,z)-4*q*d)/q
assert S.factor(remainder-identity)==0
print('SYMBOLIC: x prime = x-z^2+d^2 under monicity/depression verified')

results={
    'date':'2026-10-28',
    'primes':[5,7],
    'model_count':sum(models.values()),
    'point_count':sum(counts.values()),
    'all_finite_lattice_checks_passed':True,
    'symbolic_checks':['unit_point_expansion','quartic_discriminant','status_switching_coefficient'],
    'models':[{'p':p,'type':typ,'count':n} for (p,typ),n in sorted(models.items())],
    'points':[{'p':p,'type':typ,'x_status':status,'count':n}
              for (p,typ,status),n in sorted(counts.items())],
    'limitations':'Finite examples support the proof; no independent human review or formal verification.'
}
Path(__file__).with_name('FRONTIER_results.json').write_text(json.dumps(results,indent=2)+'\n')
