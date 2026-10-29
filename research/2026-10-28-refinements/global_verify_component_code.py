#!/usr/bin/env python3
"""Exhaustively check the component-code inequalities in dimensions <=6.

This checks finite linear algebra, not the imported elliptic descent or
Thue inputs and not the local p-adic component proof.
"""

from fractions import Fraction
from itertools import combinations, product
import json
import sys


def subspaces(n):
    """Generate every binary subspace once, using reduced echelon bases."""
    for k in range(n + 1):
        for pivots in combinations(range(n), k):
            free = [j for j in range(n) if j not in pivots]
            slots = [(i, j) for i, p in enumerate(pivots) for j in free if j > p]
            for bits in product((0, 1), repeat=len(slots)):
                rows = [1 << p for p in pivots]
                for (i, j), bit in zip(slots, bits):
                    rows[i] |= bit << j
                words = [0]
                for row in rows:
                    words += [v ^ row for v in words]
                yield k, rows, words


def masks_for(dims):
    masks = []
    offset = 0
    for d in dims:
        masks.append(((1 << d) - 1) << offset)
        offset += d
    return masks


def weight(words, masks):
    return sum((Fraction(1, 2 ** sum(bool(v & mask) for mask in masks))
                for v in words), Fraction()) / len(words)


def main():
    coefficient = 67821390
    x, y = Fraction(91), Fraction(8281)
    assert y*y-x*x*x == coefficient == 2*3**2*5*7**3*13**3
    slope = 3*x*x/(2*y)
    x2 = slope*slope-2*x
    y2 = slope*(x-x2)-y
    assert (x2, y2) == (Fraction(-719, 4), Fraction(-62999, 8))
    assert y2*y2 == x2*x2*x2+coefficient
    for p in (7, 13):
        u = coefficient // p**3
        roots = [w for w in range(p) if (w**3+u) % p == 0]
        assert len(roots) == 3 and 91//p % p in roots
        assert x2.numerator % p and x2.denominator % p
    assert 16 * Fraction(5, 8) == 10
    checked = 0
    layouts = 0
    for n in range(7):
        spaces = list(subspaces(n))
        assert len({frozenset(words) for _, _, words in spaces}) == len(spaces)
        for c in range(n // 2 + 1):
            b = n - 2 * c
            masks = masks_for([1] * b + [2] * c)
            m = len(masks)
            maxima = {}
            for s, rows, words in spaces:
                actual = weight(words, masks)
                q = min(c, s // 2)
                bound = Fraction(5, 8) ** q * Fraction(3, 4) ** (s - 2 * q)
                assert actual <= bound, (b, c, rows, actual, bound)
                maxima[s] = max(maxima.get(s, Fraction()), actual)
                projection_sum = Fraction()
                for subset in range(1 << m):
                    mask = sum(masks[i] for i in range(m) if subset >> i & 1)
                    projection_sum += Fraction(1, len({v & mask for v in words}))
                assert actual == projection_sum / (1 << m)
                for i in range(len(rows)):
                    smaller = [0]
                    for j, row in enumerate(rows):
                        if i != j:
                            smaller += [v ^ row for v in smaller]
                    assert actual <= weight(smaller, masks)
                checked += 1
            for s, maximum in maxima.items():
                q = min(c, s // 2)
                assert maximum == Fraction(5, 8) ** q * Fraction(3, 4) ** (s - 2 * q)
            layouts += 1
    if "--json" in sys.argv[1:]:
        print(json.dumps({
            "status": "PASS",
            "maximum_ambient_dimension": 6,
            "subspace_layout_pairs": checked,
            "block_layouts": layouts,
            "checked_properties": [
                "dimension_bound", "abstract_sharpness", "projection_rank_identity",
                "monotonicity_for_tested_codimension_one_subspaces", "exact_example_arithmetic"
            ],
            "example": {
                "B": coefficient, "point": [str(x), str(y)],
                "double": [str(x2), str(y2)], "nonzero_component_primes": [7, 13],
                "old_local_product": 16, "certified_weight_upper_bound": "5/8",
                "new_effective_local_product": 10
            }
        }, indent=2, sort_keys=True))
    else:
        print(f"PASS: {checked} subspace/layout pairs across {layouts} layouts.")
        print("Verified dimension bound, sharpness, projection-rank identity,")
        print("monotonicity against the tested codimension-one subspaces, and exact example arithmetic.")


if __name__ == "__main__":
    main()
