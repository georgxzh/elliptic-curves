# An explicit second term for the candidate cusp

**A proved statement about the defined coefficient profiles.** This does
not prove a prime-average law, and does not establish an explanation of
finite-prime drift. It strengthens [COEFFICIENT_CUSP.md](COEFFICIENT_CUSP.md)
using the classical Dirichlet hyperbola method and elementary Fourier
estimates. No novelty for these methods or their application is asserted.

Keep that note's b,c,F_1,F_7 and C. Set alpha=1/6, delta=2/21,
zeta_2=zeta(2), and let gamma_E denote Euler's constant.

## 1. A summatory estimate with a smaller error

**Lemma.** For x>=2,

\[
A_b(x)=\sum_{a\le x}b(a)
 =x^\alpha(k_b\log x+l_b)+O(x^\delta\log x),
\]
\[
k_b=\frac{C}{2\zeta_2},\qquad
l_b=\frac{C}{\zeta_2}
 \left(5\gamma_E-3-4\frac{\zeta'(2)}{\zeta_2}\right).
\tag{1}
\]

**Proof.** Let sf mean squarefree, and put

\[
H(Y)=\sum_{\substack{n\le Y\\n\ {\rm sf}}}\frac1n,\quad
J(Y)=\sum_{\substack{n\le Y\\n\ {\rm sf}}}n^{-1/3}.
\]

The identity 1_sf(n)=sum_{d^2|n} mu_Mob(d), with absolute bounds on the
tails of sum d^(-2) and sum log(d)d^(-2), gives

\[
H(Y)=\frac{\log Y+\gamma_E}{\zeta_2}
 -\frac{2\zeta'(2)}{\zeta_2^2}
 +O(Y^{-1/2}\log(2Y)).
\tag{2}
\]

Indeed insert H_floor(Y/d^2)=log(Y/d^2)+gamma_E+O(d^2/Y).
The accumulated harmonic error is O(Y^(-1/2)); extending the two
absolutely convergent d-sums gives the displayed tail error.
The same square-divisor identity proves
Q(Y)=sum_{n<=Y}1_sf(n)=Y/zeta_2+O(sqrt(Y)).
Partial summation against t^(-1/3) therefore gives

\[
J(Y)=\frac{3}{2\zeta_2}Y^{2/3}+O(Y^{1/6}).
\tag{3}
\]

Write X=x^(1/6), M=floor(x^(1/14)), N=floor(x^(1/7)).
The exact representation b(m^6 n^4)=2C n^(-1/3), n squarefree,
gives the hyperbola decomposition

\[
\frac{A_b(x)}{2C}
=\sum_{\substack{n\le N\\n\ {\rm sf}}}n^{-1/3}
       \lfloor Xn^{-2/3}\rfloor
 +\sum_{m\le M}J(x^{1/4}m^{-3/2})-M J(N).
\tag{4}
\]

Every admissible pair has m<=M or n<=N, because otherwise
m>x^(1/14) and n>x^(1/7). Every pair in the overlap is admissible.
The first term in (4) is X H(N)+O(N^(2/3)); by (3) the second is
(3/(2zeta_2)) X H_M+O(x^(1/24)M^(3/4)).
The overlap term is (3/(2zeta_2)) M N^(2/3)+O(M N^(1/6)).
Using H_M=log M+gamma_E+O(1/M), together with (2), all errors are
O(x^(2/21)log x). Floors cause no larger error, since

    log N + (3/2)log M = (1/4)log x + O(1/M),
    M N^(2/3) = X + O(x^(2/21)).

The constant term after division by 2C is
(5gamma_E-3)/(2zeta_2)-2zeta'(2)/zeta_2^2. This proves (1).

For c, use the already proved Dirichlet-series multiplier

\[
R(s)=\frac{3^{-s-1/3}+3^{-3s}}{1+3^{-4s-1/3}}.
\]

Its coefficients on powers of 3 are absolutely summable after multiplication
by n^(-delta)(1+log n). Convolving (1), and bounding the omitted n>x
tail with this same stronger summability, gives

\[
A_c(x)=x^\alpha(k_c\log x+l_c)+O(x^\delta\log x),
\quad k_c=R(\alpha)k_b,\quad
l_c=R(\alpha)l_b+R'(\alpha)k_b.
\tag{5}
\]

Here R(alpha)=sqrt(3)/2 and R'(alpha)=-R(alpha)log 3.
Thus no unproved Tauberian or prime-average assumption enters (1) or (5).

## 2. An Abelian argument retaining the constant term

For v=b or c write A_v(x)=x^alpha(k log x+l)+O(x^delta log(2x)).
Let d=alpha k and e=k+alpha l. For f(t)=sin t or 1-cos t,

\[
\sum_a\frac{v(a)}a f(\lambda a)
=\lambda^{1-\alpha}
 \left[d I_f(\alpha)\log(1/\lambda)
       +e I_f(\alpha)+d I_f'(\alpha)+o(1)\right],
\tag{6}
\]
\[
I_f(\alpha)=\int_0^\infty t^{\alpha-2}f(t)\,dt.
\]

Here the derivative integral, with a factor log t, is absolutely
convergent both at zero and infinity for 0<alpha<1.

**Justification of the error and both tails.**
Extend the model x^alpha(k log x+l) down to positive x; its contribution
below x=1 is O(lambda), hence negligible compared with lambda^(1-alpha).
Set L=log(1/lambda), T=L^3 and cut at x=T/lambda.
For the error measure on [1,T/lambda], partial summation with
q(t)=f(t)/t gives the bound

    O(lambda + lambda^(1-delta) (L+log T)(1+T^delta)).

Indeed q' is bounded at zero and O(1/t) for t>=1, and the boundary
terms satisfy the same bound. Dividing by lambda^(1-alpha) makes
this tend to zero, because alpha>delta.
For the actual positive measure and for the model, partial summation
and |f|<=2 bound the tail beyond T/lambda by

    O(lambda^(1-alpha) T^(alpha-1)(L+log T)).

Since T=L^3 and alpha=1/6, this too is o(lambda^(1-alpha)).
Thus integration of the differentiated model is justified with an
o(lambda^(1-alpha)) error, proving (6).
This argument does not integrate an oscillatory big-O error over the
whole half-line without controlling its tail.

## 3. Explicit profile constants

For b+c or b-c, set d=d_+ or d_- from the first cusp note. The corresponding
ratio e/d is

\[
E_\pm=10\gamma_E-8\frac{\zeta'(2)}{\zeta(2)}
 \mp\frac{(\sqrt3/2)\log3}{1\pm\sqrt3/2}.
\tag{7}
\]

This follows either from (1),(5), or by expanding their double-pole
Dirichlet series to its simple-pole term. Use

\[
I_{\sin}(\alpha)=\frac{\Gamma(\alpha)\cos(\pi\alpha/2)}{1-\alpha},
\quad
I_{1-\cos}(\alpha)=\frac{\Gamma(\alpha)\sin(\pi\alpha/2)}{1-\alpha}.
\]

**Theorem.** With the positive K_1,K_7 already proved in the first note,

\[
F_r(u)=-K_r u^{5/6}
 \left(\log(1/u)+\eta_r+o(1)\right)\qquad(u\downarrow0),
\tag{8}
\]
\[
\eta_1=E_++\psi(1/6)-\frac{\pi}{2}\tan(\pi/12)
                   +\frac65-\log(2\pi)
       =2.4310786771678095\ldots,
\]
\[
\eta_7=E_-+\psi(1/6)+\frac{\pi}{2}\cot(\pi/12)
                   +\frac65-\log(2\pi)
       =16.325673191518164\ldots .
\]

Here psi is the logarithmic derivative of Gamma.
To prove (8), apply (6) separately to b and c, add or subtract, then
put lambda=2pi u and multiply by -1/pi. Differentiating the two displayed
I formulas gives the constants.

The relative correction to the leading term is eta_r/log(1/u).
Its much larger coefficient for class 7 explains an intrinsic source
of slow convergence in the **candidate function**. It does not imply
that moderate u has reached this asymptotic range: further oscillations
are visible in the numerical check. Neither (8) nor its computation
establishes the sharp-window prime limit or explains its finite-p drift.

[check_second_order.py](check_second_order.py) checks the constants,
summatory errors, and candidate functions independently of prime data.
It is numerical support for the formulas; the proof is the argument above.
