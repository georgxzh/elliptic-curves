# Literature audit and novelty assessment

Accessed 2026-10-25. This is a targeted audit, not an exhaustive search or a
priority certificate. The exact point-count inequality was not located as an
explicit statement in the sources inspected. Its local mechanism is closely
connected to established minimal-model theory, so absence of an exact search
match is weak evidence of novelty.

## Primary sources inspected

1. **Levent Alpoge and Wei Ho, The second moment of the number of integral
   points on elliptic curves is bounded.**
   [arXiv 1807.03761](https://arxiv.org/html/1807.03761).
   The relevant inputs are Theorem 2.2 and Section 3.1 (point quartics and
   rational orbits), Lemma 3.3 (primitive first row and determinant bound),
   and Theorem 3.5 (uniform homogeneous Thue--Mahler bound). Proposition 3.6
   counts square values after discarding some conditions on transformations.
   Our refinement retains the depression condition before counting row
   lattices. Remark 3.7 already improves a local factor by examining root
   disks; thus even the general strategy of refining factors locally is
   present in the original paper.

2. **Mohammad Sadek, Counting Models of Genus One Curves.**
   [arXiv 1002.0467](https://arxiv.org/html/1002.0467), published in
   Mathematical Proceedings of the Cambridge Philosophical Society 150
   (2011), 399--417,
   [DOI 10.1017/S0305004110000666](https://doi.org/10.1017/S0305004110000666).
   Theorem 4.2 classifies marked minimal local models by component
   configurations. Corollary 4.3 and Table 1 count all such models; Theorem
   6.1 supplies a global product formula over a class-number-one field.
   This is the closest prior-work lead. Table 1 gives two degree-two models
   for nonsplit IV and three for nonsplit IV*, so simply quoting its total
   model count would not eliminate inert primes. The restriction supplied
   by a monic quartic is essential.

3. **John Cremona, Tom Fisher and Michael Stoll, Minimisation and reduction
   of 2-, 3- and 4-coverings of elliptic curves.**
   [arXiv 0908.1741](https://arxiv.org/html/0908.1741).
   Section 3, especially Theorem 3.8 and Lemma 3.12, constructs integral
   models for the degree-two divisor O+P and relates their discriminants
   to that of a Weierstrass model. These constructions and minimisation
   theory predate the proposed refinement. They should be credited, rather
   than presenting point quartics or minimal-model counts as new ideas.

4. **Stephanie Chan, Integral points on cubic twists of Mordell curves.**
   [arXiv 2203.11366v2](https://arxiv.org/html/2203.11366).
   This treats the same nonsquare-d family using binary cubics and
   discriminant lowering. Theorems 1.1--1.2 concern density and average
   point counts. Lemma 5.3 contains the relevant exclusion of a cube-free
   parameter with v_p(n)=2 and v_p(x)=1. These results neither certify nor
   contradict our individual-curve rank-and-splitting bound. In particular,
   the present refinement must not be described as the first bounded-average
   result for this family.

5. **Jan-Hendrik Evertse, On equations in S-units and the Thue-Mahler
   equation, Inventiones Mathematicae 75 (1984), 561--584.**
   Bibliographic details were checked on the
   [author's publication list](https://pub.math.leidenuniv.nl/~evertsejh/publications.shtml).
   The precise form used in GLOBAL_PROOF.md is quoted from Alpoge--Ho,
   Theorem 3.5; this audit did not independently inspect the full 1984
   article. The distinction matters when reviewing the explicit constant.

## Why the local count is compatible with Sadek

For p>3 and v_p(B)=2 or 4, the minimal Weierstrass reduction is of type
IV or IV*. Its geometric multiplicity-one component group has order 3;
the rational component group has order 3 in the split case and order 1
in the nonsplit case. The splitting condition is whether the unit part
of B is a square, exactly the character used in LOCAL_PROOF.md.

A monic binary quartic has two distinct smooth rational sections at
infinity (away from 2). The degree-two divisor they define meets rational
multiplicity-one components. In an additive notation G for those rational
components, a fixed divisor class with component c corresponds to unordered
pairs a+b=c. Their number is

\[
 \frac{|G|+\#\{a\in G:2a=c\}}{2}.
\]

For G of order 1 or 3, multiplication by 2 is bijective, so the number
is respectively 1 or 2. General minimal degree-two models also permit
configurations that do not arise from two individually rational sections.
This explains why Sadek's unrestricted table has larger entries.

This is a geometric interpretation of the local result, not an additional
unproved input into GLOBAL_PROOF.md. The direct proof counts actual
transformation lattices and avoids the task of identifying every marking
and equivalence relation needed for a deduction solely from Sadek.

## What can responsibly be claimed

* The local obstruction has a direct proof, and the row-lattice argument
  completes a proof draft of the stronger bound with base 2 per split prime.
* Direct specialization of Alpoge--Ho's displayed Theorem 1.1 gives factors
  9 and 17 at good-to-d primes with v_p(n)=1 and 2. The proposed bound uses
  1 at inert primes and 2 at split primes, with a d-dependent constant.
* The underlying local geometry is substantially present in prior theory.
  The likely contribution, if the exact consequence has not appeared, is
  an explicit corollary/refinement and an elementary proof, not a new
  minimisation theory or a resolution of a major open problem.
* Expert review of the argument and a broader citation search are still
  needed before claiming a new publishable theorem. No authors have been
  contacted and no external announcement has been made.

Targeted web searches included combinations of integral points, cubic twists,
Mordell curves, inert/split primes, binary quartic orbits, component groups,
Tamagawa numbers, Alpoge--Ho, and Sadek. Most exact-phrase searches produced
no directly relevant result. This is recorded as search scope, not proof
that the inequality is absent from the literature.
