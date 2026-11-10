# Sharp intervals: weaker sufficient conditions, not a tail theorem

This secondary investigation follows the primary outcome in
[Q4_REPORT.md](Q4_REPORT.md). Everything here is an unconditional
approximation inequality or an explicitly conditional transfer.
It does not assume that Q4, much less the general fixed-mode hypotheses,
has been proved.

## 1. The minimal signed criterion

Use the definitions of T_p, I_u, h_p(a), m_r(a), F_r, and the normalized
nonnegative W-weighted progression average Avg_X from the preceding
prime audit. Suppose the fixed-mode limits Avg_X h_p(a)->m_r(a) hold
for each fixed a. Then the necessary and sufficient additional condition
for uniform convergence of the sharp profile is

\[
 \lim_{M\to\infty}\limsup_{X\to\infty}\sup_{0\le u\le1}
 \left|\operatorname{Avg}_X
   [T_p(I_u)-T_p(K_M*I_u)]\right|=0.                         \tag{T}
\]

This was already proved in the preceding Astra audit. It follows simply
by adding and subtracting the finite Fejer polynomial and its candidate:
for fixed M, fixed-mode convergence controls the finite polynomial;
the candidate polynomials converge uniformly to F_r. Conversely, if
the sharp averages converge uniformly, the same three-term identity
proves (T). For a pointwise result fix u and remove the supremum.
Thus no absolute value inside the prime average, individual-prime tail
bound, or growing-mode maximum estimate is logically necessary.

The following useful sufficient conditions do not replace this equivalence
with a claim that a particular cutoff is necessary.

## 2. Jackson smoothing removes the logarithm in the physical error

Let K_L be the Fejer kernel of degree L and put

\[
 J_L(t)=K_L(t)^2/c_L,\qquad
 c_L=\int_0^1K_L(t)^2dt
     =\frac{2(L+1)^2+1}{3(L+1)}.
\]

J_L is a nonnegative probability kernel of degree 2L. Its Fourier
coefficients j_L(a) are real, nonnegative, at most 1, and vanish for
|a|>2L: this follows by convolving the nonnegative triangular Fourier
coefficients of K_L and normalizing at zero. For circle distance ||t||,

\[
 J_L(t)\ll\min\{L+1,(L+1)^{-3}\|t\|^{-4}\}.
\]

Splitting the integrals at 1/(L+1) gives

\[
 \int\|t\|J_L(t)dt\ll (L+1)^{-1},\qquad
 \int\|t\|^2J_L(t)dt\ll (L+1)^{-2},
 \quad |1-j_L(a)|\ll a^2/(L+1)^2.                           \tag{11}
\]

The last assertion uses evenness and 1-cos(2pi at)<=2pi^2 a^2||t||^2.
The translation inequality for an interval gives
||I_u-J_L*I_u||_1=O(1/(L+1)), uniformly in u. Both I_u and its convolution
have circle variation at most 2. The sampled-grid BV error is at most
4/p, including the endpoint convention at u=0,1 and trace zero at B=0.
Hasse's bound therefore proves

\[
 \sup_u|T_p(I_u)-T_p(J_L*I_u)|
       \ll p^{2/3}/(L+1)+p^{-1/3}.                         \tag{12}
\]

The candidate coefficient bound already proved in the cusp notes is
sum_{a<=Y}|m_r(a)|=O(Y^(1/6)log(Y+2)). Its tail divided by a is
O(L^(-5/6)log(L+2)). The attenuation error from (11) is bounded by
(L+1)^(-2) sum_{a<=2L} a|m_r(a)|, of the same order. Thus the
candidate Jackson polynomials converge uniformly at that rate.

Set e_X(a)=Avg_X h_p(a)-m_r(a), and
Delta_X(M)=max_{a<=M}|e_X(a)|. For L=o(X), all contributing primes
eventually exceed 2L. Exact finite Fourier inversion, followed by
the bounds |alpha_a(u)|<=1/(pi a), |beta_a(u)|<=2/(pi a), proves

\[
 \sup_u|\operatorname{Avg}_X T_p(I_u)-F_r(u)|
 \ll_W \frac{X^{2/3}}{L+1}+X^{-1/3}
       +\Delta_X(2L)\log(L+2)+(L+1)^{-5/6}\log(L+2).         \tag{13}
\]

Hence L=o(X), L/X^(2/3)->infinity and Delta_X(2L)log L->0 suffice.
For example L=ceil(X^(2/3)log log X) would work **if** the stated
arithmetic estimate held there. The previous Fejer physical bound
required L/(X^(2/3)log L)->infinity. This is a logarithmic improvement
in a sufficient smoothing threshold, not a new prime-average theorem.
The square of the Fejer kernel is classical Jackson smoothing;
no novelty is asserted.

## 3. A sufficient mean-square condition on the averaged coefficients

Instead of their maximum, Cauchy--Schwarz gives

\[
 \sum_{a\le2L}\frac{|e_X(a)|}{a}
 \le\left(\sum_{a\le2L}\frac1a\right)^{1/2}
       \left(\sum_{a\le2L}\frac{|e_X(a)|^2}{a}\right)^{1/2}.
                                                               \tag{14}
\]

Thus in (13) one may replace Delta_X(2L)log(L+2) by

\[
 \left(\log(L+2)\sum_{a\le2L}\frac{|e_X(a)|^2}{a}\right)^{1/2}.
                                                               \tag{15}
\]

Together with the same physical cutoff, the weaker sufficient
arithmetic condition is

\[
 \sum_{a\le2L}\frac{|\operatorname{Avg}_X h_p(a)-m_r(a)|^2}{a}
                        =o(1/\log L).                         \tag{MS}
\]

It is the square of an already **averaged** coefficient. A theorem
for the mean of the individual-prime squares is a different statement.
The maximum criterion implies (MS), but (MS) permits a much larger
error at a sparse collection of large frequencies. This is a
sufficient condition, not a claimed necessary one.

### Why the available elementary estimates do not supply it

For a split prime p, additive orthogonality gives exactly

\[
 \sum_{a=1}^{p-1}|G_p(a)|^2=2p(p-1),\qquad
 \sum_{a=1}^{p-1}|h_p(a)|^2=2p^{1/3}(p-1).                    \tag{16}
\]

Indeed the number of pairs x,y with x^3=y^3 is 1+3(p-1);
the full additive Parseval sum is p[1+3(p-1)] and the zero frequency
contributes p^2. On nonzero frequencies rho_p(a)^2=1, giving the second
identity. For inert primes the corresponding nonzero-frequency energy
is zero. These are exact finite-field statements.

The individual coefficient bound |h_p(a)|<=2p^(1/6), Jensen, and
(14) at best give a growing bound of order X^(1/3)log L for the
weighted energy of averaged coefficients before subtracting m_r.
Equation (16) likewise gives growing individual-prime energy, rather
than (MS). These upper bounds do not disprove (MS), but they do not
prove it. Extra cancellation/correlation information across primes
is needed. The angular large sieve and angular-prime estimates inspected
in [DR] do not state (MS) for our numerator modes with quadratic factors.
We have not proved that no other mean-square method could do so.

Positivity of J_L controls the approximation of the indicator. It does
not make the trace measure positive: the weights a_p(B) have both signs.
Consequently sandwiching I_u between positive approximations does not
give a Tauberian inequality for its signed trace pairing. The step from
fixed-mode limits to (T) remains additional analytic content.

## 4. Limit bookkeeping

For a fixed L, all Fourier manipulations above are finite. For a
growing L(X), (12)--(15) bound the error directly before taking a limit;
there is no interchange of a prime limit with an infinite series.
The infinite *candidate* series converges absolutely and uniformly by
its proved arithmetic coefficient bound. These facts justify only
the conditional transfers stated here. Neither the cusp proof nor
pointwise Fourier convergence at each prime supplies (T) or (MS).

The Q4 problem concerns a single mode and precedes these general
tail requirements. The new balanced-block theorem in Q4_REPORT.md
has no uniform numerator-mode conclusion and is not used to assert (MS).
