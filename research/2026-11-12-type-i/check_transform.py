#!/usr/bin/env python3
"""Exact finite metaplectic transforms over Eisenstein quotient rings.

Standard library only. Roots of unity are reduced modulo the exact
cyclotomic polynomial; no floating point or asymptotic experiment.
"""
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import lcm
from pathlib import Path


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(n, x):
    return n*x[0], n*x[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def conj(x):
    return x[0]-x[1], -x[1]


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def trace(x):
    return 2*x[0]-x[1]


def key(x, modulus):
    a, b = mul(x, conj(modulus))
    n = norm(modulus)
    return a % n, b % n


def reps(modulus):
    n = norm(modulus)
    found = {}
    for x in product(range(n), repeat=2):
        found.setdefault(key(x, modulus), x)
        if len(found) == n:
            return list(found.values())
    raise AssertionError('Incomplete quotient representatives')


def cubic(z, prime):
    """Return exponent of omega, or None for zero, at a prime ideal."""
    if key(z, prime) == (0, 0):
        return None
    n = norm(prime)
    e = (n-1)//3
    out = (1, 0)
    z = tuple(a % n for a in z)
    while e:
        if e % 2:
            out = tuple(a % n for a in mul(out, z))
        z = tuple(a % n for a in mul(z, z))
        e //= 2
    for j, root in enumerate([(1, 0), (0, 1), (-1, -1)]):
        if key(out, prime) == key(root, prime):
            return j
    raise AssertionError('Cubic value not a cube root of unity')


def chi_r(z, factors):
    values = [cubic(z, p) for p in factors]
    return None if None in values else sum(values) % 3


def chi4(z):
    return {(1, 0): 0, (0, 1): 2, (1, 1): 1}.get(
        (z[0] % 2, z[1] % 2))


def kappa(z):
    n = norm(z) % 4
    return 0 if n % 2 == 0 else 2-n


def divide_monic(a, b):
    a = list(a)
    out = [0]*(len(a)-len(b)+1)
    for i in range(len(out)-1, -1, -1):
        out[i] = a[i+len(b)-1]
        for j, v in enumerate(b):
            a[i+j] -= out[i]*v
    assert not any(a)
    return tuple(out)


@lru_cache(None)
def cyclotomic(n):
    p = [-1]+[0]*(n-1)+[1]
    for d in range(1, n):
        if n % d == 0:
            p = divide_monic(p, cyclotomic(d))
    return tuple(p)


class Roots:
    def __init__(self, order):
        self.m = order
        self.polynomial = cyclotomic(order)

    def zero(self):
        return [0]*self.m

    def shifted_add(self, dest, src, shift, coefficient=1):
        for j, v in enumerate(src):
            if v:
                dest[(j+shift) % self.m] += coefficient*v

    def reduced(self, values):
        a = list(values)
        p = self.polynomial
        degree = len(p)-1
        nonzero = [(j, v) for j, v in enumerate(p[:-1]) if v]
        for i in range(len(a)-1, degree-1, -1):
            if a[i]:
                v = a[i]
                for j, c in nonzero:
                    a[i-degree+j] -= v*c
                a[i] = 0
        return tuple(a[:degree])


def check_case(r, factors, exhaustive=False):
    R = norm(r)
    assert all((p[0] % 3, p[1] % 3) == (1, 0) for p in factors)
    q = scale(4, r)
    rr = reps(r)
    qr = [add(mul(r, b), scale(4, c))
          for b in product(range(4), repeat=2) for c in rr]
    assert len({key(x, q) for x in qr}) == 16*R
    unit = lambda x: kappa(x) != 0 and chi_r(x, factors) is not None
    units = [x for x in qr if unit(x)]
    roots = Roots(lcm(3, 4*R))
    m = roots.m
    phase = lambda z: trace(mul(z, conj(r)))*(m//(4*R)) % m
    omega = m//3
    lam = (1, 2)
    lam_char = chi_r(lam, factors)
    assert chi4(lam) == 0 and kappa(lam) == -1
    assert chi_r((4, 0), factors) == chi4(r)

    # Direct additive Fourier transform for EVERY residue, including nonunits.
    hats = {}
    for d in qr:
        value = roots.zero()
        for x in units:
            j = (phase(mul(x, d))-omega*chi_r(x, factors)) % m
            value[j] += kappa(x)
        hats[key(d, q)] = value
        if not unit(d):
            assert not any(roots.reduced(value))
    G = hats[key((1, 0), q)]
    for d in units:
        rhs = roots.zero()
        roots.shifted_add(rhs, G, omega*chi_r(d, factors), kappa(d))
        assert roots.reduced(hats[key(d, q)]) == roots.reduced(rhs)

    # Independent conjugate cubic Gauss sum at r; CRT scalar (9).
    gbar = roots.zero()
    for x in rr:
        chi = chi_r(x, factors)
        if chi is not None:
            exponent = (trace(mul(x, conj(r)))*(m//R)-omega*chi) % m
            gbar[exponent] += 1
    rhs = roots.zero()
    roots.shifted_add(rhs, gbar, -omega*chi_r((4, 0), factors),
                      -4*kappa(r))
    assert roots.reduced(G) == roots.reduced(rhs)

    # Solve exactly the 81 a d=1 congruence in DR (5.23).
    inverse81 = {}
    one = key((1, 0), q)
    for a in units:
        d = next(d for d in units if key(scale(81, mul(a, d)), q) == one)
        inverse81[key(a, q)] = d

    selected = qr if exhaustive else [
        (0, 0), (1, 0), (0, 1), (1, 1), (1, 2), (2, 0),
        lam, r, scale(2, r), add(r, (1, 0)), *factors,
    ]
    tested = []
    for v in selected:
        actual = roots.zero()
        for a in units:
            d = inverse81[key(a, q)]
            shift = omega*(lam_char+chi4(a)+chi_r(a, factors))+phase(mul(a, v))
            roots.shifted_add(actual, hats[key(d, q)], shift)

        # Exact Ramanujan sum checked against its prime-factor evaluation.
        cr = 1
        for p in factors:
            cr *= norm(p)-1 if key(v, p) == (0, 0) else -1
        ramanujan = roots.zero()
        for x in rr:
            if chi_r(x, factors) is not None:
                exponent = trace(mul(mul(x, v), conj(r)))*(m//R) % m
                ramanujan[exponent] += 1
        scalar = roots.zero()
        scalar[0] = cr
        assert roots.reduced(ramanujan) == roots.reduced(scalar)

        predicted = roots.zero()
        if kappa(v):
            roots.shifted_add(predicted, gbar,
                              omega*(2*lam_char-chi4(v)),
                              16*kappa(v)*cr)
        assert roots.reduced(actual) == roots.reduced(predicted)
        tested.append({'v': list(v), 'ramanujan': cr})
    return dict(r=r, norm=R, quotient_size=16*R, cyclotomic_order=m,
                fourier_residues_checked=len(qr),
                transformed_values_checked=len(tested),
                selected_values=None if exhaustive else tested)


def main():
    cases = [((1, 0), [], True), ((1, 3), [(1, 3)], True),
             ((4, 3), [(4, 3)], False), ((-2, 3), [(-2, 3)], False),
             ((-5, 0), [(-5, 0)], False),
             ((7, 0), [(1, 3), (-2, -3)], False)]
    results = [check_case(*c) for c in cases]
    # A concrete obstruction to erasing either local character factor.
    assert kappa((1, 3)) == -1  # d primary of norm7, so kappa(d^3)=-1
    assert chi4((0, 1)) == 2    # dual conjugated factor at omega is omega
    assert F(1, 12)+F(3, 2)*F(9, 20) == F(91, 120)
    assert F(3, 4)*(F(11, 20)-3*F(9, 20)) == -F(3, 5)
    assert 27*16**2 == 6912
    report = dict(cases=results,
                  total_fourier_residues=sum(c['fourier_residues_checked'] for c in results),
                  total_metaplectic_values=sum(c['transformed_values_checked'] for c in results),
                  kernel_denominator_constant=6912,
                  budget_second_exponent='91/120',
                  endpoint_dual_scale_exponent='-3/5',
                  status='Exact cyclotomic checks only. No analytic estimate, '
                         'GRH statement, or prime asymptotic is numerically certified.')
    Path(__file__).with_name('checks.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'cases'}, indent=2))


if __name__ == '__main__':
    main()
