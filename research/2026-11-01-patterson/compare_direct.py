#!/usr/bin/env python3
"""Compare the exact integer sums S_p(X) with the Fourier series from the law.

mordell_direct.c computes S_p(X) = sum_{B=1}^{X} a_p(E_B) with X = floor(u p).
With mu(a) the limiting mean of G_p(a)/p^(1/3) from analyze_law.py, the exact
Fourier identity predicts, as p -> infinity through primes,

  p = 1 mod 12:  mean S_p / p^(5/6) -> -(1/pi) sum_a m1(a) sin(2 pi a u) / a
  p = 7 mod 12:  mean S_p / p^(5/6) -> -(1/pi) sum_a m7(a) (1-cos(2 pi a u)) / a

where m1(a) = mu(a) on squares and three times squares, m7(a) = mu(a) on
squares and -mu(a) on three times squares, and both vanish elsewhere.
"""
import csv
import json
import math
import sys
from collections import defaultdict

C = (2 * math.pi) ** (2 / 3) / (3 * math.gamma(2 / 3))


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def mu(a):
    value = 2 * C
    for q, e in factor(a).items():
        if e % 3 == 2:
            return 0.0
        if e % 3 == 1:
            value *= q ** (-1 / 3)
    return value


def coherent_terms(amax):
    """Return (a, m1, m7) for a up to amax on which the mean can be non-zero."""
    out = []
    for a in range(1, amax + 1):
        f = factor(a)
        odd = {q for q, e in f.items() if e % 2}
        if not odd:
            m = mu(a)
            out.append((a, m, m))
        elif odd == {3}:
            m = mu(a)
            out.append((a, m, -m))
    return [t for t in out if t[1]]


TERMS = coherent_terms(2_000_000)


def phi1(u):
    return -sum(m1 * math.sin(2 * math.pi * a * u) / a for a, m1, _ in TERMS) / math.pi


def phi7(u):
    return -sum(m7 * (1 - math.cos(2 * math.pi * a * u)) / a for a, _, m7 in TERMS) / math.pi


def main(path, min_bin):
    tot = defaultdict(lambda: [0, 0.0, 0.0])
    K = None
    for row in csv.DictReader(open(path)):
        if int(row["bin"]) < min_bin:
            continue
        K = int(row["K"])
        key = (int(row["p_mod_12"]), int(row["k"]))
        tot[key][0] += int(row["count"])
        tot[key][1] += float(row["sum"])
        tot[key][2] += float(row["sum2"])
    rows, chi2 = [], 0.0
    print(f"terms={len(TERMS)} K={K}")
    print(f"{'res':>3} {'u':>7} {'mean':>9} {'+-':>7} {'predict':>9} {'z':>6}")
    for (res, k), (n, s1, s2) in sorted(tot.items()):
        u = k / K
        mean = s1 / n
        err = math.sqrt(max(s2 / n - mean * mean, 0) / n)
        pred = phi1(u) if res == 1 else phi7(u)
        # At u = 1/2 with p = 1 mod 4 the symmetry a_p(E_-B) = a_p(E_B) forces S_p = 0.
        z = (mean - pred) / err if err else 0.0
        chi2 += z * z
        rows.append({"residue": res, "u": u, "mean": mean, "stderr": err, "predicted": pred, "z": z, "primes": n})
        print(f"{res:>3} {u:>7.4f} {mean:>9.4f} {err:>7.4f} {pred:>9.4f} {z:>6.2f}")
    print(f"chi2={chi2:.1f} dof={len(rows)}")
    with open(path + ".cmp.json", "w") as fh:
        json.dump({"rows": rows, "chi2": chi2}, fh, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 16)
