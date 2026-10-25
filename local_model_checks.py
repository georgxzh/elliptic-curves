"""Exploratory checks, not a manuscript or a proof of a novel theorem.

Tests necessary square-value conditions for monic depressed quartic changes
in the repeated-root disk. Tests component-pair counts independently.
"""
import itertools
import json


def sqrt_lift(value, p, precision):
    root, modulus = 1, p
    for _ in range(1, precision):
        root += (((value-root*root)//modulus)*pow(2*root, -1, p) % p)*modulus
        modulus *= p
    assert (root*root-value) % modulus == 0
    return root


def square_mod_odd_prime_power(a, p, precision):
    if a == 0:
        return True
    valuation = 0
    while a % p == 0:
        valuation += 1
        a //= p
    return valuation % 2 == 0 and pow(a % p, (p-1)//2, p) == 1


rows = []
for p in (5, 7, 11):
    for k in (1, 2, 4, 5):
        precision, modulus = k+1, p**(k+1)
        for unit in range(1, p):
            # An actual local smooth point with x=1, constructed to this precision.
            y = sqrt_lift(1+unit*p**k, p, precision)
            t = y
            split = pow(unit, (p-1)//2, p) == 1
            square_count = checked = 0
            for z in range(t % p, modulus, p):
                value = (z**4-6*z*z+8*y*z-3) % modulus
                actual = square_mod_odd_prime_power(value, p, precision)
                expected = (k in (2, 4) and split and (z-t) % p**(k//2) == 0)
                assert actual == expected, (p, k, unit, z, value)
                square_count += actual
                checked += 1
            rows.append(dict(p=p, v_B=k, unit=unit, residues=checked,
                             square_values=square_count, matches_prediction=True))


component_checks = []
for moduli in ((1,), (2,), (3,), (4,), (6,), (2, 2)):
    elements = list(itertools.product(*(range(m) for m in moduli)))
    add = lambda a, b: tuple((x+y) % m for x, y, m in zip(a, b, moduli))
    for target in elements:
        pairs = [(a, b) for i, a in enumerate(elements) for b in elements[i:]
                 if add(a, b) == target]
        fixed = sum(add(a, a) == target for a in elements)
        assert 2*len(pairs) == len(elements)+fixed
        component_checks.append(dict(group=list(moduli), target=list(target),
                                     unordered_pairs=len(pairs), doubling_fiber=fixed))

# For type IV, the two invariant pairs in the nonsplit case are {0,0}
# and {1,2}; the latter has no individually rational components.
cyclic3 = [(0, 0), (1, 2)]
frobenius_fixed_pairs = [pair for pair in cyclic3
                        if sorted((-a) % 3 for a in pair) == list(pair)]
rational_component_pairs = [pair for pair in frobenius_fixed_pairs
                            if all((-a) % 3 == a for a in pair)]
assert len(frobenius_fixed_pairs) == 2 and rational_component_pairs == [(0, 0)]

print(json.dumps(dict(
    scope="Finite arithmetic and component-combinatorics checks only; global orbit gluing and novelty require separate review.",
    local_cases=len(rows), residues_checked=sum(r['residues'] for r in rows),
    local_counterexamples=0, local_checks=rows,
    component_checks=component_checks,
    nonsplit_IV=dict(all_invariant_pairs=frobenius_fixed_pairs,
                     pairs_with_rational_components=rational_component_pairs),
), indent=2))
