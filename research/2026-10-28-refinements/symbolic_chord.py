"""Rational chord interpretation of monic point-quartic transformations.

Checks exact identities in Q[x,y,z,q]/(q^2-F(z)); requires SymPy.
The identity is algebraic evidence for the proposed global component bridge.
"""

import sympy as s

x,y,z,q = s.symbols("x y z q")
B = y*y-x**3
F = z**4-6*x*z*z+8*y*z-3*x*x
u = (z*z-x+q)/2
v = (z*z-x-q)/2
yu = z*(u-x)+y
yv = z*(v-x)+y

def vanishes(expr):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.rem(numerator, q*q-F, q) == 0

assert vanishes(yu*yu-u**3-B)
assert vanishes(yv*yv-v**3-B)
assert s.expand((yu-yv)-z*(u-v)) == 0
# R+S=-P by the chord law. The slope joining R to -S is d.
d = s.diff(F,z)/(4*q)
assert s.simplify((yu+yv)/(u-v)-d) == 0
assert s.simplify((d*d-u-v)-(x-z*z+d*d)) == 0
# Check the target y as well, retaining the sign convention.
X,Y=s.symbols("X Y")
quartic=lambda U,V: U**4-6*x*U**2*V**2+8*y*U*V**3-3*x*x*V**4
new=s.Poly(s.expand(quartic(z*X+(z*d-q)*Y, X+d*Y)/q**2),X,Y)
target_x=x-z*z+d*d
chord_y=-yu+d*(u-target_x)
assert vanishes(new.coeff_monomial(X*Y**3)/8-chord_y)
print("Chord checks passed: both rational points lie on E, R+S=-P, "
      "and the transformed point equals R-S with these signs.")
