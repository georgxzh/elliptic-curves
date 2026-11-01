#!/usr/bin/env python3
"""Measure the untwisted law: mean of G_p(a) / p^(1/3) over primes p = 1 mod 3.

Candidate law, from the shape of Patterson's cubic theta coefficients.  Write a
positive integer a = a1 * a2^2 * a3^3 with a1, a2 squarefree and coprime.  Then

    mean G_p(a) / p^(1/3) -> 2 C a1^(-1/3)   if a2 = 1,
    mean G_p(a) / p^(1/3) -> 0               otherwise,

where C = (2 pi)^(2/3) / (3 Gamma(2/3)).  This script prints the measurement
and the candidate side by side.  It treats split primes (= 1 mod 3), inert
primes (= 2 mod 3) and 3 as separate cases, since nothing guarantees one rule.
"""
import json
import math
import sys

import numpy as np

REC = np.dtype([("p", "<u4"), ("g", "<u4"), ("eta0", "<f8"), ("eta1", "<f8")])
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


def candidate(a):
    value = 2 * C
    for q, e in factor(a).items():
        if e % 3 == 2:
            return 0.0
        if e % 3 == 1:
            value *= q ** (-1 / 3)
    return value


def main(path, amax=60, pmin=0):
    r = np.fromfile(path, dtype=REC)
    r = r[r["p"] >= pmin]
    ps = r["p"].astype(np.int64)
    gs = r["g"].tolist()
    plist = ps.tolist()
    eta = np.stack([r["eta0"], r["eta1"], -1 - r["eta0"] - r["eta1"]], axis=1)
    primes_a = [q for q in range(2, amax + 1) if all(q % d for d in range(2, q))]
    cls = {}
    for q in primes_a:
        c = np.zeros(len(ps), dtype=np.int8)
        for i, (p, g) in enumerate(zip(plist, gs)):
            if p == q:
                continue
            w = pow(g, (p - 1) // 3, p)
            v = pow(q, (p - 1) // 3, p)
            c[i] = 0 if v == 1 else (1 if v == w else 2)
        cls[q] = c
    rows = []
    print(f"primes={len(ps)} range=[{ps.min()},{ps.max()}] 2C={2 * C:.5f}")
    print(f"{'a':>3} {'factors':>14} {'mean':>9} {'+-':>7} {'candidate':>9} {'z':>7} {'ratio':>7}")
    zs = []
    for a in range(1, amax + 1):
        f = factor(a)
        i = np.zeros(len(ps), dtype=np.int64)
        for q, e in f.items():
            i += e * cls[q]
        i %= 3
        G = 1 + 3 * eta[np.arange(len(ps)), i]
        # The cubic-coset formula only applies to nonzero a mod p.
        # Historically these few entries were incorrectly assigned a coset.
        G = np.where(a % ps == 0, ps, G)
        h = G / ps ** (1 / 3)
        mean, err = h.mean(), h.std(ddof=1) / math.sqrt(len(ps))
        cand = candidate(a)
        z = (mean - cand) / err
        zs.append(z)
        ratio = mean / cand if cand else float("nan")
        desc = ".".join(f"{q}^{e}" for q, e in f.items()) or "1"
        rows.append({"a": a, "mean": mean, "stderr": err, "candidate": cand, "z": z})
        print(f"{a:>3} {desc:>14} {mean:>9.4f} {err:>7.4f} {cand:>9.4f} {z:>7.2f} {ratio:>7.3f}")
    zs = np.array(zs)
    print(f"chi2={np.sum(zs**2):.1f} dof={len(zs)} max|z|={np.abs(zs).max():.2f}")
    with open(path + ".law.json", "w") as fh:
        json.dump({"primes": len(ps), "pmax": int(ps.max()), "C": C, "rows": rows}, fh, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 60, int(sys.argv[3]) if len(sys.argv) > 3 else 0)
