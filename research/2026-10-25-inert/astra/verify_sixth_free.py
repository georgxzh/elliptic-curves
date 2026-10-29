"""Finite checks of all six valuation cases; standard library only.

Points are exact p-adic approximations modulo p^7, not claimed global points.
For m>0 all residues in the repeated-root disk modulo p^3 are examined.
The square and derivative conditions independently generate a set of actual
lattice labels, which is compared with the theorem's predicted exact set.
This tests necessity and local attainment, not the global Thue bound.
"""

from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("original_verify", HERE.parent / "verify.py")
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def predicted(p, m, u, x, y):
    if m in (0, 1, 5):
        return set()
    if m in (2, 4):
        if pow(u % p, (p - 1) // 2, p) != 1:
            return set()
        e = m // 2
        center = y * pow(x, -1, p**e) % p**e if x % p else 0
        return {(e, center)}
    if x % p:
        t = y * pow(x, -1, p**2) % p**2
        return {(2, (t + p * v) % p**2) for v in range(p)
                if ((t * v)**3 + u) % p == 0}
    return {(1, 0)} if pow(-3 % p, (p - 1) // 2, p) == 1 else set()


def points(p, m):
    for u in range(1, p):
        B = p**m * u
        # Every unit x residue and every y root; higher digits are Hensel lifts.
        for x in range(1, p):
            for y0 in range(1, p):
                if (y0*y0 - x**3 - B) % p == 0:
                    yield B, x, old.lift_sqrt(x**3 + B, y0, p, 7)
        if m in (2, 4):
            e = m // 2
            for X in range(p):
                for Y0 in range(1, p):
                    if (Y0*Y0-u) % p == 0:
                        Y = old.lift_sqrt(u + p**e * X**3, Y0, p, 7-2*e)
                        yield B, p**e * X, p**e * Y
    if m == 3:
        # Exact integer points, including y=0, with v_p(B)=3.
        for X in range(1, p):
            for Y in range(p):
                x, y = p*X, p*p*Y
                yield y*y-x**3, x, y
    if m == 0:
        # Include nonsingular-reduction points with x=0 and/or y=0.
        for x in range(p):
            for y in range(p):
                B = y*y-x**3
                if B % p and (not x or not y):
                    yield B, x, y


def check():
    counts = Counter()
    coverage = Counter()
    examples = {}
    for p in (5, 7, 11, 13, 19):
        modulus = p**7
        for m in range(6):
            for B, x, y in points(p, m):
                assert old.vp(B, p) == m
                assert (y*y-x**3-B) % modulus == 0
                u = B // p**m
                want = predicted(p, m, u, x, y)
                seen = set()
                if m:
                    center = y * pow(x, -1, p) % p if x % p else 0
                    residues = range(center, p**3, p)
                else:
                    residues = range(p)
                for z in residues:
                    F = (z**4-6*x*z*z+8*y*z-3*x*x) % modulus
                    derivative = 4*(z**3-3*x*z+2*y)
                    counts["residues_examined"] += 1
                    if F % p or derivative % p:
                        continue
                    if F == 0:
                        # A square indistinguishable from zero mod p^7 has
                        # valuation >=8, but its derivative has valuation <4.
                        assert old.vp(derivative, p) < 4
                        counts["zero_values_excluded_by_derivative"] += 1
                        continue
                    valuation = old.vp(F, p)
                    if valuation % 2 or not old.square_mod(F, p, 7):
                        continue
                    k = valuation // 2
                    if old.vp(derivative, p) < k:
                        counts["squares_excluded_by_derivative"] += 1
                        continue
                    assert k > 0
                    seen.add((k, z % p**k))
                    counts["admissible_residues"] += 1
                assert seen == want, (p, m, B, x, y, seen, want)
                kind = "unit_x" if x % p else "nonunit_x"
                coverage[f"m={m},{kind},lattices={1+len(seen)}"] += 1
                counts["point_cases"] += 1
                if m == 3:
                    key = f"{kind},lattices={1+len(seen)}"
                    examples.setdefault(key, {"p": p, "B": B, "x": x, "y": y,
                                               "nonstandard_lattices": sorted(seen)})
    # Check the genuinely new branches were exercised, including all cubic
    # splitting types, and both outcomes on the nonunit-x branch.
    for size in (1, 2, 4):
        assert coverage[f"m=3,unit_x,lattices={size}"]
    for size in (1, 2):
        assert coverage[f"m=3,nonunit_x,lattices={size}"]
    N = lambda p, K: sum(sum(p**j for j in range(k+1)) for k in range(K+1))
    assert (N(2, 11), N(3, 6), N(2, 7), N(3, 2)) == (8178, 1636, 502, 18)
    assert 4*8178*1636 == 53516832
    assert 4*502*18 == 36144
    return {"counts": dict(counts), "coverage": dict(sorted(coverage.items())),
            "cubic_examples": examples, "counterexamples": 0,
            "precision": "p^7; all repeated-disk residues modulo p^3",
            "primes": [5, 7, 11, 13, 19],
            "scope": "Finite exact modular checks; does not replace proof or establish novelty."}


if __name__ == "__main__":
    rendered = json.dumps(check(), indent=2) + "\n"
    (HERE / "sixth_free_results.json").write_text(rendered)
    print(rendered, end="")
