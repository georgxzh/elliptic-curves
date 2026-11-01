# Exact reductions, theta coefficients, and a conditional finite-mode theorem

Status, 1 November 2026: the finite-field identities and the arithmetic
calculations below are proofs. The prime asymptotics explicitly labelled
as hypotheses have **not** been proved here. See [LITERATURE.md](LITERATURE.md)
for the normalization conflict in the printed Patterson statements.

Put \(e(t)=\exp(2\pi it)\), \(C=(2\pi)^{2/3}/(3\Gamma(2/3))\).
For \(p>3\), define the character-sum trace at every \(B\bmod p\), including
the singular parameter \(B=0\). Its value there is zero.

## 1. Exact Fourier transform

Let \(\tau_p=\sum_t\rho_p(t)e(t/p)\), so that \(\tau_p=\sqrt p\) for
\(p=1\bmod4\), and \(i\sqrt p\) for \(p=3\bmod4\).
For \(a\ne0\bmod p\), changing variables \(t=x^3+B\) gives

\[
\widehat a_p(a):=\sum_B a_p(B)e(-aB/p)
 =-\rho_p(-a)\tau_pG_p(a).
\]

The zero mode vanishes because \(\sum_t\rho_p(t)=0\). If \(p=1\bmod3\),
\(-1\) is a cube and \(G_p(-a)=G_p(a)\) is real. Fourier inversion and
pairing \(a,-a\) give precisely the cosine/sine identities in the README.
For \(p=2\bmod3\), cubing permutes the field and every trace is zero.
These arguments use the classical quadratic Gauss-sum evaluation; the
normalization and signs can also be checked by squaring \(\tau_p\).

In particular \(G_p(ac^3)=G_p(a)\) whenever \(p\nmid c\).
Values at such frequencies are identical, not independent observations.
If \(p\mid a\), the correct value is \(G_p(a)=p\); these finitely many primes
must be treated explicitly in finite data.

## 2. The proposed coefficients really are rational theta coefficients

This identifies the arithmetic shape; it does not prove a prime theorem.
Write \(\lambda=\sqrt{-3}\), \(\mathcal O=\mathbb Z[\omega]\). Use the cubic
theta coefficients \(\tau(\nu)\) normalized as in Dunn–Radziwiłł (5.6–5.8).
The imported Patterson coefficient formula, in the two cases used here, is

\[
\tau(\pm\lambda^{3n-4}cd^3)
 =\overline{g(\lambda^2,c)}\,|d/c|\,3^{n/2+2}\quad(n\ge1),
\]
\[
\tau(\pm\lambda^{3n-3}cd^3)
 =\overline{g(1,c)}\,|d/c|\,3^{n/2+5/2}\quad(n\ge0).
\]

Here \(c,d\equiv1\bmod3\), \(c\) is squarefree in \(\mathcal O\); there are
also two unit variants not needed below. Coefficients outside the listed
support vanish. In particular \(\tau(\lambda^{-3})=3^{5/2}\).

**Lemma.** For a positive integer \(a=a_1a_2^2a_3^3\), with \(a_1,a_2\)
squarefree and coprime,

\[
\Theta(a):=\frac{\tau(\lambda^{-3}a)}{3^{5/2}a^{1/3}}
 =\begin{cases}a_1^{-1/3}&a_2=1,\\0&a_2>1.\end{cases}
\tag{1}
\]

**Proof of the Gauss-sum input.** If \(c\) is a real, primary, squarefree
Eisenstein integer prime to 3, then \(g(1,c)=|c|\). At a split rational
prime \(q=\pi\bar\pi\), cubic reciprocity and conjugation give
\((\bar\pi/\pi)_3=(\pi/\bar\pi)_3=\overline{(\bar\pi/\pi)_3}\), hence both
symbols are 1. The normalized Gauss sums at \(\pi,\bar\pi\) are conjugate
of absolute value 1, so twisted multiplicativity gives \(g(1,q)=q\).

At an odd inert rational prime q, work in \(\mathbb F_{q^2}\). The cubic
character is trivial on \(\mathbb F_q^*\). All nonzero trace fibers have
the same character sum. The trace-zero line is \(\lambda\mathbb F_q\);
its nonzero elements have cubic character 1, since
\(\lambda^{q-1}=-1\) and \((q+1)/3\) is even. Thus its sum is \(q-1\),
each nonzero trace fiber has sum \(-1\), and the Gauss sum is q.
For q=2 the same conclusion follows directly from \(\mathbb F_4\):
the trace-zero nonzero element is 1 and the other two cubic character
values sum to -1. This proves \(g(1,-q)=q\) in primary normalization.

For a rational numerator u coprime to a real primary denominator c,
\((u/c)_3=1\): conjugate factors cancel at split primes, and the character
is trivial on the prime field at inert primes. Therefore all cross
factors in the multiplicativity formula are 1. This proves the claimed
evaluation for composite c as well. It also proves
\(g(\lambda^2,c)=g(-3,c)=g(1,c)=|c|\), by scaling the additive character.

Now write \(a=3^e b\), \(3\nmid b\). Away from 3, the displayed theta
support permits only valuations 0 or 1 modulo 3. Splitting does not
alter this criterion for rational b. At \(\lambda\), the valuation of
\(\lambda^{-3}a\) is \(2e-3\); the permitted cases are \(e=0,1\bmod3\).
If any valuation of a is 2 modulo 3, the coefficient is consequently zero.

Otherwise write \(b=c_0d_0^3\) with \(c_0\) squarefree; signs make
c and d primary and are absorbed by the displayed \(\pm\).
For \(e=3k\), the second formula has \(n=2k\), and gives
\(3^{k+5/2}d_0\). For \(e=3k+1\), the first has \(n=2k+1\), and gives
the same value. Dividing by \(3^{5/2}a^{1/3}\) gives (1), including
the factor \(3^{-1/3}\) in the second case. There is no coprimality
requirement between c and d in the imported formula. This proves (1).

Thus the numerical candidate is **exactly** \(\mu(a)=2C\Theta(a)\);
the earlier description as an unverified analogy can be strengthened
to this coefficient identity. The implication from these theta
coefficients to *prime-restricted* twisted means is still missing.

## 3. Where the factor two enters, and what remains unproved

For a primary prime \(\pi\) above a split rational prime p, let
\(\widetilde g(\pi)=g(1,\pi)/\sqrt p\). Directly counting cube roots and
using reciprocity gives

\[
G_p(a)/\sqrt p=
 \overline{(a/\pi)_3}\widetilde g(\pi)
 +\overline{(a/\bar\pi)_3}\widetilde g(\bar\pi).
\tag{2}
\]

To verify the additive normalization, on the prime-field representatives
the additive character \(e(\operatorname{Tr}(x/\pi))\) has coefficient
\(\bar\pi\bmod\pi\); this coefficient has cubic symbol 1 by the
reciprocity argument above. This proves (2) without a choice of angle.

Suppose, explicitly as an **additional prime-twist hypothesis**, that
the sum of \(\overline{(a/\pi)_3}\widetilde g(\pi)\) over all primary
primes, smoothly weighted by \(V(N\pi/X)\), has main term

\[
C\Theta(a)\frac{X^{5/6}}{\log X}
 \int_0^\infty V(t)t^{-1/6}\,dt .
\tag{TP-a}
\]

Primes dividing 3a are omitted. Inert primes have norm \(q^2\) and
contribute \(O(\sqrt X)\), since their normalized Gauss sums have
absolute value 1. Using (2), replacing V by \(t^{1/6}W(t)\), and the
prime number theorem in progressions then gives the W-weighted mean
of \(G_p(a)/p^{1/3}\) over \(p=1\bmod3\) as \(2C\Theta(a)\).
The factor two is the reciprocal density of the split rational primes.
There is no additional factor from taking a real part after conjugate
prime ideals have already been paired.

This is an explanation **under TP-a**, not a derivation of TP-a from
the theta formula. One still needs prime detection, its error estimates,
the finite-character twists, and the correct residue after imposing
coprimality. The all-moduli residue alone does not supply these steps.
In particular this run does not prove the squarefactor vanishing for
prime means. At a=1 the historical normalization issue and the later
preprint must be kept visible; see the literature note.

## 4. A finite-mode conditional theorem with no tail

Fix an integer M and real coefficients \(\alpha_a,\beta_a\), and put

\[
w(t)=w_0+\sum_{a=1}^M
 [\alpha_a\cos(2\pi at)+\beta_a\sin(2\pi at)].
\]

This is a smooth periodic trigonometric polynomial. Arbitrary smooth
weights do **not** have finite Fourier support. Define

\[
T_p(w)=p^{-5/6}\sum_{B\bmod p} a_p(B)w(B/p).
\]

For every p>2M, orthogonality in the exact Fourier identity proves

\[
T_p(w)=-\sum_{a=1}^M\alpha_a\,\rho_p(a)G_p(a)/p^{1/3}
 \quad(p=1\bmod12),
\]
\[
T_p(w)=-\sum_{a=1}^M\beta_a\,\rho_p(a)G_p(a)/p^{1/3}
 \quad(p=7\bmod12).
\tag{3}
\]

There is no approximation or endpoint error in (3).

Fix \(r\in\{1,7\}\), and a nonnegative nonzero
\(W\in C_c^\infty((0,\infty))\). For each frequency with a nonzero
coefficient assume the following **joint twisted-prime hypothesis**,
with \(V(t)=t^{1/6}W(t)\):

\[
\sum_{\substack{p\equiv r\ (12)\\p\nmid a}}
 \frac{\rho_p(a)G_p(a)}{2\sqrt p}V(p/X)
 =\frac{m_r(a)}8\frac{X^{5/6}}{\log X}
   \int_0^\infty V(t)t^{-1/6}\,dt
  +o_{a,V}(X^{5/6}/\log X).
\tag{JTP}
\]

Here \(m_1(a)\) equals \(\mu(a)\) on squares and three times squares,
and zero elsewhere. \(m_7(a)\) equals \(\mu(a)\) on squares,
\(-\mu(a)\) on three times squares, and zero elsewhere.
The two supports are disjoint.

**Conditional theorem.** Under these finitely many JTP assumptions,

\[
\frac{\sum_{p\equiv r(12)}W(p/X)T_p(w)}
     {\sum_{p\equiv r(12)}W(p/X)}
 \longrightarrow
 \begin{cases}-\sum_{a=1}^M\alpha_am_1(a)&r=1,\\
               -\sum_{a=1}^M\beta_am_7(a)&r=7.
 \end{cases}
\]

**Proof.** Multiply JTP by \(2X^{1/6}\).
The main term becomes \(m_r(a)X/(4\log X)\int W\), and the error
is \(o(X/\log X)\). The denominator is
\(X/(4\log X)\int W+o(X/\log X)\), by the prime number theorem
modulo 12. Apply (3) and sum its finitely many terms. All excluded
small primes eventually lie outside the support of W(p/X).
This proves the claim. Constants may depend on the fixed modes and
weights; no uniformity for M growing with X is asserted.

GRH for Hecke L-functions over \(\mathbb Q(\omega)\) may be added as
a hypothesis, but it is not needed by this elementary deduction once
JTP is assumed. We have **not** shown that GRH alone implies JTP.

For squares, and for three times squares in a fixed progression, the
quadratic symbol is respectively 1, or +1/-1. On other positive
squareclasses it is nonconstant on that progression. This explains
which characters are trivial; it does not prove cancellation of
their product with a cubic Gauss sum. Untwisted means do not establish
the zero cases of JTP, nor do they automatically split into the two
progressions.

The sharp interval \(1\le B\le\lfloor up\rfloor\) has infinitely many
Fourier modes. Its limiting profile remains conjectural: the finite
theorem gives no uniform averaged tail bound and no interchange of
M and X.
