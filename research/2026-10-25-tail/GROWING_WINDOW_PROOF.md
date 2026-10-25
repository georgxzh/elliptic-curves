# Third moments in a coordinate range that grows with coefficient height

This extends the preceding fixed-L derivation. It is a consequence of standard
divisor bounds and the uniform Bombieri–Pila theorem, with no novelty claim.
It does not bound the third moment of the full integral-point count.

Let
\[
\mathcal F_T=\{(A,B)\in\mathbb Z^2:|A|\le T^2,\ |B|\le T^3,
\ 4A^3+27B^2\ne0\},
\]
and let N_X count signed affine integral points with |x| <= X. All expectations
are uniform over these coefficient models, and include nonminimal models.
For T <= X <= T^2, we derive

\[
\mathbb E N_X^3\ll_\epsilon
T^{-1/2}+\frac{X^{5/2+\epsilon}}{T^3}. \tag{1}
\]

Consequently, for every fixed 0 < delta < 1/5,

\[
\mathbb E N_{T^{6/5-\delta}}^3\longrightarrow0. \tag{2}
\]

This allows X/T to tend to infinity. It still leaves a very large coordinate
range untreated and does not improve the full Alpöge–Ho moment theorem.

## Uniform first-moment estimate

For |x| <= 2T, choose A,x,y, and recover B. There are O(T^2 * T * T^{3/2})
= O(T^{9/2}) choices. For x < -2T there are no points, since
x^3+Ax+B < 0 for every model in the box.

For x > 2T, all possible nonnegative y lie in the interval

\[
\sqrt{x^3-T^2x-T^3}\le y\le\sqrt{x^3+T^2x+T^3}.
\]

The interval has length O(T^2/sqrt(x)); hence it contains at most
O(1+T^2/sqrt(x)) integers. For fixed x,y the condition on B forces

\[
\frac{y^2-x^3-T^3}{x}\le A\le\frac{y^2-x^3+T^3}{x}.
\]

There are at most O(1+T^3/x) possible integers A. Thus the point count is
bounded by

\[
O\left(T^{9/2}+\sum_{2T<x\le X}
\left(1+\frac{T^2}{\sqrt{x}}\right)
\left(1+\frac{T^3}{x}\right)\right)
\]

\[
\ll T^{9/2}+X+T^2\sqrt X+T^3\log(2X).
\]

After dividing by |F_T| asymptotic to 4T^5,

\[
\mathbb E N_X\ll T^{-1/2}+\frac X{T^5}
+\frac{\sqrt X}{T^3}+\frac{\log(2X)}{T^2}. \tag{3}
\]

In particular, this is O(T^{-1/2}) for T <= X <= T^2. This enumeration is
the same elementary idea used in Lemma 16 of
[Alpöge's average-point paper](https://arxiv.org/abs/1412.1047), and is also
the basis of the new computational scanner. No improvement to that lemma is
being claimed.

## A divisor estimate uniform in the center of an interval

For an interval of H positive integers contained in [1,M], the elementary
hyperbola argument gives

\[
\sum_{n\text{ in the interval}}\tau(n)
\le 2\sum_{d\le\sqrt M}\left(\frac Hd+1\right)
\ll H\log(2M)+\sqrt M. \tag{4}
\]

The same estimate, up to an absolute constant, applies to tau(|n|) on an
interval of integers crossing zero, after excluding zero.

Let K_X count distinct x coordinates among the N_X points. For an ordered
pair x_1 != x_2 use nonnegative y representatives and write

\[
d=x_2-x_1,\qquad s=x_1^2+x_1x_2+x_2^2.
\]

The identity

\[
(y_2-y_1)(y_2+y_1)=d(A+s)
\]

gives at most 2 tau(|d|) tau(|A+s|) choices when A+s != 0. Since
|s| <= 3X^2, (4) bounds the sum over A by

\[
\sum_{|A|\le T^2,\ A+s\ne0}\tau(|A+s|)
\ll T^2\log(2X)+X.
\]

Also
\[
\sum_{|x_i|\le X,\ x_1\ne x_2}\tau(|x_2-x_1|)
\ll X^2\log(2X).
\]

For the excluded case A+s = 0, positive definiteness gives
s >= (x_1^2+x_2^2)/2. Thus both x_i = O(T), independently of X. There are
O(T^2) pairs, A is fixed, and y_1 = y_2 = O(T^{3/2}). This contributes
O(T^{7/2}). We therefore obtain the uniform estimate

\[
\mathbb E[K_X(K_X-1)]
\ll\frac{(T^2+X)X^2(\log(2X))^2}{T^5}+T^{-3/2}.
\]

For T <= X <= T^2 this simplifies to

\[
\mathbb E[K_X(K_X-1)]\ll\frac{X^2(\log(2X))^2}{T^3}. \tag{5}
\]

## From distinct-x pairs to a third moment

All the points lie in a square of side O(X^{3/2}). The cubic is absolutely
irreducible, so the uniform
[Bombieri–Pila theorem, Theorem 5](https://people.maths.ox.ac.uk/pila/Ovals.pdf)
gives, for every eta > 0,

\[
N_X\ll_\eta X^{1/2+\eta}, \tag{6}
\]

with a constant independent of the coefficients.

Let Z be the number of y = 0 points. Such points have |x| <= 2T, so
E Z = O(T^{-2}). The elementary pointwise estimate

\[
|N_X^3-4N_X|\ll (\max_{\mathcal F_T}N_X)K_X(K_X-1)+Z
\]

follows by treating K_X = 0 or 1 separately and using N_X <= 2K_X otherwise.
Combining (3), (5), and (6), and absorbing logarithms into epsilon, proves
(1). Put X = T^{6/5-delta} and choose epsilon small enough that
(6/5-delta)(5/2+epsilon) < 3 to obtain (2).

More generally, with beta = max(theta-2,0), the same argument gives

\[
\left|\mathbb E N_X^\theta-2^{\theta-1}\mathbb E N_X\right|
\ll_{\theta,\epsilon}
\frac{X^{2+\beta/2+\epsilon}}{T^3}+T^{-2}
\quad(T\le X\le T^2).
\]

For theta >= 2 and X = T^c with 1 <= c <= 2, this proves vanishing when
c(1+theta/2) < 3. These are sufficient ranges from this argument, not claimed
optimal boundaries.

## What the deeper computations do and do not test

At T = 32 the new search reaches X = 134,217,728, far outside X <= T^2.
That is a finite computation; it is not evidence establishing uniformity of
(1) in such a range. The unproved full tail estimate in the previous note
remains unproved. The computations instead expose the substantial correlation
between large-coordinate points and models already containing several points.
