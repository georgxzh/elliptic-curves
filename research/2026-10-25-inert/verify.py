"""Exact checks of the local proof and row-lattice implementation.

Run: python research/2026-10-25-inert/verify.py
Writes results.json next to this script. This is finite verification, not a
replacement for the proofs. Only Python's standard library is required.
"""

from collections import Counter
from fractions import Fraction
from math import comb, gcd, isqrt
from pathlib import Path
import json


def vp(a, p, cap=100):
    if a == 0:
        return cap
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def square_mod(a, p, exponent):
    a %= p**exponent
    if not a:
        return True
    v = vp(a, p)
    return v % 2 == 0 and pow((a // p**v) % p, (p - 1) // 2, p) == 1


def lift_sqrt(a, root, p, exponent):
    modulus = p
    for _ in range(1, exponent):
        root += (((a - root * root) // modulus) * pow(2 * root, -1, p) % p) * modulus
        modulus *= p
    assert (root * root - a) % modulus == 0
    return root


def transform(coeffs, matrix):
    a, b, c, d = matrix
    det = a * d - b * c
    assert det
    out = [Fraction(0) for _ in range(5)]
    for i, coefficient in enumerate(coeffs):
        for r in range(5 - i):
            for s in range(i + 1):
                out[r + s] += Fraction(
                    coefficient * comb(4 - i, r) * comb(i, s)
                    * a**(4 - i - r) * c**r * b**(i - s) * d**s,
                    det * det,
                )
    return out


def coeffs(x, y):
    return [1, 0, -6 * x, 8 * y, -3 * x * x]


def eval_form(f, a, b):
    return sum(c * a**(4 - i) * b**i for i, c in enumerate(f))


def local_checks():
    counts = Counter()
    # Every unit u mod p; all unit x mod p^2 admitting y; both y signs.
    # Singular points: x=p^e*x0 with all x0 mod p^2 and both y signs.
    # For each point, exhaust the repeated-root disk mod p^(e+1).
    for p in (5, 7, 11, 13):
        for e in (1, 2):
            exponent = 2 * e + 1
            modulus = p**exponent
            for unit in range(1, p):
                B = p**(2 * e) * unit
                points = []
                for x in range(1, p * p):
                    if x % p == 0:
                        continue
                    for y0 in range(1, p):
                        if (y0 * y0 - x**3) % p == 0:
                            y = lift_sqrt(x**3 + B, y0, p, exponent)
                            points.append((x, y, "unit_x"))
                for root in range(1, p):
                    if (root * root - unit) % p:
                        continue
                    for x0 in range(p * p):
                        x = p**e * x0
                        y = p**e * lift_sqrt(unit + p**e * x0**3, root, p, e + 1)
                        points.append((x, y, "nonunit_x"))

                for x, y, kind in points:
                    assert (y * y - x**3 - B) % modulus == 0
                    center = y * pow(x, -1, modulus) % modulus if x % p else 0
                    counts[f"point_cases_{kind}"] += 1
                    for z in range(center % p, p**(e + 1), p):
                        F = (z**4 - 6 * x * z * z + 8 * y * z - 3 * x * x) % modulus
                        derivative = 4 * (z**3 - 3 * x * z + 2 * y)
                        counts["repeated_disk_residues"] += 1
                        if not square_mod(F, p, exponent):
                            continue
                        if F == 0:
                            # A square with this truncated value would have
                            # k>=e+1, excluded by the necessary derivative.
                            assert vp(derivative, p) < e + 1
                            counts["zero_value_excluded_by_derivative"] += 1
                            continue
                        k = vp(F, p) // 2
                        if vp(derivative, p) < k:
                            counts["square_excluded_by_derivative"] += 1
                            continue
                        assert k == e, (p, e, unit, x, y, z, k)
                        assert pow(unit, (p - 1) // 2, p) == 1
                        assert (z - center) % p**e == 0
                        counts[f"necessary_condition_survivors_{kind}"] += 1
    return dict(counts)


def row_lattice_key(matrix):
    """Exact row HNF, independent of the selected basis of the lattice."""
    a, b, c, d = matrix
    index = abs(a * d - b * c)
    # A lattice is determined by membership of points modulo its index.
    # For these small test examples, use the standard upper triangular
    # row basis (h,0),(r,g), with g=gcd(b,d), h=index/g.
    def egcd(v, w):
        if w == 0:
            return (abs(v), 1 if v >= 0 else -1, 0)
        g, r, s = egcd(w, v % w)
        return g, s, r - (v // w) * s
    g, u, v = egcd(b, d)
    h = index // g
    r = (u * a + v * c) % h
    return h, r, g


def matrix_checks():
    counts = Counter()
    examples = []
    lattice_groups = {}
    normalizations = {}
    for d in (-3, -1, 2, 5, 104, 2504):
        for n in (5, 7, 11, 13, 25, 49):
            B = d * n * n
            disc = -2**12 * 3**3 * B * B
            points = []
            for x in range(-50, 501):
                value = x**3 + B
                if value < 0:
                    continue
                y = isqrt(value)
                if y * y == value:
                    points.append((x, y))
            for x, y in points:
                f = coeffs(x, y)
                counts["integral_base_points"] += 1
                # Retain both determinant signs explicitly.
                assert transform(f, (1, 0, 0, -1)) == coeffs(x, -y)
                for a in range(-8, 9):
                    for b in range(0, 9):
                        if gcd(a, b) != 1:
                            continue
                        value = eval_form(f, a, b)
                        if value <= 0:
                            continue
                        D0 = isqrt(value)
                        if D0 * D0 != value or disc % value:
                            continue
                        for D in (D0, -D0):
                            # Depression and determinant solve the second
                            # row uniquely for each signed D.
                            nc = 3 * x * a * a * b - 6 * y * a * b * b + 3 * x * x * b**3
                            nd = a**3 - 3 * x * a * b * b + 2 * y * b**3
                            if nc % D or nd % D:
                                continue
                            c, dd = nc // D, nd // D
                            if gcd(gcd(a, b), gcd(c, dd)) != 1:
                                continue
                            matrix = a, b, c, dd
                            assert a * dd - b * c == D
                            target = transform(f, matrix)
                            if any(t.denominator != 1 for t in target):
                                continue
                            if target[2] % 6 or target[3] % 8:
                                continue
                            xx, yy = -target[2] // 6, target[3] // 8
                            assert target == coeffs(xx, yy)
                            assert yy * yy == xx**3 + B
                            counts["admissible_signed_matrices"] += 1
                            for p in (5, 7, 11, 13):
                                if 6 * d % p == 0 or n % p:
                                    continue
                                k, e = vp(D, p), vp(n, p)
                                group = (d, n, x, y, p)
                                if k == 0:
                                    label = "standard"
                                else:
                                    assert k == e
                                    assert pow(d % p, (p - 1) // 2, p) == 1
                                    assert b % p
                                    center = y * pow(x, -1, p**e) % p**e if x % p else 0
                                    assert (a - center * b) % p**e == 0
                                    assert (c - center * dd) % p**e == 0
                                    label = "nonstandard"
                                    counts["nonstandard_local_lattices_seen_with_multiplicity"] += 1
                                    if len(examples) < 8 and D > 0:
                                        examples.append({"d": d, "n": n, "p": p,
                                                         "P": [x, y], "Q": [int(xx), int(yy)],
                                                         "matrix": list(matrix), "det": D})
                                lattice_groups.setdefault(group, set()).add(label)
                            # Within each actual row lattice, normalize by
                            # one occurring matrix and verify the GL2 action.
                            key = (d, n, x, y, row_lattice_key(matrix))
                            if key not in normalizations:
                                normalizations[key] = matrix, target
                            else:
                                T, FT = normalizations[key]
                                ta, tb, tc, td = T
                                dt = ta * td - tb * tc
                                U = tuple(Fraction(v, dt) for v in
                                          (a * td - b * tc, -a * tb + b * ta,
                                           c * td - dd * tc, -c * tb + dd * ta))
                                assert all(v.denominator == 1 for v in U)
                                U = tuple(int(v) for v in U)
                                assert abs(U[0] * U[3] - U[1] * U[2]) == 1
                                assert transform(FT, U) == target
                                assert eval_form(FT, U[0], U[1]) == 1
                                counts["same_lattice_unimodular_normalizations"] += 1
    counts["local_groups_with_both_lattices"] = sum(len(v) == 2 for v in lattice_groups.values())
    assert counts["local_groups_with_both_lattices"] > 0
    assert counts["same_lattice_unimodular_normalizations"] > 0
    return dict(counts), examples


if __name__ == "__main__":
    local = local_checks()
    matrices, examples = matrix_checks()
    result = {"local": local, "matrices": matrices, "examples": examples,
              "counterexamples": 0,
              "scope": "Finite exact checks of selected p-adic points, both unit and nonunit x; bounded global points and first rows. Does not certify novelty or replace either proof."}
    rendered = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("results.json").write_text(rendered)
    print(rendered, end="")
