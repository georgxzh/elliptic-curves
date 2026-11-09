#!/usr/bin/env python3
"""Exact exploratory checks; not a substitute for the written proofs.

Run from any directory. Requires Python 3 and SymPy. Default compares with
validation.json; --write explicitly regenerates that file.
"""
import argparse
from collections import Counter
from fractions import Fraction
import json
from math import isqrt, prod
from pathlib import Path

import sympy as sp


def primes(limit):
    return [n for n in range(2, limit + 1)
            if all(n % d for d in range(2, isqrt(n) + 1))]


def quartic_checks():
    t, a, b, X = sp.symbols("t a b X")
    f = t**4 - 6*a*t**2 + 8*b*t - 3*a**2
    assert sp.expand(t*sp.diff(f, t) - f - 3*(t*t-a)**2) == 0
    q = X**2 + (a-t*t)*X + a*a + a*t*t - 2*b*t
    assert sp.expand((X-a)*q - (X**3+b*b-a**3-(b+t*(X-a))**2)) == 0
    assert sp.expand(sp.discriminant(q, X)-f) == 0
    pairs = {(sp.Rational(i), sp.Rational(j))
             for i in range(-10, 11) for j in range(-10, 11)}
    for r in [sp.Rational(i, j) for i in range(-5, 6) if i
              for j in range(1, 5)]:
        pairs.add((r*r, r**3))
    for aa, bb in pairs:
        polynomial = sp.Poly(f.subs({a: aa, b: bb}), t)
        # Squarefree part ensures this independent root count is DISTINCT.
        roots = polynomial.sqf_part().count_roots(-sp.oo, sp.oo)
        assert roots == (1 if aa == bb == 0 else 2), (aa, bb, roots)
    return {"symbolic_identities": 3, "exact_parameter_pairs": len(pairs),
            "method": "SymPy squarefree part and exact real-root count",
            "integer_grid": [-10, 10], "includes_rational_triple_roots": True}


def count_checks():
    details = []
    for p in primes(101):
        working = []
        for a in range(p):
            counts = [0]*p
            values = [(x**3+a*x) % p for x in range(p)]
            # Direct enumeration of (x,y), placing each in its unique b bin.
            for value in values:
                for y in range(p):
                    counts[(y*y-value) % p] += 1
            assert sum(counts) == p*p
            if p > 2:
                collision_count = sum(c*c for c in Counter(values).values())
                assert sum((n-p)**2 for n in counts) == p*(collision_count-p)
            if len(set(counts)) == 1:
                working.append(a)
        expected = list(range(2)) if p == 2 else [0, 1] if p == 3 else (
            [0] if p % 3 == 2 else [])
        assert working == expected, (p, working)
        details.append({"p": p, "constant_count_classes": working})
    return {"prime_limit": 101, "parameter_classes": sum(d["p"] for d in details),
            "prime_results": details}


def polynomial_checks():
    t = sp.symbols("t")
    # Checks the finite-prefix trap, not the infinite hypothesis or proof.
    for m in range(1, 9):
        p = 2 + prod(t-j for j in range(1, m+1))
        assert sp.degree(p, t) == m
        assert all(p.subs(t, j)**3+1 == 9 for j in range(1, m+1))
    # Independently verify the finite-difference/interpolation identity on
    # several integer-valued polynomials with nonintegral coefficients.
    examples = [t*(t-1)/2, t*(t-1)*(t-2)/6, t**4-3*t+7]
    for h in examples:
        difference = h
        for _ in range(sp.degree(h, t)+1):
            difference = sp.expand(difference.subs(t, t+1)-difference)
        assert difference == 0
    return {"finite_prefix_counterexamples": 8,
            "finite_difference_examples": len(examples),
            "scope": "illustrations only; universal result rests on written proof"}


def reserve_checks():
    residue_primes = []
    for p in primes(199):
        if p % 4 != 3:
            continue
        squares = {x*x % p for x in range(1, p)}
        count = sum(all((a+d) % p in squares for d in [-1, 0, 1])
                    for a in range(p))
        assert count == (p-3)//8
        residue_primes.append(p)
    sides = [Fraction(41, 15), Fraction(101, 21), Fraction(156, 35)]
    assert sum(sides) == 12
    assert 6*prod(6-s for s in sides) == 36

    def squarefree(b):
        return b != 0 and all(b % (d*d) for d in range(2, isqrt(abs(b))+1))

    def tangent(x, y):
        if y == 0:
            return None
        slope = Fraction(3*x*x, 2*y)
        xx = slope*slope-2*x
        yy = y+slope*(xx-x)
        return xx, yy

    integral_start_count = 0
    survivors = []
    for b in range(-100, 101):
        if not squarefree(b):
            continue
        for x in range(-50, 101):
            value = x**3+b
            if value <= 0 or isqrt(value)**2 != value:
                continue
            for y in [isqrt(value), -isqrt(value)]:
                integral_start_count += 1
                q = tangent(x, y)
                if not all(c.denominator == 1 for c in q):
                    continue
                r = tangent(*q)
                if r is not None and all(c.denominator == 1 for c in r):
                    survivors.append([b, x, y])
    assert sorted(survivors) == [[1, 0, -1], [1, 0, 1], [1, 2, -3], [1, 2, 3]]
    return {"consecutive_residue_primes": residue_primes,
            "triangle_perimeter": "12", "triangle_area_squared": "36",
            "tangent_B_range": [-100, 100], "tangent_x_range": [-50, 100],
            "integral_nonvertical_start_points": integral_start_count,
            "two_step_survivors": sorted(survivors)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = {"quartic": quartic_checks(), "counts": count_checks(),
              "polynomial": polynomial_checks(), "reserves": reserve_checks()}
    target = Path(__file__).with_name("validation.json")
    if args.write:
        target.write_text(json.dumps(result, indent=2)+"\n")
    else:
        assert result == json.loads(target.read_text()), "Recorded results differ"
    print("All exact checks passed.")
    print(f"Quartic parameter pairs: {result['quartic']['exact_parameter_pairs']}")
    print(f"Finite-field a classes: {result['counts']['parameter_classes']}")
    print("These bounded checks support, but do not replace, the proofs.")


if __name__ == "__main__":
    main()
