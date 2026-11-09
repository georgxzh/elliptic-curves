# Prior-art checks and originality limits

Checked 2026-11-08. These are freshly composed contest formulations of
established mathematics, with complete elementary solutions. They are not
new research theorems. Exact expressions, key methods, and stronger results
have precedents. No unsuccessful search establishes novelty, and none of
these problems is certified unused in competitions or teaching materials.

## Sources inspected and close precedents

### Problem 1: exact polynomial known

The immediate inspiration was the repository's
[chord discriminant](../../research/2026-10-28-refinements/CHORD_GLOBAL.md).
The same polynomial, after renaming variables and changing one parameter's
sign, appears in Denis Leonov's 2017 question
[“Solve quartic equation …”](https://math.stackexchange.com/questions/2174599/solve-quartic-equation-a4-6a2b-8ac-3b2-0).
Its answers include a radical factorization by Quanto (2020).
The related [system-of-equations question](https://math.stackexchange.com/questions/2168850/simplest-way-to-solve-this-system-of-equations)
also contains tangent formulas. Both pages were opened and inspected.

This is an exact-expression precedent, not merely thematic similarity.
The inspected question seeks explicit roots, whereas our problem asks for
their number over the reals and uses a monotonic quotient. We did not locate
that exact root-count exercise in the sources checked. This limited
distinction supports retaining it as a proposed exercise, not claiming
novelty of the polynomial or underlying fact.

### Problem 2: a direct consequence of known variance formulas

Bogdan Nica, [*Variance of point-counts for families of cubic curves over
\(\mathbb F_p\) and Jacobsthal sums*](https://arxiv.org/abs/2504.15505),
arXiv:2504.15505, submitted 2025. Theorem 2.1 and the introduction were
inspected in the [HTML text](https://arxiv.org/html/2504.15505v1#S2).
That theorem gives the variance for the more general family with a fixed
quadratic term. Its zero-variance cases imply our classification. The
paper also identifies earlier work on these moments by Jacobsthal,
Birch, and He–McLaughlin; those older papers were not independently read
in this session.

Thus the mathematical content of this finalist has a clear stronger
precedent. The proposed exercise focuses on a collision-count equivalence
and a power-sum proof, avoiding quadratic characters. It should be described
as an independently developed contest formulation of classical/known
material, not as a new finite-field result. The primary source was found
after the statement and elementary approach had been developed.

### Problem 3: the main lemma is known

The [2018 Math Stack Exchange question about polynomials taking square
values](https://math.stackexchange.com/questions/2976138/is-it-true-that-if-px-is-a-square-number-for-every-integer-then-px-qx)
has an answer by user1751589 presenting the same finite-difference method
for integer-coefficient polynomials. The answer and its comments were
inspected. This is a close methodological precedent. Our proof permits
real coefficients, supplies the derivative estimate explicitly, and uses
an iterated-integral identity to avoid ambiguity in repeated mean-value
arguments. The derivative contradiction for a square differing from a cube
by 1 is elementary classical polynomial arithmetic.

M. Ram Murty's *Polynomials assuming square values*, in *Number Theory and
Discrete Geometry*, Ramanujan Mathematical Society Lecture Notes Series 6
(2008), pp. 155–163, is listed in his
[publication bibliography](https://mrammurty-ai.github.io/index2.html).
The old [PDF address](https://mast.queensu.ca/~murty/poly2.pdf) redirected to
a faculty page when opened here. The bibliography and indexed abstract were
accessible; the full paper was **not** read. We do not attribute the
specific finite-difference proof to that paper on this evidence.

Targeted searches did not locate the exact combined condition
“\(P(n)^3+1\) is an integer square for every positive integer” in a
past problem. This is limited negative evidence, not a novelty finding.

### Rejected triangle seed: exact teaching precedent

Peter Hawkes's [*An Innocent Question?* handout](https://www.birmingham.ac.uk/Documents/college-eps/college/stem/Transitions-in-UG-Maths-Education-Event/Hawkes---handout.pdf)
asks about another rational triangle with area 6 and perimeter 12.
Chapter 15 of M. Ben-Ari's *Mathematical Surprises* (2022),
[“Are Triangles with Equal Areas and Perimeters Congruent?”](https://doi.org/10.1007/978-3-031-13566-8_15),
has an accessible [chapter extract](https://dlib.hust.edu.vn/bitstream/HUST/25910/1/OER000005566.pdf)
showing the exact triangle \((156/35,101/21,41/15)\).
These were returned with substantive text in the source search. The exact
numbers and geometric setup make this a particularly close precedent;
we rejected it, and did not try to disguise it by changing constants.

## Putnam comparison

We consulted the [MAA archive](https://maa.org/maa-putnam-archive/) and
[Kiran Kedlaya's archive](https://kskedlaya.org/putnam-archive/), and searched
the 673 informal statements in
[PutnamBench](https://github.com/trishullab/PutnamBench/blob/a635813f5edf297d928f9bd5ef8324a26bdde09c/informal/putnam.json)
at commit `a635813f5edf297d928f9bd5ef8324a26bdde09c`.
That snapshot spans 1962–2025 but is **not a complete historical corpus**.
Keyword and formula searches are also imperfect at detecting equivalent
problems under different notation. The corpus was cloned to `/tmp` for
inspection; it is not copied into this repository.

Relevant comparisons actually inspected:

| Past problem | Relationship and distinction |
| --- | --- |
| [1991 B5](https://kskedlaya.org/putnam-archive/1991.pdf) | Counts the intersection of square residues with a translate. This is closely related to the rejected consecutive-residue seed and to difference-of-squares counting, but not the selected cubic-family classification. |
| [2012 B6](https://kskedlaya.org/putnam-archive/2012s.pdf) | Studies the parity of the cubing permutation. Cubing modulo primes is a genuine shared ingredient; our question instead concerns constant point counts and rules out nonzero linear terms. |
| [2007 A1](https://kskedlaya.org/putnam-archive/2007s.pdf) | Tangency of two quadratic graphs. The accompanying commentary mentions an elliptic-curve obstruction, but neither the statement nor its solution matches our quartic root-count task. |
| [2000 A6](https://prase.cz/kalva/putnam/putn00.html) | Polynomial iteration on integers; checked after a broad search hit. Its periodicity question differs from the square-value rigidity problem. |
| 1981 A5, in the pinned PutnamBench corpus | Derivatives and a lower bound on distinct real roots; thematic calculus overlap only. |
| 2019 B5, in that corpus | Finite interpolation of Fibonacci values; relates to difference/interpolation methods but not the square-root rigidity argument. |

The 2012 solution source is by Kedlaya and Ng, and the 2007 solution source
by Bhargava, Kedlaya, and Ng; they are not labeled “official MAA solutions”
here. We link rather than reproduce the old problems or their solutions.

## Search record and limits

Representative web queries included:

- `Putnam elliptic curve problems tangent rational points`
- `Putnam finite field cubic quadratic residues number solutions second moment`
- `"a^4-6a^2b-8ac-3b^2"`
- `"quartic" "6a" "8b" "roots"`
- `"three consecutive quadratic residues"`
- `"perimeter 12" "area 6" "rational" triangles`
- `"y^2=x^3+ax+b" "independent" "b" points`
- `"permutation" "x^3+ax" prime`
- `"Variance of point-counts" "Jacobsthal"`
- `"polynomial" "P(n)^3+1"`
- `"polynomial" "f(n)^3" "square"`
- `polynomial square integer every integer finite differences real coefficients`

Local corpus searches covered quartics, cubic equations, tangents,
quadratic residues, squares/cubes, rational points, polynomial values at
integers, and interpolation. Returned candidate statements were read and
compared rather than treating keyword absence as proof.

No comprehensive search of national olympiad archives, journal problem
columns, non-English collections, or all pre-1962 Putnam exams was made.
The proper conclusion is: **three usable, independently proved exercises
with explicit sources and unresolved originality of the exact formulations**.
