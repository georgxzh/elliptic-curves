#!/usr/bin/env python3
"""Check exact quotient counting independently of p-adic and descent claims."""

from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    "old_codes", ROOT / "research/2026-10-28-refinements/global_verify_component_code.py"
)
old_codes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old_codes)


def output(word, source, masks):
    # Canonical representative of each coset modulo span(source_block).
    return tuple(min(word & mask, (word ^ source) & mask) for mask in masks)


def quotient_average(words, masks):
    total = Fraction()
    output_total = 0
    for source in words:
        kernel = [a for a in words if all(
            (a & mask) in (0, source & mask) for mask in masks
        )]
        fibers = Counter(output(a, source, masks) for a in words)
        assert set(fibers.values()) == {len(kernel)}
        assert len(fibers) * len(kernel) == len(words)
        total += Fraction(1, len(kernel))
        output_total += len(fibers)
    assert total == Fraction(output_total, len(words))
    return total


def main():
    pairs = 0
    sources = 0
    layouts = 0
    counts = []
    for n in range(7):
        spaces = list(old_codes.subspaces(n))
        counts.append(len(spaces))
        for two_blocks in range(n // 2 + 1):
            one_blocks = n - 2 * two_blocks
            masks = old_codes.masks_for([1] * one_blocks + [2] * two_blocks)
            for s, _, words in spaces:
                actual = quotient_average(words, masks)
                assert actual <= Fraction(2**s + 1, 2)
                # Comparison to the previous bound: each local quotient has
                # |V_p| choices if c_p=0, and half as many otherwise.
                assert actual <= 2**n * old_codes.weight(words, masks)
                if s == n:
                    assert actual == Fraction(3, 2)**one_blocks * Fraction(5, 2)**two_blocks
                pairs += 1
                sources += len(words)
            layouts += 1
    # Gaussian binomial sums independently check the enumeration scope.
    assert counts == [1, 2, 5, 16, 67, 374, 2825]
    result = {
        "status": "PASS", "maximum_ambient_dimension": 6,
        "subspaces_by_ambient_dimension": counts,
        "subspace_layout_pairs": pairs, "block_layouts": layouts,
        "source_component_cases": sources,
        "checked_properties": [
            "exact_fiber_equivalence_and_size", "orbit_average_identity",
            "dimension_upper_bound", "full_product_formula",
            "comparison_to_previous_binary_weight_bound"
        ],
        "scope": "Finite linear algebra only; not the local arithmetic or global descent."
    }
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("component_quotient_results.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
