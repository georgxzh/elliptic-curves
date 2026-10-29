# Literature comparison and proof status

Checked 2026-10-28. These notes record a targeted literature search and the
status of the research derivations; they are not a priority certificate.

## What is already established in the literature

Rank-only bounds for quasi-minimal Mordell curves are classical. The
[previous comparison](../2026-10-25-inert/astra/LITERATURE_EXTENSION.md)
records Silverman and Gross--Silverman, and Bennett--Ghadermarzi's explicit
statement of their consequence for sixth-power-free Mordell coefficients.
Thus removing all prime-count factors at the cost of a larger exponential
base is not a new qualitative phenomenon. We have not established that
the numerical bases in this continuation improve every prior quantitative
bound. No claim of a best known bound is made.

[Alpoge--Ho, Sections 2--3](https://arxiv.org/html/1807.03761v3) supply the
rational quartic orbits, primitive-matrix lemma, and uniform Thue bound used
throughout. Refining local factors by root disks is already part of their
method. The contribution investigated here is a more explicit use of the
point-quartic conditions and the global origin of the local data.

[Silverman, *The Arithmetic of Elliptic Curves*, second edition,
VII.2, Proposition 2.1](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf)
was inspected directly for the nonsingular-reduction subgroup and reduction
homomorphism. The order-two and order-three local quotient calculations in
this continuation are supplied explicitly by torsion translations; they
do not require importing a classification table. The rank bounds on the
finite global images use Mordell--Weil and the standard Weil pairing.

[Chan, *Integral points on cubic twists of Mordell curves*, Sections 4--5](https://arxiv.org/html/2203.11366v2)
already separates points by the prime divisors common to x and the twist
parameter. Lemma 4.1 lowers a binary cubic discriminant using a divisor
coprime to x; Lemma 4.2 controls the resulting marked forms. The paper proves
average and density results for this family. Our fixed-pattern rank bound
must not be presented as the first use of this divisibility partition.

[Sadek, *Counting Models of Genus One Curves*](https://arxiv.org/abs/1002.0467)
and [Cremona--Fisher--Stoll, *Minimisation and reduction of 2-, 3- and
4-coverings*](https://arxiv.org/abs/0908.1741) remain especially close to the
general additive-prime classification. Their relevance is discussed in the
[original audit](../2026-10-25-inert/LITERATURE.md). The component geometry
is established theory; deriving explicit lattices directly does not itself
establish novelty of a counting consequence.

[Choi, arXiv:2509.03274v3](https://arxiv.org/abs/2509.03274v3) states a
4^rank bound for sufficiently large positive squarefree parameters in a
fixed quadratic-twist family. Only its abstract has been inspected for
this comparison. It is adjacent to the valuation-three case, and should
be compared carefully before any priority claim about that special case.

Searches included combinations of primitive integral points, Mordell
curves, rank, component groups, Tamagawa numbers, quartic lattices, weight
enumerators, and the numerical bases 4, 6 and 12. Most results were unrelated
or concerned algorithms and multiples of points. Absence of an exact match
does not show that a theorem is new.

## What the continuation actually checks

The fixed-pattern proof is based on the exact transformation identity
x'=x-z^2+(F'(z)/(4q))^2 and the interchange of smooth and singular reduction
at valuation-two/four primes. A separate Astra agent scrutinized this
argument without finding a flaw. Its symbolic identity and finite local
examples are checked independently by scripts.

The component-code proof sums over global 2-classes with their actual
component labels. Its finite-linear-algebra identity, dimension bound and
subgroup monotonicity are exhaustively checked in small dimensions. A
known subgroup gives a valid upper bound on this weight. In contrast,
the size or dimension of a known subgroup cannot be used as an upper bound
on the full ternary image or on the number of possible reduction patterns.

The general additive theorem has a direct valuation proof and finite tests
for every listed type. Its constants at 2 and 3 retain their discriminant
dependence. No result about potentially multiplicative reduction is claimed.

The chord identities are checked symbolically and in exact rational examples.
Finite checks of the valuation-three component labels include both smooth
and singular source points. Denominator and infinity cases require the
written argument; the residue scripts do not certify them.

All mathematical results here remain research proof drafts with AI review.
There has been no independent human review, formal proof verification,
external announcement, or contact with authors. None of these arguments
bounds the ranks themselves or proves an average theorem on a thin family.

## Next review targets

The most valuable review is of the global rational-chord/local-lattice
link, including its behavior when a matrix fixes a point quartic. Next is
the quantitative comparison with established rank-only bounds and the exact
relationship with marked minimal-model classifications. The elementary
component proofs make these questions concrete enough for expert scrutiny.
