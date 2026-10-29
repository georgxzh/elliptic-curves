"""Verify the target-x coefficient identity modulo F(z)=q^2; needs SymPy."""

import sympy as s

X, Y, x, y, z, q = s.symbols("X Y x y z q")
f = lambda U,V: U**4-6*x*U**2*V**2+8*y*U*V**3-3*x*x*V**4
F = f(z, 1)
d = s.diff(F,z)/(4*q)
new = s.Poly(s.expand(f(z*X+(z*d-q)*Y, X+d*Y)/q**2), X, Y)
residual = new.coeff_monomial(X**2*Y**2)+6*(x-z*z+d*d)
numerator = s.together(residual).as_numer_denom()[0]
assert s.rem(numerator, q*q-F, q) == 0
print("Target-x transformation identity passed modulo the exact square equation.")
