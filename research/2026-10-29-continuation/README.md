# Exact component quotients and the limit of dimension-only counting

The [arithmetic follow-up](../2026-10-29-arithmetic/README.md) completes
the separate Astra audit, proves a class-group restriction, and gives
both certified global exclusions and a mixed extremal-image counterexample.

Continuation, 2026-10-29. The main refinement replaces the factor 2^s in
the earlier rational-chord argument by an average of exact quotient sizes.
For a nonzero sixth-power-free Mordell coefficient B, the resulting draft is

\[
 \#E_B(\mathbb Z)\le C\,2^r A(H_2)S(H_3),\qquad
 A(H_2)\le(2^s+1)/2,\quad S(H_3)\le(3^h+1)/2.
\]

Here H_2,H_3 are the full global images in the retained local component
groups, s,h their dimensions, S counts distinct supports, and C is the
same explicit absolute constant as before. The [quotient proof](BINARY_QUOTIENT.md)
defines A and explains the averaging over rational 2-classes. It improves
the prefactor in the rank-only bound; the exponential base remains 12.

The [code obstruction](CODE_OBSTRUCTION.md) proves an exact equality
criterion and supplies simplex codes attaining both dimension bounds.
Consequently an improvement of the exponential base cannot come from
bounding these expressions for arbitrary component codes by dimension
alone. This is a limit of that method, not a lower bound on integral points
or a realization theorem for elliptic curves. The equality criterion is
connected explicitly to established minimal/intersecting-code theory.

A concrete arithmetic example is B=-166375. The points (55,0),
(130,1425), and (176,-2299) prove that the binary image at 5 and 11
is all of F_2^2. They certify A=9/4, strictly below the dimension-only
value 5/2, without a rank or saturation computation. This example also
agrees with the previous full-product component-weight formula.

## Reproduce the checks

From the repository root, using only the Python standard library:

```sh
python research/2026-10-29-continuation/verify_component_quotients.py
python research/2026-10-29-continuation/verify_code_obstruction.py
```

Both scripts write structured JSON results alongside their source. The
first checks 12,668 subspace/layout pairs and 113,950 source-component
cases. The second checks the equality and deficit criteria on the same
12,668 pairs, accounts for 112,102 ordered disjoint-decomposition witnesses,
tests binary simplex codes through dimension 8 and ternary simplex codes
through dimension 6, and verifies the displayed rational arithmetic.
All assertions passed. The finite checks do not prove the p-adic,
descent, or Thue inputs of the arithmetic bound.

## Review and next research target

Astra suggested the quotient formula and simplex obstruction in partial
audit messages; its runs hit a usage limit before delivering completed
audit files. The root agent reconstructed the arguments, added the exact
equality criterion, located its coding-theory connection, and independently
wrote and ran the checks. The chord bridge still needs a completed separate
audit. Independent human review and novelty assessment remain open.

The concrete next target is an arithmetic restriction on the component
images, or on which abstract lattice outputs can come from integral
transformations. Disjoint-support vectors give a certified deficit, and
a proved decomposition of the full image gives a multiplicative saving.
Neither conclusion can be inferred just from an incomplete generating set.
Rank-only bounds for Mordell curves are already classical; this continuation
makes no claim to a new qualitative phenomenon or best known estimate.
