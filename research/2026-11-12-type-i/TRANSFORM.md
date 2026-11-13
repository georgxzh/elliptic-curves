# The quadratic-twisted completed Type I transform and its residue

Continuation of `8e72e3d`. The transformation and residue theorems below
are **unconditional deductions from published theta-function machinery**.
The stronger uniform de-completed Type I estimate needed in the prime
proof is not established. The ranges and error budget are documented
first in [RANGES.md](RANGES.md). Independent review: [ASTRA_AUDIT.md](ASTRA_AUDIT.md).

## 1. Exact reconstruction of the sum

Put O=Z[omega], omega^2+omega+1=0, lambda=1+2omega=sqrt(-3),
N(z)=z conjugate(z), |z|=sqrt(Nz), and
E(z)=exp(2pi i Tr(z)). All unspecified u,d,c,r sums use primary
elements (congruent to 1 modulo 3), not arbitrary associates.
Let r be odd, squarefree and primary, including r=1; write R=Nr.
Put chi_r(z)=(z/r)_3, chi_4(z)=(z/4)_3,
kappa(z)=chi_-4(Nz), and extend characters by zero at nonunits.
The convention chi_1=1 includes every element.

The unnormalized cubic Gauss sum is g(r); gtilde(r)=g(r)/sqrt(R).
Fix W in C_c^infinity((0,infinity)). The pointwise Type I expression is

\[
 T_r(U;W)=\sum_u\kappa(u)\widetilde g(ur)W(Nu/U).
                                                               \tag{1}
\]

The original twist kappa(ur) instead gives kappa(r)T_r; this outer
factor has absolute value one for odd r. Even r contributes zero
to that original expression and is not covered by the theorem below.
Twisted Gauss-sum multiplicativity gives
gtilde(ur)=gtilde(r)gtilde(u) conjugate(chi_r(u)), including zero
when (u,r)!=1. Define the **cube-completed** sum

\[
 \mathcal C_r(Y;W)=
 \sum_{\substack{u,d\equiv1(3)\\(d,r)=1}}
 |d|\widetilde g(u)\overline{\chi_r(u)}
       \underbrace{\kappa(u)\kappa(d)}_{\kappa(ud^3)}
       W\left(\frac{N(ud^3)}Y\right).                         \tag{2}
\]

Both quadratic factors are indispensable. In particular replacing the
cube-variable factor by 1 produces a different Dirichlet series.
The exact analogue of [DR, (8.7)] after Mobius inversion is

\[
 T_r(U;W)=\widetilde g(r)
 \sum_{\substack{c\equiv1(3)\\(c,2r)=1}}
       \mu_O(c)\kappa(c)|c|\,
       \mathcal C_r(U/Nc^3;W).                               \tag{3}
\]

Here Nc^3 means (Nc)^3. All sums are finite because W has compact
support. To prove (3), expand (2), set h=cd, use
kappa(c)kappa(d)=kappa(h), and sum mu_O(c) over c|h. Only h=1
survives. The coprimality restriction is legitimate because kappa
vanishes on even elements and the completing d-variable is prime to r.
There is no use of GRH or an infinite-sum interchange in this identity.

For Re(s)>1, define

\[
 \psi(z)=\kappa(z)\overline{\chi_r(z)},\qquad q=4r,
 \quad \mathcal R_r(s)=\sum_u\frac{\widetilde g(u)\psi(u)}{(Nu)^s},
\]
\[
 L_r(w,\kappa)=\sum_{d\equiv1(3),\ (d,r)=1}
                  \frac{\kappa(d)}{(Nd)^w},\qquad
 F_r(s)=L_r(3s-\tfrac12,\kappa)\mathcal R_r(s).               \tag{4}
\]

L_r omits the Euler factors above 3 and dividing r, and kappa itself
omits 2. It is not the untwisted zeta factor in [DR, (5.61)]. Absolute
convergence proves that F_r is the Mellin Dirichlet series of (2).

## 2. Local and finite transforms: r=1 first

The character kappa is primitive modulo 4O. The previous continuation
proved that its additive Fourier transform on O/4O is -4kappa.
The metaplectic transform also involves the cubic character chi_4.
Since (2) is inert, chi_4(z)=(z/(-2))_3^2 depends only on z modulo 2.
It is nontrivial of order three on (O/2O)^*=F_4^*.

**Local lemma.** With H_4(y)=sum_{z mod4} kappa(z)chi_4(z)E(zy/4),

\[
 H_4(y)=-4\kappa(y)\overline{\chi_4(y)}.                     \tag{5}
\]

**Proof.** Write each unit uniquely as z=v(1+2t), v in
{1,omega,omega^2}, t in F_4. Its kappa value is
(-1)^Tr_F4/F2(t), while chi_4(z)=chi_4(v). The inner sum over t is
zero unless vy=1 modulo 2. If y is even no v works. Otherwise exactly
one does; write vy=1+2s. The inner sum is then
4E(vy/4)=-4kappa(y), and chi_4(v)=conjugate(chi_4(y)). This proves
(5), with all characters extended by zero. In particular H_4(1)=-4.
Nontriviality of kappa on 1+2omega proves its conductor is 4, not 2.

We use exactly the finite transforms of [DR, (5.21)--(5.23)]:

\[
 \widehat\psi(d)=\sum_{x\bmod q}\psi(x)E(xd/q),
 \quad
 \widetilde\psi(v)=\chi_q(\lambda)
 \sum_{\substack{a,d\bmod q\ {m units}\\81ad=1\bmod q}}
       \widehat\psi(d)\chi_q(a)E(av/q).                      \tag{6}
\]

The 81 is lambda^8; changing it changes phases. For r=1, q=4,
psi=kappa, chi_4(lambda)=1, and 81=1 modulo 4. Thus (6) and (5) give

\[
           \widetilde\psi(v)=16\kappa(v)\overline{\chi_4(v)}.
                                                               \tag{7}
\]

This is a **metaplectic** transform, not the ordinary -4kappa Fourier
transform. The extra conjugated cubic character cannot be dropped.
In particular its value at zero vanishes. It is nonzero at units.

## 3. Odd squarefree r: all CRT phases and the transformed residue

**Theorem 1 (finite transform).** For every odd squarefree primary r,

\[
 \boxed{\quad\widetilde\psi(v)=
 16\chi_r(\lambda^2)\overline{g(r)}
      \kappa(v)\overline{\chi_4(v)}c_r(v),\quad}
 \qquad c_r(v)=\sum_{a\bmod r\ {m units}}E(av/r).
                                                               \tag{8}
\]

Set c_1=1. For general r, c_r(v) is the product over pi|r of
Npi-1 if pi|v, and -1 otherwise. In particular |c_r(v)|<=phi_O(r).

**Proof.** Every nontrivial local cubic character at an odd prime
factor of squarefree r is primitive. Its product with the primitive
kappa at conductor 4 is primitive modulo q. Thus
hat(psi)(d)=conjugate(psi(d))G(psi;q), supported on units. This is
also precisely the support hypothesis of [DR, Lemma 5.2].

Use CRT in the form x=rb+4c. Since the two moduli are coprime,

\[
 G(\psi;q)=-4\kappa(r)\overline{\chi_r(4)}\overline{g(r)}.
                                                               \tag{9}
\]

Here the quadratic local Gauss sum is -4, and
sum_{c modr} conjugate(chi_r(c))E(c/r)=conjugate(g(r)), since
chi_r(-1)=1. In (6), 81ad=1 implies
conjugate(psi(d))=psi(81a). The scalar
chi_q(lambda)psi(81)=chi_r(lambda^2), because chi_4(lambda)=1,
kappa(81)=1, and cubic exponents reduce modulo three. The remaining
character of a is kappa(a)chi_4(a). Applying CRT again, its exponential
sum is

\[
 (\kappa\chi_4)(r)H_4(v)c_r(v).
\]

Finally cubic reciprocity for the coprime primary elements 4,r gives
chi_r(4)=chi_4(r). These factors and kappa(r)^2 cancel, while the
two local -4 factors multiply to 16. This proves (8).

The explicit dependence is |g(r)|=sqrt(R) and the Ramanujan factor;
there is no unspecified r-dependent scalar. Since kappa(0)=0,

\[
                     \widetilde\psi(0)=0                     \tag{10}
\]

for every r in the theorem, including r=1.

## 4. Matching the completed sum to the theta series

Use [DR]'s normalization of the theta coefficients tau, cusp coefficients
d_j, and sigma=3^(5/2)/2. Its sieved support is

\[
 S=\{\lambda^{-3}ud^3:u,d\equiv1(3),\ u\ {m squarefree}\}.
\]

Define

\[
 D_r(s)=\sum_{\mu\in S}
       \frac{\overline{\tau(\mu)}\psi(\lambda^4\mu)}{(N\mu)^s}.
\]

The coefficient identity [DR, (5.7), (5.62)--(5.63)] proves, initially
by absolute convergence,

\[
 D_r(s)=3^{5/2+3s}\psi(\lambda)F_r(s),\qquad
 \psi(\lambda)=-\overline{\chi_r(\lambda)}.                  \tag{11}
\]

Indeed conjugate(tau(lambda^(-3)ud^3))=3^(5/2)gtilde(u)|d|,
N(lambda^(-3))=1/27, and psi(lambda u d^3)=psi(lambda)
kappa(u)conjugate(chi_r(u))kappa(d) when (d,r)=1. The completing
factor is therefore the quadratic L-factor in (4), not a principal
one. In particular psi(lambda)=-1 at r=1; omitting it gives a wrong
sign in the following transformation.

**Theorem 2 (unconditional residue theorem).** F_r(s) extends to an
entire function. The uncompleted series R_r(s) is holomorphic at
s=5/6. Consequently neither has a polar term at 5/6.

**Proof and source hypotheses.** q=4r is primary and prime to 3.
It need not be squarefree: [DR, Lemma 5.2 and Proposition 5.1] require
periodicity modulo q and support of hat(psi) on units, both verified
above. At angular mode zero the completed theta Mellin function has
only a possible simple pole at 5/6. Its residue in [DR, (5.46)] is
sigma tilde(psi)(0)/(6(Nq)^(5/3)), which vanishes by (10). Its gamma
factors are those of [DR, Lemma 5.3]; division by them creates zeros,
not poles. Thus D_r and, by (11), F_r are entire.

More explicitly the possible residue of F_r would be

\[
 \frac{(2\pi)^{5/3}\widetilde\psi(0)}
 {3^{7/2}\psi(\lambda)\Gamma(2/3)(Nq)^{5/3}}=0.              \tag{12}
\]

At s=5/6 the L-factor in (4) is L_r(2,kappa), whose absolutely
convergent Euler product is nonzero, including the removed factors.
Division proves the local assertion for R_r. This reasoning uses no
GRH. It does not assert that R_r is entire: zeros of the completing
L-function can obstruct continuation of its quotient without poles
elsewhere. QED.

Thus the relevant all-moduli polar contribution has been calculated,
not assumed to cancel. This does **not** exclude a main term of order
X^(5/6)/log X in the prime-restricted Q4 sum.

## 5. Explicit functional equation and smooth transformation

Let

\[
 a(\mu)=\overline{d_1(-\mu)}+
       \omega\overline{d_{19}(-\mu)}+
       \omega^2\overline{d_{10}(-\mu)},\quad
 \mu\in\lambda^{-4}O\setminus\{0\},
\]
\[
 D_r^*(s)=\sum_{\mu\ne0}
     \frac{a(\mu)\widetilde\psi(\lambda^4\mu)}{(N\mu)^s},
 \quad
 G(s)=\frac{\Gamma(5/6-s)\Gamma(7/6-s)}
           {\Gamma(s-1/6)\Gamma(s+1/6)}.
\]

The d_j are the explicit published cusp coefficients [DR, (5.12)--(5.16),
Appendix A]; these definitions fix every unit and conjugation convention.
The series is absolutely convergent for Re(s)>1. Equations (5.44),
(5.48) of [DR] and (11) give the identity of meromorphic functions

\[
 \boxed{\quad F_r(s)=
 \frac{(2\pi)^{4s-2}}{3^{7/2}\psi(\lambda)}
       (27(Nq)^2)^{-s}G(s)D_r^*(1-s).\quad}                 \tag{13}
\]

The apparent gamma poles on the right cancel as required by the
entire left side. Formula (13) is not restricted to a squarefree q.

For any fixed b>0 define

\[
 \mathcal W(z)=\frac1{2\pi i}\int_{\Re s=-b}
                      z^sG(s)\widehat W(s)\,ds,
 \qquad \widehat W(s)=\int_0^\infty W(t)t^{s-1}dt.
\]

The value is independent of b>0. There are no gamma poles in this
left half-plane, and the Mellin transform of W decays faster than any
power on fixed vertical strips. In particular |Wcal(z)|<=C_(b,W)z^(-b).

**Theorem 3 (smooth completed transformation).** For all Y>0,

\[
 \boxed{\quad
 \mathcal C_r(Y;W)=
 \frac1{3^{7/2}\psi(\lambda)(2\pi)^2}
 \sum_{\mu\in\lambda^{-4}O\setminus\{0\}}
 \frac{a(\mu)\widetilde\psi(\lambda^4\mu)}{N\mu}
 \mathcal W\left(\frac{(2\pi)^4YN\mu}{27(Nq)^2}\right).
 \quad}                                                     \tag{14}
\]

Insert (8) for the completely evaluated finite factor. Since Nq=16R,
the denominator in the kernel argument is **6912R^2**. At r=1 this
is the explicit modulus-4 formula: psi(lambda)=-1 and
tilde(psi)(v)=16kappa(v)conjugate(chi_4(v)). There is no residue term.

**Contour justification.** Mellin inversion on Re(s)>1 is absolutely
convergent by (4). For fixed r, the theta Mellin representation gives
at most exponential vertical growth for D_r after removing gamma
factors. On the right boundary of a strip, its Dirichlet series is
bounded. On Re(s)=-b the functional equation bounds it polynomially:
the dual series is absolutely convergent and Stirling gives
|G(-b+it)|=O_b((1+|t|)^(2+4b)). The Phragmen--Lindelof principle
therefore supplies polynomial bounds throughout the strip. One can
apply it directly after dividing by a sufficiently large power of
s+M (with its zero outside the strip) and multiplying by exp(epsilon s^2);
this suppresses the initial exponential growth on horizontal edges,
and epsilon is then sent to zero. W's Mellin decay now permits the
shift to -b. The entire function F_r contributes no residues.
Finally the absolutely convergent dual series on Re(1-s)=1+b may
be interchanged with the integral. This proves (14), rather than
assuming that a functional equation alone justifies a contour shift.

## 6. What is uniform, and what is still missing

**Corollary 4 (conservative uniform bound).** For every fixed b>0,

\[
 |\mathcal C_r(Y;W)|\ll_{b,W}
       R^{1/2}\varphi_O(r)\left(\frac{R^2}{Y}\right)^b
 \le R^{3/2}\left(\frac{R^2}{Y}\right)^b O_{b,W}(1).         \tag{15}
\]

The constant is independent of r and Y. Indeed (8) bounds the finite
factor by 16sqrt(R)phi_O(r), while
sum_mu |a(mu)|/(Nmu)^(1+b) converges independently of r. Apply the
kernel bound in (14); its remaining level dependence is exactly
R^(2b). The numerical constants 27,16 and 2pi are absorbed only into
the b,W constant, not an r-dependent one.

For fixed r this proves O_(b,W,r)(Y^(-b)) for every b>0, including
the r=1 case. This rapid decay belongs to the **completed** sum (2).
It does not pass directly through the growing Mobius sum (3).

The weakness of (15) is explicit. For the small-c cutoff in RANGES.md,
Y/R^2 is approximately (U/R^3)^(3/4), before epsilon losses. At the
edge of Section 11, Case 1, U=X^(11/20), R=X^(9/20), this ratio is
X^(-3/5), so (15) grows as b increases. It is not the uniform theorem
needed for Q4 despite being rapid decay for each fixed r.

The next precise target is the estimate (TI) in RANGES.md, or a direct
averaged substitute with its stated error budget. The zero residue
removes the expected polar term from this calculation. It does not
bound the dual sum sharply enough in the required level range.
In (14), retaining the Ramanujan factor c_r(lambda^4 mu), rather than
bounding it by phi_O(r), is a possible route to better estimates.
[DR, (8.10)] performs a related divisor-sensitive estimate after
regrouping cube coefficients. To reuse it here one must verify that
regrouping with the additional kappa conjugate(chi_4) factor and
the twisted Mobius sum. We do not promote that expectation to a theorem.

GRH is not used in (1)--(15). It remains in the previous nonzero
split-prime average, in the earlier balanced-block theorem, and in
the proposed adaptation of the Mobius/Hecke bounds in (TI). A proof
of (TI) would still leave the other prime-decomposition blocks to audit.

## 7. Sources, checks, and scope

[DR] A. Dunn and M. Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, Annals of Mathematics 200 (2024), 967--1057;
[published page](https://annals.math.princeton.edu/2024/200-3/p03),
[inspected v3](https://arxiv.org/html/2109.07463v3).
The decisive imported inputs are the theta coefficients (5.7),
general-periodic transformation Lemma 5.2, and Proposition 5.1 with
its Mellin normalization. We use the general theorem, not the
specialized cubic-character Proposition 5.3 or an angular-prime theorem.
No squarefreeness hypothesis is imposed on the general modulus q.

The prior report correctly identified that Proposition 5.3 could not
be reused unchanged. This continuation supplies the missing local
transform and residue calculation via the more general published
machinery. Yoshimoto's restricted prime-modulus theorem is unnecessary.
These are explicit specializations and elementary CRT calculations;
no novelty or priority is claimed.

`check_transform.py` verifies the finite characters and transforms using
exact cyclotomic arithmetic, including the modulus-4 case and several
odd squarefree r. It also checks the phase cancellation and budget
exponents. These finite checks do not certify the analytic machinery,
GRH, (TI), or the prime asymptotic Q4.
