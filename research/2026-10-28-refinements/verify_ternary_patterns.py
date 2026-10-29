"""Exhaustive small ternary support bounds, plus rational component arithmetic."""

from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path


def spaces(n):
    for k in range(n+1):
        for pivots in combinations(range(n), k):
            free = [j for j in range(n) if j not in pivots]
            slots = [(i,j) for i,p in enumerate(pivots) for j in free if j>p]
            for values in product(range(3), repeat=len(slots)):
                rows = [[0]*n for _ in pivots]
                for i,p in enumerate(pivots):
                    rows[i][p] = 1
                for (i,j),v in zip(slots,values):
                    rows[i][j] = v
                words = [tuple(0 for _ in range(n))]
                for row in rows:
                    words = [tuple((v+a*r)%3 for v,r in zip(w,row))
                             for w in words for a in range(3)]
                yield k,words


def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x,y=P;u,v=Q
    if x==u and y==-v: return None
    slope=(v-y)/(u-x) if x!=u else 3*x*x/(2*y)
    xx=slope*slope-x-u
    return xx,-y+slope*(x-xx)


def vp(a,p):
    if a==0: return 1000
    if isinstance(a,F): return vp(a.numerator,p)-vp(a.denominator,p)
    out=0
    while a%p==0: out+=1;a//=p
    return out


def residue(a,p):
    return a.numerator*pow(a.denominator,-1,p)%p


def component(P,p,e,root):
    if P is None or vp(P[0],p)<=0: return 0
    sign=residue(P[1]/p**e,p)*pow(root,-1,p)%p
    assert sign in (1,p-1)
    return 1 if sign==1 else 2


if __name__=="__main__":
    tested=0
    by_dimension={}
    for n in range(6):
        count=0
        distinct=set()
        for h,words in spaces(n):
            frozen=frozenset(words)
            assert frozen not in distinct
            distinct.add(frozen)
            supports={tuple(i for i,v in enumerate(w) if v) for w in words}
            assert len(supports)<=min(2**n,(3**h+1)//2)
            tested+=1;count+=1
        by_dimension[n]=count
    # Known subspace counts are independent checks on exhaustive generation.
    assert [by_dimension[n] for n in range(6)]==[1,2,6,28,212,2664]
    P=(F(5),F(15));B=100
    multiples=[None]
    for _ in range(8): multiples.append(add(multiples[-1],P))
    labels=[component(Q,5,1,2) for Q in multiples]
    assert labels==[(j*labels[1])%3 for j in range(len(labels))]
    for Q in multiples:
        if Q: assert Q[1]**2==Q[0]**3+B
    result={"ternary_subspaces_checked":tested,"ambient_dimension_max":5,
            "subspaces_by_ambient_dimension":by_dimension,
            "component_example":{"B":B,"P":[5,15],"prime":5,
                                 "labels_of_multiples_0_through_8":labels},
            "status":"PASS","scope":"Finite linear algebra and exact rational example; not a proof of global descent or the local quotient classification."}
    rendered=json.dumps(result,indent=2)+"\n"
    Path(__file__).with_name("ternary_pattern_results.json").write_text(rendered)
    print(rendered,end="")
