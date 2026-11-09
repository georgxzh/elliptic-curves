# Problem 1 — Two zeros

Let \(a,b\) be real numbers, not both zero. Prove that
\[
P(t)=t^4-6at^2+8bt-3a^2
\]
has exactly two distinct real zeros.

## Graduated hints

1. Deal with \(a=0\) first. Otherwise zero is not a root.
2. Dividing by \(t\) does not change the nonzero roots. What does it do
   to the derivative?
3. The derivative of \(P(t)/t\) is a square times a positive factor.
   Consider the two half-lines separately.

## Elementary solution

If \(a=0\), then \(b\ne0\) and \(P(t)=t(t^3+8b)\). Its real roots
are zero and the nonzero real cube root of \(-8b\), so there are exactly two.

Suppose \(a\ne0\). Zero is not a root. For \(t\ne0\), set
\[
G(t)=\frac{P(t)}t=t^3-6at+8b-\frac{3a^2}t.
\]
The useful cancellation is
\[
G'(t)=3t^2-6a+\frac{3a^2}{t^2}
      =\frac{3(t^2-a)^2}{t^2}\ge0.
\]
On either half-line \(G\) is nondecreasing. Equal values at two distinct
points would make it constant between them, contradicting the fact that
\(G'\) vanishes at at most one point on each half-line. Thus \(G\) is
strictly increasing there.
Furthermore,
\[
\begin{array}{ll}
\displaystyle\lim_{t\to-\infty}G(t)=-\infty,&
\displaystyle\lim_{t\to0^-}G(t)=+\infty,\\[4pt]
\displaystyle\lim_{t\to0^+}G(t)=-\infty,&
\displaystyle\lim_{t\to+\infty}G(t)=+\infty.
\end{array}
\]
Continuity and strict monotonicity give exactly one zero on each half-line.
These are precisely the zeros of \(P\). \(\square\)

### Degeneracies checked

The exclusion \((a,b)=(0,0)\) is essential: then there is just one distinct
root. Multiple roots are allowed in the statement. If \(r\) is a multiple
real root, then
\[
0=rP'(r)-P(r)=3(r^2-a)^2.
\]
The nonzero parameter assumption forces \(r\ne0\); hence
\(a=r^2\), \(b=r^3\), and
\[
P(t)=(t-r)^3(t+3r).
\]
There are still two distinct roots. This check is not needed in the proof:
the strict-monotonicity argument already includes these cases.

## Optional elliptic-curve background

Take \(B=b^2-a^3\), so \((a,b)\) lies on \(Y^2=X^3+B\). Substituting
the line \(Y=b+t(X-a)\) and dividing the intersection polynomial by
\(X-a\) leaves
\[
X^2+(a-t^2)X+(a^2+at^2-2bt).
\]
Its discriminant is exactly \(P(t)\). Thus the polynomial arises by asking
when the two remaining intersections of a line through a fixed cubic point
coalesce. This is the elementary part of the repository's chord calculation.
For \(B\ne0\) the cubic is an elliptic curve; \(B=0\) is singular, and
the problem deliberately remains true there. No theory of such curves is
used in the solution.

## Design assessment

Target: Putnam A1/A2, probably A2. Prerequisites: differentiation,
monotonicity, limits, and the intermediate value theorem. The central move
is to differentiate after dividing by the variable; a quartic formula is
unnecessary. See [audit notes](AUDIT.md) for the independent assessment and
[prior-art notes](PRIOR_ART.md) for the exact-quartic precedent. The
polynomial itself is classical; originality is claimed only cautiously for
this proposed contest formulation and presentation.
