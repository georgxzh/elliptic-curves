# Q4: a proved balanced block and the remaining long-variable problem

Continuation of `c011f0c`, 10 November 2026. This report distinguishes
unconditional identities, consequences of published results **under GRH**,
and unresolved estimates. It does not prove Q4 or assert novelty.

## 1. Definitions, normalization, and the exact target

Let K=Q(omega), O=Z[omega], omega^2+omega+1=0. A primary element is
congruent to 1 modulo 3. Ideals prime to 3 have unique primary generators.
Throughout, sums over primary primes count **both** generators over a
split rational prime. Set

\[
 e(z)=\exp(2\pi i z),\quad
 \widetilde g(c)=N(c)^{-1/2}\sum_{v\bmod c}(v/c)_3
          e(\operatorname{Tr}_{K/\mathbb Q}(v/c)),\quad
 \kappa(c)=\chi_{-4}(N(c)).
\]

Extend kappa by zero on even norm. It is the quadratic Hecke character
of K(i)/K, of finite conductor 4O, with trivial infinity type. The
conductor assertion is also proved directly in Section 4. Put

\[
 C=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)},\quad
 P(X;V)=\sum_{\substack{\pi\ {m primary\ prime}\\(\pi,6)=1}}
       \widetilde g(\pi)V(N\pi/X),\quad
 Q(X;V)=\sum_{\substack{\pi\ {m primary\ prime}\\(\pi,6)=1}}
       \kappa(\pi)\widetilde g(\pi)V(N\pi/X).
\]

Here V is **fixed** in C_c^infinity((0,infinity)). Thus the prime norms
range over [cX,dX] for fixed positive c,d, rather than necessarily up to X.
The exact missing estimate is

\[
                 Q(X;V)=o_V(X^{5/6}/\log X).                 \tag{Q4}
\]

For one specified nonnegative nonzero weight W, it is enough to assume
Q4 just for V(t)=t^(1/6)W(t). No conductor, mode, or weight-family
uniformity is needed for that particular progression limit. For all
weights, require the assertion separately for every fixed V. An error
O_V(X^(5/6)/log^(1+delta) X), delta>0, suffices, as does any power saving.
The bound O_V(X^(5/6)/log X) alone does not suffice.

The input P(X;V)=C X^(5/6)/log X integral V(t)t^(-1/6)dt
+o_V(X^(5/6)/log X) is taken
**under GRH** from Dunn--Radziwill [DR], proof equation **(13.20)** at
angular mode zero. Its two limits are X first and then the fixed small
epsilon. The rational-prime Theorem 1.1 as printed has the factor-two
conflict documented in the preceding audit. We use the primary-prime
proof equation explicitly. The unreviewed 2026 unconditional preprint
is not an input to this report.

### Exact implication and necessity at this scale

Write G_p(1)=sum_{x mod p} e(x^3/p), h_p(1)=G_p(1)/p^(1/3),
D_r(X)=sum_{p=r mod12}W(p/X), and epsilon_1=1, epsilon_7=-1.
Conjugate pairing gives G_p(1)/sqrt(p), without a factor 1/2.
The inert prime element -q has norm q^2 and gtilde(-q)=1. Therefore,
with I(X;V)=sum_{q>3 prime, q=2 mod3} V(q^2/X), exactly

\[
 \sum_{p\equiv r(12)}\frac{G_p(1)}{\sqrt p}V(p/X)
   =\frac{P(X;V)+\epsilon_r Q(X;V)-(1+\epsilon_r)I(X;V)}2.
                                                               \tag{1}
\]

I=O_V(sqrt X), sufficient here. With V=t^(1/6)W,

\[
 M_r(X):=\frac{\sum_{p\equiv r(12)}W(p/X)h_p(1)}{D_r(X)}
 =\frac{X^{1/6}}{2D_r(X)}[P+\epsilon_rQ-(1+\epsilon_r)I].       \tag{2}
\]

For completeness, the inert evaluation uses the cubic character on
F_(q^2). It is trivial on F_q^*, and also on the nonzero trace-zero
line: for lambda=sqrt(-3), lambda^(q-1)=-1 and (q+1)/3 is even.
Its sum on that line is q-1. Scaling by F_q^* shows that each nonzero
trace fiber has the same character sum, necessarily -1. Summing against
the additive character therefore gives the unnormalized Gauss sum q,
and division by sqrt(N(-q))=q gives gtilde(-q)=1.

The ordinary prime number theorem in fixed progressions gives
D_r~X/(4 log X) integral W. Given the GRH input for P, (2) yields

\[
 M_r(X)=2C+\epsilon_r\frac{X^{1/6}Q(X;V)}{2D_r(X)}+o_W(1).
                                                               \tag{3}
\]

Consequently Q4 for this V is **equivalent** to M_r->2C for either
one of r=1,7. It then gives both. This proves the weakest necessary and
sufficient error scale in this reduction, without estimating an
uncontrolled term by an asymptotic denominator. If Q instead has main
coefficient D multiplying X^(5/6)/log X integral Vt^(-1/6), the two
limits are 2(C+D) and 2(C-D). We have not excluded such a coefficient.
The Fourier identity in the earlier audit gives the corresponding
active trace-mode limit -2C: cosine in class 1, sine in class 7.

## 2. What the published proofs do and do not supply

The source locations below were inspected, including their proofs.
Quotes are deliberately short; formulas used subsequently are our
specializations, not an assertion of a published quadratic-twist theorem.

| Source | Actual scope | Consequence for Q4 |
|---|---|---|
| [DR] Theorems 1.1, 1.3; (13.20) | GRH; fixed smooth weight; primary Gauss-sum first moment and power/angular moments | Supplies P with the proof normalization; does not supply kappa |
| [DR] Definition 3.1, (3.2) | Cancellation against cubic and angular characters for a coefficient class C_eta | A quadratic coefficient twist requires a new admissibility check |
| [DR] Lemma 6.1, (6.1)--(6.5) | GRH; rough products of primes, uniformly in the tested cubic/angular character | Its R=1 proof extends to our prime blocks; proved in Section 3 |
| [DR] Proposition 10.1, (10.1) | Broad Type II, with beta in C_eta, squarefree alpha, w>log^10 X | Gives our balanced quadratic-twist theorem after admissibility is checked |
| [DR] Proposition 8.1, (8.2)--(8.8); Proposition 5.3 | Pointwise Type I; angular factor; specialized cubic-character Voronoi formula | The small-C transform changes on inserting kappa |
| [DR] Proposition 11.1, (11.4)--(11.5) | Average Type I; Case 1 invokes Corollary 8.1 | Cannot substitute a finite quadratic character for the angular factor |
| Yoshimoto [Y], Theorem 2, pp.160--161, (3.14) | Noncubic character, but modulus r a degree-one prime, r=1 mod9; a functional equation over all moduli | Does not directly cover conductor 4O or prove a prime asymptotic |

The words “uniformly in” the angular exponent in [DR] do not mean
uniformly in arbitrary finite-order Hecke characters. For Yoshimoto,
the explicitly stated hypothesis is “r is a prime number of degree 1”.
The prime 2 of O is inert, of degree two, and our conductor is its
**square**. Thus the general description of noncubic twists in [DR]'s
introduction is not a license to apply [Y, Theorem 2] to kappa. Theorem 2
also requires alpha^3 nonprincipal and alpha(-1)(-1)^ell=1; these latter
conditions would hold for kappa at ell=0, but do not fix the modulus
failure. No normalization change makes 4O a degree-one prime.

The general periodic-twist framework in [DR, Section 5, Proposition 5.1]
is a possible starting point for the missing transform. Its specialized
Propositions 5.2--5.3 and ensuing uniform bounds cannot simply be reused
unchanged. Our search did not locate a stated Q4 theorem. This is a
limited literature audit, not proof that no such theorem exists.

### The precise step that needs new work

In [DR, (8.7)] the completed inner sum contains

\[
 \sum_{d,u}|d|\widetilde g(u)\overline{(u/r)_3}
       W(N(ud^3)/Y),\qquad (d,r)=1.
\]

After inserting kappa into the original Type I sum, cube completion
instead inserts kappa(ud^3)=kappa(u)kappa(d). The character in u is
kappa(u) overline((u/r)_3), and the d-series is twisted too. For odd
squarefree r this entails modulus 4r, with a nonsquarefree local factor
at 2, and a noncubic character. The use of Proposition 5.3 immediately
after (8.7) is therefore unsupported for this new sum. In the average
Type I argument the same issue occurs at (11.4)->(11.5), Case 1.

One must calculate the periodic transform and possible residues,
then bound the dual sums **uniformly in the growing short variable r**.
Controlling each fixed r with an unspecified constant is insufficient.
The large-C part (8.6) uses a GRH bound for a Mobius/Hecke sum; the extra
fixed quadratic conductor is not the same difficulty there. Section 3
also repairs a specific Type II block. Neither observation proves all
the modified combinatorial estimates in Sections 11--13.

Absence of a zero-frequency term in a finite transform, or of a pole
in an all-moduli series, does not establish prime cancellation. The
previous Mobius-series counterexample remains applicable. We have not
proved that the long Type I issue is the **only** remaining issue in
a complete adaptation of [DR].

## 3. A proved GRH consequence: balanced prime-factor blocks

We use [DR]'s coefficient class C_eta(B,w). Its members are bounded
by 1, supported on squarefree w-rough primary b with Nb asymptotic to B,
and satisfy, for every epsilon>0,

\[
 \sum_{u\mid b}\beta_b(b/|b|)^\ell (Nb)^{it}(k/b)_3
 \ll_\varepsilon (1+|\ell|)^\varepsilon (Nk)^\varepsilon
 (1+|t|)^\varepsilon(B/Nu)^{1/2+\eta+\varepsilon},               \tag{4}
\]

when ell!=0, or ell=0 and k is not a cube; k,u are primary. This is
the actual uniformity needed below. The implied constants may depend
on fixed characters and fixed smoothing functions, not on k,u,t,ell,B.

**Lemma 1 (GRH, prime-block admissibility).** Let 0<eta and
10<=w<B, and let beta_b be the indicator of primary primes with
B<=Nb<=2B. Then kappa beta belongs to C_eta(B,w). The same is true
of kappa conjugate(psi) beta for any fixed cubic Hecke character psi
of the form (k_0/.)_3, with zero extension at its finitely many bad primes.

**Proof.** For u=1 the tested character is
kappa conjugate(psi) (k/.)_3 times the angular character. At ell=0,
its finite-order quadratic part cannot be cancelled by a character of
order dividing three. At ell!=0, nonzero infinity type cannot be
cancelled by a finite-order character. Thus the tested Hecke character
is always nonprincipal. Primary generators fix the otherwise relevant
unit convention; these are the Hecke characters used in [DR, (6.4)].

Apply the R=1 argument of [DR, (6.1)--(6.5)], inserting the fixed factor
kappa conjugate(psi) in its prime Dirichlet series. The GRH contour
remains to the right of Re(s)=1/2, and no principal pole occurs. The
finite conductor increases by at most a fixed factor depending on
4 and k_0 (norm factor at most 16 for kappa alone), with the same
fixed primary-generator conductor convention at 3; its bounds retain exactly
the uniform factors in (4). The proof allows sharp prime-norm endpoints
(the Perron cutoffs in (6.4)); equivalently they may be placed at
half-integers without changing the sum. With R=1, its remaining
logarithmic losses are absorbed in B^eta. A smooth cutoff identically
one on [1,2] puts this in the stated setup of Lemma 6.1.

If u!=1 divides a prime b, u must be that prime, so at most one summand
remains and B/Nu is between 1/2 and 1. Otherwise the sum is empty.
All other conditions of C_eta are immediate. This proves the uniform
assertion, including u, not just cancellation for each fixed character.
The proof uses GRH for the enlarged family of Hecke characters. QED.

**Theorem 2 (GRH, a balanced bilinear saving).** Put A=X^(3/5),
B=X^(2/5). Let alpha_a be arbitrary complex coefficients of absolute
value at most 1, supported on squarefree primary a with
A/10<=Na<=10A. Let W be fixed smooth, supported in [1,2]. Then there
is an absolute delta>0 such that, uniformly in these coefficients,

\[
 \sum_a\sum_{\substack{b\ {m primary\ prime}\\B\le Nb\le2B}}
   \alpha_a\kappa(ab)\widetilde g(ab)W(N(ab)/X)
             \ll_W X^{5/6-\delta}.                            \tag{5}
\]

Both conjugate prime generators are included. This is a theorem about
**composite prime-factor blocks**, not about sums supported on primes.

**Proof.** In [DR, Proposition 10.1] take its auxiliary pi=1,
eta=1/100, epsilon=10^(-6), w=B/2, and coefficients
alpha'=kappa alpha, beta'=kappa beta. Lemma 1 verifies beta' in C_eta;
squarefree support and all size/norm assumptions hold for large X.
The condition w>log^10 X holds. Also ||alpha'||_2=O(A^(1/2)), by
counting O(A) Eisenstein integers in a norm annulus. No admissibility
assumption on alpha is used in this proposition.

The main term is

\[
 C\sum_{a,b}\alpha_a\kappa(a)\kappa(b)
       \frac{\mu_O^2(ab)}{N(ab)^{1/6}}W(N(ab)/X).               \tag{6}
\]

Since a is squarefree and b prime, mu_O^2(ab) is the indicator b∤a.
For fixed a, the GRH prime-ideal estimate for the fixed nonprincipal
character kappa, followed by partial summation on [B,2B], bounds

\[
 \sum_{B\le Nb\le2B\atop b\ {m prime}}
       \kappa(b)(Nb)^{-1/6}W(Na\,Nb/X)
       \ll_W B^{1/3}(\log B)^2.                              \tag{7}
\]

The scaled smooth weights have uniformly bounded derivatives because
Na/A lies in [1/10,10]. Removing b|a costs O(B^(-1/6)):
there are O(log(Na)/log B)=O(1) such divisors. Hence (6) is

\[
 O_W(A^{5/6}B^{1/3}\log^2 X)=O_W(X^{19/30}\log^2 X).         \tag{8}
\]

Let rho=rho(epsilon)>0 be the saving in [DR, Proposition 10.1]. After
the factor ||alpha'||_2, its six error exponents specialize to

| Term | Exponent of X |
|---|---|
| w-saving | 5/6-9/50 |
| rho-saving | 5/6-rho/2 |
| A^(1/12+epsilon/2)B^(5/6) | 41/60+3epsilon/10 |
| B^(29/24)A^(-1/24) | 91/120+epsilon/2 |
| B^(1+eta) | 7/10+2eta/5+epsilon/2 |
| X^(1/2)(1+(B^2/A)^(-500)) | 4/5+epsilon/2 |

Here B^2/A=X^(1/5); the parenthesis in the last row is bounded.
Every exponent is strictly below 5/6. One may take
delta=min(rho(10^(-6))/4,1/100). The proposition supplies existence
of rho; no unprinted explicit numerical value is asserted. Equations
(8) and the error bounds prove (5). QED.

This is a concrete repair of one part of the quadratic-twist argument.
Taking alpha to be another prime indicator is permitted, but not needed.
It does not require a growing-conductor prime theorem or a supposition
about the main term of Q4. The constant is uniform in alpha and X;
W and the fixed character/conductor are permitted dependencies.

### A counterexample to unrestricted coefficient absorption

**Proposition 3 (GRH).** For 0<eta<1/2, C_eta is not in general
closed under multiplication by kappa, even on prime-supported families.

Fix psi=(4/.)_3, a nonprincipal cubic Hecke character, and put
gamma_b=kappa(b) conjugate(psi(b)) beta_b, with the prime block above.
Lemma 1 proves gamma in C_eta. But multiplying it by kappa gives
conjugate(psi(b)) beta_b away from finitely many bad primes. In (4)
take u=1, ell=t=0, k=4. The sum is the number of primary primes in
[B,2B], apart from finitely many exceptions, and is asymptotic to
B/log B. For epsilon<1/2-eta this contradicts (4). The character psi
is nonprincipal since 4 is not a cube in K (its cube root has degree
three over Q and cannot lie in the quadratic field); equivalently
use cubic Kummer theory. The same noncubic k=4 is an allowed test.
QED.

Thus preserving coefficient absolute values does not justify applying
Propositions 7.1 or 10.1 after an arbitrary quadratic twist. This is a
counterexample to a proof shortcut, not a counterexample to Q4.

## 4. Exact local information at 2 (unconditional)

**Lemma 4.** In R=O/4O, use the perfect additive pairing
E(z,y)=e(Tr(zy)/4). Then

\[
 \sum_{z\in R}\kappa(z)E(z,y)=-4\kappa(y)\quad(y\in R),
 \qquad
 \kappa(u)=-\frac14\sum_{y\in R}\kappa(y)E(u,y).              \tag{9}
\]

In particular the transform has zero constant coefficient, but twelve
nonzero coefficients. It is not the zero transform.

**Proof.** R/2R is F_4. Every unit has a unique representation
z=v(1+2t), where v is one of 1,omega,omega^2 and t runs through F_4.
Since Nv=1 and N(1+2t)=1+2Tr(t) mod4,
kappa(z)=(-1)^Tr_F4/F2(t). Consequently the inner sum over t is

\[
 e(\operatorname{Tr}(vy)/4)
 \sum_{t\in\mathbb F_4}(-1)^{\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}
                                     (t(1+\bar v\bar y))}.
\]

Here bars mean reduction modulo 2, not complex conjugation. This is zero
unless vy=1 mod2, when it is 4e(Tr(vy)/4). For nonunit y there is
no such v. For unit y exactly one v works; write vy=1+2s. Then
e(Tr(vy)/4)=-(-1)^Tr(s)=-kappa(vy)=-kappa(y). This proves the first
identity, and its symmetry proves the second.

The character is nontrivial on the kernel of reduction of units modulo
4 to units modulo 2: kappa(1+2omega)=-1 whereas kappa(1)=1. Its
conductor is therefore 4O, rather than 2O; 2 is inert and these are the
only proper local conductor divisors. Multiplicativity follows from
the norm. This also proves that it cannot be an order-three character.
QED.

For any finite or compactly supported Type I sum, (9) gives exactly

\[
 \sum_u\kappa(u)\widetilde g(ur)W(Nu/U)
 =-\frac14\sum_{y\in(O/4O)^\times}\kappa(y)
       \sum_u\widetilde g(ur)e(\operatorname{Tr}(uy)/4)W(Nu/U).
                                                               \tag{10}
\]

This reduces the extra local twist to twelve fixed additive twists.
The level-r transform and its estimates still need to be developed;
an angular-mode theorem does not evaluate these additive-twist sums.
In particular (9) is not a proof that their possible polar terms
cancel, or that the prime sum Q has zero main coefficient.

`check_q4.py` verifies (9) exhaustively using integer-pair arithmetic
(Eisenstein residues and Gaussian-integer Fourier values), multiplicativity,
the conductor witness, the cube-twist rule,
and the exponent arithmetic in Theorem 2 with exact rational numbers.
These are finite identities, not tests of prime-average asymptotics.

## 5. Primary outcome and remaining analytic input

The strongest new proved analytic statement here is Theorem 2, a
**GRH-dependent power saving** in a balanced prime-factor bilinear sum.
Proposition 3 rigorously prevents an overly broad coefficient-absorption
argument; Lemma 4 supplies the exact extra local transform. None resolves
the full prime-restricted Q4.

For the intended mode-one progression conclusion, the precise unresolved
lemma is Q4 for V=t^(1/6)W, with no extra uniformity. Equations (1)--(3)
prove both sufficiency and necessity, conditional on the published GRH
input P. A possible route through [DR] needs a modulus-4-twisted version
of its long Type I estimates, including residues and estimates uniform
in r, and admissibility checks for all prime-product coefficient blocks.
Theorem 2 verifies one balanced block, not that full list. A fixed-r
functional equation, or an O(X^(5/6)) bound, does not meet the target.

No nonzero mode-one bias in a single class modulo 12 is newly proved.
The earlier split-prime mean 2C remains a GRH consequence of (13.20).
The constructed w_* remains a designed cancellation example.

## 6. Sources and novelty boundary

* [DR] A. Dunn and M. Radziwill, *Bias in cubic Gauss sums: Patterson's
  conjecture*, Annals of Mathematics 200 (2024), 967--1057.
  [Published page](https://annals.math.princeton.edu/2024/200-3/p03),
  [inspected arXiv v3](https://arxiv.org/html/2109.07463v3).
  Checked Definition 3.1; Lemma 6.1 and (6.1)--(6.5); Proposition 10.1
  and (10.1); Proposition 8.1 and (8.2)--(8.8); Proposition 11.1,
  Case 1, (11.4)--(11.5); and (13.20). Its R=1 GRH argument cites
  Iwaniec--Kowalski, Theorem 5.19. We import that argument through [DR],
  without claiming to have independently re-proved its Hecke-L estimate.
* [Y] A. Yoshimoto, *On the cubic theta function*, Nagoya Math. J. 105
  (1987), 153--167, [original PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E6BBC2186686BFE390689C36B8036BD3/S0027763000000817a.pdf/on_the_cubic_theta_function.pdf).
  Checked (1.3), Section 3, Proposition 1, Theorem 2 and (3.14),
  especially the degree-one prime-modulus hypothesis. No prime theorem
  or modulus-4 extension is imported from this source.

Theorem 2 is a specialization of published Type II machinery plus a
GRH character check. Lemma 4 is an elementary local quadratic Gauss sum.
Proposition 3 is a diagnostic of that coefficient class. These are
advances in this repository's verified reduction, with no claim of
research priority. Targeted searches for cubic Gauss prime quadratic
twists and Yoshimoto's noncubic functional equation are not exhaustive.
Secondary sharp-interval analysis is recorded separately in TAIL_REPORT.md.
