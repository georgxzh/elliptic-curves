#!/usr/bin/env python3
"""Exact abstract-code checks; no elliptic realization is claimed."""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from verify_component_quotients import old_codes, quotient_average


def expand(word, dims):
    offset = 0
    values = []
    for dim in dims:
        u = (word >> offset) & 1
        if dim == 1:
            values.append(u)
        else:
            v = (word >> (offset + 1)) & 1
            values.extend((u, v, u ^ v))
        offset += dim
    return sum(v << i for i, v in enumerate(values))


def check_small_codes():
    cases = witnesses = 0
    for n in range(7):
        for two in range(n // 2 + 1):
            dims = [1] * (n - 2 * two) + [2] * two
            masks = old_codes.masks_for(dims)
            for s, _, words in old_codes.subspaces(n):
                expanded = {a: expand(a, dims) for a in words}
                nonminimal = 0
                actual = Fraction()
                intersecting = True
                for c in words:
                    kernel = [a for a in words if all(
                        (a & mask) in (0, c & mask) for mask in masks
                    )]
                    shortened = [a for a in words if expanded[a] & ~expanded[c] == 0]
                    assert kernel == shortened
                    decompositions = [a for a in words if a and a != c and all(
                        not ((a & mask) and ((a ^ c) & mask)) for mask in masks
                    )]
                    assert len(decompositions) == (len(kernel) - 2 if c else 0)
                    if decompositions:
                        intersecting = False
                        nonminimal += 1
                        witnesses += len(decompositions)
                    actual += Fraction(1, len(kernel))
                bound = Fraction(2**s + 1, 2)
                assert (actual == bound) == intersecting
                assert actual <= bound - Fraction(nonminimal, 4)
                cases += 1
    return cases, witnesses


def binary_simplex(s):
    words = [sum(((a & ell).bit_count() % 2) << (ell - 1)
                 for ell in range(1, 2**s)) for a in range(2**s)]
    assert len(set(words)) == 2**s
    sizes = [sum(a & ~c == 0 for a in words) for c in words]
    assert sizes == [1] + [2] * (2**s - 1)
    actual = sum((Fraction(1, size) for size in sizes), Fraction())
    assert actual == Fraction(2**s + 1, 2)
    if s <= 5:
        assert quotient_average(words, old_codes.masks_for([1] * (2**s - 1))) == actual
    return {"dimension": s, "length": 2**s - 1, "A": str(actual)}


def ternary_simplex(h):
    vectors = list(product(range(3), repeat=h))
    functionals = [v for v in vectors if any(v) and next(a for a in v if a) == 1]
    words = [tuple(sum(a*b for a, b in zip(v, ell)) % 3 for ell in functionals)
             for v in vectors]
    assert len(set(words)) == 3**h
    supports = {tuple(i for i, a in enumerate(w) if a) for w in words}
    assert len(supports) == (3**h + 1) // 2
    return {"dimension": h, "length": len(functionals), "support_count": len(supports)}


def main():
    cases, witnesses = check_small_codes()
    binary = [binary_simplex(s) for s in range(9)]
    ternary = [ternary_simplex(h) for h in range(7)]
    # Independently count a product of two simplex codes, on disjoint blocks.
    left = [0, 0b011, 0b101, 0b110]
    right = [0, 0b111]
    words = [a | (b << 3) for a in left for b in right]
    assert quotient_average(words, old_codes.masks_for([1] * 6)) == Fraction(5, 2) * Fraction(3, 2)
    coefficient = -55**3
    point = (130, 1425)
    torsion = (55, 0)
    slope = Fraction(point[1] - torsion[1], point[0] - torsion[0])
    xx = slope**2 - point[0] - torsion[0]
    yy = slope * (point[0] - xx) - point[1]
    translated = (xx, yy)
    assert translated == (176, -2299)
    assert coefficient == -(5**3)*(11**3)
    labels = []
    for x, y in (torsion, point, translated):
        assert y*y == x*x*x + coefficient
        assert Fraction(x).denominator == Fraction(y).denominator == 1
        labels.append(tuple(int(x % p == 0) for p in (5, 11)))
    assert labels == [(1, 1), (1, 0), (0, 1)]
    for p in (5, 11):
        assert len([a for a in range(p) if (a**3 + coefficient // p**3) % p == 0]) == 1
    assert quotient_average([0, 1, 2, 3], [1, 2]) == Fraction(9, 4)
    result = {
        "status": "PASS", "subspace_layout_pairs": cases,
        "ordered_disjoint_decomposition_witnesses": witnesses,
        "checked_properties": ["binary_expansion_shortening_identity",
            "disjoint_decomposition_criterion", "equality_criterion",
            "nonminimal_word_deficit", "direct_product_example",
            "binary_simplex_attainment", "ternary_simplex_attainment",
            "arithmetic_complete_image_example"],
        "binary_simplex": binary, "ternary_simplex": ternary,
        "arithmetic_example": {"B": coefficient, "T": list(torsion),
            "P": list(point), "P_plus_T": [int(xx), int(yy)],
            "component_primes": [5, 11], "labels_T_P_P_plus_T": labels,
            "image_dimension": 2, "A": "9/4", "dimension_bound": "5/2"},
        "scope": "Simplex-code sharpness is abstract, with no elliptic realization asserted; includes one exact nonextremal arithmetic example."
    }
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("code_obstruction_results.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
