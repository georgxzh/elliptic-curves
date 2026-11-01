#!/usr/bin/env python3
"""Exact check of the Fourier identity for Mordell Frobenius traces.

For a prime p > 3 and any integer B, let a_p(B) = -sum_x legendre(x^3+B, p).
For an integer a, let G_p(a) = sum_x e(a x^3 / p), which is real.  Then

  p = 1 mod 4:  a_p(B) = -(2/sqrt p) sum_{a=1}^{(p-1)/2} (a/p) G_p(a) cos(2 pi a B/p)
  p = 3 mod 4:  a_p(B) = -(2/sqrt p) sum_{a=1}^{(p-1)/2} (a/p) G_p(a) sin(2 pi a B/p)

The script checks this at high precision, cross-checks a_p against PARI's
ellap for B != 0 mod p, and checks the elementary symmetries used later.
"""
import sys

import mpmath as mp
from cypari import pari

mp.mp.dps = 40


def legendre(n, p):
    n %= p
    if n == 0:
        return 0
    return 1 if pow(n, (p - 1) // 2, p) == 1 else -1


def a_p(B, p):
    return -sum(legendre(x * x * x + B, p) for x in range(p))


def G(a, p):
    two_pi = 2 * mp.pi
    return mp.fsum(mp.cos(two_pi * (a * pow(x, 3, p) % p) / p) for x in range(p))


def rhs(B, p, Gs):
    root = mp.sqrt(p)
    two_pi = 2 * mp.pi
    trig = mp.cos if p % 4 == 1 else mp.sin
    total = mp.fsum(
        legendre(a, p) * Gs[a] * trig(two_pi * a * B / p)
        for a in range(1, (p - 1) // 2 + 1)
    )
    return -(2 / root) * total


def main():
    primes = [int(q) for q in pari("primes([5, 400])")]
    worst, checks, pari_checks = mp.mpf(0), 0, 0
    for p in primes:
        Gs = {a: G(a, p) for a in range(1, (p - 1) // 2 + 1)}
        for B in range(0, p):
            exact = a_p(B, p)
            err = abs(exact - rhs(B, p, Gs))
            worst = max(worst, err)
            checks += 1
            assert err < mp.mpf(10) ** -25, (p, B, exact)
            if B:
                e = pari(f"ellinit([0,0,0,0,{B}])")
                assert int(pari.ellap(e, p)) == exact, (p, B)
                pari_checks += 1
            assert a_p(-B, p) == legendre(-1, p) * exact
        assert sum(a_p(B, p) for B in range(p)) == 0, p
    print(f"primes={len(primes)} identity_checks={checks} ellap_checks={pari_checks}")
    print(f"max_abs_error={mp.nstr(worst, 5)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
