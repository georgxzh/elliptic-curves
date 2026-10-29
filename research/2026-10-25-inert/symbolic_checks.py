"""Symbolic checks of the identities used in the proof; requires SymPy."""

import sympy as sp

X, Y, m, x, y, a, b = sp.symbols("X Y m x y a b")


def quartic(xx, yy, u, v):
    return u**4 - 6 * xx * u**2 * v**2 + 8 * yy * u * v**3 - 3 * xx**2 * v**4


source = quartic(1, 1 + 2 * m**2, X - 3 * m * Y, X + m * Y)
target = quartic(m**2, -m * (m**2 + 2), X, Y)
assert sp.expand(source - 16 * m**2 * target) == 0

f = quartic(x, y, X, Y)
discriminant = sp.discriminant(f.subs(Y, 1), X)
assert sp.expand(discriminant + 2**12 * 3**3 * (y**2 - x**3)**2) == 0

# The unique second row for each signed determinant D is (nc/D, nd/D).
nc = 3 * x * a**2 * b - 6 * y * a * b**2 + 3 * x**2 * b**3
nd = a**3 - 3 * x * a * b**2 + 2 * y * b**3
assert sp.expand(a * nd - b * nc - quartic(x, y, a, b)) == 0
assert sp.expand(
    sp.diff(f, X).subs({X: a, Y: b}) * nc
    + sp.diff(f, Y).subs({X: a, Y: b}) * nd
) == 0

print("Four symbolic checks passed: sharpness family, discriminant, determinant, depression.")
