# Integral tripling and points beyond the enlarged search

The basic large-point families here are classical. In particular, the A = +/-1
and +/-2 examples below appear in equation (16) of
[Zagier, Large integral points on elliptic curves](https://archive.mpim-bonn.mpg.de/id/eprint/737/1/preprint_1986_23.pdf)
(1986), which also discusses integral tripling more generally. We use them
to test whether a coordinate cutoff can be mistaken for completeness.
The divisibility calculation below is an elementary derivation, with no
novelty claim.

Take A != 0 and b != 0, and suppose

\[
E:\ y^2=x^3+Ax+b^2
\]

is nonsingular. The point P = (0,b) is integral. Direct application of the
group law gives

\[
x(3P)=\frac{8b^2(A^3+8b^4)}{A^4},\qquad
y(3P)=\frac{b(3A^6+96A^3b^4+512b^8)}{A^6}. \tag{1}
\]

The point 3P is finite because the 3-division polynomial at x = 0 is -A^2.
Its integrality has the exact criterion

\[
3P\text{ is integral}\quad\Longleftrightarrow\quad A^2\mid8b^3. \tag{2}
\]

It suffices to test whether x(3P) is integral: a rational y whose square is
an integer is itself an integer.

For an odd prime p let a = v_p(A), c = v_p(b). If 2a > 3c, then 3a > 4c,
so the two terms A^3 and 8b^4 have distinct valuations and

\[
v_p(x(3P))=6c-4a<0.
\]

If 2a <= 3c, the valuation is bounded below by

\[
2c+\min(3a,4c)-4a=\min(2c-a,6c-4a)\ge0.
\]

At p = 2, if 2a > 3c+3, then 3a > 4c+3, giving
v_2(x(3P)) = 6+6c-4a < 0. If 2a <= 3c+3, its valuation is at least

\[
3+2c+\min(3a,3+4c)-4a
=\min(3+2c-a,6+6c-4a)\ge0.
\]

These conditions at all primes are exactly (2).

For A = +/-1, (1) becomes the polynomial identity

\[
x=64b^6\pm8b^2,\qquad
y=512b^9\pm96b^5+3b,
\]

on y^2 = x^3 +/- x + b^2. If b is of order T^{3/2}, then the coefficients
fit the box |A| <= T^2, |B| <= T^3, while x has order T^9. These points
can lie far beyond a very extensive direct coordinate search.

## How thin is this construction?

For a fixed positive b, the number of nonzero A with A^2 | 8b^3 is at most
2 tau(8b^3). Therefore for any epsilon > 0, there are
O_epsilon(T^{3/2+epsilon}) such coefficient models with b^2 <= T^3.
The bound |A| <= T^2 can only decrease this count. Nonsingular models are
understood throughout.

The **designated points** +/-P and +/-3P provide at most four points per
model, so their own cubic-moment contribution, averaged over all coefficient
models, is O_epsilon(T^{-7/2+epsilon}). This does not bound the contribution
of *all* integral points on this thin family, which could contain additional
points. It also does not classify all integral triples arising from points
whose x coordinate is nonzero.

The accompanying computation enumerates (2) exactly in each coefficient box,
verifies both (1) and the rational group law, and records constructed points
that the deeper direct search cannot reach.

## Tripling all known small points at T = 8

The previous census saved every nonnegative-y point with |x| <= 2048 at
T = 8. For each P = (x,y), use

\[
f=x^3+Ax+B,\quad
\psi_3=3x^4+6Ax^2+12Bx-A^2,
\]

\[
q_6=x^6+5Ax^4+20Bx^3-5A^2x^2-4ABx-8B^2-A^3.
\]

When psi_3 != 0,

\[
x(3P)=x-\frac{8f q_6}{\psi_3^2}.
\]

The script tests exact divisibility, verifies the resulting integer point,
and checks the rational group law independently. Duplicated constructed
points are counted once per model and x coordinate, and +/-y are treated
as one nonnegative-y representative. Points beyond the direct cutoff are
certified extra points; finding them does not certify the full point set.
