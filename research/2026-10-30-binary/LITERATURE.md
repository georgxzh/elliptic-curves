# Literature comparison and hypothesis boundaries

Inspected 2026-10-30–31. This is a documented targeted comparison, not
an exhaustive priority search. The binary ideal-class map is an explicit
specialization of classical descent machinery. We claim no new descent
principle and no established novelty for the component formulation.

## 1. Classical cubic-algebra descent and the exact obstruction

For a maximal cubic étale order O, write I for its group of fractional
ideals. The elementary exact sequence

    K×/(K×)² → I/2I → Cl(O)/2Cl(O) → 0

sends an element to the parity of its principal ideal. Quotienting I by
ideals over 2 and 3 gives precisely the exceptional-prime class quotient
used here. Composing the explicit component parity patterns with this
sequence gives our map. This is classical ideal arithmetic, not a new
cohomological construction. In particular Cl/2Cl is the natural
cokernel; it is not canonically the subgroup Cl[2], even though their
F₂ dimensions agree for finite class groups.

[Schaefer, *2-Descent on the Jacobians of Hyperelliptic Curves*, JNT
51 (1995)](https://www.sciencedirect.com/science/article/pii/S0022314X8571044X), describes descent for
odd-degree equations using K[T]/f(T) and squareclasses (publisher abstract
inspected). The cubic, characteristic-zero case includes our field
construction. Our parity proof is provided directly, so no unspecified
local hypothesis from that paper is imported.

[Cremona, *Algorithms for Modular Elliptic Curves*, §3.6, Method 2,
pp. 88–91](https://johncremona.github.io/book/fulltext/chapter3.pdf),
describes general two-descent using quartic coverings, with or without
rational 2-torsion. It supplies context for the already classical quartic
orbit construction. This section is not cited as a theorem identifying
our component-class map.

[Schaefer--Stoll, *How to do a p-descent on an elliptic curve*,
§§1,2,5](https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
describes the number-field approach and the S-unit/S-class-group exact
sequence in §5. However, §2 explicitly assumes p is odd. Its main
algorithm cannot simply be quoted with p=2. The ideal-class exact
sequence above is elementary and valid for squares; the paper is used
for comparison, not to bypass that hypothesis. This distinction matters
when comparing our binary and ternary restrictions.

[Schaefer, *Class groups and Selmer groups*, JNT 56 (1996), 79–114](https://arxiv.org/abs/1507.08324),
compares Selmer and class-related groups through local conditions and
global intersections. The abstract and publication metadata were checked;
its individual theorems were not audited here. It is directly relevant
prior work. The 2015 arXiv upload must not be mistaken for the original
publication date.

[Chao Li, *2-Selmer groups, 2-class groups and rational points on elliptic
curves*, §§2.4–2.11](https://www.math.columbia.edu/~chaoli/EC4d.pdf), gives
the norm-square cohomological description (Lemma 2.7), the x-beta Kummer
map (Propositions 2.8–2.9), and explicitly handles local 2-torsion where
the expression vanishes (Remark 2.10). Its main class-rank comparison
assumes an irreducible monic cubic with **negative squarefree polynomial
discriminant**. T³+B has discriminant -27B², so that main theorem and
its all-prime even-valuation Lemma 2.12 cannot be applied here. Our
valuation-three parity vectors are exactly an obstruction to doing so.
The elementary Kummer description remains the standard background;
our containment proof uses the norm and ideals directly.

A full 2-Selmer computation imposes further unit and local squareclass
conditions. Our kernel is only a necessary projection-level constraint,
and generally need not equal the rational component image. The exact
images in this run are certified by a matching point subgroup or by a
zero kernel, not by assuming equality with a Selmer upper bound.

For the certificates, [Milne, *Class Field Theory*, Theorem 0.4 and
Chapter V, §3, Example 3.9](https://www.jmilne.org/math/CourseNotes/CFT.pdf)
identifies the ordinary class group with the Galois group of the maximal
abelian extension unramified at all finite places and split at all real
places. The real-place condition distinguishes it from a narrow-class
statement. The prime-splitting description and the S-class formulation
in Exercise 3.15 justify killing precisely the classes on which the
chosen character is zero. The exact examples check unramifiedness,
real positivity, and splitting above 2 and 3 explicitly; the counterexample
instead checks nonsplitting above 2. No class-field existence assumption
beyond this standard theorem is hidden in the numerical checker.

## 2. Class-group bounds do not establish a new principle here

[Bhargava--Shankar--Taniguchi--Thorne--Tsimerman--Zhao,
*Bounds on 2-torsion in class groups of number fields and integral points
on elliptic curves*, §5.1, Theorem 5.2](https://www.math.kobe-u.ac.jp/HOME/tani/bstttz.pdf)
quotes Brumer--Kramer (1977), Proposition 7.1 and the following remark:

    rank E ≤ dim Sel₂(E) ≤ dim Cl(K)[2] + 2 omega(|Disc(E)|) + 2,

with K the cubic étale algebra. This directly documents that Selmer,
cubic ideal classes, and coefficient primes are established machinery.
The displayed inequality bounds total Selmer dimension. It does not
itself identify the individual linear-prime columns at valuation-three
places or the quotient statistic A(H₂). We inspected this quoted
statement, not the original Brumer--Kramer proof.

The same paper's Theorem 5.1 gives a discriminant-dependent point bound
O_epsilon(|Disc(E)|^epsilon exp((beta+epsilon)r)), with beta≈0.2782
(base exp(beta)≈1.321). The discriminant factor cannot be absorbed into
an absolute constant as B varies. Its Theorem 1.2(c) instead gives a
power of the discriminant. Neither statement directly subsumes an
absolute C·2^r criterion on a varying family, but both are relevant
numerical alternatives for particular curves.

## 3. Rank bases and constants: no new universal base in this run

The [earlier primary-source comparison](../2026-10-29-arithmetic/LITERATURE.md)
remains applicable. Its strongest broadly compared published bound,
Chi--Lai--Tan (2005), retains base 24 in the proof, versus the rounded
displayed base 7^1.64≈24.319844. A safe absolute prefactor for sixth-free
Mordell coefficients is 11·7^72.31, decimal logarithm about 62.15.
The draft's universal base 12 has prefactor C with logarithm about
169.99; its smaller base does not give numerical superiority at every
rank. Gross--Silverman's older general specialization has base
32·10^9 after absorbing finitely many bounded-height exceptions.

Choi's [preprint, Theorem 1.1](https://arxiv.org/html/2509.03274v3) gives
base 4 in a fixed quadratic-twist family above a threshold depending on
the base curve. Its absolute prefactor in that range becomes potentially
base-curve-dependent when all small twists are included. This already
subsumes weaker qualitative rank-only assertions in a fixed family
B=bD³. It does not directly yield our absolute base-two criterion across
varying fields. We rely on the earlier documented inspection of this
statement, not a newly audited proof.

This continuation lowers A(H₂)S(H₃) on certified examples and gives
conditional class-kernel savings. It does **not** lower the universal
base 12 to a new universal base. Both exhibited strict numerical
improvements are constant-factor improvements. For fixed cubic K the
class-map dimension deficit is bounded by its fixed class 2-rank;
[the quantitative note](QUANTITATIVE.md) states the precise limitation.

## 4. Potential contribution and unresolved priority

Established machinery subsumes the norm descent, parity-to-class
obstruction, and use of unramified quadratic characters to detect ideal
classes. The concrete contribution of these notes is the explicit
maximal-order component table, its application to the actual integral
quartic row-lattice count, the certified full images without rank/basis
computations, and a small-prime counterexample preventing an overstrong
formulation. The restricted root-1 image eliminates a locally admissible
lattice in an actual integral point's rational 2-class.

Whether this precise component/lattice synthesis has appeared before is
unresolved. An unsuccessful search is not evidence of novelty. The
papers on minimisation and integral quartic orbits identified in previous
notes remain part of the broader priority comparison; no comprehensive
review of that literature is asserted.
