# Which prime inputs are actually needed?

Continuation of commit 7027a5b. Proofs, imported theorems and unresolved
inputs are distinguished below. The independent [Astra audit](ASTRA_AUDIT.md)
checks the normalizations and transfers. No novelty claim is made.

## 1. Fixed-mode hypotheses with exact constants

Fix r in {1,7}, a positive integer a, and a nonnegative nonzero
W in C_c^infinity((0,infinity)). Write

\[
D_{r,W}(X)=\sum_{p\equiv r\ (12)}W(p/X)
 \sim\frac{X}{4\log X}\int W,\qquad
h_p(a)=\rho_p(a)G_p(a)/p^{1/3}.
\]

Define h_p(a)=0 when p divides a. For fixed a those primes eventually
leave the support. Put V(t)=t^(1/6)W(t). The needed hypothesis is

\[
\sum_{\substack{p\equiv r\ (12)\\p\nmid a}}
 \frac{\rho_p(a)G_p(a)}{2\sqrt p}V(p/X)
=\frac{m_r(a)}8\frac{X^{5/6}}{\log X}
   \int V(t)t^{-1/6}\,dt
 +o_{a,r,V}(X^{5/6}/\log X).
\tag{JTP}
\]

Here mu(a)=2C Theta(a), C=(2pi)^(2/3)/(3Gamma(2/3));
m_1 is mu on squares and three times squares, and zero elsewhere;
m_7 is mu on squares, -mu on three times squares, and zero elsewhere.
Theta is the proved rational theta specialization in the previous notes,
not an already proved prime mean.

Multiplying JTP by 2X^(1/6) gives a main term
m_r(a)X/(4log X) integral W and error o(X/log X).
Division by D gives Avg h_p(a) -> m_r(a).
Every fixed trigonometric polynomial needs only finitely many such
statements. Its coefficients and frequencies stay fixed; no error rate
or uniformity in a follows from these little-oh statements.

The exact Fourier identity is valid separately for every integer mode
not divisible by p, including modes above p. Modes divisible by p
give a constant on the sampled grid and contribute zero. Thus there
is no unnoticed aliasing assumption in the infinite special family
proved in ASTRA_AUDIT.md. The earlier condition p>2M is sufficient
for the finite theorem but stronger than necessary.

## 2. Two finite-character prime sums, not an angular moment

Let K=Q(sqrt(-3)), O=Z[omega], and count every primary prime element
pi=1 mod3, including both conjugates above a split rational prime.
Write gtilde(pi)=g(1,pi)/sqrt(N pi). For primes away from 6a define

\[
P_{a,j}(X;V)=\sum_{\pi\ {\rm primary\ prime}}
 \chi_a(N\pi)\chi_{-4}(N\pi)^j
 \overline{(a/\pi)_3}\widetilde g(\pi)V(N\pi/X),
 \quad j=0,1.
\tag{1}
\]

chi_a is the primitive rational quadratic character of Q(sqrt(a)),
principal when a is a square; chi_-4(n)=(-1/n) on odd n.
The omitted primes are precisely those above rational divisors of 6a.
The numerator cubic character is defined by the residue symbol, so
the formula also covers a divisible by 3 after omitting the ramified prime.

These are finite-order characters on primary generators. For example,
144a O is a sufficient common modulus: the quadratic norm factors
depend on the generator modulo 4D_a O, with D_a dividing 4a; cubic
reciprocity and the supplementary law at 3 give modulus dividing
9a O for the cubic numerator. This deliberately coarse modulus is
not a claim about the exact conductor or a uniform estimate in it.

The exact pairing identity is

\[
\frac{G_p(a)}{\sqrt p}=
 \overline{(a/\pi)_3}\widetilde g(\pi)
 +\overline{(a/\bar\pi)_3}\widetilde g(\bar\pi).
\]

Inert prime elements have norm q^2 and total contribution O_V(sqrt X).
Consequently, with epsilon_1=1 and epsilon_7=-1,

\[
\sum_{p\equiv r(12)}\frac{h_p(a)}{2p^{1/6}}V(p/X)
 =\frac{P_{a,0}+\epsilon_rP_{a,1}}4+O_{a,V}(\sqrt X).
\tag{2}
\]

If P_{a,j} has main coefficient L_j(a) at scale
X^(5/6)/log X times integral V(t)t^(-1/6), JTP for both r is
equivalent to

\[
L_0(a)=\frac{m_1(a)+m_7(a)}4,\qquad
L_1(a)=\frac{m_1(a)-m_7(a)}4.
\tag{3}
\]

Thus the proposed coefficients are C Theta(a) for L_0 on squares
and for L_1 on three times squares, and zero elsewhere.

**Proved character criterion.** The quadratic factor in (1) is
principal on K exactly when a is a square for j=0, or a is three
times a square for j=1.
Indeed its associated extension is K(sqrt((-1)^j a))/K.
A rational number becomes a square in K only if its rational
squareclass is 1 or -3: square x+y sqrt(-3) and use 2xy=0.
The converse is immediate. Quadratic class field theory identifies
the norm pullback with this extension's character.

This criterion explains the proposed support; it proves no cancellation
of the product with gtilde. In the principal cases the cubic numerator
still remains unless a is a cube. A square cube is k^6; a cube which
is three times a square is 27k^6.

| Frequency | P_{a,0} | P_{a,1} | What is reduced to known untwisted input? |
|---|---|---|---|
| 1 or k^6 | untwisted | quadratic twist chi_-4 | Only the first sum |
| 27k^6 | quadratic twist chi_-4 | untwisted | Only the second sum |
| 3 | nonprincipal quadratic times cubic twist | cubic numerator 3 | Neither from the stated prime theorems |
| 4 | cubic numerator 4, predicted coefficient zero | quadratic times cubic twist | Neither |
| 8 | quadratic chi_2 | quadratic chi_-2 | Neither |

All equalities in the first two rows omit finitely many bad primes.
For the second row chi_3 and chi_-4 have the same pullback to K.

## 3. Resolve the normalization using the published proof

Source: Dunn--Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
[Annals 200 (2024), 967--1057](https://annals.math.princeton.edu/2024/200-3/p03),
[arXiv v3](https://arxiv.org/html/2109.07463v3).
The first-moment theorem begins:
> “Assume the Generalized Riemann Hypothesis for Hecke L-functions over Q(omega).”

Its literal rational-prime Theorem 1.1 prints coefficient C for
G_p(1)/(2sqrt p). But **equation (13.20) of the proof** explicitly compares
the all-primary-prime sum with C times its N(pi)^(-1/6) model.
At angular mode zero, that proof equation yields

\[
\sum_{\pi\ {\rm primary\ prime}}\widetilde g(\pi)V(N\pi/X)
=C\frac{X^{5/6}}{\log X}\int V(t)t^{-1/6}\,dt
 +o_V(X^{5/6}/\log X)
\tag{P0}
\]

under GRH, for each fixed smooth compactly supported V.
Here is the order of limits: fix the proof's positive epsilon, put
xi=epsilon^1000 and A=epsilon^(-1000), and let X tend to infinity.
The error in (13.20), divided by X^(5/6)/log X, has limsup O_V(epsilon).
Now let epsilon tend to zero. Its remaining power savings have positive
exponents for each fixed pair of parameters; no joint limit is used.
The following prime-ideal asymptotic evaluates the model with coefficient 1.

This provides a normalization-explicit **published GRH input**.
Pairing both conjugates proves the rational coefficient is C/2,
and the weighted mean of G_p(1)/p^(1/3) over split rational primes is 2C.
It is not consistent to combine the literal coefficient in Theorem 1.1
with the all-primary coefficient in (13.20). We use the latter equation
explicitly, rather than silently changing the former or claiming an erratum
has been published. No numerical evidence is used in this resolution.

Theorem 1.3 is, under the same GRH and fixed smooth V,

\[
\sum_{\pi\ {\rm primary\ prime}}\widetilde g(\pi)^kV(N\pi/X)
 =o(X^{5/6}/\log X),\qquad 1<|k|\le X^{1/100},
\]

uniformly in those integer powers. The identity
gtilde(pi)^3=-pi/|pi| converts these to angular twists.
This is not uniformity in the numerator a of G_p(a), nor in the finite
characters (1). Inserting chi_-4 is an additional assertion, even for a=1.

## 4. What other sources do and do not supply

* Heath-Brown's 2000 *Kummer's conjecture for cubic Gauss sums* gives
  unconditional bounds at the X^(5/6+epsilon) scale; see
  [Oxford's record](https://ora.ox.ac.uk/objects/uuid%3A16c3966e-61cb-499d-839c-559b3794fcff)
  and its restatement in Dunn--Radziwill (1.2).
  These are not little-oh at X^(5/6)/log X. The direct PDF was not
  retrieved in this audit; we use the stated bound as restated in the
  inspected paper, not a claimed new audit of its proof.
* Patterson's theta coefficients and Yoshimoto's *On the cubic theta
  function*, Nagoya Math. J. 105 (1987), 153--167, concern all-moduli
  Dirichlet series. Dunn--Radziwill explicitly describe Yoshimoto's
  primitive-character condition psi^3 nonprincipal in Section 1.3.
  Their Section 5 treats periodic twists; Proposition 5.2 specializes
  to squarefree primary cubic moduli. No prime-weighted JTP follows
  just by substituting a character into these functional equations.
  Yoshimoto's full paper was not independently re-proved here.
* The [September 2026 OpenAI preprint](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf),
  Theorem 1.1, claims the unconditional sharp all-primary coefficient
  (6/5)C. Its Remark 1.2 already documents the conflicting normalizations.
  Partial summation gives (P0): on the fixed support of V, the sharp
  little-oh is uniformly small, and integration by parts contributes 5/6.
  The stated fixed-angular extension does not include (1).
  Its full proof and Lean development were not independently audited.
  We separately label consequences obtained by accepting this unreviewed
  theorem; we do not present them as independently established here.

The absence of a residue in an all-moduli series cannot by itself settle
the missing zero main terms. A rigorous generic counterexample is
v(n)=mu_Mob(n)n^(-1/6):

\[
\sum_{n\ge1}\frac{v(n)}{n^s}=\frac1{\zeta(s+1/6)}
\]

is analytic and vanishes at s=5/6, whereas the prime number theorem gives

\[
\sum_{p\le X}v(p)=-\sum_{p\le X}p^{-1/6}
\sim-\frac65\frac{X^{5/6}}{\log X}.
\]

This is an obstruction to that general inference, not a counterexample
to the proposed cubic Gauss-sum law. The product of a nonprincipal
character with a correlated sequence likewise need not cancel.

## 5. The smallest remaining progression lemma

Even after importing (P0), the expected nonzero mode-one limit in
either class modulo 12 needs

\[
\boxed{\quad
\sum_{\pi\ {\rm primary\ prime}}\chi_{-4}(N\pi)
 \widetilde g(\pi)V(N\pi/X)=o_V(X^{5/6}/\log X).
\quad}
\tag{Q4}
\]

With (P0), Q4 implies JTP for a=1 and a=27, and their sixth-power
multiples. Conversely JTP at a=1 in both progressions implies Q4
by subtraction. If the sum instead has coefficient D, the two weighted
means of G_p(1)/p^(1/3) are 2(C+D) and 2(C-D); the pooled mean
does not determine D. None of the inspected prime theorem statements
proves Q4. We have not proved that their proofs cannot be extended to it.

## 6. Search and novelty limits

Additional searches included cubic Gauss sums with quadratic-character
twists, primes in arithmetic progressions, Patterson first-moment errata,
Yoshimoto character-twisted functional equations, and the 2026 first-moment
claim. Primary source sections were compared with the exact characters
and normalizations above. General equidistribution, angular moments and
all-moduli residues were not promoted into JTP statements.

The special-family transfer uses established Fourier and sextic-twist
identities. The Fejer estimate uses standard bounded variation and Hasse.
Their application here is checkable, but priority is not established.
The exact missing finite-character sums and sharp-window estimate are
specified; an unsuccessful search is not proof that they are new or open
in all of the literature.
