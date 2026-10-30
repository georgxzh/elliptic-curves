# Global component refinements of the integral-point bound

The [October 29 continuation](../2026-10-29-continuation/README.md) sharpens
the binary component factor by averaging exact quotients and proves a
dimension-only obstruction to reducing the exponential base further.

This continuation develops the earlier local prime factors into global
compatibility bounds. The main new proof draft uses rational chords to show
that all the local lattice choices of a transformation come from one rational
point. They therefore lie in a finite global component image.

Let E_B:y^2=x^3+B, with B nonzero and sixth-power-free, and r=rank E_B(Q).
Let H_2 and H_3 be the rational-point images in the relevant local component
groups of exponent two and three. Write s=dim_F2 H_2 and h=dim_F3 H_3.
With the same absolute C as the earlier sixth-free bound, the draft proves

\[
 \#E_B(\mathbb Z)\le C\,2^r
       \min\!\left\{\prod_{p>3}\lambda_p(B),\ 2^s3^h\right\}
       \le 6C\,12^r.
\]

Here s<=r+1 and h<=r+1. The lambda_p are the previously proved explicit
local factors. This can be strengthened using both a component-code weight
and the number of supports in the ternary image; see the proof.

| Family or subset | Consequence of the draft |
|---|---|
| All nonzero sixth-power-free B | Absolute bound of order 12^r |
| No p>3 with v_p(B)=2 or 4 | Absolute bound of order 4^r |
| Squarefree B | Earlier absolute bound of order 2^r |
| B=dn^2, fixed nonzero d, positive cube-free n | Bound of order 6^r, constant depending on d |
| Same family, restricted to gcd(x,n)=1 | Bound of order 2^r, constant depending on d |
| Any single prescribed pattern of p dividing x, for p dividing n outside 6d | Same bound of order 2^r |

The original bound with 2^(r+omega_split(n)) remains available; either
estimate may be stronger. Constants are explicit and deliberately very large.
Rank-only bounds for Mordell curves were already known. Novelty and comparison
with the best prior quantitative bounds remain unresolved.

## Proofs and additional refinements

1. [Reduction-pattern theorem](REDUCTION_PATTERNS.md): nonstandard matrices
   interchange singular and nonsingular points at valuation-two/four primes.
2. [Ternary global image](GLOBAL_PATTERN_IMAGE.md): at most (3^h+1)/2
   support patterns occur, giving the unrestricted 6^r cubic-twist bound.
3. [Rational chord theorem](CHORD_GLOBAL.md): explicit global points control
   the actual local lattices, including denominator and infinity cases.
4. [Component-code saving](GLOBAL_COMPONENT_CODE.md): replace the old product
   by its product times W(H_2), with a precise dimension bound. Any known
   rational subgroup can certify this saving without saturation. For
   B=67,821,390, the point (91,8281) reduces the relevant factor from 16 to 10.
5. [General additive extension](FRONTIER_ADDITIVE.md): exact local formulas
   for all tame potentially good additive types on y^2=x^3+Ax+B, with
   explicit dependence at primes 2 and 3. This extends beyond j=0.

The known-subgroup principle applies to W(H_2). It does **not** permit
substituting an incomplete subgroup's size for 2^s3^h or its dimension
for h in an upper bound on the number of patterns.

## Verification

From the repository root, the standard-library checks are:

```sh
python research/2026-10-28-refinements/verify_reduction_patterns.py
python research/2026-10-28-refinements/global_verify_component_code.py --json
python research/2026-10-28-refinements/verify_ternary_patterns.py
python research/2026-10-28-refinements/verify_chord_lattices.py
```

The SymPy checks are:

```sh
python research/2026-10-28-refinements/symbolic_reduction_patterns.py
python research/2026-10-28-refinements/symbolic_chord.py
python research/2026-10-28-refinements/FRONTIER_verify_additive.py
```

All assertions passed. The finite scope is:

- 642,516 residues for reduction-status switching.
- 12,668 binary subspace/layout pairs for the component weight identities.
- 2,913 ternary subspaces for the support bound, plus rational addition checks.
- 321,258 repeated-disk residues for the chord bridge, 5,160 denominator
  cases, and exact rational stabilizers and infinity cases.
- 110 seed coefficient models and 1,166 local point samples for the general
  additive extension, including every listed type.

Structured results are saved next to the scripts. Finite checks support the
calculations but do not prove the imported descent/Thue theorems or replace
the general local and global arguments.

## Research status

Astra supplied the component-image and additive derivations and scrutinized
the fixed-pattern lemma. The root agent developed the chord bridge, inspected
the saved proofs, and added independent symbolic and finite checks. The chord
bridge now has a [completed separate Astra audit](../2026-10-29-arithmetic/AUDIT.md).
All results
remain research drafts pending independent human review, and no best-known
bound or novelty is claimed. See [literature and status](LITERATURE_AND_STATUS.md).

No rank bound, new thin-family average theorem, general solution of Lang's
conjecture, or simultaneous global attainment of local maxima is asserted.
