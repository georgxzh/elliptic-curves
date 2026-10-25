"""Finite checks for a candidate inert-prime refinement of Alpoge--Ho descent.

Exhausts one residue disk modulo p^(2e+1) for each selected local point.
These checks support, but do not replace, the p-adic argument or a novelty audit.
"""
import json
import sympy as sp

z, t, x, s = sp.symbols('z t x s')
f = z**4-6*x*z**2+8*t*x*z-3*x**2
h = t**2-x
assert sp.expand(f.subs(z,t+s) - (s**4+4*t*s**3+6*h*s**2+4*t*h*s+h*(4*x+h))) == 0
assert sp.expand(f.subs(x,t**2) - (z-t)**3*(z+3*t)) == 0

def sqrt_lift(value, root, p, exponent):
    modulus = p
    for _ in range(1, exponent):
        correction = ((value-root*root)//modulus * pow(2*root,-1,p)) % p
        root += correction*modulus
        modulus *= p
    assert (root*root-value) % modulus == 0
    return root

checks = 0
disk_values = 0
simple_root_square_examples = 0
for p in (5,7,11,13):
    for d in (-3,-1,2,5):
        if d % p == 0 or pow(d % p,(p-1)//2,p) != p-1:
            continue
        for e in (1,2):
            modulus = p**(2*e+1)
            square_residues = {a*a % modulus for a in range(modulus)}
            for t0 in (1,2):
                xp = t0*t0
                yp = sqrt_lift(xp**3+d*p**(2*e), t0**3 % p, p, 2*e+1)
                tp = yp*pow(xp,-1,modulus) % modulus
                def quartic(a):
                    return (a**4-6*xp*a*a+8*yp*a-3*xp*xp) % modulus
                for a in range(tp % p,modulus,p):
                    assert quartic(a) not in square_residues, (p,d,e,xp,yp,a)
                    disk_values += 1
                # The simple-root disk CAN contain squares. Ignoring the
                # derivative condition would invalidate the proposed refinement.
                simple_root_square_examples += any(
                    quartic(a) == p*p % modulus
                    for a in range((-3*tp)%p,modulus,p)
                )
                checks += 1

print(json.dumps({
    'symbolic_identities_verified': 2,
    'local_point_cases': checks,
    'repeated_root_disk_residues_checked': disk_values,
    'counterexamples_in_repeated_root_disk': 0,
    'cases_with_square_in_simple_root_disk': simple_root_square_examples,
    'scope': 'Selected primes and local points only; not a proof of the global bound.'
}, indent=2))
