# Prior-art and hypothesis audit

Checked 1 November 2026. This is a targeted comparison, not an exhaustive
novelty search. The calculations do not establish priority.

## Sources read and the normalization problem

**Dunn–Radziwiłł**, [Annals 200 (2024), 967–1057](https://annals.math.princeton.edu/2024/200-3/p03),
[arXiv v3](https://arxiv.org/html/2109.07463v3).
Theorem 1.1 assumes GRH for Hecke L-functions over \(\mathbb Q(\omega)\)
and a fixed smooth compactly supported weight on \((0,\infty)\).
The printed rational-prime coefficient is C for \(G_p(1)/(2\sqrt p)\).
The display after (1.8) gives the same coefficient after smoothing
for all primary Eisenstein primes.
Theorem 1.3 treats powers of normalized Gauss sums; Section 13
reduces these to angular twists, not arbitrary numerator twists.
Section 5 supplies periodic twists and an all-moduli Voronoi formula;
(5.7) supplies the theta coefficients. These are not, as stated,
the required joint twisted-prime asymptotics.
Read in detail: introduction, coefficient formulas, twist/residue
statements, and initial prime reduction. The entire analytic proof
was not independently re-proved.

Here is our normalization calculation. Pairing conjugate primary primes
gives \(G_p(1)/\sqrt p\), not \(G_p(1)/(2\sqrt p)\).
Thus a coefficient C for the primary-prime sum corresponds to C/2 for
the displayed rational-prime summand. Using the density \(1/2\) of
split rational primes gives:

| Input convention | Coefficient of \(X^{5/6}/\log X\int Vt^{-1/6}\) | Implied W-weighted mean of \(G_p(1)/p^{1/3}\) |
|---|---:|---:|
| All primary primes, normalized Gauss sum | C | 2C = 1.6763788059 |
| Rational split primes, \(G_p(1)/(2\sqrt p)\), consistently paired | C/2 | 2C |
| Literal printed rational-prime Theorem 1.1 | C | 4C = 3.3527576118 |

For the last column use \(V(t)=t^{1/6}W(t)\), multiply the
rational-prime sum by \(2X^{1/6}\), and divide by
\(\sum_{p=1(3)}W(p/X)\sim X/(2\log X)\int W\).
This is an exact normalization deduction, not a numerical inference.
The formulas as printed cannot all be identified under the same
convention. We retain the discrepancy instead of silently correcting
a published theorem or claiming that finite data refute GRH.

**A later source already records this issue.**
OpenAI, [*An unconditional first moment for cubic Gauss sums*,
25 September 2026](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf),
Theorem 1.1, Section 1.2 and Remark 1.2, explicitly count both primary
primes, give sharp coefficient \((6/5)C\), and explain the rational
coefficient \((3/5)C\). It cites Wan, Conjecture 4.13, for the latter.
Its [formalization scope page](https://github.com/openai/math/blob/main/lean/docs/023.md)
reports an unconditional result. We read its theorem, conversion,
scope, and classical-input discussion, but did not audit the complete
proof or run Lean. We treat it as an unreviewed preprint claim, not
as a newly verified unconditional input.
Its fixed angular-mode extension does not state our full JTP hypothesis.
The factor-two warning is **already documented prior work**.

Wan's [2021 survey](https://doi.org/10.1007/s11424-021-0066-8) was located;
the author's PDF could not be retrieved. Its constant is therefore
attributed through the 2026 preprint, not independently checked.

## Established machinery and the remaining target

Fourier inversion, sextic twist invariance, quadratic Gauss-sum evaluation,
cubic reciprocity, and Patterson's theta coefficients are established.
Our rational-integer specialization is an elementary deduction.
The finite-mode theorem transfers finitely many JTP hypotheses; it
proves neither those hypotheses nor a new prime theorem.

This repository now has a checked specialization with ramified-prime
bookkeeping, an explicit description of the missing twists, and a
correction to the proposed Dirichlet series. The cusp theorem uses
elementary summatory estimates and an Abelian argument. Its novelty
in the literature is not established.
Potentially new analytic content would require the joint fixed-numerator,
quadratic-character and progression prime asymptotic, or a uniform
averaged Fourier-tail theorem giving the sharp interval profile.
Neither is proved here.

## Adjacent literature

* David–Dunn–Hamieh–Lin,
  [*Quartic Gauss sums over primes and metaplectic theta functions*,
  v5, January 2026](https://arxiv.org/html/2306.11875v5),
  Theorem 1.1 bounds a smooth von-Mangoldt sum by
  \(X^{5/6+\varepsilon}+X^{3/4+\varepsilon}|\ell|^{3/2+\varepsilon}\).
  Conjecture 1.2 predicts a \(3/4\) main-term exponent.
  Its Gaussian-prime normalization and finite congruence conditions
  need matching before transfer to a rational quartic family.
* Berg–Ryan–Young,
  [*Vanishing of quartic and sextic twists of L-functions*](https://arxiv.org/abs/2301.05329),
  and its [data/code page](https://eg.bucknell.edu/~ncr006/quartic-sextic-twists-website/):
  Gauss-sum equidistribution and twist-family vanishing are adjacent,
  but not the parameter-window first moments here. Screened at
  abstract/scope level.
* [Chantal David's 2025 seminar abstract](https://math.uni.lu/nt/NT-Sem/index-24-25.html)
  links quartic-twist rank/nonvanishing to a Patterson-type conjecture.
  The broad Gauss-sum/CM-curve connection is prior art.
* Sawin–Sutherland,
  [*Murmurations for elliptic curves ordered by height*](https://arxiv.org/abs/2504.12295):
  the prime-average density is conjectured; a smooth average over
  integers without small prime factors is proved. The root-number
  weighting and conductor scale differ from our unweighted j=0 window.
* Cowan, [*Murmurations and ratios conjectures*](https://arxiv.org/abs/2408.12723):
  elliptic-curve conclusions use ratios conjectures. They cannot be
  recast as GRH-only theorems for our thin family.

## Search log and limits

Queries included:

* Dunn Radziwill Bias cubic Gauss sums Patterson conjecture twisted fixed a theorem
* Mordell curves cubic Gauss sums Patterson bias Fourier Frobenius traces averages
* "Mordell curves" "Gauss sums" average trace
* "Patterson" "elliptic curves" bias
* "cubic Gauss sums" "twisted" primes asymptotic fixed
* "j=0" "average" "trace" Gauss Fourier
* "sextic twists" "Gauss sums" average rank
* "Fourier transform" "cubic Gauss" "elliptic"
* "Mordell curves" "average" "Frobenius"
* "cubic twists" "one-level density" Gauss sums Young
* Dunn Radziwill Patterson constant factor 2 erratum cubic Gauss sums

The search also returned general elliptic-family moment papers, older
Gauss-sum surveys, function-field twist results, and unrelated or
unreviewed claims. None was promoted from a snippet into a theorem.
We did not locate the exact sharp-window j=0 profile with all constants
and uniform tail control. That failure is **not evidence of novelty**.
