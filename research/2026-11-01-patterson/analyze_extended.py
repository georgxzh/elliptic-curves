#!/usr/bin/env python3
"""Stratified tests of proposed means; stderr is descriptive, not a p-value.

Includes quadratic-character-weighted means and excludes p dividing a.
Usage: python analyze_extended.py periods.bin output.csv [amax=400]
"""
import csv
import json
import math
import sys
from pathlib import Path
import numpy as np
from analyze_law import REC, C, factor, candidate


def powvec(base, exponent, modulus):
    # Safe here because p <= 30 million, so products fit uint64 exactly.
    b = np.full(len(modulus), base, dtype=np.uint64) % modulus
    e = exponent.copy()
    out = np.ones(len(modulus), dtype=np.uint64)
    while np.any(e):
        out = np.where(e & 1, out*b % modulus, out)
        b = b*b % modulus
        e >>= 1
    return out


def expected_twist(a, residue):
    if math.isqrt(a)**2 == a:
        return candidate(a)
    if a % 3 == 0 and math.isqrt(a//3)**2 == a//3:
        return candidate(a) * (1 if residue == 1 else -1 if residue == 7 else 0)
    return 0.


def main(path, output, amax=400):
    records = np.fromfile(path, dtype=REC)
    ps = records['p'].astype(np.uint64)
    assert np.all(ps[1:] > ps[:-1]) and np.all(ps % 3 == 1)
    assert ps.max() <= 30000000
    eta = np.stack([records['eta0'], records['eta1'], -1-records['eta0']-records['eta1']], axis=1)
    # Larger split/inert products, square factors, and exact cube correlations.
    extras = set()
    for q in [7, 13, 19, 31, 37, 43]:
        for r in [2, 5, 11, 17, 23, 29]:
            extras.update([q*r, q*q*r, q*r*r, 8*q*r])
    aa = sorted(set(range(1, amax+1)) | extras | {729, 1000, 4096, 3**8, 2**12})
    fs = {a: factor(a) for a in aa}
    qq = sorted(set().union(*(set(f) for f in fs.values())))
    w = np.ones(len(ps), dtype=np.uint64)
    e = (ps-1)//3
    b = records['g'].astype(np.uint64)
    while np.any(e):
        w = np.where(e & 1, w*b % ps, w)
        b = b*b % ps
        e >>= 1
    cls, rho = {}, {}
    for q in qq:
        v = powvec(q, (ps-1)//3, ps)
        cls[q] = np.where(v == 1, 0, np.where(v == w, 1, 2)).astype(np.int8)
        rho[q] = np.where(powvec(q, (ps-1)//2, ps) == 1, 1, -1).astype(np.int8)
    masks = []
    # Full range, matching previous p>=2^16 direct comparison, and disjoint dyads.
    ranges = [(int(ps.min()), int(ps.max())+1, 'all'), (65536, int(ps.max())+1, 'high')]
    ranges += [(2**k, min(2**(k+1), int(ps.max())+1), 'dyadic') for k in range(12, int(ps.max()).bit_length())]
    for lo, hi, tag in ranges:
        for res in [0, 1, 7]:
            masks.append((lo, hi, tag, res, (ps >= lo) & (ps < hi) & ((ps % 12 == res) if res else True)))
    summary = []
    with open(output, 'w', newline='') as fh:
        fields = ['a', 'mode', 'range', 'lo', 'hi_exclusive', 'p_mod_12', 'count', 'mean', 'stderr', 'candidate', 'z']
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for a in aa:
            c = np.zeros(len(ps), dtype=np.int32)
            character = np.ones(len(ps), dtype=np.int8)
            valid = np.ones(len(ps), dtype=bool)
            for q, exponent in fs[a].items():
                c += exponent*cls[q]
                if exponent % 2: character *= rho[q]
                valid &= ps != q
            values = (1+3*eta[np.arange(len(ps)), c % 3])/np.cbrt(ps.astype(float))
            for mode, vals in [('G', values), ('rhoG', values*character)]:
                for lo, hi, tag, res, mask in masks:
                    sample = vals[mask & valid]
                    if len(sample) < 2: continue
                    pred = candidate(a) if mode == 'G' else expected_twist(a, res)
                    mean = float(sample.mean())
                    se = float(sample.std(ddof=1)/math.sqrt(len(sample)))
                    row = dict(a=a, mode=mode, range=tag, lo=lo, hi_exclusive=hi, p_mod_12=res,
                               count=len(sample), mean=mean, stderr=se, candidate=pred, z=(mean-pred)/se)
                    writer.writerow(row)
                    if tag == 'high': summary.append(row)
            if a % 100 == 0: print('processed', a, flush=True)
    result = dict(primes=len(ps), a_count=len(aa), pmax=int(ps.max()), C=C,
                  note='Correlated deterministic samples; standardized residuals are not calibrated significance tests.',
                  worst_high=sorted(summary, key=lambda r: abs(r['z']), reverse=True)[:30],
                  anchors=[r for r in summary if r['a'] in [1,2,3,4,7,9,25,35,77,143,323]])
    Path(output+'.summary.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('anchors','worst_high')}, indent=2))
    print('worst', result['worst_high'][:3])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 400)
