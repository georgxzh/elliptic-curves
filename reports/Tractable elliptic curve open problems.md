# Tractable elliptic curve open problems

Synthesis dated **1 November 2026**. This report combines the four
[research notes](<../research_notes/Tractable elliptic curve open problems/>):
[ranks and records](<../research_notes/Tractable elliptic curve open problems/rank_torsion_records.md>),
[arithmetic statistics](<../research_notes/Tractable elliptic curve open problems/murmurations_arithmetic_statistics.md>),
[BSD and Galois images](<../research_notes/Tractable elliptic curve open problems/bsd_galois_deep_problems.md>),
and [computational/cryptographic problems](<../research_notes/Tractable elliptic curve open problems/ecdlp_isogeny_computational.md>).
Those are unrefereed AI notes. Their detailed bibliographies remain
useful leads, but their labels, estimates, and claimed priorities
are not automatically adopted as established results.

The most defensible workstation projects produce finite certificates,
test a precisely stated asymptotic in a new regime, or isolate a
missing theoretical lemma. A larger table, record, or attractive plot
is not by itself a breakthrough. Costs and success probabilities in
the source notes are mostly unbenchmarked judgments. We do not
endorse their numerical probabilities.

## 1. Rechecked rank records: lower bounds are not exact ranks

The claim that 29 is still the record is out of date according to the
live primary record pages checked for this report.

| Claim | Source rechecked | Safe description |
|---|---|---|
| Rank at least 30, Alpöge–Howell, 2026 | [Dujella, rank 30](https://web.math.pmf.unizg.hr/~duje/tors/rk30.html) | Explicit curve and 30 points labelled independent |
| Rank at least 31, Alpöge–Howell, 2026 | [Dujella, rank 31](https://web.math.pmf.unizg.hr/~duje/tors/rk31.html) | Explicit curve and 31 points labelled independent |
| Rank at least 32, Elkies–Klagsbrun–Li, October 2026 | [Dujella, rank 32](https://web.math.pmf.unizg.hr/~duje/tors/rk32.html), [ICARM #4239](https://elliptic-rank.icarm.cloud/curve/4239) | Public lower-bound record with 32 point witnesses |
| Exact unconditional rank 22, Li | [Dujella history](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html), [dedicated rank-22 page](https://web.math.pmf.unizg.hr/~duje/tors/rkeq22.html) | Record table reports exactness; its upper-bound certificate was not independently rerun |

This is source re-verification, not an independent proof of point
independence or a rerun of descent. For #4239, the commentary records
an explicit-formula upper bound below 34 and root number +1. It labels
exact rank 32 as subject to GRH and BSD. Independent rational points
alone give an algebraic lower bound; they must not be used to infer
the same analytic lower bound without an additional theorem or
hypothesis. The wording “analytic rank exactly 32 under GRH” in the
commentary needs that distinction.

The dedicated rank-22 page identifies the curve that the original
notes left uncertain: its coefficients agree with their #4118.
It still does not display the descent proof of the upper bound.
The older MathWorld snapshot at 31 and frozen leaderboard snapshots
before the rank-32 submission are historical, not contradictory
current records. Credits to AI systems and claims about how the
search was performed are announcements; no unpublished method is
reconstructed from press coverage.

For torsion-restricted searches, the notes identify rank-5 targets
with torsion Z/9, Z/10, Z/12 and rank 4 with Z/2 x Z/8. These are
reasonable *record-search candidates*, pending a fresh check of the
[live torsion table](https://web.math.pmf.unizg.hr/~duje/tors/tors.html).
The height of a successful parameter does not reveal how far others
have searched. Counts of high-rank leaderboard submissions are a
selected sample, not a probability model for a new sweep.

Likewise, “smallest known conductor at rank r” is an upper bound on
the minimum. The notes' ranks 5 and above must not be described as
proved minimal. The new Mordell rank-18 and number-field torsion
claims in the notes were not independently certified in this run;
retain them as record/preprint leads with their original links.

## 2. Arithmetic statistics and trace bias

The Bhargava–Shankar Selmer-average results are firm starting points;
the minimalist rank prediction over all elliptic curves remains
conjectural. PPVW is a probabilistic model, not a theorem bounding
all elliptic-curve ranks. Its “all but finitely many” prediction is
not disproved by any finite list of rank records.

The notes describe Smith's general quadratic-twist Selmer-corank
result and subsequent p-converse work. The distinction is essential:
a distribution of Selmer coranks is not automatically the full
analytic Goldfeld conjecture. Any use must preserve the precise
curve, prime, parity, and converse hypotheses. Recent preprints and
later claims of stronger results require their own audit.

For murmurations, the primary sources rechecked here are
[Sawin–Sutherland](https://arxiv.org/abs/2504.12295) and
[Cowan](https://arxiv.org/abs/2408.12723).
Sawin–Sutherland conjecture a height-ordered prime-average density
and prove a smoothed variant over integers with no small prime factors.
Cowan's elliptic-curve results invoke ratios conjectures.
Neither is a general GRH-only prime-average theorem for elliptic curves.
Results for all weight-two modular forms cannot simply be restricted
to the sparse subset associated to elliptic curves.

The source notes also report corrections to Zubrilina and later
prime-power formulas. Their precise ranges, the claimed RH distinction,
and a suspicious date/identifier pairing were not reconciled here.
Use the papers' latest statements before importing a bound; do not
combine an original range with a later repaired conclusion.

Useful experiments include testing explicit density formulas on
the correct scale, studying convergence in disjoint size windows,
and controlling twist duplicates in machine-learning datasets.
Rank prediction from coefficients, or Sha prediction from quantities
already appearing in the BSD formula, may recover known formulas or
dataset structure rather than new arithmetic. Train/test separation
by twist class and conductor range is a minimum evidential check.
The source notes' absolute assertion that only one ML discovery has
ever produced mathematics is not established by their search.

**This repository's concrete continuation.**
The [Patterson project](../research/2026-11-01-patterson/README.md)
has an exact Fourier reduction for Mordell parameter traces.
Its proposed fixed-frequency means specialize classical theta
coefficients, but the full joint prime hypotheses remain unproved.
A proved coefficient-series calculation corrects the alleged
double pole: it occurs after the square/three-times-square selection,
not in the unrestricted series of mu. The resulting logarithmic
cusp is a theorem about the candidate functions, not yet about
the sharp-interval prime average.
The experiment uses B of size p, generally conductor of size p^2,
so it should not be relabelled as the usual p~conductor murmuration.

## 3. Finite BSD and Galois-image certificates

The most attractive finite theorem projects in the deep-problems
notes are:

* Extend a **certified** rank-zero/one BSD verification range, with
  every exceptional prime and isogeny accounted for. The published
  conductor-5000 benchmark is [Creutz–Miller](https://arxiv.org/abs/1105.4018);
  the absence of a later range in the notes is not a priority claim.
* Certify new individual pairs with \(\Sha(E)[p^\infty]=0\), or
  investigate exceptional p-adic regulators and Iwasawa invariants.
  An isolated p-primary vanishing result does not prove finiteness
  of the whole Sha group.
* Reduce a specified finite list of modular-curve cases by local
  obstructions, quotients, or a Mordell–Weil sieve, with exact models
  and completeness certificates.

The bottleneck is often theorem applicability and descent, not raw
point counting. A floating-point value close to a square is not
an exact Sha order. A computed analytic rank bound under GRH is
not an unconditional Mordell–Weil rank. A class group computed
conditionally must be certified before calling its descent bound
unconditional. Known points certify a subgroup unless an upper
bound or saturation argument establishes completeness.

The notes distinguish full BSD from rank equality and individual
p-parts, but their broad phrase “rank 0/1 theory nearly complete”
is too compressed for use as a theorem. The ordinary/supersingular,
residual-image, ramification, small-prime, and reduction hypotheses
must be checked curve by curve.

Serre uniformity is an infinite-prime problem, not a finite search.
The proposed residual 7-adic quartic is a concrete theoretical target;
the notes' X_ns^+(19), X_ns^+(23) announcements and higher prime-power
classifications remain claims to verify against current papers.
Searching to a height bound does not prove that a curve has only
its listed rational points.

The cited H10 results over rings of integers/finitely generated
rings are distinct from H10 over Q. Effective Mordell conditional
on major conjectures does not provide a practical height bound.
The abc/IUT dispute and formalization announcements are not inputs
to any theorem in this report. Record Hall or Szpiro examples
neither settle those conjectures nor refute asymptotic versions
allowing constants or finitely many exceptions.

## 4. Computational and cryptographic questions

The cryptographic notes contain several fast-moving 2026 claims.
Their figures are retained as leads, not independently benchmarked
security estimates.

* Distinguish a full-group discrete logarithm from a bounded-key
  interval problem. A larger interval bit count on a 256-bit curve
  is not a full 256-bit ECDLP solution. An ongoing GPU campaign
  is not a completed record.
* Quantum logical qubits, Toffoli counts, physical qubits, runtime,
  and success probability are different resources. The lowest
  number in each column cannot be combined into one imaginary
  machine. Withheld circuits and architecture assumptions limit
  reproducibility.
* SIDH attacks exploit auxiliary information; they do not alone
  break all isogeny protocols. The notes report a heuristic
  \(p^{1/3+o(1)}\) isogeny algorithm and a very recent claim of
  removing its heuristic. Neither claim was re-proved here.
  Concrete time, memory, hidden factors and applicable problem
  must be compared before declaring parameter sets insecure.
* The withdrawn supersingular-graph sampling/QUE claim mentioned
  in the notes must not be used as a positive theorem.

Plausible small projects are controlled benchmarks of public
isogeny algorithms at toy sizes, order-reciprocity searches with
exact certificates, and improved arithmetic pipelines for
Lang–Trotter, Koblitz, aliquot-cycle or elliptic-Carmichael statistics.
Each needs a targeted prior-art check and a specified open claim.
The notes do not establish that extending an old table is novel.
Finding a prime pair satisfying an order condition is not yet a
construction of a pairing-friendly curve cycle.

## 5. Choosing a project with a checkable outcome

| Priority | Finite deliverable | Principal risk / first check |
|---|---|---|
| 1 | Exact local or descent certificate excluding a rational component pattern | Verify maximal orders, exceptional primes, denominators and completeness; compare classical descent |
| 2 | A sharply stated trace-bias identity, coefficient theorem or counterexample | Separate all-moduli, prime, twist and tail hypotheses; audit constants |
| 3 | A finite BSD or p-primary certificate table with explicit exceptions | Read all imported hypotheses; benchmark one hard pair before scaling |
| 4 | A torsion-family rank record with independent points and an upper-bound status | Geometry and point finding can dominate the sieve; check live records |
| 5 | Reproducible order-reciprocity or isogeny benchmark | Distinguish toy evidence from asymptotic complexity/security claims |

This ordering reflects checkability, not a prediction of breakthrough
probability. The repository's [binary/ternary quantitative note](../research/2026-10-30-binary/QUANTITATIVE.md)
sets a useful standard: explicit constants, exact image certificates,
and a clear distinction between constant-factor and potentially
rank-dependent savings. Do not assume binary and ternary image
dimensions add to at most the rank.

Before scaling any project, reproduce one published calculation,
state the intended lemma, seek a counterexample, and define the
certificate that would count as completion. Preserve failed
conjectures and limits of the method. There is no justification
for converting the source notes' runtime extrapolations or
success percentages into promised outcomes.

## 6. What this report has and has not verified

The four notes were read and synthesized; rank claims above 29
were rechecked against explicit current record pages. The main
Patterson and quartic-Gauss statements and the two elliptic
murmuration abstracts were compared directly with this project's
objects and normalizations. The detailed 2026 cryptographic,
Galois-image, BSD, number-field-torsion and rank-construction claims
were not all independently audited. They remain labelled leads.

No universal rank bound, BSD breakthrough, new cryptographic attack,
prime-average Patterson extension, or novelty claim is made.
The strongest concrete outcome of this continuation is the proved
coefficient/profile refinement and the reproducible enlarged trace
experiments, with their missing analytic steps stated explicitly.
