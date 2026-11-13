#!/usr/bin/env python3
"""Exact local-mass, exceptional-Euler-factor, and exponent checks.

Standard-library integer/rational arithmetic only. Finite computations
verify identities, not GRH or uniform analytic estimates.
"""
import json
from fractions import Fraction as F
from math import isqrt, prod
from pathlib import Path


def primes(limit):
    return [n for n in range(2, limit+1)
            if all(n % d for d in range(2, isqrt(n)+1))]


def local_mass(Q, t, z):
    D = (1+t)/(1-z)
    E = 1+(Q-1)*(D-1)
    assert E == (1+(Q-1)*t+(Q-2)*z)/(1-z)
    return D, E


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def multiply(p, q):
    out = [0]*(len(p)+len(q)-1)
    for j, a in enumerate(p):
        for k, b in enumerate(q):
            out[j+k] += a*b
    return trim(out)


def main():
    # Local factors enumerate BOTH squarefree e=0,1 and arbitrary cube k.
    # The rational grid tests the algebra and the stated monotone envelope.
    norms = [4, 7, 13, 19, 25, 31, 37, 43, 61, 67, 73, 79, 97, 121]
    mass_checks = 0
    for Q in norms:
        for t in [F(0), F(1, 2*Q), F(1, Q)]:
            for z in [F(0), F(1, 2*Q*Q), F(1, Q*Q)]:
                D, E = local_mass(Q, t, z)
                assert D >= 1 and E <= 2 and E/D <= 2
                for K in range(7):
                    direct_D = sum(t**e*z**k for e in [0, 1]
                                   for k in range(K+1))
                    direct_E = sum((Q-1 if e+3*k else 1)*t**e*z**k
                                   for e in [0, 1] for k in range(K+1))
                    assert direct_D == (1+t)*(1-z**(K+1))/(1-z)
                    assert E-direct_E == (Q-1)*(1+t)*z**(K+1)/(1-z)
                    mass_checks += 1
        assert local_mass(Q, F(1, Q), F(1, Q*Q))[1] == 2

    # Actual (rather than envelope) factors at sigma=3/2 for inert norms.
    inert_factors = []
    for p in [2, 5, 11]:
        Q = p*p
        t, z = F(1, p**3), F(1, p**8)
        D, E = local_mass(Q, t, z)
        assert E <= 2
        inert_factors.append(dict(prime=p, norm=Q, D=str(D), E=str(E)))

    # Products include both conjugate factors of the split prime 7.
    product_checks = []
    for qs in [[], [7], [7, 7], [7, 13, 25], [7, 7, 13, 19, 121]]:
        ratio = prod((local_mass(q, F(1, q), F(1, q*q))[1]
                      / local_mass(q, F(1, q), F(1, q*q))[0]
                      for q in qs), start=F(1))
        assert ratio <= 2**len(qs)
        product_checks.append(dict(norms=qs, ratio=str(ratio),
                                   ideal_prime_bound=2**len(qs)))

    # Cubic valuation support and the two quadratic factors in completion.
    cube_checks = 0
    for sign in [-1, 1]:
        for exponent in range(9):
            # Local Mobius inversion: c has exponent j=0 or1, h=cd.
            result = sum((-1)**j*sign**j*sign**(exponent-j)
                         for j in range(min(1, exponent)+1))
            assert result == (1 if exponent == 0 else 0)
            cube_checks += 1
    assert 1-(-1) == 2  # dropping kappa(d) fails already at exponent one
    for e in [0, 1]:
        for k in range(9):
            assert ((e+3*k) % 3) in [0, 1]
            assert (e+3*k > 0) == (e+k > 0)
    # At sigma=3/2 the ratio of successive ramified-3 terms is 3^-4.
    assert F(1, 2)-3*F(3, 2) == -4
    assert all(3*n-4 >= -1 for n in range(1, 10))
    assert all(3*n-3 >= -3 for n in range(10))

    # L_K(w,kappa)=L(w,chi_-4)L(w,chi_12), including 2 and3.
    euler_checks = []
    for p in primes(101):
        chi4 = 0 if p == 2 else (1 if p % 4 == 1 else -1)
        chi12 = 0 if p in [2, 3] else chi4*(1 if p % 3 == 1 else -1)
        rational_denominator = multiply([1, -chi4], [1, -chi12])
        if p == 2:
            hecke_denominator = [1]
        elif p == 3:
            hecke_denominator = [1, 1]
        elif p % 3 == 1:
            hecke_denominator = multiply([1, -chi4], [1, -chi4])
        else:
            hecke_denominator = [1, 0, -1]
        assert rational_denominator == hecke_denominator
        euler_checks.append(dict(prime=p, denominator=hecke_denominator))
    # Removing the 3 Euler factor of the reciprocal leaves exactly 1.
    reciprocal_at_three = [1, 1]
    inverse_removal = [(-1)**j for j in range(8)]
    assert multiply(reciprocal_at_three, inverse_removal)[:8] == [1]+[0]*7

    # Exact interpolation exponents and cutoff balance.
    for a in [F(1, 1000), F(1, 100), F(1, 20)]:
        eta = a
        left = F(1, 2)+2*a+eta
        uncond = left*F(1, 2)/(1+2*a)
        cond = left*F(2, 3)/(1+2*a)
        assert uncond == F(1, 4)+(a+eta)/(2*(1+2*a))
        assert cond == F(1, 3)+2*(a+eta)/(3*(1+2*a))
        assert uncond <= F(1, 4)+a
        assert cond+eta <= F(1, 3)+F(7, 3)*a

    bounds = {
        'old_unconditional': (F(1, 2), F(3, 4), F(4, 15)),
        'old_grh_interpolation': (F(1, 3), F(1), F(3, 10)),
        'new_unconditional': (F(1, 2), F(1, 4), F(4, 9)),
        'new_grh_cutoff': (F(3, 7), F(2, 7), F(17, 36)),
        'new_grh_interpolation': (F(1, 3), F(1, 3), F(1, 2)),
    }
    budget = {}
    for name, (a, b, threshold) in bounds.items():
        slope = 1+b-a
        assert (F(5, 6)-a)/slope == threshold
        budget[name] = dict(U_exponent=str(a), R_exponent=str(b),
                            average_R_exponent=str(slope),
                            threshold=str(threshold))
    assert F(1, 3)+F(9, 20) == F(47, 60)
    assert F(5, 6)-F(47, 60) == F(1, 20)
    assert F(1, 2)+F(3, 4)*F(9, 20) == F(67, 80)
    assert F(67, 80)-F(5, 6) == F(1, 240)
    assert F(4, 3)-F(11, 20) == F(47, 60)
    assert F(4, 3)-F(1, 2) == F(5, 6)

    for zu, zr, lu, lr in [(F(1, 3), -F(1, 6), F(1, 2), F(1, 4)),
                           (F(2, 7), -F(1, 7), F(3, 7), F(2, 7))]:
        assert F(3, 2)*zu == lu and F(1, 2)+F(3, 2)*zr == lr
        assert zu+2*zr == 0  # cutoff is1 whenR=U²

    report = dict(local_mass_checks=mass_checks, inert_exact_factors=inert_factors,
                  product_checks=product_checks, quadratic_cube_checks=cube_checks,
                  fixed_L_euler_checks=euler_checks, exponent_budget=budget,
                  case_one_exponent='47/60', case_one_saving='1/20',
                  status='Exact finite identities and rational exponent budgets only; '
                         'no analytic cancellation or GRH statement is certified.')
    Path(__file__).with_name('checks.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(local_mass_checks=mass_checks,
                          fixed_L_prime_checks=len(euler_checks),
                          quadratic_cube_checks=cube_checks,
                          exponent_budgets=len(budget),
                          status='All exact checks passed.'), indent=2))


if __name__ == '__main__':
    main()
