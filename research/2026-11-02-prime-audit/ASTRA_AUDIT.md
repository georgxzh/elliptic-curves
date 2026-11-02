# Independent audit: exact special weights and the missing prime twists

Audited 2 November 2026. This note independently checks the four notes in
`research/2026-11-01-patterson/` and records a larger exact special case.
It does not independently prove a cubic-Gauss prime theorem. No claim of
novelty is made.

## 1. Findings on the existing proofs

The exact Fourier transform, its cosine/sine signs, the normalization
`p^(-5/6)`, and the factor `1/8` in JTP are consistent. Multiplication by
`2 X^(1/6)` and division by the weighted prime count in one class modulo
12 give the stated finite-mode conditional theorem. The condition
`p > 2M` is sufficient; an individual Fourier-mode identity only needs
`p` not to divide its integer frequency. A frequency divisible by `p`
is constant on the sampled grid, hence contributes zero.

The coefficient cusp and its second term also pass this audit. In
particular:

* The representation `a=m^6 n^4`, with squarefree `n`, is unique and
  requires no coprimality of `m,n`.
* The hyperbola cuts `M=floor(x^(1/14))`, `N=floor(x^(1/7))` cover all
  admissible pairs. Their complete overlap is admissible. Every displayed
  error is `O(x^(2/21) log x)` or smaller.
* The sign of the squarefree harmonic constant involving `zeta'(2)` is
  correct. The local derivative is `R'(1/6)=-R(1/6) log 3`, giving the
  displayed constants `E_+`, `E_-` and `eta_1`, `eta_7`.
* In the two-term Abelian proof the model below 1 contributes `O(lambda)`.
  The middle error is negligible because `2/21 < 1/6`; the actual and
  model tails are negligible with `T=log(1/lambda)^3`. Applying the proof
  separately to the positive sequences `b,c` justifies their subtraction.

These conclusions concern the explicitly defined coefficient profiles.
They do not identify those profiles with sharp-window prime averages.

## 2. State the prime input without choosing a disputed constant

Write `gtilde(pi)=g(1,pi)/sqrt(N pi)` in the primary normalization of
THEORY.md, and let `K_0` denote the constant in the following input:

\[
 \sum_{\substack{\pi\equiv1\ (3)\\\pi\ {\rm prime}}}
 \widetilde g(\pi)V(N\pi/X)
 =K_0\frac{X^{5/6}}{\log X}
   \int_0^\infty V(t)t^{-1/6}\,dt
 +o_V(X^{5/6}/\log X).
 \tag{P0}
\]

Both conjugate primary primes above each split rational prime are counted.
The weight is fixed and smooth with compact support in `(0,infinity)`.
Pairing conjugates gives exactly `G_p(1)/sqrt(p)`; the inert contribution
is `O(sqrt(X))`. For a nonnegative nonzero smooth compactly supported `W`,
substitute `V(t)=t^(1/6)W(t)`, multiply by `X^(1/6)`, and use

\[
 \sum_{p\equiv1\ (3)}W(p/X)
 \sim\frac{X}{2\log X}\int_0^\infty W(t)\,dt.
\]

Consequently (P0) implies

\[
 \frac{\sum_{p\equiv1\ (3)}W(p/X)G_p(1)/p^{1/3}}
 {\sum_{p\equiv1\ (3)}W(p/X)}\longrightarrow 2K_0.
 \tag{1}
\]

This conversion has no additional real-part factor. A rational-prime
input written with summand `G_p(1)/(2 sqrt(p))` and coefficient `K_rat`
instead gives `4 K_rat` in (1), so `K_rat=K_0/2`.

## 3. An infinite Fourier family needing only (P0)

Let real coefficients satisfy

\[
 \sum_{k\ge1}k^{1/6}(|A_k|+|B_k|)<\infty,
 \qquad H=\sum_{k\ge1}(A_k+B_k).
 \tag{2}
\]

Define the continuous periodic weight by its uniformly absolutely
convergent series

\[
\begin{split}
w(t)=w_0+\sum_{k\ge1}\{&A_k[\cos(2\pi k^6t)+\sin(2\pi k^6t)]\\
 &+B_k[\cos(2\pi\,27k^6t)-\sin(2\pi\,27k^6t)]\}.
\end{split}
\tag{3}
\]

As before put `T_p(w)=p^(-5/6) sum_{B mod p} a_p(B) w(B/p)`.

**Exact identity.** For every split prime `p>3`,

\[
 T_p(w)=-\frac{G_p(1)}{p^{1/3}}
               \sum_{\substack{k\ge1\\p\nmid k}}(A_k+B_k).
 \tag{4}
\]

**Proof.** Absolute convergence allows summation through the finite sum
over `B`. If `p` divides `k`, each relevant cosine is 1 on the grid and
each sine is 0; the constant trace sum is zero. Otherwise both frequencies
`k^6` and `27k^6=(3k^2)^3` are cubes, hence their cubic Gauss sums equal
`G_p(1)`. Their quadratic symbols are respectively 1 and `(3/p)`.
For `p=1 mod12` only the cosines contribute and `(3/p)=1`. For `p=7
mod12` only the sines contribute and `(3/p)=-1`; the minus sign in front
of the second sine compensates this symbol. Each of the two brackets
therefore contributes exactly `-G_p(1)/p^(1/3)`. This proves (4).

Using `|G_p(1)|<=2 sqrt(p)`, the error upon replacing the sum in (4) by
`H` satisfies

\[
\begin{split}
 \left|T_p(w)+H G_p(1)/p^{1/3}\right|
 &\le 2p^{1/6}\sum_{p\mid k}(|A_k|+|B_k|)\\
 &\le 2\sum_{k\ge p}k^{1/6}(|A_k|+|B_k|)=o(1).
\end{split}
\tag{5}
\]

The bound is uniform over primes tending to infinity. Thus it can be
averaged against nonnegative `W` without any estimate uniform in a
growing Fourier cutoff.

**Corollary of (P0).** For the fixed weights (3),

\[
 \frac{\sum_{p\equiv1\ (3)}W(p/X)T_p(w)}
 {\sum_{p\equiv1\ (3)}W(p/X)}
 \longrightarrow -2K_0 H.
 \tag{6}
\]

Finite support gives an exact identity outside finitely many primes.
Rapidly decreasing `A_k,B_k` give smooth weights and satisfy (2).
Condition (2) itself guarantees continuity, not arbitrary smoothness.
For inert primes every trace vanishes. Averaging over all rational
primes instead gives the limit `-K_0 H`, by the density of split primes.
This remains a special family of weights, not the sharp interval.

There is a useful larger version. Allow independent coefficients
`alpha_k,beta_k` at the cosine and sine of `k^6`, and `gamma_k,delta_k`
at the cosine and sine of `27k^6`, with the analogous weighted absolute
summability. It is enough that

\[
 \sum_k(\alpha_k+\gamma_k)
 =\sum_k(\beta_k-\delta_k)=H.
\]

The same proof gives (5) and (6). This includes cross-frequency examples
such as `cos(2 pi t)-sin(2 pi 27t)` as well as the brackets in (3).

### A nonzero smooth weight with an unconditional zero limit

Set

\[
 b_k^*(t)=\cos(2\pi k^6t)+\sin(2\pi k^6t),\qquad
 w_+(t)=\sum_{k\ge1}2^{-k}b_k^*(t),\qquad
 w_*(t)=w_+(t)-b_1^*(t).
\]

These weights are smooth: for every derivative order `d`, the series
of derivative bounds is at most a constant times
`sum_k 2^(-k) k^(6d)<infinity`. The weight `w_*` is nonzero, since its
cosine coefficient at frequency 1 is `-1/2`. Its total coefficient
`H` is nevertheless zero. For every split prime `p>3`, (4) and the
geometric series give exactly

\[
 T_p(w_*)=\frac{G_p(1)}{p^{1/3}(2^p-1)},\qquad
 T_p(w_+)=-\frac{G_p(1)}{p^{1/3}}
                    \left(1-\frac1{2^p-1}\right).
 \tag{6a}
\]

Indeed `sum_{p|k}2^(-k)=1/(2^p-1)`, and the subtracted `k=1` term is
never among those omitted multiples. For inert primes both traces are
zero. Consequently

\[
 |T_p(w_*)|\le\frac{2p^{1/6}}{2^p-1}
\]

unconditionally. If `supp W` is contained in `[a,b]` with `a>0`, every
normalized nonnegative weighted prime average of `T_p(w_*)` is
`O_W(X^(1/6) 2^(-aX))`, including either progression modulo 12.
Thus this nonzero smooth weight has an unconditional zero limit with
an exponential bound, without (P0). This is designed exact cancellation,
not a new theorem about biased prime Gauss sums. For comparison, `w_+`
has pooled split-prime mean `-2C` under the GRH input from Section 5.

## 4. Audit of the joint-character reduction

Fix a positive integer `a`. Exclude primes dividing `6a`, which eventually
lie outside the support of each fixed scaled weight. Let `chi_a(p)=(a/p)`
at unramified rational primes and `chi_{-4}(p)=(-1/p)`. Define

\[
 P_{a,j}(X;V)=\sum_{\pi\ {\rm primary\ prime}}
 \chi_a(N\pi)\chi_{-4}(N\pi)^j
 \overline{(a/\pi)_3}\widetilde g(\pi)V(N\pi/X),
 \qquad j\in\{0,1\}.
\]

Put `epsilon_1=1`, `epsilon_7=-1`. Conjugate pairing and the progression
indicator on split primes give

\[
 \sum_{p\equiv r\ (12)}\frac{\rho_p(a)G_p(a)}{2\sqrt p}V(p/X)
 =\frac{P_{a,0}(X;V)+\epsilon_rP_{a,1}(X;V)}4+O_{a,V}(\sqrt X).
 \tag{7}
\]

The factor `1/4` consists of the rational summand's `1/2` and the
progression indicator's `1/2`. If `L_j(a)` is the main coefficient of
`P_{a,j}` at scale `X^(5/6)/log X` with integral `int V(t)t^(-1/6)dt`,
then JTP for both progressions is equivalent to

\[
 L_0(a)=\frac{m_1(a)+m_7(a)}4,
 \qquad L_1(a)=\frac{m_1(a)-m_7(a)}4.
 \tag{8}
\]

For the proposed coefficients these are respectively `C Theta(a)` on
squares and on three times squares, and zero off the corresponding
supports.

The quadratic norm character in `P_{a,j}` is the restriction to
`K=Q(sqrt(-3))` of the rational quadratic character associated to
`Q(sqrt((-1)^j a))`. It is principal precisely when this quadratic field
is `Q` or `K`. For positive `a`, this is equivalent to `a` square if
`j=0`, and to `a` three times square if `j=1`.

This proves exactly when the quadratic factor disappears. It does not
prove that its product with a numerator-twisted cubic Gauss sum cancels
when nonprincipal. Even in the principal cases, the fixed numerator
twist remains unless `a` is a cube. Neither theta coefficient formulas
over all moduli nor angular-mode prime theorems supply (8) as stated.

A simple counterexample demonstrates the logical problem with inferring
prime cancellation from the absence of an all-moduli pole. Define
`v(n)=mu_Mob(n) n^(-1/6)`. In its half-plane of absolute convergence,

\[
 \sum_{n\ge1}\frac{v(n)}{n^s}=\frac1{\zeta(s+1/6)}.
\]

The right side is analytic near `s=5/6` and has a zero there. Nevertheless,
the prime number theorem and partial summation give

\[
 \sum_{p\le X}v(p)=-\sum_{p\le X}p^{-1/6}
 \sim-\frac65\frac{X^{5/6}}{\log X}.
\]

The smooth prime version has coefficient `-1` multiplying
`X^(5/6)/log X` and `int V(t)t^(-1/6)dt`. This example is a logical
obstruction to the pole-only inference; it does not determine any of
the missing cubic-Gauss twisted means.

## 5. What may be called a published or unconditional consequence

The independently inspected [Dunn--Radziwill arXiv v3](https://arxiv.org/html/2109.07463v3)
states its first moment under GRH. Its Theorem 1.3 concerns powers of
normalized Gauss sums, reduced to angular modes in Section 13. It does
not state the finite-numerator, quadratic, and progression twists in
(7). Its rational first-moment constant and its all-primary-prime
constant conflict under exact conjugate pairing, as already documented
in the repository and in the later source.

**A normalization-correct published input is available in the proof.**
Equation (13.20), at angular mode zero, compares the primary-prime sum
directly with `C sum_pi (N pi)^(-1/6) V(N pi/X)`. Choose
`xi=epsilon^1000`, `A=epsilon^(-1000)` as specified there. After
`X` tends to infinity, the normalized error is `O(epsilon)`; letting
`epsilon` tend to zero gives (P0) with `K_0=C` under GRH, using the
following displayed prime-ideal asymptotic. Therefore (6), with limit
`-2C H`, follows under GRH from that proof equation. This imports the
explicit primary-prime statement; it does not silently amend the
conflicting rational Theorem 1.1, whose literal coefficient gives
`-4C H` instead.

The September 2026 OpenAI preprint *An unconditional first moment for
cubic Gauss sums* explicitly claims the all-primary sharp coefficient
`(6/5)C`. Partial summation converts its stated theorem to (P0) with
`K_0=C`: differentiating the leading sharp term supplies `(5/6)` and
the smooth compact support makes the little-oh error uniform over the
needed range. Thus (6) with `-2C H` is an unconditional **corollary of
the theorem claimed in that unreviewed preprint**, if that theorem is
accepted. It is not an independently proved unconditional prime result
of this audit. Only its statement, normalization conversion and scope
have been checked here, not the complete analytic proof or Lean files.

The exact identity (4), the tail bound (5), and the character reduction
(7) are unconditional deductions independently justified above.

## 6. Audit of a uniform Fejer transfer criterion

Fix `r` in `{1,7}` and nonnegative nonzero smooth compactly supported
`W` as above. Let `Avg_X` mean its normalized weighted average over
`p=r mod12`. For `0<=u<=1` let `I_u` be the periodic interval indicator
of `(0,u]` on representatives in `[0,1)`, and put

\[
 Q_{M,u}=K_M*I_u,\qquad
 K_M(t)=\frac1{M+1}\left(\frac{\sin(\pi(M+1)t)}{\sin(\pi t)}\right)^2.
\]

The indicator is zero at the grid origin. This convention makes its
sampled trace sum exactly the sharp sum over `1<=B<=floor(up)`; at
`u=1` the missing origin has trace zero. Its Fejer polynomial has
constant term `u` and, for `1<=a<=M`, coefficients

\[
 \left(1-\frac a{M+1}\right)\alpha_a(u),\quad
 \left(1-\frac a{M+1}\right)\beta_a(u),\qquad
 \alpha_a(u)=\frac{\sin(2\pi au)}{\pi a},\quad
 \beta_a(u)=\frac{1-\cos(2\pi au)}{\pi a}.
 \tag{9}
\]

### The physical-space error

The interval has circle variation at most 2, uniformly in `u`.
Translation by distance `d` changes its `L1` norm by at most `2d`.
The bounds `K_M(t)<=M+1` and
`K_M(t)<=1/[4(M+1)||t||^2]` therefore give

\[
 \|I_u-Q_{M,u}\|_1
 \le 2\int_0^1\|t\|K_M(t)\,dt
 \ll\frac{\log(M+2)}{M+1}.
 \tag{10}
\]

Convolution by the nonnegative probability kernel contracts variation.
Taking an absolute value does not increase variation, so
`Var|I_u-Q_{M,u}|<=4`. For a function of bounded variation, comparison
on each of the `p` equal grid cells gives

\[
 \frac1p\sum_{B=0}^{p-1}|I_u-Q_{M,u}|(B/p)
 \le\|I_u-Q_{M,u}\|_1+\frac4p.
\]

Hasse's bound `|a_p(B)|<=2 sqrt(p)` holds for the nonsingular parameters,
and the singular parameter has trace zero. Hence

\[
 |T_p(I_u)-T_p(Q_{M,u})|
 \ll p^{2/3}\frac{\log(M+2)}{M+1}+p^{-1/3}.
 \tag{11}
\]

This bound, including its endpoint conventions, is uniform in `u`.
The compact support of `W` bounds each contributing prime above and
below by positive constant multiples of `X`, so its normalized average
satisfies the same estimate with `p` replaced by `X`.

### The arithmetic and candidate errors

Let `M=M(X)` tend to infinity with `M=o(X)` and define

\[
 \Delta_X(M)=\max_{1\le a\le M}
 \left|\operatorname{Avg}_X
       \frac{\rho_p(a)G_p(a)}{p^{1/3}}-m_r(a)\right|.
\]

For large `X` all contributing primes exceed `2M`. Applying the exact
finite Fourier formula to (9), the error between `Avg_X T_p(Q_{M,u})`
and its candidate polynomial is bounded uniformly in `u` by
`O(Delta_X(M) log(M+2))`, since `|alpha_a|<=1/(pi a)` and
`|beta_a|<=2/(pi a)`.

Write the candidate polynomial as

\[
 \mathcal F_{r,M}(u)
 =-\sum_{a\le M}\left(1-\frac a{M+1}\right)m_r(a)
 \begin{cases}\alpha_a(u),&r=1,\\\beta_a(u),&r=7.\end{cases}
\]

Its infinite-series limit is the candidate profile `F_r(u)` in the
earlier cusp notes. Since `|m_r(a)|<=b(a)+c(a)`, their summatory bound
gives both required parts of the Fejer error:

\[
 \sup_u|\mathcal F_{r,M}(u)-F_r(u)|
 \ll\sum_{a>M}\frac{b(a)+c(a)}a
       +\frac1{M+1}\sum_{a\le M}(b(a)+c(a))
 \ll M^{-5/6}\log(M+2).
 \tag{12}
\]

Combining these three independently justified estimates proves

\[
\begin{split}
 \sup_{0\le u\le1}|\operatorname{Avg}_X T_p(I_u)-F_r(u)|
 \ll_W{}&\frac{X^{2/3}\log(M+2)}{M+1}+X^{-1/3}\\
 &+\Delta_X(M)\log(M+2)+M^{-5/6}\log(M+2).
\end{split}
\tag{13}
\]

Thus a sufficient arithmetic hypothesis for uniform sharp-profile
convergence is that there exists an integer cutoff `M(X)` such that

\[
 M=o(X),\qquad
 \frac{M}{X^{2/3}\log(M+2)}\longrightarrow\infty,\qquad
 \Delta_X(M)\log(M+2)\longrightarrow0.
 \tag{14}
\]

The placement of `log(M+2)` in the denominator of the middle ratio is
essential. For example, `M=floor(X^(3/4))` satisfies the two size
conditions, but the corresponding arithmetic condition has not been
proved here. Fixed-frequency JTP provides no rate or uniformity that
implies the last condition in (14).

### An exact signed averaged-tail criterion

For a fixed cutoff `M`, put

\[
 R_{X,M}(u)=\operatorname{Avg}_X
                 [T_p(I_u)-T_p(Q_{M,u})].
\]

Assume JTP for every fixed frequency. Its finite-mode consequence gives
`Avg_X T_p(Q_{M,u}) -> mathcal F_{r,M}(u)` uniformly in `u` for each
fixed `M`. In conjunction with (12), uniform sharp-profile convergence
is then **equivalent** to

\[
 \lim_{M\to\infty}\limsup_{X\to\infty}
       \sup_{0\le u\le1}|R_{X,M}(u)|=0.
 \tag{15}
\]

Sufficiency follows by inserting the polynomial between the sharp
average and the candidate. Necessity follows by subtracting the two
uniform limits for fixed `M`, then using (12). For a pointwise version,
fix `u` and remove the supremum throughout. The absolute value in (15)
is outside the prime average; cancellation between primes is allowed.
A bound for the average of the absolute remainder would be stronger.

The unconditional estimate (11) grows with `X` when `M` is fixed, so
it does not establish (15). No stated published prime theorem in this
audit supplies either (14) or (15). These are explicit transfer
criteria, not completed proofs of the sharp-window prime profile.

## 7. Final review of the continuation drafts

A fresh review of this note, `README.md`, and `PRIME_HYPOTHESES.md`
confirms the special-family identity, the exact infinite smooth
`w_*` cancellation, the finite-character reduction, and the Fejer
transfer criterion. In particular, the coarse common modulus
`144a O` accommodates both `4D_a O` (since `D_a` divides `4a`)
and `9a O`; no exact conductor assertion or conductor-uniform
estimate is being inferred. The factors `1/4` in the pairing and
`1/8` in JTP give precisely the displayed coefficients `L_0,L_1`.
Given (P0), Q4 is equivalent to the predicted mode-one limits in
both progressions, and implies the stated sixth-power and
`27`-times-sixth-power cases.

The bound for `w_*` is pointwise in the prime, so its normalized
nonnegative weighted averages require no prime Gauss-sum theorem.
The Fejer criterion requires its displayed growing-cutoff arithmetic
estimate; fixed-mode limits alone yield only the stated equivalence
with the signed averaged-tail condition. The source qualifications
are essential: the nonzero pooled special-family limit uses the
published proof equation under GRH, or the explicitly qualified
unreviewed 2026 claim. This review supplies no new proof of either
imported prime theorem and no nonzero progression-specific or
sharp-window prime asymptotic.
