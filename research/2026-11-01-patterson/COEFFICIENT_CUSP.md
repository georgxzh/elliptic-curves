# A logarithmic cusp theorem for the proposed coefficients

**Proved here about an explicitly defined coefficient sequence.**
This does not prove that a prime average has this profile. No claim of
novelty for the elementary Dirichlet-series or Abelian methods is made.
The finite-mode prime theorem and its extra assumptions are in
[THEORY.md](THEORY.md).

Write \(a=a_1a_2^2a_3^3\) in the usual unique way, and *define*
\(\mu(a)=2C a_1^{-1/3}\) if \(a_2=1\), zero otherwise.
The symbol \(\mu\) in this note is this proposed mean, **not** the
Möbius function (which is denoted \(\mu_{\rm Mob}\)).

## 1. The original Dirichlet-series guess needs a correction

For \(\Re s>2/3\), absolute convergence and prime factorization give

\[
D_\mu(s):=\sum_{a\ge1}\frac{\mu(a)}{a^s}
=2C\prod_q\frac{1+q^{-s-1/3}}{1-q^{-3s}}
=2C\,\frac{\zeta(3s)\zeta(s+1/3)}{\zeta(2s+2/3)}.
\tag{1}
\]

Each Euler factor just lists exponents \(0,1\bmod3\). The rightmost
pole is **simple, at \(s=2/3\)**, with residue \(2C\). There is also
a simple pole at \(s=1/3\). Its meromorphic continuation has a
**zero**, not a double pole, at \(s=1/6\): the denominator has its
simple pole there, while both numerator factors are \(\zeta(1/2)\ne0\).
Thus the stated double-pole heuristic is false for \(D_\mu\).

It is true for the coefficients selected by the quadratic character.
Put

\[
b(a)=\mu(a)\mathbf1_{\{a\ {\rm square}\}},\qquad
c(a)=\mu(a)\mathbf1_{\{a=3\,{\rm square}\}}.
\]

For \(\Re s>1/6\),

\[
D_b(s)=2C\,\frac{\zeta(6s)\zeta(4s+1/3)}
                         {\zeta(8s+2/3)},\qquad
D_c(s)=R(s)D_b(s),
\tag{2}
\]
\[
R(s)=\frac{3^{-s-1/3}+3^{-3s}}{1+3^{-4s-1/3}}.
\]

Indeed the even permitted exponents are \(0,4\bmod6\);
at 3 the odd permitted exponents are \(1,3\bmod6\).
No other Euler factor changes. At \(\alpha=1/6\),
\(R(\alpha)=\sqrt3/2\). Consequently \(D_{b\pm c}\) have double poles,
with coefficients of \((s-\alpha)^{-2}\)

\[
d_\pm=\frac{C}{12\zeta(2)}(1\pm\sqrt3/2).
\tag{3}
\]

Both are positive. These are precisely the series of \(m_1=b+c\)
and \(m_7=b-c\) from the proposed profile.

## 2. Summatory asymptotics, without a Tauberian hypothesis

**Lemma.** As \(x\to\infty\),

\[
\sum_{a\le x}b(a)=\kappa x^{1/6}\log x+O(x^{1/6}),\qquad
\sum_{a\le x}c(a)=\frac{\sqrt3}{2}\kappa x^{1/6}\log x+O(x^{1/6}),
\tag{4}
\]
\[
\kappa=\frac{C}{2\zeta(2)}.
\]

**Proof.** Every nonzero square coefficient is uniquely at
\(a=m^6n^4\), n squarefree, with \(b(a)=2Cn^{-1/3}\).
No coprimality between m and n is required. Thus

\[
\sum_{a\le x}b(a)
=2C\sum_{\substack{n\le x^{1/4}\\n\ {\rm squarefree}}}
n^{-1/3}\lfloor x^{1/6}n^{-2/3}\rfloor
=2Cx^{1/6}\sum_{\substack{n\le x^{1/4}\\n\ {\rm squarefree}}}\frac1n
 +O(x^{1/6}).
\]

The error follows from \(\sum_{n\le Y}n^{-1/3}=O(Y^{2/3})\).
Also

\[
\sum_{\substack{n\le Y\\n\ {\rm squarefree}}}1/n
=\sum_{d\le\sqrt Y}\frac{\mu_{\rm Mob}(d)}{d^2}
     \sum_{k\le Y/d^2}1/k
=\frac{\log Y}{\zeta(2)}+O(1).
\]

Here the harmonic-sum error contributes \(O(Y^{-1/2})\);
the convergent series \(\sum(\log d)/d^2\) and its tail give the
remaining O(1). This proves the first assertion.

For the second, expand \(R(s)\) as

\[
(3^{-s-1/3}+3^{-3s})
\sum_{j\ge0}(-1)^j3^{-j/3}3^{-4js}.
\]

This is a Dirichlet series on powers of 3 whose coefficients \(r_k\)
satisfy
\(\sum |r_k|3^{-k/6}(1+k)<\infty\).
Coefficient convolution in the absolutely convergent half-plane gives
\(\sum_{a\le x}c(a)=\sum_{3^k\le x}r_k\sum_{a\le x/3^k}b(a)\).
Insert the first assertion. The error and the \(\log(3^k)\) term
are \(O(x^{1/6})\) by that absolute summability; the omitted tails
are also \(O(x^{1/6})\), using the convergent first logarithmic moment.
The leading multiplier is \(\sum r_k3^{-k/6}=R(1/6)\). This proves (4).

## 3. Exact small-u asymptotics for the candidate profile

Define the absolutely convergent series

\[
F_1(u)=-\frac1\pi\sum_{a\ge1}\frac{b(a)+c(a)}a\sin(2\pi au),
\quad
F_7(u)=-\frac1\pi\sum_{a\ge1}\frac{b(a)-c(a)}a(1-\cos(2\pi au)).
\]

**Theorem.** As \(u\downarrow0\),

\[
F_1(u)\sim -K_1u^{5/6}\log(1/u),\qquad
F_7(u)\sim -K_7u^{5/6}\log(1/u),
\tag{5}
\]
\[
K_1=\frac{(2\pi)^{5/6}}{\pi}d_+\frac65
       \Gamma(1/6)\cos(\pi/12),\qquad
K_7=\frac{(2\pi)^{5/6}}{\pi}d_-\frac65
       \Gamma(1/6)\sin(\pi/12).
\]

In particular

\[
K_7/K_1=\frac{1-\sqrt3/2}{1+\sqrt3/2}\tan(\pi/12).
\]

**Proof, including the tails.** Let \(A(x)=\sum_{a\le x}v(a)\), where
v is either nonnegative sequence b or c. By (4),
\(A(x)=k x^\alpha\log x+O(x^\alpha)\), \(\alpha=1/6\).
For \(\lambda\downarrow0\), the positive measures

\[
\frac{\lambda^\alpha}{\log(1/\lambda)}
 \sum_a v(a)\delta_{\lambda a}
\]

converge on each compact subinterval of \((0,\infty)\) to
\(k\alpha t^{\alpha-1}\,dt\), as follows by evaluating intervals
using the asymptotic for A.
Test this convergence against \(\sin(t)/t\) or \((1-\cos t)/t\).
At zero these functions are bounded. The mass below \(\delta\)
has limiting upper bound \(k\delta^\alpha\).
At infinity the functions have absolute value at most \(2/t\).
Partial summation gives
\(\sum_{a>Y}v(a)/a=O(Y^{\alpha-1}(1+\log Y))\);
after normalization the limiting upper bound for the tail above R
is \(O(R^{\alpha-1})\). Both tails therefore disappear as
\(\delta\downarrow0\), \(R\to\infty\). This justifies the convergence
despite the oscillatory sine and unbounded interval.

The resulting leading term for
\(\sum v(a)f(\lambda a)/a\) is

\[
k\alpha\lambda^{1-\alpha}\log(1/\lambda)
 \int_0^\infty t^{\alpha-2}f(t)\,dt.
\]

For \(\beta=1-\alpha=5/6\), integration by parts gives

\[
\int_0^\infty t^{-1-\beta}\sin t\,dt
 =\frac{\Gamma(\alpha)\cos(\pi\alpha/2)}{\beta},\qquad
\int_0^\infty t^{-1-\beta}(1-\cos t)\,dt
 =\frac{\Gamma(\alpha)\sin(\pi\alpha/2)}{\beta}.
\]

The boundary terms vanish. The remaining sine/cosine integrals follow
by inserting \(e^{-\varepsilon t}\) in the gamma integral and letting
\(\varepsilon\downarrow0\); Dirichlet's test controls their tails.
Add or subtract the b and c results, set \(\lambda=2\pi u\), and
use \(k\alpha=d_\pm\) to obtain (5).

For reproducible truncations a simple explicit bound is available.
With \(L=2C(1+2/\sqrt3)\), the total positive mass satisfies

\[
A_{b+c}(x)\le L x^{1/6}(1+\tfrac14\log x)\quad(x\ge1).
\]

For b this follows from the floor formula and the harmonic bound.
For c use the two representations
\(a=3m^6n^4\) and \(27m^6n^4\), with n squarefree and \(3\nmid n\);
their weights are \(2C3^{-1/3}n^{-1/3}\) and \(2Cn^{-1/3}\).
Dropping the restriction on n bounds their combined mass by
\((2/\sqrt3)\) times the preceding b bound.
Hence, for N>=1,

\[
\sum_{a>N}\frac{b(a)+c(a)}a
\le L N^{-5/6}
 \left[\frac{1+\frac14\log N}{5/6}+\frac{1/4}{(5/6)^2}\right].
\tag{6}
\]

Divide (6) by pi for the sine-profile truncation error, and multiply
it by \(2/\pi\) for the cosine-profile error. This bounds truncation,
not floating-point roundoff.

## 4. Interpretation and limit of the result

The logarithm is already forced by the harmonic sum over squarefree n
in \(m^6n^4\), after the quadratic coherence selection. It does not
require a new count of integral points. Conversely, a naive count of
integral points without that harmonic decomposition cannot establish
this law. Identifying the candidate profiles with sharp-interval
prime averages, or deriving them from integral-point statistics,
remains open in this project.

A further elementary hyperbola estimate now gives an explicit constant
after the logarithm, with a smaller summatory error. See
[SECOND_ORDER_CUSP.md](SECOND_ORDER_CUSP.md). The large secondary
constant for F_7 quantifies slow convergence of the candidate cusp;
it does not prove a prime-average limit.
