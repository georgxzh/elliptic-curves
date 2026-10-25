"""Independent arithmetic verification and analysis of the exhaustive scans."""
from __future__ import annotations

import csv
import hashlib
import itertools
import json
import math
import os
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/elliptic-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from sympy import factorint, primerange

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def read_rows(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def search_curve(a, b, bound):
    """Direct x-loop, independent of the C++ A,x,y -> B enumeration."""
    points = []
    for x in range(-bound, bound + 1):
        value = x**3 + a*x + b
        if value < 0:
            continue
        y = math.isqrt(value)
        if y*y == value:
            points.append((x, y))
    return points


def signed_count(points):
    return sum(1 if y == 0 else 2 for x, y in points)


def verify_data():
    # Full independent census of the smallest coefficient box at every cutoff.
    t = 4
    result = {}
    for l in (4, 16, 64, 256):
        counts = Counter()
        minimal_counts = Counter()
        for a in range(-t*t, t*t+1):
            for b in range(-t**3, t**3+1):
                if 4*a**3 + 27*b*b:
                    n = signed_count(search_curve(a, b, l*t))
                    counts[n] += 1
                    if not (a % 16 == 0 and b % 64 == 0):
                        minimal_counts[n] += 1
        stored = {int(r["N"]): int(r["models"]) for r in read_rows(DATA/f"hist_T{t}_L{l}.csv")}
        assert dict(counts) == stored, (l, counts, stored)
        stored_min = {int(r["N"]): int(r["minimal_models"]) for r in read_rows(DATA/f"hist_T{t}_L{l}.csv") if int(r["minimal_models"])}
        assert dict(minimal_counts) == stored_min
        result[f"independent_full_T4_L{l}"] = sum(counts.values())

    # Recompute every reported integer and fractional moment from the histograms.
    top_checks = 0
    for t in (4, 8, 16, 24, 32):
        summaries = read_rows(DATA/f"summary_T{t}.csv")
        for row in summaries:
            l = int(row["L"])
            hist = read_rows(DATA/f"hist_T{t}_L{l}.csv")
            assert sum(int(r["models"]) for r in hist) == int(row["models"])
            assert sum(int(r["minimal_models"]) for r in hist) == int(row["minimal_models"])
            for key, power in (("mean_N", 1), ("mean_N2", 2), ("mean_N_log2_5", math.log2(5)),
                               ("mean_N2_49", 2.49), ("mean_N2_75", 2.75), ("mean_N3", 3)):
                calculated = sum(int(r["models"])*int(r["N"])**power for r in hist)/int(row["models"])
                assert math.isclose(calculated, float(row[key]), rel_tol=1e-12), (t, l, key)
            for lead in read_rows(DATA/f"top_T{t}_L{l}.csv")[:5]:
                pts = search_curve(int(lead["A"]), int(lead["B"]), l*t)
                assert signed_count(pts) == int(lead["N"])
                assert sum(y == 0 for x, y in pts) == int(lead["torsion_points"])
                top_checks += 1
    result["independently_checked_leader_counts"] = top_checks
    result["histograms_and_all_six_moments_checked"] = 20
    return result


def valuation(n, p):
    assert n != 0
    n = abs(n)
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def verify_local_arithmetic():
    curves = defaultdict(list)
    for row in read_rows(DATA/"points_T8.csv"):
        a, b, x, y = (int(row[k]) for k in ("A", "B", "x", "y_nonnegative"))
        assert y*y == x**3 + a*x + b
        curves[a, b].append((x, y))
    pair_count = prime_cases = ramified_x_cases = square_denominator_checks = 0
    examples = []
    for (a, b), points in curves.items():
        disc = -16*(4*a**3 + 27*b*b)
        assert len(points) == len(set(points))
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            assert x1 != x2
            d = x2-x1
            pair_count += 1
            for numerator in (y2-y1, -y2-y1):
                slope = Fraction(numerator, d)
                xr = slope*slope-x1-x2
                assert xr.denominator == slope.denominator**2
                square_denominator_checks += 1
            for p in factorint(abs(d)):
                p = int(p)
                if p == 2 or disc % p == 0:
                    continue
                prime_cases += 1
                if y1 % p:
                    assert (Fraction(y2-y1, d).denominator % p != 0 or
                            Fraction(y2+y1, d).denominator % p != 0)
                else:
                    assert y2 % p == 0
                    assert y2 != y1 and y2 != -y1
                    k, r, s = valuation(d, p), valuation(y2-y1, p), valuation(y2+y1, p)
                    assert k == r+s and r >= 1 and s >= 1
                    assert valuation(Fraction(y2-y1,d).denominator,p) == s
                    assert valuation(Fraction(y2+y1,d).denominator,p) == r
                    ramified_x_cases += 1
                    if len(examples) < 10:
                        examples.append(dict(A=a, B=b, P=[x1,y1], Q=[x2,y2], p=p, k=k, r=r, s=s))

    final = read_rows(DATA/"summary_T8.csv")[-1]
    assert len(curves) == int(final["point_bearing"])
    assert sum(signed_count(points) for points in curves.values()) == int(final["points"])
    assert 2*pair_count == int(final["ordered_distinct_x_pairs"])

    # An infinite family refutes a good-prime integrality shortcut.
    family = []
    for p in primerange(3, 1000):
        p = int(p)
        a, b = 8-p**4, p*p
        p1, q1 = (0,p), (p*p,3*p)
        disc = -16*(4*a**3+27*b*b)
        assert disc % p and disc
        for x,y in (p1,q1):
            assert y*y == x**3+a*x+b
        xplus = Fraction(4-p**4, p*p)
        xminus = Fraction(16-p**4, p*p)
        assert xplus.denominator == xminus.denominator == p*p
        if p < 20:
            family.append(dict(p=p,A=a,B=b,x_P_plus_Q=str(xplus),x_P_minus_Q=str(xminus)))
    return dict(point_rows=sum(map(len,curves.values())), curves=len(curves),
                distinct_x_pairs=pair_count, good_odd_prime_cases=prime_cases,
                both_signs_nonintegral_cases=ramified_x_cases,
                square_denominator_checks=square_denominator_checks,
                examples=examples, counterexample_family_small_primes=family,
                counterexample_family_primes_checked=len(list(primerange(3,1000))))


def volume(l):
    # Integrate y >= 0. The real signed point count has volume 2*V_L.
    gauss_a, gauss_w = np.polynomial.legendre.leggauss(48)

    def inner(u):
        if abs(u) < 1e-10:
            return 2.0
        if u < 2:
            def primitive(c):
                return 2/(3*u)*(max(c+u,0)**1.5-max(c-u,0)**1.5)
            return primitive(u**3+1)-primitive(u**3-1)
        c = u**3 + u*gauss_a
        # Rationalization avoids loss of precision when c is large.
        values = 2/(np.sqrt(c+1)+np.sqrt(c-1))
        return float(values @ gauss_w)

    pieces = [-min(l,2), 0, min(l,2)]
    pieces += [x for x in (4,16,64,256) if 2 < x < l]
    if l > 2:
        pieces.append(l)
    pieces = sorted(set(pieces))
    value = sum(quad(inner,a,b,epsabs=1e-9,epsrel=1e-9,limit=250)[0]
                for a,b in zip(pieces,pieces[1:]))
    return value


def summarize(volumes):
    comparisons = []
    for t in (4,8,16,24,32):
        rows = {int(r["L"]):r for r in read_rows(DATA/f"summary_T{t}.csv")}
        lo, hi = rows[16],rows[256]
        comparison = dict(T=t, models=int(hi["models"]),
            mean_N_L256=float(hi["mean_N"]), mean_N3_L16=float(lo["mean_N3"]),
            mean_N3_L256=float(hi["mean_N3"]),
            mean_N3_minimal_L256=float(hi["minimal_mean_N3"]),
            cutoff_M3_increase_fraction=float(hi["mean_N3"])/float(lo["mean_N3"])-1,
            normalized_first_moment_L4=math.sqrt(t)*float(rows[4]["mean_N"]),
            predicted_normalized_first_moment_L4=volumes["4"]/2,
            normalized_first_moment_L256=math.sqrt(t)*float(hi["mean_N"]),
            predicted_normalized_first_moment_L256=volumes["256"]/2,
            multi_x_probability_L4=int(rows[4]["multi_x"])/int(rows[4]["models"]))
        hist = read_rows(DATA/f"hist_T{t}_L256.csv")
        sums = [sum(int(r["models"])*int(r["N"])**k for r in hist) for k in (1,2,3)]
        comparison["nonminimal_share_of_M3"] = 1-sum(int(r["minimal_models"])*int(r["N"])**3 for r in hist)/sums[2]
        comparison["models_N_at_least_20_share_M3"] = sum(int(r["models"])*int(r["N"])**3 for r in hist if int(r["N"])>=20)/sums[2]
        comparison["max_N_L256"] = max(int(r["N"]) for r in hist)
        comparisons.append(comparison)
    return comparisons


def make_plot(comparisons,volumes):
    fig, ax = plt.subplots(1,3,figsize=(14,4.3))
    colors = {4:"#295f98",16:"#de7e28",64:"#43956c",256:"#8c5ca6"}
    for l in colors:
        ts, m1, m3 = [],[],[]
        for t in (4,8,16,24,32):
            r = next(r for r in read_rows(DATA/f"summary_T{t}.csv") if int(r["L"])==l)
            ts.append(t); m1.append(math.sqrt(t)*float(r["mean_N"])); m3.append(float(r["mean_N3"]))
        ax[0].plot(ts,m1,"o-",color=colors[l],label=f"L={l}")
        ax[0].axhline(volumes[str(l)]/2,color=colors[l],alpha=.4,ls="--")
        ax[1].plot(ts,m3,"o-",color=colors[l],label=f"L={l}")
    ax[0].set(title="First moment approaches the volume limit",xlabel="Coefficient scale T",ylabel=r"$\sqrt{T}\,\mathbb{E}[N_{T,L}]$")
    ax[0].legend()
    ax[1].set(title="Third moment grows with the cutoff",xlabel="Coefficient scale T",ylabel=r"$\mathbb{E}[N_{T,L}^3]$")
    ax[1].legend()
    for key,label in (("mean_N3_L256","All integral models"),("mean_N3_minimal_L256","Models minimal under integer scaling")):
        ax[2].plot([r["T"] for r in comparisons],[r[key] for r in comparisons],"o-",label=label)
    ax[2].set(title="Scaling contributes little",xlabel="Coefficient scale T",ylabel="Third moment at L=256")
    ax[2].legend(fontsize=8)
    for a in ax:
        a.grid(alpha=.2)
    fig.suptitle("Exact bounded-coordinate searches; these are not complete integral-point counts",fontsize=12)
    fig.tight_layout()
    fig.savefig(ROOT/"results.png",dpi=170)
    plt.close(fig)


def main():
    checks = verify_data()
    print("Independent enumeration and histogram checks passed",flush=True)
    local = verify_local_arithmetic()
    print("Exact rational group-law checks passed",flush=True)
    volumes = {str(l):volume(l) for l in (4,16,64,256)}
    comparisons = summarize(volumes)
    make_plot(comparisons,volumes)
    result = dict(verification=checks,local_arithmetic=local,real_volumes=volumes,comparisons=comparisons)
    (ROOT/"analysis.json").write_text(json.dumps(result,indent=2)+"\n")
    # Artifact integrity; excludes itself and is regenerated after the notes are finalized.
    manifest = {}
    for path in sorted(DATA.glob("*.csv")):
        manifest[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    (ROOT/"data_sha256.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps({"verification":checks,"real_volumes":volumes,"comparisons":comparisons},indent=2))


if __name__ == "__main__":
    main()
