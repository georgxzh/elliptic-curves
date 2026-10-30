#!/usr/bin/env python3
"""Bounded target search with exact rational halving, not a completeness proof."""

from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
import sympy as sp

B = 197225
P = (F(-56), F(147))
Z = sp.Symbol("z")


def add(P,Q):
    if P is None: return Q
    if Q is None: return P
    x,y = P
    u,v = Q
    if x == u and y == -v: return None
    m = (v-y)/(u-x) if x != u else 3*x*x/(2*y)
    a = m*m-x-u
    return a, m*(x-a)-y


def halves(T):
    if T is None:
        return [None]  # No nonzero rational 2-torsion for this B.
    u,v = T
    assert v != 0
    polynomial = sp.Poly(Z**4-4*sp.Rational(u)*Z**3-8*B*Z-4*sp.Rational(u)*B,
                         Z, domain=sp.QQ)
    roots = polynomial.ground_roots()
    out = []
    for a in roots:
        a = F(int(sp.numer(a)),int(sp.denom(a)))
        b = (a**3-3*u*a*a-2*B)/(2*v)
        R = (a,b)
        if b*b == a**3+B and add(R,R) == T:
            out.append(R)
    assert len(out) <= 1
    return out


def binary_label(R):
    if R is None: return 0
    x = R[0]
    if x.denominator % 7 == 0 or x.numerator % 7:
        return 0
    unit = x/7
    label = unit.numerator * pow(unit.denominator,-1,7) % 7
    assert label in (3,5,6)
    return label


def main():
    cutoff = 100000
    points = []
    assert (-59)**3+B < 0
    for x in range(-58,cutoff+1):
        yy = x**3+B
        if yy < 0: continue
        y = isqrt(yy)
        if y*y == yy:
            points.append((F(x),F(y)))
            if y: points.append((F(x),F(-y)))
    bounded_count = len(points)
    # An exact chord construction supplies this target beyond the cutoff.
    extra = (F(22427440),F(106211014035))
    assert add(P,add((F(35),F(490)),(F(35),F(490)))) == extra
    points.extend([extra,(extra[0],-extra[1])])
    records = []
    for Q in points:
        assert Q[1]**2 == Q[0]**3+B
        for R in halves(add(Q,(P[0],-P[1]))):
            label = binary_label(R)
            # Source component at 7 is 6; source at 5 is the identity.
            output = (int(label not in (0,6)),int(Q[0] % 5 == 0))
            records.append({"target":[str(a) for a in Q],
                            "half_difference":None if R is None else [str(a) for a in R],
                            "binary_label_of_R":label,
                            "nonstandard_at_7_and_5":list(output)})
    assert bounded_count == 30 and len(records) == 6
    outputs = sorted({tuple(a["nonstandard_at_7_and_5"]) for a in records})
    assert outputs == [(0,0),(1,1)]
    result = {"status":"PASS", "B":B,"source":[str(a) for a in P],
              "bounded_x_range":[-58,cutoff],"bounded_integral_points":bounded_count,
              "additional_targets_beyond_cutoff":2,"targets_in_source_2_class":records,
              "observed_outputs":outputs,"abstract_possible_outputs":4,
              "scope":"Only the stated finite target set is exhausted. Missing outputs may occur at larger integral targets; no uniform deficit is proved."}
    rendered = json.dumps(result,indent=2)+"\n"
    Path(__file__).with_name("integral_output_probe.json").write_text(rendered)
    print(rendered,end="")


if __name__ == "__main__":
    main()
