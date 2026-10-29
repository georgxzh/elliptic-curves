# Reproducible finite checks for the general additive extension

Executed 2026-10-28 for `FRONTIER_ADDITIVE.md`. These checks are additional
evidence for the local formulas, not a substitute for their proof and not
independent human verification.

The checker examined **110 seed coefficient models and 1,166 local point samples**
at p=5,7, including all nonsingular residual cubics in the I0* branch.
For each sample it enumerated every candidate row lattice up to the
discriminant determinant bound and tested its exact finite lifting criterion.
All computed lists agreed with the theorem. The unit-point expansion and
the discriminant identity `disc(f_P)=2^8 Delta_E` were also checked symbolically.

For a candidate L(k,z), let p^k=pk and fix z modulo pk. Every lift is
z+pk*w with w in Z_p. A candidate first requires F(z)=0 modulo pk^2
and F'(z)=0 modulo pk. Taylor expansion modulo p^(2k+1) then gives

    F(z+pk*w)/pk^2 = F(z)/pk^2 + (F'(z)/pk)*w + (F''(z)/2)*w^2 mod p.

It has a square of exact valuation 2k precisely when this polynomial takes
a nonzero square value. This is an exhaustive local test for that lattice.
The code checks all z modulo p^k for every possible positive k.

The points are formed by lifting a square root modulo p^(2K+3), then
replacing B by y^2-x^3-Ax. Thus they are exact integral points and the
coefficient change is beyond the precision affecting every checked lattice.

Run the [standalone checker](FRONTIER_verify_additive.py) with Python 3 and SymPy:

```sh
python research/2026-10-28-refinements/FRONTIER_verify_additive.py
```

It writes [structured results](FRONTIER_results.json). The symbolic checks
verify the unit-point expansion, discriminant identity, and the identity
`x′=x-z^2+d^2` under monicity and depression used by the general
IV/IV* reduction-pattern corollary.
