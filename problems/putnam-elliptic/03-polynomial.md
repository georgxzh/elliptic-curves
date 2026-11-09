# Problem 3 — Squares at every integer

Let \(P\) be a polynomial with real coefficients. Suppose that, for every
positive integer \(n\), the number \(P(n)^3+1\) is the square of an
integer. Prove that \(P\) is constant.

## Graduated hints

1. For large real \(t\), study the nonnegative square root
   \(f(t)=\sqrt{P(t)^3+1}\). Its values at positive integers are integers,
   although its formula need not look polynomial.
2. Define \(\Delta f(t)=f(t+1)-f(t)\). What happens to a sufficiently
   high derivative of the square root of a polynomial? Relate derivatives
   to finite differences by the fundamental theorem of calculus.
3. A sequence of integers tending to zero is eventually zero. If
   \(\Delta^k f(n)=0\) eventually, use interpolation to show that
   \(f(n)\) eventually agrees with a polynomial.
4. You now have a polynomial identity \(H^2-P^3=1\).
   Differentiate it and use coprimality. Can \(H\) divide \(P'\)?

## Elementary solution

We first prove the discrete-to-polynomial step, rather than assuming any
theorem about square values.

**Lemma.** If a real polynomial \(F\) is an integer square at every
sufficiently large positive integer, then \(F=H^2\) for a real polynomial
\(H\).

For constant \(F\) this is immediate. Otherwise let \(D=\deg F\).
Its leading coefficient must be positive, since its eventual integer
values are nonnegative. On a sufficiently large real half-line,
\(F(t)>0\), so set \(f(t)=\sqrt{F(t)}\).

Choose an integer \(k>D/2\). We claim that \(f^{(k)}(t)\to0\).
For completeness, repeated differentiation gives
\[
f^{(j)}(t)=\frac{R_j(t)}{F(t)^{j-1/2}},
\qquad \deg R_j\le j(D-1), \tag{1}
\]
with the zero numerator allowed. For \(j=0\), take \(R_0=1\).
The induction step follows from
\[
R_{j+1}=F R_j'-(j-\tfrac12)F'R_j.
\]
Since \(F(t)\) is asymptotic to a positive constant times \(t^D\),
(1) bounds \(|f^{(k)}(t)|\) by a constant times
\(t^{D/2-k}\) for large \(t\). The exponent is negative, proving
the claim.

Define \(\Delta f(t)=f(t+1)-f(t)\). The fundamental theorem of
calculus gives \(\Delta f(t)=\int_0^1f'(t+s)\,ds\). Iterating this
identity yields
\[
\Delta^k f(n)=\int_0^1\!\cdots\!\int_0^1
 f^{(k)}(n+s_1+\cdots+s_k)\,ds_1\cdots ds_k\longrightarrow0. \tag{2}
\]
The convergence follows by bounding the integrand uniformly for
\(n\le n+s_1+\cdots+s_k\le n+k\).

But
\[
\Delta^k f(n)=\sum_{i=0}^k(-1)^{k-i}\binom{k}{i}f(n+i)
\]
is an integer. Thus it is zero for every integer \(n\ge N\), for
some \(N\). Let \(H\) be the polynomial of degree at most \(k-1\)
interpolating \(f(N),\ldots,f(N+k-1)\). Taking one difference lowers
the degree of a nonconstant polynomial by one, so \(\Delta^kH=0\).
The recurrence \(\Delta^k f(n)=0\) determines \(f(n+k)\) from
the preceding \(k\) values. Induction therefore gives
\(H(n)=f(n)\) for every \(n\ge N\).

The polynomials \(H^2\) and \(F\) agree at infinitely many points,
so they are identical. This proves the lemma.

Apply the lemma to \(F=P^3+1\), obtaining
\[
H^2-P^3=1.
\]
Suppose \(d=\deg P>0\). Degree comparison gives
\(\deg H=3d/2\); in particular \(H\) is nonconstant. Any common
polynomial divisor of \(H\) and \(P\) divides 1, so they are
coprime. Differentiation gives
\[
2HH'=3P^2P'.
\]
Since \(H\) is coprime to \(P^2\), this forces \(H\mid P'\).
Consequently
\[
\frac{3d}{2}=\deg H\le\deg P'=d-1,
\]
which is impossible. Hence \(P\) is constant. \(\square\)

## Optional elliptic-curve background

The identity \(H(t)^2=P(t)^3+1\) would trace points on the smooth cubic
\(Y^2=X^3+1\) using polynomial coordinates. The derivative argument
shows directly why a nonconstant polynomial tracing is impossible. The
surprise in the problem is that square values only at integers already
force such an identity. Neither a classification of integral points nor
an elliptic-curve theorem is required. This proof concerns polynomial
coordinates; it does not by itself prove the stronger statement about
arbitrary rational-function parametrizations.

## Design assessment and validation limits

Target: A5, at the easier end of the requested A5/A6 band. The independent
statement-only reviewer rated it A4/A5, with A5 plausible and A6 too strong.
The obstacle is discovering that small high differences must vanish
exactly; the remaining algebra is brief. Prerequisites are ordinary
calculus, polynomial interpolation, and elementary polynomial divisibility.
Finite differences and their needed properties are proved in the solution.

Real coefficients are intentional. One must not assume \(P\) is integer-
valued or has rational coefficients. The possible constants, though not
requested, are exactly \(\sqrt[3]{m^2-1}\) with
\(m\in\mathbb Z_{\ge0}\), including \(-1\) and 0. Zeros of \(F\)
are harmless because differentiation occurs only on a positive tail.

No finite numerical test can certify the hypothesis: for any positive
\(M\), the nonconstant polynomial
\[
P_M(t)=2+\prod_{j=1}^M(t-j)
\]
passes the square-value test at \(1,\ldots,M\). The proof, not bounded
experimentation, validates this finalist. The square-value lemma and the
polynomial derivative obstruction have substantial classical precedent;
see [prior-art notes](PRIOR_ART.md). The proposed combination is a contest
formulation, not a new theorem claim.
