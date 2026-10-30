# Averaging the exact binary component quotient

Research proof draft, 2026-10-29. This refines the
[rational-chord count](../2026-10-28-refinements/CHORD_GLOBAL.md), using
the same local classification, rational descent, and uniform Thue bound.
It does not assert novelty or completed independent review.

## Statement

Let B be a nonzero sixth-power-free integer and E:y^2=x^3+B. Retain the
notation H_2, H_3, s, h, r and C=4*7^192*8178*1636 of the chord note.
Write H=H_2 inside V=product V_p, where V_p is the local component group
at a valuation-three prime, a vector space over F_2 of dimension 1 or 2.
For c in H define

\[
 D_c=\prod_p\langle c_p\rangle,\qquad K_c=H\cap D_c,
 \qquad A(H)=\sum_{c\in H}\frac1{|K_c|}.                 \tag{1}
\]

Here span(0)={0}, and an empty product is the zero vector space.
Let S(H_3) be the number of distinct supports of vectors in H_3. Then

\[
 \#E(\mathbb Z)\le C\,2^r\,A(H_2)S(H_3),              \tag{2}
\]

and

\[
 A(H_2)\le\frac{2^s+1}{2},\qquad
 S(H_3)\le\min\left\{2^w,\frac{3^h+1}{2}\right\}.      \tag{3}
\]

The first bound is exact for s=0 as well. Equation (2) can be minimized
against the earlier C*2^r*(product lambda_p)*W(H_2) bound. In particular,
the new factor never exceeds the earlier component factor 2^s*S(H_3).
Using s,h<=r+1 gives the explicit consequence

\[
 \#E(\mathbb Z)\le C\,2^r
             \frac{(2^{r+1}+1)(3^{r+1}+1)}4.             \tag{4}
\]

This improves a prefactor, not the exponential base 12. Constants in
these notes are too large for practical enumeration of points.

## The local equivalence relation

Fix an occurring rational 2-class and an integral base point P in it.
Its binary component vector c is constant throughout the 2-class.
For any actual transformation from P, the chord construction supplies a
single rational point R, with binary component vector a in H.

At a retained prime p, the exact local rules in Sections 3--4 of the
chord note say:

* If c_p=0, the zero component a_p gives the standard lattice, and every
  nonzero a_p labels a different nonstandard lattice.
* If c_p!=0 and dim V_p=1, both a_p=0 and a_p=c_p give the standard
  lattice; there is no other lattice.
* If c_p!=0 and dim V_p=2, a_p in {0,c_p} gives the standard lattice,
  and the two remaining components give the unique nonstandard lattice.

Thus two allowed binary vectors a,a' give the same tuple of local
lattices precisely when a-a' belongs to D_c. On restriction to H, this
is the quotient by K_c. The number of outputs of this abstract local
map on all of H is exactly

\[
                         |H|/|K_c|.                    \tag{5}
\]

The number of outputs of actual integral transformations is at most
(5); no realization of every abstract output is needed. The denominator
and infinite-slope cases are covered by the rules already proved in the
chord note. In particular, this argument permits stabilizing matrices.

At valuation-two/four primes the local lattice depends only on whether
the target point Q has zero or nonzero component. The target's ternary
component vector lies in H_3, so at most S(H_3) outputs occur. Multiplying
this by (5) is an upper bound even if the two sets of outputs are
arithmetically dependent.

## Average over rational 2-classes

Put tau_2=dim E(Q)[2]<=1 and N=|E(Q)/2E(Q)|=2^(r+tau_2).
The map from these classes onto H has fibers of size N/|H|. As before,
each global lattice contributes at most 2*7^192 point quartics and the
primes 2,3 contribute at most M=8178*1636 lattices. Hence

\[
 \begin{aligned}
 \#E(\mathbb Z)
 &\le 2\,7^{192}M\,S(H_3)\frac{N}{|H|}
                  \sum_{c\in H}\frac{|H|}{|K_c|}\\
 &=2\,7^{192}M\,N\,S(H_3) A(H).
 \end{aligned}                                         \tag{6}
\]

We only choose base points for occurring classes. In (6), an empty
class is assigned the nonnegative expression prescribed by its c;
adding these expressions is valid without choosing a base point there.
Using N<=2*2^r proves (2). If rational 2-torsion is absent, C/2 suffices.

For c=0 we have K_c={0}. For every nonzero c, the vector c itself is
in K_c, whence |K_c|>=2. This proves

\[
 A(H)\le 1+(|H|-1)/2=(2^s+1)/2.
\]

The ternary estimate in (3) follows by identifying a and -a, which
have the same support. These observations prove (3) and (4).

## Exact calculations and completeness requirements

For the full product with b one-dimensional and c two-dimensional
blocks, (1) factors, giving

\[
                       A(V)=(3/2)^b(5/2)^c.
\]

This agrees with the previous component-weight bound for a surjective
binary image. For a one-dimensional image, A(H)=3/2 regardless of the
number or sizes of the nonzero blocks. For the zero image, A(H)=1.

For an exact H, K_c is computed by imposing the linear conditions
a_p in span(c_p) on a in H. In particular no point search is needed.
An incompletely generated subgroup must not be substituted for H in
(2). For example, H'={0} has A(H')=1 while a one-dimensional H has
A(H)=3/2. Known points alone do still certify savings through W(H),
as explained in the earlier component-weight note.

The checker in this directory independently counts the fibers of the
block quotient map, verifies (5), the average in (6), the upper bound,
and the full-product formula for all binary subspaces in the tested
ambient dimensions. This finite verification supports the combinatorics;
it does not certify the elliptic-curve or imported Thue arguments.

## Review status

Update: a [completed separate Astra audit](../2026-10-29-arithmetic/AUDIT.md)
now checks the chord bridge, imported hypotheses, and this averaging step.
The paragraph below records the status at the end of the original run.

Astra identified the quotient K_c in a partial audit. Its run ended at
a usage limit before it delivered a completed audit document. The root
agent reconstructed the proof above and wrote the finite checker. The
earlier chord bridge still needs a completed separate audit, and all
arithmetic claims remain research drafts pending independent human review.
