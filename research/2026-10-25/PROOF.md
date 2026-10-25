# Bounded-coordinate moments: a research derivation

Status: a proved consequence of standard lattice counting, a divisor estimate,
and the uniform Bombieri–Pila theorem. This note makes no novelty claim. It does
not bound the third moment of the total number of integral points.

Fix a real number L >= 1. For an integer T >= 2 set

\[
\mathcal F_T=\{(A,B)\in\mathbb Z^2: |A|\le T^2,\ |B|\le T^3,
\quad 4A^3+27B^2\ne0\}.
\]

Let N = N_{T,L}(A,B) count **signed affine points** on
\(y^2=x^3+Ax+B\) with \(|x|\le LT\). The point at infinity is excluded.
Let K count distinct x coordinates among these points, and Z count points with
y = 0. Then N = 2K - Z and 0 <= Z <= 3. Expectations below are uniform over
the integral coefficient models in \(\mathcal F_T\), including models related by
scaling. They are not averages over isomorphism classes.

We derive:

\[
\mathbb E N \sim c_L T^{-1/2},\qquad
\mathbb E[K(K-1)]\ll_L T^{-1}(\log T)^2. \tag{1}
\]

For every fixed theta > 0, put beta = max(theta - 2, 0). For every epsilon > 0,

\[
\left|\mathbb E N^\theta-2^{\theta-1}\mathbb E N\right|
\ll_{L,\theta,\epsilon}
T^{-1+\beta/2+\epsilon}(\log T)^2+T^{-2}. \tag{2}
\]

In particular,

\[
\mathbb E N^\theta\sim 2^{\theta-1}c_LT^{-1/2}
\quad (0<\theta<3), \tag{3}
\]

and

\[
\mathbb E N^\theta\longrightarrow0
\quad(0<\theta<4). \tag{4}
\]

Thus the **truncated third moment tends to zero**. In (2), theta = 3 gives
\(\mathbb E N^3\ll_{L,\epsilon}T^{-1/2+\epsilon}\), after absorbing logarithms
into epsilon. This does not give the leading constant at theta = 3.

## First moment and its constant

Define

\[
V_L=\int_{-1}^{1}\int_{-L}^{L}
\left(\sqrt{(u^3+au+1)_+}-\sqrt{(u^3+au-1)_+}\right)\,du\,da,
\qquad c_L=V_L/2,
\]

where \(v_+=\max(v,0)\). This is finite and positive.

Eliminate B by B = y^2 - x^3 - Ax, and use the scaled variables

\[
a=A/T^2,\quad u=x/T,\quad v=y/T^{3/2}.
\]

The allowed triples lie in the compact region

\[
|a|\le1,\quad |u|\le L,\quad |v^2-u^3-au|\le1.
\]

Its boundary has measure zero, so anisotropic Riemann sums apply. Its volume
is 2V_L, since both signs of y are counted. The lattice cell has volume
\(T^{-2}T^{-1}T^{-3/2}=T^{-9/2}\). Consequently the total point count,
initially including singular models, is

\[
2V_LT^{9/2}+o_L(T^{9/2}).
\]

Singular integral coefficient pairs have
\(A=-3r^2, B=2r^3\) for integral r, hence there are O(T) such models.
Each has at most O_L(T) possible x coordinates, with at most two y values
at each x. Removing them changes the point count by only O_L(T^2).
Finally,

\[
|\mathcal F_T|=(2T^2+1)(2T^3+1)-O(T)=4T^5+O(T^3).
\]

This proves the first part of (1). Points with y = 0 contribute only O_L(T^3)
to the total count: choose A and x, then B is determined. Thus
\(\mathbb E Z\ll_L T^{-2}\).

## Distinct-x pair bound, including the degenerate case

Take two different x coordinates x_1,x_2. Choose the unique nonnegative y
representative at each coordinate. Put

\[
d=x_2-x_1\ne0,\qquad s=x_1^2+x_1x_2+x_2^2,\qquad t=A+s.
\]

Subtracting the two curve equations gives

\[
(y_2-y_1)(y_2+y_1)=dt. \tag{5}
\]

If t != 0, there are at most \(2\tau(|dt|)\) signed factor pairs, and hence at
most this many choices for (y_1,y_2). Some choices fail parity, nonnegativity,
or the bound on B; discarding those conditions gives an upper bound.
Once y_1 is chosen, B is determined.

The inequality
\(\tau(mn)\le\tau(m)\tau(n)\) therefore gives an upper bound

\[
2\sum_{x_1\ne x_2}\tau(|d|)
\sum_{|A|\le T^2,\ A+s\ne0}\tau(|A+s|). \tag{6}
\]

Here |s| <= 3L^2 T^2. The inner sum is at most the sum of tau(n) over all
positive and negative n with |n| <= (3L^2+1)T^2. The elementary divisor-sum
estimate therefore bounds it by O_L(T^2 log T), uniformly in x_1,x_2.
For each nonzero d with |d| <= 2LT there are O_L(T) choices of x_1. Thus

\[
\sum_{x_1\ne x_2}\tau(|d|)
\ll_L T\sum_{1\le d\le2LT}\tau(d)
\ll_L T^2\log T.
\]

The contribution to (6) is O_L(T^4 (log T)^2).

If t = 0, the divisor argument cannot be used. Instead A = -s is fixed by
x_1,x_2, and y_2 = y_1 for nonnegative representatives. Since
\(y_i\ll_L T^{3/2}\), the total number of these pairs is
O_L(T^2 * T^{3/2}) = O_L(T^{7/2}). This is smaller than the preceding bound.
Dividing by |F_T| proves the second part of (1).

In particular,
\(\Pr(K\ge2)\ll_L T^{-1}(\log T)^2\), whereas
\(\mathbb E N\asymp_L T^{-1/2}\).

## Passing from pairs to higher moments

The curve \(y^2-x^3-Ax-B=0\) is absolutely irreducible and has degree 3.
All points being counted fit into a square of side O_L(T^{3/2}), after an
integer translation. The **uniform** Bombieri–Pila theorem gives, for every
delta > 0,

\[
N\ll_{L,\delta}T^{1/2+\delta}. \tag{7}
\]

The constant is independent of A and B. This uniformity is essential.
The source is Bombieri and Pila, *The Number of Integral Points on Arcs and
Ovals*, Theorem 5, printed page 353 (page 17 of the author's PDF):
[author PDF](https://people.maths.ox.ac.uk/pila/Ovals.pdf),
[DOI](https://doi.org/10.1215/S0012-7094-89-05915-2).

For M >= max N and beta = max(theta-2,0), the elementary inequality

\[
|N^\theta-2^{\theta-1}N|
\le C_\theta\{M^\beta K(K-1)+Z\} \tag{8}
\]

holds. For K = 0 both sides vanish. For K = 1 the only nonzero discrepancy
is a y = 0 point. For K >= 2, use N <= 2K, K^2 <= 2K(K-1), and the definition
of beta. Combining (7), (8), and (1), choosing delta sufficiently small
relative to epsilon, proves (2). Choosing epsilon sufficiently small proves
(3) and (4). For theta <= 2 the epsilon in (2) can be omitted.

Without Bombieri–Pila, the trivial bound N = O_L(T) still gives vanishing
moments for theta < 3 and the asymptotic for theta < 5/2.

## What this leaves unresolved

The constants depend on fixed L. These estimates do not justify letting L
tend to infinity with T, or replacing N_{T,L} by the full integral-point count.
The searches also do not certify that there are no points beyond their cutoff.

To obtain a bounded third moment for the full count, a sufficient missing
estimate would be a uniform bound on

\[
\mathbb E_{\mathcal F_T}
\#\{(x,y)\in E_{A,B}(\mathbb Z): |x|>LT\}^3.
\]

To obtain a vanishing third moment by this decomposition, one could aim for
the stronger tail condition

\[
\lim_{L\to\infty}\limsup_{T\to\infty}
\mathbb E_{\mathcal F_T}
\#\{(x,y)\in E_{A,B}(\mathbb Z): |x|>LT\}^3=0.
\]

Neither estimate is proved here. The inequality (a+b)^3 <= 4(a^3+b^3)
explains why such a tail estimate would finish the corresponding argument.
Alpöge already treats small points in a substantially larger range in Lemma 16
of his [average-point paper](https://arxiv.org/abs/1412.1047). This bounded-range
calculation is a research exercise and a diagnostic for the unresolved tail,
not a claimed improvement to the full moment theorem of Alpöge–Ho.
