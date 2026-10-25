# A failed local shortcut and an exact counterexample family

One possible shortcut would be to assert that, for two integral points P,Q,
at every odd prime of good reduction at least one of P+Q and P-Q remains
p-integral. That assertion is false. This note records a direct counterexample,
and the familiar local mechanism that explains it; no novelty is claimed.

For **every odd prime p**, take

\[
E_p:\quad y^2=x^3+(8-p^4)x+p^2,
\qquad P=(0,p),\quad Q=(p^2,3p).
\]

Both points satisfy the equation. The discriminant is
\(\Delta=-16(4(8-p^4)^3+27p^4)\), and

\[
\Delta\equiv-2^{15}\not\equiv0\pmod p.
\]

Thus p is a prime of good reduction. The slopes for P+Q and P-Q are 2/p
and -4/p, respectively. The group law gives

\[
x(P+Q)=\frac{4-p^4}{p^2},\qquad
x(P-Q)=\frac{16-p^4}{p^2}.
\]

Each fraction has denominator exactly p^2. Hence neither sum is p-integral.
For p = 3, the curve is y^2 = x^3 - 73x + 9, with P = (0,3), Q = (9,9),
and x coordinates -77/9 and -65/9 for the two sums.

The points P and Q both reduce to the same nonidentity 2-torsion point
(0,0) modulo p. Their sum and their difference therefore reduce to the point
at infinity. Good reduction of the curve does not exclude this phenomenon.

More generally, let P = (x_1,y_1) and Q = (x_2,y_2) be integral points with
x_1 != x_2. Let p be odd, p not divide the discriminant, and
x_1 = x_2 mod p. If p does not divide y_1, at least one of the slopes
(y_2-y_1)/(x_2-x_1) and (y_2+y_1)/(x_2-x_1) is p-integral. This follows
because one numerator is a unit and their product is divisible by x_2-x_1.

If instead p divides y_1, it also divides y_2. The common point with y = 0
has a simple root in the cubic, so

\[
s=A+x_1^2+x_1x_2+x_2^2\not\equiv0\pmod p.
\]

Writing d = x_2-x_1, the identity
\((y_2-y_1)(y_2+y_1)=ds\) gives

\[
v_p(d)=v_p(y_2-y_1)+v_p(y_2+y_1)=r+s',
\qquad r,s'\ge1.
\]

Thus the reduced slope denominators have valuations s' and r, respectively;
both are positive. The x coordinates of the sums have denominator valuations
2s' and 2r. This exactly characterizes the obstruction in this setting.

The accompanying script checks this valuation identity on every applicable
pair of distinct-x points in the T = 8 census and checks the counterexample
family for all odd primes below 1000. These checks verify the implementation;
the displayed algebra proves the family for all odd primes.

This does **not** contradict the discriminant-dependent bounds of Alpöge–Ho.
Their local factors arise in a different descent argument. It only rejects
the proposed shortcut of assigning all group-law denominator obstructions
to primes of bad reduction.
