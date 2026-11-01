#!/usr/bin/env python3
"""Test the stationary-phase prediction for twisted cubic exponential sums.

G_p(a) = sum_x e(a x^3/p).  Prediction, for primes p = 1 mod 3 in a given class
mod 12, with C = (2 pi)^(2/3) / (3 Gamma(2/3)):

    mean of (a/p) G_p(a) / p^(1/3) -> C a^(-1/3)   if (a/p) is constant = 1 there,
    mean -> -C a^(-1/3)                            if constant = -1,
    mean -> 0                                      otherwise.

Reads the binary records written by gauss_periods.c.
"""
import json
import math
import sys

import numpy as np

REC = np.dtype([("p", "<u4"), ("g", "<u4"), ("eta0", "<f8"), ("eta1", "<f8")])
C = (2 * math.pi) ** (2 / 3) / (3 * math.gamma(2 / 3))


def squarefree_part(n):
    s, d = 1, 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e % 2:
            s *= d
        d += 1
    return s * n


def expected_sign(a, residue):
    """(a/p) on primes p = residue mod 12, p = 1 mod 3, or 0 if it varies."""
    s = squarefree_part(a)
    if s == 1:
        return 1
    if s == 3:
        return 1 if residue == 1 else -1
    return 0


def main(path, amax=40, pmin=0):
    r = np.fromfile(path, dtype=REC)
    r = r[r["p"] >= pmin]
    ps = r["p"].astype(np.int64)
    eta = np.stack([r["eta0"], r["eta1"], -1 - r["eta0"] - r["eta1"]], axis=1)
    primes_a = [q for q in range(2, amax + 1) if all(q % d for d in range(2, q))]
    cls, leg = {}, {}
    for q in primes_a:
        cq = np.zeros(len(ps), dtype=np.int8)
        lq = np.zeros(len(ps), dtype=np.int8)
        for i, (p, g) in enumerate(zip(ps.tolist(), r["g"].tolist())):
            if q == p:
                continue
            w = pow(g, (p - 1) // 3, p)
            v = pow(q, (p - 1) // 3, p)
            cq[i] = 0 if v == 1 else (1 if v == w else 2)
            lq[i] = 1 if pow(q, (p - 1) // 2, p) == 1 else -1
        cls[q], leg[q] = cq, lq
    kummer = (1 + 3 * eta[:, 0]) / (2 * np.sqrt(ps))
    out = {
        "file": path.replace("\\", "/").split("/")[-1],
        "primes": int(len(ps)),
        "pmin": int(ps.min()),
        "pmax": int(ps.max()),
        "C": C,
        "rows": [],
    }
    print(f"primes={len(ps)} range=[{ps.min()},{ps.max()}] C={C:.6f}")
    weight = np.mean(ps ** (-1 / 6))
    print(f"mean cos(theta)={kummer.mean():.5f}  stationary-phase={C / 2 * weight:.5f}")
    print(f"{'a':>3} {'res':>3} {'mean':>9} {'+-':>7} {'predicted':>9} {'z':>7}")
    for a in range(1, amax + 1):
        i = np.zeros(len(ps), dtype=np.int64)
        s = np.ones(len(ps), dtype=np.int64)
        n = a
        for q in primes_a:
            while n % q == 0:
                n //= q
                i += cls[q]
                s *= leg[q]
        i %= 3
        G = 1 + 3 * eta[np.arange(len(ps)), i]
        h = s * G / ps ** (1 / 3)
        for residue in (1, 7):
            m = ps % 12 == residue
            mean = h[m].mean()
            err = h[m].std(ddof=1) / math.sqrt(m.sum())
            pred = expected_sign(a, residue) * C * a ** (-1 / 3)
            z = (mean - pred) / err
            out["rows"].append(
                {"a": a, "residue": residue, "mean": mean, "stderr": err, "predicted": pred, "z": z}
            )
            print(f"{a:>3} {residue:>3} {mean:>9.4f} {err:>7.4f} {pred:>9.4f} {z:>7.2f}")
    zs = np.array([row["z"] for row in out["rows"]])
    out["chi2"] = float((zs**2).sum())
    out["dof"] = int(len(zs))
    print(f"chi2={out['chi2']:.1f} dof={out['dof']} max|z|={np.abs(zs).max():.2f}")
    with open(path + ".json", "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 40, int(sys.argv[3]) if len(sys.argv) > 3 else 0)
