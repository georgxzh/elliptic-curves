#!/usr/bin/env python3
"""Exact finite checks for the Q4 report; no prime-average experiment.

Only Python's standard library is used. All arithmetic is integral or
rational. Analytic estimates, GRH statements, and prime asymptotics are
not certified by these checks.
"""
import json
from math import isqrt
from fractions import Fraction as F
from itertools import product
from pathlib import Path


R = list(product(range(4), repeat=2))
I_POWERS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def multiply(x, y):
    a, b = x
    c, d = y
    return ((a*c-b*d) % 4, (a*d+b*c-b*d) % 4)


def norm(x):
    a, b = x
    return (a*a-a*b+b*b) % 4


def kappa(x):
    n = norm(x)
    return 0 if n % 2 == 0 else 2-n


def trace_product(x, y):
    a, b = x
    c, d = y
    return (2*a*c-a*d-b*c-b*d) % 4


def primes(limit):
    return [n for n in range(5, limit)
            if all(n % d for d in range(2, isqrt(n)+1))]


def main():
    fourier = []
    for y in R:
        value = tuple(sum(kappa(x)*I_POWERS[trace_product(x, y)][j]
                          for x in R) for j in range(2))
        assert value == (-4*kappa(y), 0)
        fourier.append(dict(y=y, kappa=kappa(y), transform=value))
    for x, y in product(R, repeat=2):
        assert kappa(multiply(x, y)) == kappa(x)*kappa(y)
    for x in R:
        assert kappa(multiply(multiply(x, x), x)) == kappa(x)
    assert kappa((1, 0)) == 1 and kappa((1, 2)) == -1
    assert sum(kappa(x) for x in R) == 0
    assert sum(kappa(x) != 0 for x in R) == 12

    # Check the complete local parametrization and its character formula.
    teich = [(1, 0), (0, 1), (3, 3)]  # 1, omega, omega^2
    units = set()
    for v in teich:
        for a, b in product(range(2), repeat=2):
            z = multiply(v, (1+2*a, 2*b))
            units.add(z)
            assert kappa(z) == (-1)**b  # trace(a+b omega) mod 2 = b
    assert units == {x for x in R if kappa(x)}

    # Check the two independent character witnesses used by Astra.
    # Norm(1+3 omega)=7. At pi=-2+3 omega of norm19, omega=7 mod19.
    assert 1-3+9 == 7 and kappa((1, 3)) == -1
    assert 4+6+9 == 19
    assert (7*7+7+1) % 19 == 0
    assert pow(4, (19-1)//3, 19) == pow(7, 2, 19)

    eps, eta = F(1, 10**6), F(1, 100)
    a, b = F(3, 5), F(2, 5)
    exponents = {
        'w_term': a*F(5, 6)+b*F(5, 6)-b*F(9, 20),
        'third_term': a*(F(7, 12)+eps/2)+b*F(5, 6),
        'fourth_term': a*F(11, 24)+b*F(29, 24)+eps/2,
        'fifth_term': a/2+b*(1+eta)+eps/2,
        'sixth_term': a/2+F(1, 2)+eps/2,
        'model_term': a*F(5, 6)+b/3,
        'excluded_prime_divisors': a*F(5, 6)-b/6,
    }
    expected = [F(49, 75), F(41, 60)+3*eps/10,
                F(91, 120)+eps/2, F(7, 10)+2*eta/5+eps/2,
                F(4, 5)+eps/2, F(19, 30), F(13, 30)]
    assert list(exponents.values()) == expected
    assert all(v < F(5, 6)-F(1, 100) for v in exponents.values())
    assert 2*b-a == F(1, 5)
    # The remaining rho term has gap rho/2; delta<=rho/4 by definition.

    jackson = []
    for L in range(1, 21):
        f = {n: F(L+1-abs(n), L+1) for n in range(-L, L+1)}
        square = {n: sum((f[k]*f.get(n-k, F(0)) for k in f), F(0))
                  for n in range(-2*L, 2*L+1)}
        c = F(2*(L+1)**2+1, 3*(L+1))
        assert square[0] == c
        j = {n: v/c for n, v in square.items()}
        assert j[0] == 1 and all(0 <= v <= 1 for v in j.values())
        assert all(j[n] == j[-n] for n in j)
        jackson.append(dict(L=L, normalization=str(c)))

    energy = []
    for p in primes(102):
        counts = [0]*p
        for x in range(p):
            counts[pow(x, 3, p)] += 1
        pairs = sum(v*v for v in counts)
        nonzero_gauss_energy = p*pairs-p*p
        expected_energy = 2*p*(p-1) if p % 3 == 1 else 0
        assert nonzero_gauss_energy == expected_energy
        energy.append(dict(prime=p, cube_equal_pairs=pairs,
                           nonzero_gauss_energy=nonzero_gauss_energy))

    report = dict(
        local_fourier_values=fourier, multiplicativity_cases=256,
        cube_twist_cases=16, unit_parametrizations=12,
        conductor_witness={'one': 1, 'one_plus_two_omega': -1},
        primary_character_witness_norms=[7, 19],
        type_ii_exponents={k: str(v) for k, v in exponents.items()},
        jackson_normalizations=jackson, exact_gauss_energies=energy,
        status='Exact finite identities only; no prime asymptotic, GRH, '
               'coefficient-class bound, or averaged-tail estimate is tested.')
    Path(__file__).with_name('checks.json').write_text(
        json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(local_fourier_cases=16,
                          multiplicativity_cases=256,
                          cube_twist_cases=16,
                          jackson_cases=len(jackson),
                          finite_energy_cases=len(energy),
                          exponent_checks=len(exponents),
                          status='All exact checks passed.'), indent=2))


if __name__ == '__main__':
    main()
