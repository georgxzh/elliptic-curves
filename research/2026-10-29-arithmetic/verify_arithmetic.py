#!/usr/bin/env python3
"""Exact certificates; no CAS, rank oracle, or exhaustive point claim."""

from fractions import Fraction as F
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path
import json


def reduced_forms(D):
    assert D < 0 and D % 4 in (0, 1)
    forms = []
    for a in range(1, isqrt((-D)//3) + 1):
        for b in range(-a, a + 1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if a > c or gcd(gcd(a, abs(b)), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            forms.append((a, b, c))
    return forms


def reduce_form(a, b, c):
    D = b*b-4*a*c
    assert a > 0 and D < 0
    for _ in range(1000):
        # Substitution (X,Y) -> (X+mY,Y), determinant one.
        m = (a-b)//(2*a)
        a, b, c = a, b+2*a*m, a*m*m+b*m+c
        assert b*b-4*a*c == D
        if a > c:
            # Substitution (X,Y) -> (-Y,X), determinant one.
            a, b, c = c, -b, a
            continue
        if (abs(b) == a or a == c) and b < 0:
            b = -b  # Equivalent boundary representative.
        assert -a < b <= a and a <= c
        return (a, b, c)
    raise AssertionError("reduction did not terminate")


def lifted_root(D, p, b, exponent):
    assert exponent >= 1 and (b*b-D) % (4*p) == 0
    modulus = p
    for _ in range(1, exponent):
        roots = [b+2*modulus*j for j in range(p)
                 if ((b+2*modulus*j)**2-D) % (4*modulus*p) == 0]
        assert len(roots) == 1
        b = roots[0]
        modulus *= p
    return modulus, b


def prime_product_form(D, factors):
    # Product of chosen prime ideals, with no conjugate ideal in the list.
    # A square root b of D modulo 4A specifies (A,(-b+sqrt(D))/2).
    A, b = 1, 1
    for p, initial_b, exponent in factors:
        if not exponent:
            continue
        modulus, residue = lifted_root(D, p, initial_b, exponent)
        assert gcd(A, modulus) == 1
        t = ((residue-b)//2 * pow(A, -1, modulus)) % modulus
        b += 2*A*t
        A *= modulus
        assert (b*b-D) % (4*A) == 0
    return reduce_form(A, b, (b*b-D)//(4*A))


def squarefree(n):
    n = abs(n)
    for p in range(2, isqrt(n)+1):
        if n % (p*p) == 0:
            return False
    return True


def class_certificate(D, primes):
    assert squarefree(D) and D % 4 == 1
    assert D % 8 == 5 and D % 3 == 2  # Both 2 and 3 inert.
    forms = reduced_forms(D)
    principal = (1, 1, (1-D)//4)
    products = []
    for exponents in product(range(3), repeat=len(primes)):
        form = prime_product_form(D, [(p,b,e) for (p,b),e in zip(primes,exponents)])
        products.append({"exponents": list(exponents), "reduced_form": list(form)})
    assert {tuple(a["reduced_form"]) for a in products} == set(forms)
    assert len(forms) == 3**len(primes) == len(products)
    for p,b in primes:
        assert prime_product_form(D, [(p,b,3)]) == principal
    return {"discriminant": D, "reduced_forms": forms,
            "class_group": [3]*len(primes), "products": products,
            "small_primes_2_and_3": "inert, hence principal"}


def hensel_singular(B, p, precision=8):
    assert B % p**2 == 0 and B % p**3 != 0
    unit = p + B//p**2
    roots = [r for r in range(1, p) if (r*r-unit) % p == 0]
    assert len(roots) == 2
    r, modulus = roots[0], p
    for _ in range(1, precision):
        candidates = [r+modulus*k for k in range(p)
                      if ((r+modulus*k)**2-unit) % (modulus*p) == 0]
        assert len(candidates) == 1
        r = candidates[0]
        modulus *= p
    assert ((p*r)**2 - p**3 - B) % (p*p*modulus) == 0
    return {"p": p, "x": p, "y_mod_p_power": p*r,
            "modulus": p*modulus, "unit_square_root_precision": precision,
            "derivative_is_unit": (2*r) % p != 0}


def transform(P, matrix):
    x,y = P
    a,b,c,d = matrix
    det = a*d-b*c
    coeffs = [1,0,-6*x,8*y,-3*x*x]
    out = [F(0) for _ in range(5)]
    for i, coefficient in enumerate(coeffs):
        for j in range(5-i):
            for k in range(i+1):
                out[j+k] += F(coefficient*comb(4-i,j)*comb(i,k)
                              *a**(4-i-j)*c**j*b**(i-k)*d**k, det**2)
    return out


def main():
    classes = [class_certificate(-139, [(5,1)]),
               class_certificate(-4027, [(13,9),(17,11)])]
    exclusions = []
    for D, primes, points in [(-139,[5],[]),
                             (-4027,[13,17],[(1691,68108),(2027,90176)])]:
        n = 1
        for p in primes: n *= p
        B = D*n*n
        for x,y in points:
            assert y*y == x*x*x+B
            assert all(x % p for p in primes)
        exclusions.append({"B": B, "excluded_component_primes": primes,
                           "certified_H3_dimension": 0, "known_integral_points": points,
                           "singular_local_certificates": [hensel_singular(B,p) for p in primes]})

    B = 197225
    assert B == 5**2*7**3*23
    P1, P2 = (35,490), (70,735)
    for x,y in (P1,P2): assert y*y == x*x*x+B
    roots7 = [w for w in range(7) if (w**3+B//7**3) % 7 == 0]
    assert roots7 == [3,5,6]
    assert P1[0]//7 % 7 == 5 and P2[0]//7 % 7 == 3
    assert B//25 % 5 == 4
    assert P1[1]//5 % 5 == 3 and P2[1]//5 % 5 == 2
    # Distinct nonzero F2^2 components span the full binary ambient group;
    # either nonzero F3 component spans the full ternary ambient group.
    A = F(1) + 3*F(1,2)
    assert A == F(5,2)
    source, target = (-56,147), (1120,-37485)
    matrix = [-7,1,-210,35]
    for x,y in (source,target): assert y*y == x*x*x+B
    assert gcd(gcd(abs(matrix[0]),abs(matrix[1])),gcd(abs(matrix[2]),abs(matrix[3]))) == 1
    assert matrix[0]*matrix[3]-matrix[1]*matrix[2] == -35
    u,v = target
    assert transform(source,matrix) == [1,0,-6*u,8*v,-3*u*u]
    mixed = {"B":B,"points_certifying_full_images":[P1,P2],
             "H2_dimension":2,"H3_dimension":1,"A":"5/2","S":2,
             "product_A_S":5,"simultaneous_nonstandard_matrix":matrix,
             "determinant":-35,"source":source,"target":target}
    result = {"status":"PASS", "class_group_certificates":classes,
              "global_component_exclusions":exclusions,"mixed_extremal_example":mixed,
              "scope":"Exact form-class certificates, arithmetic and matrix identities; no rank or integral-point completeness assertion."}
    rendered = json.dumps(result,indent=2)+"\n"
    Path(__file__).with_name("arithmetic_results.json").write_text(rendered)
    print(rendered,end="")


if __name__ == "__main__":
    main()
