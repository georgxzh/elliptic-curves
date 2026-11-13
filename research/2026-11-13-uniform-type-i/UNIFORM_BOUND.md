# Uniform quadratic-twisted Type I bounds after Mobius inversion

Continuation of `fb4273e`, 13 November 2026. Proofs and imported inputs
are distinguished below. The result is uniform in a growing short
variable; it is not merely decay at each fixed level. Independent
review is recorded in [ASTRA_AUDIT.md](ASTRA_AUDIT.md).

## 1. Target, conventions, and proved statements

Use O=Z[omega], lambda=1+2omega, primary generators equal to 1 modulo 3,
and the normalized cubic Gauss sum gtilde of the preceding
[transformation report](../2026-11-12-type-i/TRANSFORM.md). Let r be
odd, squarefree and primary, R=Nr, U>=1, and W a fixed smooth compactly
supported function on (0,infinity). Define

\[
 T_r(U;W)=\sum_{u\equiv1(3)}\kappa(u)\widetilde g(ur)W(Nu/U),
 \quad \kappa(z)=\chi_{-4}(Nz),\quad \chi_r(z)=(z/r)_3.
                                                               \tag{1}
\]

The full product twist kappa(ur) differs by the unit-modulus outer
factor kappa(r). Even r contributes zero to that product-twisted sum;
nonsquarefree r contributes zero through gtilde(ur). We include r=1.

**Theorem A (unconditional).** For every epsilon>0, uniformly in r,U,

\[
             T_r(U;W)\ll_{\varepsilon,W}
                   (UR)^\varepsilon U^{1/2}R^{1/4}.           \tag{2}
\]

**Theorem B (GRH).** Assume GRH for the fixed Hecke L-function
L_K(s,kappa), K=Q(omega). Then, uniformly in r,U,

\[
 \boxed{\quad T_r(U;W)\ll_{\varepsilon,W}
                   (UR)^\varepsilon U^{1/3}R^{1/3}.\quad}    \tag{3}
\]

Equivalently, it suffices here to assume GRH for the two fixed Dirichlet
L-functions of characters chi_-4 and chi_12; the Euler-factor identity
is proved in Section 5. No GRH hypothesis with conductor growing with
r is needed for this particular theorem. Earlier prime theorems retain
their separately stated GRH assumptions.

Both estimates hold uniformly when W varies in a bounded smooth family
with common compact support away from zero. Only finitely many smooth
seminorms, depending on epsilon, enter the constants. They are pointwise
in r; no cancellation over r is assumed.

For X=UR, summing over primary r in a norm annulus of size R, with
arbitrary bounded coefficients, consequently gives

\[
 \ll X^{1/2+\varepsilon}R^{3/4}\quad\hbox{unconditionally},
 \qquad
 \ll X^{1/3+\varepsilon}R\quad\hbox{under GRH}.               \tag{4}
\]

Fixed divisor-bounded coefficients are also allowed, with their
R^epsilon loss absorbed. Against the required X^(5/6) scale, the
respective power-saving ranges are R<=X^(4/9-delta) and
R<=X^(1/2-delta), for fixed delta>0 and sufficiently small epsilon.
Section 7 verifies the actual rough/smooth factorization used in the
long Type I block, rather than assuming its multiplicities are bounded.

## 2. Audit of the starting transform and exact Mobius inversion

Put q=4r, psi=kappa conjugate(chi_r). The completed sum is

\[
 \mathcal C_r(Y;W)=\sum_{u,d\equiv1(3),\ (d,r)=1}
 |d|\widetilde g(u)\overline{\chi_r(u)}\kappa(u)\kappa(d)
                       W(N(ud^3)/Y).
\]

The exact inversion, with both quadratic factors retained, is

\[
 T_r(U;W)=\widetilde g(r)
 \sum_{c\equiv1(3),\ (c,2r)=1}\mu_O(c)\kappa(c)|c|
                       \mathcal C_r(U/(Nc)^3;W).             \tag{5}
\]

This finite identity follows by setting h=cd and summing mu_O(c)
over divisors of h. No character is silently dropped.

Its equivalent Mellin formulation is

\[
 \mathcal R_r(s)=\sum_u\widetilde g(u)\psi(u)(Nu)^{-s},
 \qquad F_r(s)=L_r(3s-\tfrac12,\kappa)\mathcal R_r(s),         \tag{6}
\]

where L_r is L_K with the factors above 3 and dividing r removed;
the factor at 2 is already absent from kappa. The following starting
facts were rechecked against [DR]:

* The general periodic-twist theorem, Lemma 5.2 and Proposition 5.1,
  requires q primary and Fourier support on units, not squarefree q.
  psi is primitive modulo 4r, so these hypotheses hold.
* The finite metaplectic factor is
  tilde(psi)(v)=16 chi_r(lambda^2) conjugate(g(r))
  kappa(v) conjugate(chi_4(v)) c_r(v). In particular tilde(psi)(0)=0.
  The additional cubic factor at 2 is preserved throughout.
* With D_r the sieved theta Dirichlet series,
  D_r(s)=3^(5/2+3s)psi(lambda)F_r(s), and
  psi(lambda)=-conjugate(chi_r(lambda)). The only possible completed
  residue vanishes by [DR, (5.46)--(5.47)]. Thus F_r is entire.
* The normalized functional equation is

\[
 F_r(s)=\frac{(2\pi)^{4s-2}}{3^{7/2}\psi(\lambda)}
 (27(Nq)^2)^{-s}
 \frac{\Gamma(5/6-s)\Gamma(7/6-s)}
      {\Gamma(s-1/6)\Gamma(s+1/6)}D_r^*(1-s),                \tag{7}
\]

where Nq=16R and

\[
 D_r^*(s)=\sum_{\mu\in\lambda^{-4}O\setminus\{0\}}
 \frac{a(\mu)\widetilde\psi(\lambda^4\mu)}{(N\mu)^s},
 \quad
 a(\mu)=\overline{d_1(-\mu)}+
        \omega\overline{d_{19}(-\mu)}+
        \omega^2\overline{d_{10}(-\mu)}.
\]

The gamma quotient and constants, including the kernel denominator
6912R^2, agree with the previous exact checks. These starting identities
are unconditional. Entirety of F_r does not imply that its quotient
R_r is entire; the allowed division is proved below in specific regions.

## 3. The quantitative loss and its repair

The previous majorant used |c_r(v)|<=phi_O(r) at every dual coefficient.
It produced sqrt(R)phi_O(r)(R^2/Y)^b. The scalar sqrt(R), coming from
|g(r)|, is really present. The fixed conductor at 4 contributes only
fixed constants. The avoidable loss is using the largest Ramanujan
value at every theta-supported frequency simultaneously.

**Lemma 1 (absolute dual mass).** For every sigma>1,

\[
 \sum_{\mu\ne0}
 \frac{|a(\mu)c_r(\lambda^4\mu)|}{(N\mu)^\sigma}
                  \ll_\sigma 2^{\omega_O(r)}.               \tag{8}
\]

Here omega_O counts prime ideals, so both conjugate factors of a split
rational prime are counted if they divide r. The constant is independent
of r. The lemma uses absolute values, not cancellation in the dual sum.

**Proof.** Appendix A of [DR], rows 1,10,19, gives the majorant

    |a(mu)| <= |tau(mu)| + |tau_1(-omega^2 mu)|
                            + |tau_2(-omega mu)|.

By [DR, (5.7), (5.13)--(5.14)], each term is supported on finitely many
unit variants of lambda^j u d^3, with u squarefree, u,d primary, and
coefficient magnitude a fixed ramified-3 factor times |d|. There is
**no** requirement that (u,d)=1. At a prime pi not above 3, write
Q=Npi, e=v_pi(u) in {0,1}, and k=v_pi(d)>=0. The local coefficient
mass without the Ramanujan weight is

\[
 D_Q=\sum_{e=0}^1\sum_{k\ge0}Q^{-e\sigma}
                      Q^{k(1/2-3\sigma)}
      =\frac{1+t}{1-z},\quad
 t=Q^{-\sigma},\ z=Q^{1/2-3\sigma}.                         \tag{9}
\]

For pi|r the absolute Ramanujan value is 1 when e=k=0, and Q-1
otherwise, since e+3k>0 exactly in the latter case. Therefore the
replacement local factor is

\[
 E_Q=1+(Q-1)(D_Q-1)
      =\frac{1+(Q-1)t+(Q-2)z}{1-z}.                        \tag{10}
\]

It increases with t,z>=0. For sigma>1, t<=1/Q and z<=1/Q^2, and
substitution of those two upper bounds gives **exactly E_Q<=2**.
Also D_Q>=1, so the ratio E_Q/D_Q is at most 2. The product of the
unweighted factors D_Q converges for sigma>1. Replacing the factors
at pi|r therefore costs at most 2^omega_O(r).

The ramified factor is independent of r, since r is primary. More
explicitly an upper bound for the unit/3 contribution is

\[
 6\sum_{n\ge1}3^{n/2+2-\sigma(3n-4)}
 +2\sum_{n\ge0}3^{n/2+5/2-\sigma(3n-3)}
 +54\,3^{4\sigma}.
\]

The first two geometric ratios are 3^(1/2-3sigma)<1. The last term
covers both exceptional cusp families at lambda-exponent -4.
This also checks the ramified and unit cases rather than hiding a
level-dependent factor there. Multiplication by lambda^4 and by units
does not alter any valuation at pi|r. The lemma follows. QED.

For every eta>0, the elementary bound 2^omega_O(r)<<_eta R^eta
holds: the finitely many small prime ideals enter the constant, and
2<=Q^eta for all sufficiently large Q. Thus the completed bound improves to

\[
 |\mathcal C_r(Y;W)|\ll_{b,W}
 \sqrt R\,2^{\omega_O(r)}(R^2/Y)^b\qquad(b>0).              \tag{11}
\]

Unlike the old estimate, this already gives
C_r(Y)<<_(epsilon,W) R^(1/2+epsilon) uniformly for Y bounded below
by any fixed positive constant. The next step avoids losing this
gain by taking absolute values of the whole Mobius sum.

## 4. Uniform interpolation in the level

Fix small a>0 and eta>0. On Re(s)=1+a, (6) is absolutely convergent
and |F_r(s)|<<_a 1, independently of r. On Re(s)=-a, (7), (8), and
Stirling give

\[
 |F_r(-a+it)|\ll_{a,\eta}
     R^{1/2+2a+\eta}(1+|t|)^{2+4a}.                       \tag{12}
\]

Every level power is now explicit: R^(1/2) is the Gauss scalar,
R^(2a) the transformed conductor, and R^eta bounds the local mass.
There is no remaining phi_O(r) factor. Set A=1/2+2a+eta.

**Lemma 2 (uniform strip bound).** For -a<=sigma<=1+a,

\[
 |F_r(\sigma+it)|\ll_{a,\eta}
 R^{A(1+a-\sigma)/(1+2a)}(1+|t|)^K,                       \tag{13}
\]

where an integer K>2+4a is fixed. Constants are independent of r,t.

**Proof.** Divide F_r(s) by

    (s+3)^K R^[A(1+a-s)/(1+2a)].

The boundary bounds from (12) and absolute convergence are uniform.
The previous theta-Mellin argument gives at most exponential vertical
growth for each fixed r. Multiply by exp(h s^2), h>0, apply the
maximum principle on expanding rectangles, and let h tend to zero.
The horizontal edges vanish. Although the preliminary interior growth
constant may depend on r, the boundary constants do not; doing this
for each r therefore proves the displayed uniform inequality. This
is an explicit level-uniform Phragmen--Lindelof argument. QED.

For a,eta as small as necessary, the level exponent at sigma=1/2+a
is 1/4+O(a+eta), and at sigma=1/3+a it is 1/3+O(a+eta).
Only a fixed polynomial in |t| remains; a fixed number of derivatives
of W supplies enough Mellin decay to absorb it.

## 5. Mobius inversion in Mellin space; precise GRH use

Let L_K(w,kappa) include its usual Euler factors, with the ramified
factor at 2 absent. The reciprocal completing factor is

\[
 \frac1{L_r(w,\kappa)}=
 \frac1{L_K(w,\kappa)}(1+3^{-w})^{-1}
     \prod_{\pi\mid r}(1-\kappa(\pi)(N\pi)^{-w})^{-1}.
                                                               \tag{14}
\]

The plus sign at 3 uses kappa(lambda)=-1. This is also the Dirichlet
series of mu_O(c)kappa(c) restricted to primary c prime to r, so
division in (6) is exactly Mobius inversion, not a cancellation
assumption about its coefficients.

Unconditionally, for Re(w)>1 the reciprocal series is absolutely
convergent and bounded independently of r on any fixed right half-plane.
Under GRH for the fixed L_K(w,kappa), the following weaker reciprocal
bound is sufficient. For fixed delta>0 there is A_delta such that

\[
 L_K(\sigma+it,\kappa)^{-1}
        \ll_\delta(2+|t|)^{A_\delta},
        \qquad \sigma\ge1/2+\delta.                        \tag{15}
\]

Here is a proof needing only classical fixed-conductor polynomial growth
and the Borel--Caratheodory theorem. It is enough to take 0<delta<1/2.
For large |t|, center disks at 2+it, with outer radius 3/2-delta/2 and
inner radius 3/2-delta. GRH makes L_K zero-free on the outer disk, so
the Euler-product branch of log L_K at its center continues analytically
there. Fixed-conductor polynomial growth gives
Re(log L_K)=log|L_K|=O_delta(log(2+|t|)) above on the outer disk;
the value of log L_K at the center is O(1). Borel--Caratheodory bounds
|log L_K| on the inner disk by O_delta(log(2+|t|)), proving (15) for
1/2+delta<=sigma<=2. Euler products handle sigma>=2, and compactness
handles bounded t. Smooth Mellin decay absorbs this fixed polynomial;
no sharp subpower reciprocal estimate is required.

The character and its conductor 4O are fixed. The omitted factors in
(14) cost only R^eta, uniformly in t on that half-plane: bound each
by (1-Q^(-1/2-delta))^(-1), absorb the finitely many small primes in
the constant, and use the Q^eta bound for all remaining primes.
The factor at 3 is bounded in the same region. Thus the constants
do not deteriorate with a newly assumed family of L-functions of level r.

For clarity about the GRH hypothesis, Euler factors give

\[
       L_K(w,\kappa)=L(w,\chi_{-4})L(w,\chi_{12}).           \tag{16}
\]

At odd split primes the two rational factors agree and reproduce the
two degree-one factors. At inert primes they are opposites and give
(1-p^(-2w))^(-1). At 3 the only factor is (1+3^(-w))^(-1);
at 2 both sides omit the factor. This verifies every exceptional prime.

Since F_r is entire, its quotient in (6) is holomorphic for Re(s)>1/2
unconditionally, and for Re(s)>1/3 under the stated GRH. Finite Euler
removals introduce no zeros in these regions. We assert neither
global entirety of R_r nor a shift through the possible boundary zeros.

Mellin inversion initially on a line right of 1 gives

\[
 T_r(U;W)=\frac{\widetilde g(r)}{2\pi i}
        \int\frac{F_r(s)}{L_r(3s-1/2,\kappa)}
                           U^s\widehat W(s)\,ds.             \tag{17}
\]

Shift to 1/2+a unconditionally, or 1/3+a under GRH. Holomorphy,
(13)--(15), and rapid Mellin decay justify both shifts, with no residue.
Because |gtilde(r)|=1, the estimates are respectively

    U^(1/2+a) R^(1/4+O(a+eta)),
    U^(1/3+a) R^(1/3+O(a+eta)).

Choosing a,eta sufficiently small in terms of the requested epsilon
proves Theorems A and B, including uniformity over bounded smooth
families. This is a bound after Mobius inversion with growing r.

## 6. Comparison with the old loss, and a cutoff cross-check

For a fair comparison, apply the same interpolation/quotient argument
to the previous majorant phi_O(r)<=R. Its left-boundary level exponent
is 3/2+2a rather than 1/2+2a. It would yield the following ranges:

| Input majorant | Pointwise, unconditional | Short-sum power-saving threshold | Pointwise, GRH | Short-sum threshold |
|---|---|---|---|---|
| Old uniform Ramanujan maximum | U^(1/2)R^(3/4) | R<X^(4/15) | U^(1/3)R | R<X^(3/10) |
| Lemma 1 | U^(1/2)R^(1/4) | R<X^(4/9) | U^(1/3)R^(1/3) | R<X^(1/2) |

Arbitrary small epsilon losses and a fixed margin below each endpoint
are understood. The old row is a deduction available from that old
majorant using the current contour argument; it was not already a
documented theorem in the previous commit. The difference is an
avoidable local-mass estimate, not an obstruction forced by the conductor.

There is also a check using literal (5). Use a smooth dyadic partition
in Nc, cutting whole dyadic pieces at Z, 1<=Z<=U^(1/3). Small pieces
cost at most R^(1/2+epsilon)Z^(3/2) by (11). On a large piece Nc~C,
expanding the completed sum leaves total u,d mass O(U/C^3), since
sum_d (Nd)^(-5/2) converges. The c sum costs C^(3/2) trivially, or
R^epsilon C^(1+epsilon) under (14)--(15). Rescaled smooth weights
stay bounded whenever the piece is nonempty. Thus the large pieces
cost U/Z^(3/2) unconditionally, or (UR)^epsilon U/Z^2 under GRH.
Balancing gives (2), and the weaker GRH bound
U^(3/7)R^(2/7)(UR)^epsilon. The cutoffs are admissible for R<=U^2;
otherwise the trivial O_W(U) bound suffices. No sharp cutoff is inserted
in a GRH Mobius estimate. The stronger theorem (3) avoids the extra
absolute-value loss from this cutoff argument.

## 7. The actual long-variable block and its error budget

Fix w>=2, X,N>=1, and C>0. Let alpha_s be bounded by 1, supported on primary w-rough
s (all prime norms >w). Let t range over primary w-smooth elements.
For fixed V_1,V_2,W in C_c^infinity((0,infinity)), consider the
dyadic long-variable block after roughness Mobius inversion:

\[
 B(N)=\sum_{s,t,n}\alpha_s\mu_O(t)\kappa(nst)\widetilde g(nst)
 V_1(Nn/N)V_2(N(nt)/C)W(N(nst)/X).                          \tag{18}
\]

This is the angular-zero twisted version of the structure in [DR,
(11.2)--(11.4)], with the sum over the count of small prime factors
assembled into mu_O(t). Restrictions to an individual count are also
allowed. No C_eta cancellation hypothesis on alpha_s is needed here.

For r=st there is a **unique** possible split: s is its w-rough part,
t its w-smooth part. Terms with r nonsquarefree or even vanish.
On the support of the first and third weights, Nr is asymptotic to X/N.
For a fixed r the rescaled weight on x=Nn/N is

    V_1(x) V_2((N Nt/C)x) W((N Nr/X)x).

Whenever nonzero, both scale parameters lie in fixed compact intervals,
because V_1 has support away from zero. Hence these weights form the
bounded smooth family allowed in (3). Summing that pointwise bound over
O(X/N) possible r gives, under the fixed-character GRH,

\[
                  B(N)\ll_{\varepsilon,V_1,V_2,W}
                         X^{4/3+\varepsilon}/N.              \tag{19}
\]

This bound does not use cancellation over r. The unique factorization
checks the possible multiplicity rather than concealing it in a constant.
It remains valid with fixed divisor-bounded short coefficients after
absorbing their loss in epsilon.

For [DR, Section 11, Case 1], N>=X^(11/20), (19) gives

\[
                  B(N)\ll X^{47/60+\varepsilon},
       \qquad 5/6-47/60=1/20.                              \tag{20}
\]

The dyadic sum over such N has the same power bound; its reciprocal-N
weights form a geometric series. Even fixed powers of log X arising
in a finite-parameter prime decomposition fit inside this saving when
epsilon<1/20. In particular this contribution is o(X^(5/6)/log X).

More generally (19) saves a power whenever N>=X^(1/2+delta), yielding
X^(5/6-delta+epsilon). This covers all of Case 1 and the portion of
Case 2 with long variable above X^(1/2+delta). Without GRH, the
analogous short-sum bound requires N>=X^(5/9+delta). At the exact
Case 1 endpoint it gives X^(67/80+epsilon), which exceeds X^(5/6)
by exponent 1/240; the conditional and unconditional scopes differ.

The barrier at N=X^(1/2) is a limitation of these upper bounds, not
a counterexample to further cancellation. At that endpoint (19) is
only O(X^(5/6+epsilon)). The shorter-variable bilinear ranges still
require the relevant twisted coefficient/admissibility and comparison
arguments. The previous norm-X^(2/5) prime-block result is not a proof
for all coefficients occurring there. We have not assembled Q4.

## 8. Literature, correctness, and novelty

[DR] Dunn--Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), 967--1057,
[v3 source](https://arxiv.org/html/2109.07463v3).
Checked inputs: (5.7), (5.13)--(5.14), Appendix A rows 1,10,19;
the general transformation/residue hypotheses (5.21)--(5.48);
the Mobius/Hecke estimate (8.5)--(8.6); and the decomposition ranges
(11.2)--(11.4), (13.17)--(13.20).

The source's Proposition 8.1 is not applied to a quadratic twist by
analogy. Its coefficient formulas and general transformation are used
with verified hypotheses, followed by a new explicit majorant and
standard interpolation and GRH reciprocal-L estimates. Its divisor-
sensitive dual estimate (8.10) is related established machinery; our
proof does not assume that estimate already holds for these twists.
No large-sieve theorem is needed for the bounds proved here.

This is a useful specialization of classical theta/Voronoi machinery,
absolute Euler products, convexity, and GRH bounds. Priority for the
specialized estimates is not established. Searches for cubic-Gauss
noncubic twists and quadratic-twist convexity bounds also returned
function-field and quartic settings and unreviewed online claims;
none is imported as a theorem for this problem. No novelty is inferred
from failure to locate an exact printed version.

The finite checks in check_uniform.py verify the local mass identities,
exceptional Euler factors, and exponent budget. They do not establish
GRH or analytic cancellation. Sharp-interval tails are not advanced here.
The completed zero residue alone still does not imply prime cancellation
or exclude a prime-restricted main term; the new estimates settle the
specified long block, not the full prime problem.
