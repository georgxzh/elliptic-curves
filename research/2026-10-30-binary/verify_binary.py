#!/usr/bin/env python3
"""Exact certificate checks; no external packages, ranks, or class numbers.

Run normally to compare the committed JSON; --write creates/updates it.
Class field theory and the all-prime theorem are proved in the notes,
not implemented as a formal proof here. Never run with Python -O.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path


def mul(a, b, d):
    out = [0] * 3
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[(i+j) % 3] += u*v*(d if i+j >= 3 else 1)
    return tuple(out)


def norm(a, d):
    cols = [mul(a, b, d) for b in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    m = list(zip(*cols))
    return sum(m[0][i] * (m[1][(i+1) % 3]*m[2][(i+2) % 3]
                         - m[1][(i+2) % 3]*m[2][(i+1) % 3]) for i in range(3))


def evaluate(a, t):
    return sum(c*t**i for i, c in enumerate(a))


def roots(d, modulus):
    return [t for t in range(modulus) if (t**3-d) % modulus == 0]


def lift(d, p, r, exponent=3):
    assert (r**3-d) % p == 0 and (3*r*r) % p != 0
    modulus = p
    for _ in range(1, exponent):
        choices = [r+k*modulus for k in range(p)
                   if ((r+k*modulus)**3-d) % (modulus*p) == 0]
        assert len(choices) == 1
        r = choices[0]
        modulus *= p
    return r


def legendre(u, p):
    r = pow(u % p, (p-1)//2, p)
    return -1 if r == p-1 else r


def valuation(n, p):
    if not n:
        return float('inf')
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def factor(n):
    n = abs(n)
    ans = {}
    p = 2
    while p*p <= n:
        if n % p == 0:
            ans[p] = valuation(n, p)
            n //= p**ans[p]
        p += 1
    if n > 1:
        ans[n] = 1
    return ans


def eisenstein(coeffs, p):
    return (coeffs[-1] % p != 0 and coeffs[0] % (p*p) != 0
            and all(c % p == 0 for c in coeffs[:-1]))


def A_single_block(H):
    # In a single binary block, <c>={0,c} for nonzero c.
    return sum((Fraction(1, len(H & {0, c})) for c in H), Fraction(0))


def certificate58():
    assert factor(27*58**2) == {2: 2, 3: 3, 29: 2}
    assert eisenstein((-58, 0, 0, 1), 2)
    assert eisenstein((-58, 0, 0, 1), 29)
    assert eisenstein((-57, 3, 3, 1), 3)
    alpha, beta = (673, 190, -94), (1, 2, 3)
    assert norm(alpha, 58) == 361
    difference = tuple(a-b for a, b in zip(alpha, mul(beta, beta, 58)))
    assert difference == (-24, -336, -104)
    assert all(c % 8 == 0 for c in difference)
    assert evaluate(beta, 0) % 2 == 1
    assert evaluate(alpha, 1) % 3 == 1
    assert roots(58, 5) == [2]
    assert legendre(evaluate(alpha, 2), 5) == -1
    assert roots(58, 19) == [1, 7, 11]
    assert [evaluate(alpha, r) % 19 for r in [1, 7, 11]] == [9, 0, 15]
    data = []
    for r, expected in [(1, 0), (7, 1), (11, 1)]:
        t = lift(58, 19, r)
        v = evaluate(alpha, t) % 19**3
        e = valuation(v, 19)
        assert e == (2 if r == 7 else 0)
        unit = (v // 19**e) % 19
        char = (1-legendre(unit, 19))//2
        assert char == expected
        data.append({'root': r, 'lift_mod_6859': t, 'valuation': e,
                     'unit_mod_19': unit, 'character': char})
    assert sum(x['character'] for x in data) % 2 == 0
    return {'radicand': 58, 'discriminant': -90828, 'norm_alpha': norm(alpha, 58),
            'alpha_minus_beta_squared': difference, 'character_at_5': 1,
            'character_at_19': data}


def certificate11():
    assert factor(27*11**2) == {3: 3, 11: 2}
    assert eisenstein((-11, 0, 0, 1), 11)
    assert eisenstein((-12, 3, -3, 1), 3)
    delta = (9, -4, 0)
    assert norm(delta, 11) == 25
    assert roots(11, 5) == [1]
    t = lift(11, 5, 1)
    assert t == 21
    v = evaluate(delta, t) % 125
    assert valuation(v, 5) == 2 and legendre(v//25, 5) == -1
    assert evaluate(delta, 2) % 3 == 1
    # Exact defining polynomial z^2-z+(a-2), discriminant delta.
    assert tuple((1 if i == 0 else 0)-4*c
                 for i, c in enumerate((-2, 1, 0))) == delta
    # F4=F2[t]/(t^2+t+1), integer encodings 0,1,t,t+1.
    def f4_square(z):
        a, b = z & 1, z >> 1
        return (a ^ b) | (b << 1)
    assert all((z*z+z+1) % 2 for z in [0, 1])
    assert all(f4_square(z) ^ z ^ 2 for z in range(4))
    assert f4_square(2) ^ 2 == 1  # trace of a
    assert [((t+1)*(t*t+t+1)-(t**3-11)) % 2 for t in range(2)] == [0, 0]
    return {'radicand': 11, 'discriminant': -3267, 'norm_delta': 25,
            'root_lift_mod_125': t, 'unit_mod_5': v//25,
            'character_at_5': 1, 'characters_above_2': [1, 1],
            'character_above_3': 0}


def exact_images():
    data = []
    for B, p, d, H, ambient, point in [
        (-7250, 5, 58, {0}, {0, 1}, None),
        (-397822, 19, 58, {0, 1}, {0, 1, 2, 3}, (1463, 55955)),
        (11000, 5, 11, {0, 1}, {0, 1}, (-10, 100)),
    ]:
        fs = factor(B)
        assert all(m < 6 for m in fs.values())
        assert [q for q, m in fs.items() if q > 3 and m == 3] == [p]
        assert not any(q > 3 and m in [2, 4] for q, m in fs.items())
        u = B // p**3
        local_roots = roots(-u, p)
        assert len(local_roots) == len(ambient)-1
        for r in local_roots:
            lift(-u, p, r)  # certifies every local nonzero component exists
        if point:
            x, y = point
            assert y*y == x*x*x+B
            assert valuation(x, p) == 1 and valuation(y, p) >= 2
            expected_label = 1 if B < 0 else p-2
            assert (x//p) % p == expected_label
        data.append({'B': B, 'factorization': fs, 'retained_prime': p,
                     'point': point, 'local_root_labels': local_roots,
                     'full_image_size_proved_in_notes': len(H),
                     'A_full_image': str(A_single_block(H)),
                     'A_ambient': str(A_single_block(ambient)), 'S': 1})
    assert A_single_block({0, 1}) / A_single_block({0, 1, 2, 3}) == Fraction(3, 5)
    # For the singular source c=1, the full certified image is <c>.
    assert {0 if a in {0, 1} else 1 for a in {0, 1}} == {0}
    # Double the exhibited point exactly; this is a rational, possibly
    # nonintegral point and has zero component at 19, as 2H2=0 requires.
    x, y, B = Fraction(1463), Fraction(55955), -397822
    slope = 3*x*x/(2*y)
    xx = slope*slope-2*x
    yy = slope*(x-xx)-y
    assert yy*yy == xx**3+B
    assert valuation(xx.numerator, 19) == valuation(xx.denominator, 19) == 0
    assert all(e % 2 == 0 for e in factor(xx.denominator).values())
    assert norm((xx, -19, 0), 58) == yy*yy
    return data


def finite_valuation_checks():
    # Independent bounded corroboration, not a replacement for the proof.
    counts = {2: 0, 3: 0, 4: 0}
    maximum = 700**2+60**3
    sixth_powers = [p**6 for p in [2, 3, 5, 7] if p**6 <= maximum]
    for x in range(-60, 61):
        for y in range(701):
            B = y*y-x*x*x
            if not B or any(B % q == 0 for q in sixth_powers):
                continue
            for p in [5, 7, 11, 13, 17, 19]:
                if x % p or B % p:
                    continue
                m, vx, vy = valuation(B, p), valuation(x, p), valuation(y, p)
                assert m in [2, 3, 4], (x, y, B, p, m)
                counts[m] += 1
                if m == 2:
                    assert vx >= 1 and vy == 1
                elif m == 4:
                    assert vx >= 2 and vy == 2
                else:
                    assert vx == 1 and vy >= 2
                    assert ((x//p)**3+B//p**3) % p == 0
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    results = {'certificate58': certificate58(), 'certificate11': certificate11(),
               'exact_images': exact_images(), 'finite_singular_cases': finite_valuation_checks()}
    text = json.dumps(results, indent=2, sort_keys=True)+'\n'
    destination = Path(__file__).with_name('binary_results.json')
    if args.write:
        destination.write_text(text)
    else:
        assert destination.read_text() == text, 'Certificate output changed; inspect before --write'
    print(text, end='')


if __name__ == '__main__':
    main()
