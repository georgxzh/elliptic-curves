# Prime-transfer audit: special weights and the precise missing estimates

Continuation of 7027a5b on research/continuation-2026-11.
The previous Fourier and two-term cusp proofs pass an independent
**Astra** audit. This continuation proves a restricted transfer without
a growing-mode hypothesis, an unconditional smooth-weight cancellation,
and a quantitative criterion for the sharp window. It does not prove
the general progression-specific bias law.

Detailed proofs and the independent review are in [ASTRA_AUDIT.md](ASTRA_AUDIT.md).
[PRIME_HYPOTHESES.md](PRIME_HYPOTHESES.md) matches each required prime
statement to the inspected literature and fixes all normalization factors.

## 1. A published input with an unambiguous normalization

Let C=(2pi)^(2/3)/(3Gamma(2/3)).
Dunn--Radziwill's proof equation **(13.20)**, at angular mode zero,
gives the smooth all-primary-prime first moment with coefficient C
under GRH for Hecke L-functions over Q(omega). Both conjugates are counted.
Their literal rational-prime Theorem 1.1 prints an inconsistent coefficient;
we explicitly use the proof equation, rather than silently changing the theorem.

Exact conjugate pairing then gives coefficient C/2 for G_p(1)/(2sqrt p),
and weighted split-prime mean **2C** for G_p(1)/p^(1/3).
The limits in the proof equation are X first, then its fixed small epsilon.

The 2026 unreviewed preprint claims this all-primary input unconditionally.
Its statement implies the same corollaries, but its full analytic proof
and formalization have not been independently audited here. Results
relying on it are not presented as newly established unconditional
prime asymptotics.

## 2. A nonzero prime-average theorem requiring only that input

Write T_p(w)=p^(-5/6) sum_{B mod p} a_p(B)w(B/p). Let

\[
w(t)=w_0+\sum_{k\ge1}\left\{
A_k[\cos(2\pi k^6t)+\sin(2\pi k^6t)]
 +B_k[\cos(2\pi\,27k^6t)-\sin(2\pi\,27k^6t)]\right\},
\]
\[
\sum_{k\ge1}k^{1/6}(|A_k|+|B_k|)<\infty,\qquad
H=\sum_k(A_k+B_k).
\]

**Exact identity, unconditional.** For every split p>3,

\[
T_p(w)=-\frac{G_p(1)}{p^{1/3}}\sum_{p\nmid k}(A_k+B_k).
\]

The omitted divisibility tail is bounded by
2 sum_{k>=p} k^(1/6)(|A_k|+|B_k|), hence tends to zero uniformly in p.
The infinite Fourier sum is interchanged only with a finite sum over B,
using absolute convergence. There is no interchange of a prime limit
with an uncontrolled Fourier tail.

**GRH corollary of the published proof equation.** For each fixed
nonnegative nonzero W in C_c^infinity((0,infinity)),

\[
\frac{\sum_{p\equiv1(3)}W(p/X)T_p(w)}
     {\sum_{p\equiv1(3)}W(p/X)}
\longrightarrow -2CH.
\]

Rapidly decreasing coefficients give smooth weights. The moment condition
alone gives continuity. A single harmonic cos(2pi t)+sin(2pi t) already
has limit -2C under GRH; finite sums are included. This is a specified
progression modulo 3, not an unsupported separation modulo 12.
Assuming the theorem claimed in the 2026 preprint removes GRH for
this corollary, with that source-status qualification.

## 3. An unconditional smooth-weight theorem

Put b_k(t)=cos(2pi k^6t)+sin(2pi k^6t), and define the nonzero smooth weight

\[
w_*(t)=\sum_{k\ge1}2^{-k}b_k(t)-b_1(t).
\]

Every derivative converges absolutely since sum 2^(-k)k^(6d) is finite.
Its frequency-one cosine coefficient is -1/2, so w_* is not zero.
The exact identity and a geometric series give, for every split p>3,

\[
\boxed{\quad T_p(w_*)=
\frac{G_p(1)}{p^{1/3}(2^p-1)},\qquad
|T_p(w_*)|\le\frac{2p^{1/6}}{2^p-1}.\quad}
\]

For inert p the trace sums vanish. Thus its normalized prime mean tends
to **zero unconditionally**, including separately in both classes 1 and 7
modulo 12. If supp W is contained in [c,d] with c>0, the weighted error
is O_W(X^(1/6)2^(-cX)). This is a designed cancellation theorem, not
a nonzero Patterson-bias asymptotic or a solution for the interval weight.

Finite examples also hold exactly: cos(2pi t)-cos(2pi 27t) has zero
trace pairing in class 1, and sin(2pi t)+sin(2pi 27t) in class 7.

## 4. What remains for one ordinary mode in a class modulo 12

At a=1, the missing statement is already

\[
\sum_{\pi\ {\rm primary\ prime}}\chi_{-4}(N\pi)
\widetilde g(\pi)V(N\pi/X)=o_V(X^{5/6}/\log X).
\tag{Q4}
\]

Together with the untwisted first moment, Q4 is exactly what separates
the predicted mode-one limits in the two progressions. The published
power/angular-moment theorem does not state Q4.

For general a there are two finite-character sums P_{a,0},P_{a,1}.
Their quadratic factor is principal exactly on squares for the first,
and on three times squares for the second. This is proved arithmetically;
it does not prove cancellation when the factor is nonprincipal.
Even after it disappears, a cubic numerator twist can remain.
The required main coefficients and error scales are given explicitly
in PRIME_HYPOTHESES.md.

That note also gives a rigorous obstruction to a tempting inference:
the all-moduli series of mu_Mob(n)n^(-1/6) has a zero at 5/6, but its
prime sum has a nonzero main term at X^(5/6)/log X. Absence of an
all-moduli pole alone cannot justify a zero prime coefficient.
This is a logical counterexample, not a counterexample to JTP.

## 5. A quantitative sharp-window transfer criterion

Fix one class r modulo 12 and write Avg_X for its normalized W-weighted
prime average. Define

\[
\Delta_X(M)=\max_{a\le M}
\left|\operatorname{Avg}_X h_p(a)-m_r(a)\right|,
\quad h_p(a)=\rho_p(a)G_p(a)/p^{1/3}.
\]

**Proved inequality.** For M=o(X), eventually,

\[
\begin{split}
\sup_{0\le u\le1}
\left|\operatorname{Avg}_X\frac{S_p(\lfloor up\rfloor)}{p^{5/6}}
       -F_r(u)\right|
\ll_W{}&\frac{X^{2/3}\log(M+2)}{M+1}+X^{-1/3}\\
 &+\Delta_X(M)\log(M+2)+M^{-5/6}\log(M+2).
\end{split}
\]

The proof uses Fejer approximation, bounded variation on the sampled
grid, Hasse's bound, and the proved candidate coefficient mass bound.
It includes endpoint and Fejer-attenuation errors; see Astra's Section 6.
For example, uniform control

    Delta_X(floor(X^(3/4))) = o(1/log X)

would suffice. No inspected theorem supplies this numerator uniformity.
The exponent 3/4 here is a sufficient cutoff choice, not an optimal
threshold or a claim that this particular estimate is necessary.

There is also an exact weaker formulation. If JTP holds at every fixed
frequency, uniform sharp-profile convergence is equivalent to

\[
\lim_{M\to\infty}\limsup_{X\to\infty}
\sup_u\left|\operatorname{Avg}_X
[T_p(I_u)-T_p(K_M*I_u)]\right|=0.
\tag{Tail}
\]

The absolute value is outside the prime average, so cancellation is allowed.
For a pointwise theorem fix u and remove the supremum. Pointwise Fourier
convergence at fixed p, or fixed-mode prime limits, does not prove Tail.
Our unconditional bound grows with X at fixed M.

## 6. Checks, source status and novelty

Run:

    python research/2026-11-02-prime-audit/check_reductions.py

[checks.json](checks.json) records small direct character-sum checks of
Fourier signs, aliases, divisible frequencies, Fejer polynomials,
endpoint conventions, and the sparse-family formula, plus finite
witnesses for nonprincipal quadratic characters. There was no larger
prime-bias run. These computations support the exact reductions,
not the unproved prime asymptotics.

The strongest nonzero limit established here from a refereed input is
the GRH special-family corollary. The smooth w_* zero limit, exact
character reduction, and quantitative transfer inequality are unconditional.
The finite-character prime sums, beginning with Q4, and Tail remain the
precise bottlenecks for the original sharp-window target.
All ingredients are classical; novelty of their specialization is not established.
