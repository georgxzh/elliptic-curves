# Extensions: exact identities versus conjectural transfers

## Sixth-power-free parameters

For \(p\nmid d\), scaling \(x=d^2x'\), \(y=d^3y'\) proves
\(a_p(d^6B)=a_p(B)\). For \(0\le X<p\), Möbius inversion gives

\[
\sum_{\substack{1\le B\le X\\B\ {\rm sixth\!-\!power\!-\!free}}}a_p(B)
=\sum_{d\le X^{1/6}}\mu_{\rm Mob}(d)
   S_p(\lfloor X/d^6\rfloor).
\]

This is exact. Here d<p automatically; no bad scaling prime is hidden.
It does not justify passing to prime means with d growing with p.
A fixed-d limit plus the Hasse bound is insufficient: the resulting
tail bound grows with p. A uniform averaged tail estimate is missing.

The formal candidate is \(\sum_{d\ge1}\mu_{\rm Mob}(d)F_r(u/d^6)\).
As a series of the *defined candidate functions* it converges absolutely,
by the proved cusp bound, and its leading small-u coefficient is
\(K_r/\zeta(5)\). Indeed \(\sum\mu_{\rm Mob}(d)d^{-5}=1/\zeta(5)\)
and \(\sum(\log d)d^{-5}<\infty\), also justifying passage of the
small-u asymptotic through this particular series. Its identification
with the sixth-power-free prime average remains conjectural.

## The j=1728 family: a quadratic term must be removed

For \(b_p(A)=-\sum_x\rho_p(x^3+Ax)\), put
\(Q_p(a)=\sum_x\rho_p(x)e(ax^2/p)\).
For nonzero a, substituting \(t=x^3+Ax\) for each nonzero x proves

\[
\sum_A b_p(A)e(-aA/p)=-\rho_p(-a)\tau_p Q_p(a).
\tag{1}
\]

The x=0 term vanishes; \(\rho_p(x^{-1})=\rho_p(x)\).
Counting square roots gives, for every odd p,

\[
Q_p(a)=\sum_xe(ax^4/p)-\sum_xe(ax^2/p)=G_{4,p}(a)-G_{2,p}(a).
\tag{2}
\]

Thus the transform is **quartic minus quadratic**, not the pure quartic
exponential sum. For p=3 mod4, pairing x and -x makes Q zero, and
all family traces vanish. For p=1 mod4,
\(G_{2,p}(a)=\rho_p(a)\sqrt p\).
Fourier inversion of the quadratic correction contributes -1 at
nonzero A and p-1 at A=0. For a periodic weight it contributes
\(p\,w(0)-\sum_A w(A/p)\), of order p, cancelling the same term in
the quartic part. It cannot be dropped in a \(p^{3/4}\) law.

If the relevant fixed-mode means of \(\rho_p(a)Q_p(a)/p^{1/4}\)
had finite nonzero limits, (1) would give exponent 3/4 for weighted
parameter sums. That premise is **conjectural here**.
The quartic literature is compared in [LITERATURE.md](LITERATURE.md).
The theory check verifies (1) and (2) for all nonzero a and all primes
5<=p<=100. No large quartic bias experiment was run.

## Root numbers and murmurations

The root number of a rational curve depends on all its bad primes.
It is not generally a function of B modulo the trace prime p.
Inserting it breaks the periodic Fourier calculation here. One must
specify a family, minimal models, ordering, signs, and the relation
of p to conductor before making a comparison.

Even the scales differ: for squarefree Mordell B prime to 6,
the conductor away from 6 is the square of the product of primes
dividing B. Thus B of size p gives conductor of size p^2 up to the
small-prime factor, whereas usual murmurations use p of the same
order as conductor. Shared trace bias does not prove a common limit.
We give no root-number-weighted theorem or new murmuration claim.

## The logarithmic heuristic and integral points

The Dirichlet series of mu has no double pole at 1/6.
The *coherent* series does, and [COEFFICIENT_CUSP.md](COEFFICIENT_CUSP.md)
proves the logarithmic cusp of the candidate functions.
This locates the logarithm in a squarefree harmonic sum. Relating it
to rational or integral point counts, or the repository's integral-quartic
lattice bounds, is unresolved. Neither a naive point-count heuristic
nor the previous integral-point bounds establishes the prime averages.
