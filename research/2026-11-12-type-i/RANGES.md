# Required ranges and error budget, before estimating the new transform

Continuation of `8e72e3d`, 12 November 2026 (Toronto).
Source: Dunn--Radziwill, [arXiv v3](https://arxiv.org/html/2109.07463v3),
Sections 8, 11, 13. This records the target, not a proved twisted prime theorem.

Write R=N(r) for a single short squarefree primary element and U for
the long variable's norm, with UR asymptotic to X. We restrict to angular
mode zero, the case relevant to Q4. All smooth weights have fixed compact
support away from zero. A uniform statement must allow the rescaled
weights obtained from W(N(ur)/X); their derivative bounds stay uniform
when UR is asymptotic to X.

| Stage | Range needed | Error requirement |
|---|---|---|
| Prime decomposition, (13.17)--(13.18) | One long factor at least X^(2/3-xi); the product of the other factors at most X^(1/3+xi) | For each dyadic configuration, O(X^(5/6)/log^A X), with arbitrarily large fixed A relative to decomposition parameters |
| Average Type I, (11.1) | Long c of scale C>X^(2/3-epsilon), original short r_0 of norm asymptotic to X/C | Published untwisted error O(X^(5/6)/log^(9A_0/20-10) X), with roughness w>=log^(A_0) X |
| After roughness Mobius inversion, (11.4), Case 1 | Long n has scale U>=X^(11/20); effective short element r=r_0 h has R asymptotic to X/U, hence R<=O(X^(9/20)) | A uniform pointwise estimate, summed over short factorizations, must save a fixed power of X |
| Case 2 of Section 11 | U<X^(11/20), restructured into bilinear sums | Additional coefficient admissibility and bilinear checks remain; a pointwise Type I result alone does not handle this case |
| Assembly, (13.19)--(13.20) | Up to O(log^(1/epsilon) X) dyadic configurations for fixed epsilon | Total error o(X^(5/6)/log X), with X tending to infinity before auxiliary small parameters |

In the cube-completion argument of Section 8, denote the Mobius cube
variable by c (different from the outer long c in Section 11). Its dyadic
norm cutoff is

    Z=(UR)^(1/12+epsilon/2).

The transformed completed sum is evaluated at Y=U/N(c)^3. Even though
U is long, Y can be much smaller. At the small-c cutoff its size is
approximately U^(3/4) R^(-1/4), with the additional epsilon loss explicit
from the displayed Z. This is why rapid decay for each fixed r does not
by itself solve the uniform problem.

## A concrete sufficient pointwise target

A zero-main-term analogue of [DR, Proposition 8.1] at angular mode zero
would be the following **additional estimate**, for some rho(epsilon)>0:

\[
 \left|\sum_{u\equiv1(3)}\kappa(u)\widetilde g(ur)W(Nu/U)\right|
 \ll_{\varepsilon,W}
 \frac{U^{5/6-\rho}}{R^{1/6+\rho}}
       +U^{1/12+\varepsilon}R^{7/12+\varepsilon}.             \tag{TI}
\]

The constant must be independent of odd squarefree primary r and U.
We do not obtain (TI) merely by applying the untwisted proposition.
GRH remains part of the proposed adaptation of its Mobius estimates.

Ignoring only separately bounded factorization multiplicities, summing
(TI) over O(R) short elements in a dyadic annulus gives

\[
 X^{5/6-\rho}+X^{1/12+\varepsilon}R^{3/2}.
\]

For R<=X^(9/20) the second exponent is 91/120, strictly below 5/6.
Thus this is a sufficient pointwise strength for the Case 1 range.
Factorization multiplicities are not literally constants: a completed
proof must bound them, for example by X^nu with nu smaller than the
available power saving, or by explicit divisor sums. No such loss may
be hidden in an r-dependent implied constant. Case 2, prime-product
admissibility, and the final comparison model still need their own proofs.

For the logarithmic budget, if a per-configuration estimate has exponent
B on log X, the dyadic loss in (13.17) leaves B-1/epsilon. One needs
B-1/epsilon>1 (or an explicit little-oh at the endpoint) for the Q4 scale.
This explains why the published arbitrarily large log-saving parameter
is stronger than a fixed O(X^(5/6)/log X) error. The final O(epsilon)
normalized error in (13.20) is removed by taking epsilon to zero only
after X tends to infinity. No angular or numerator uniformity beyond
mode zero is asserted here.

The transformation and residue result in TRANSFORM.md is unconditional.
It is meaningful progress even without (TI), but its conservative
uniform bound has a much worse level dependence than (TI).
