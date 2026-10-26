"""Check the local existence construction and Taylor basis; requires SymPy."""

import sympy as s

X, Y, x, y, z, q, h = s.symbols("X Y x y z q h")
f = lambda U, V: U**4-6*x*U**2*V**2+8*y*U*V**3-3*x*x*V**4
F = f(z, 1)
d = s.diff(F, z)/(4*q)
g = s.Matrix([[z, 1], [z*d-q, d]])
T = s.Matrix([[z, 1], [h, 0]])
U = s.Matrix([[1, 0], [d, -q/h]])
assert s.simplify(g.det()-q) == 0
assert s.simplify(U*T-g) == s.zeros(2)

form = s.Poly(s.expand(f(z*X+h*Y, X)/h**2), X, Y)
expected = [F/h**2, s.diff(F, z)/h, s.diff(F, z, 2)/2,
            h*s.diff(F, z, 3)/6, h**2]
for i in range(5):
    assert s.simplify(form.coeff_monomial(X**(4-i)*Y**i)-expected[i]) == 0

# Work in the quotient by the exact square equation F(z)=q^2.
square_relation = q*q-F
transformed = s.Poly(s.expand(f(z*X+(z*d-q)*Y, X+d*Y)/q**2), X, Y)
def zero_mod_square(expr):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.rem(numerator, square_relation, q) == 0

assert zero_mod_square(transformed.coeff_monomial(X**4)-1)
assert zero_mod_square(transformed.coeff_monomial(X**3*Y))
A, C, E = [transformed.coeff_monomial(X**(4-i)*Y**i) for i in (2, 3, 4)]
assert zero_mod_square(12*E+A*A)
assert zero_mod_square((C/8)**2-(-A/6)**3-(y*y-x**3))
print("Extension identities passed: determinant, basis action, five Taylor coefficients, "
      "monicity, depression, and recovery of a point on the same curve.")
