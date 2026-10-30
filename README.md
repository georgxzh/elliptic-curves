# Elliptic-curve research

[Arithmetic restrictions and completed chord audit](research/2026-10-29-arithmetic/README.md):
a class-group kernel restricts the full ternary component image, with exact
one- and two-prime exclusion certificates and a criterion for an absolute
base-two bound. Also records an arithmetic extremal-code counterexample,
an integral-output experiment, and numerical comparisons with published bounds.

[Exact component quotients and method limits](research/2026-10-29-continuation/README.md):
average the actual binary quotients to improve the chord bound, characterize
equality using intersecting codes, and prove that dimension-only estimates
cannot further lower its exponential base. Includes exhaustive finite checks,
an exact arithmetic example, and an explicit record of the unfinished audit.

[Global component continuation](research/2026-10-28-refinements/README.md):
rational chords constrain the tuple of local lattices, giving proof drafts
with absolute 12^rank bounds for sixth-power-free Mordell coefficients,
6^rank bounds for the fixed-d cubic-twist family, and 2^rank bounds within
each reduction pattern. Includes component-code savings, a general additive
extension, reproducible checks, and explicit review and novelty limits.

[Sixth-power-free continuation](research/2026-10-25-inert/astra/README.md):
an Astra-derived proof draft with explicit local factors for every
sixth-power-free Mordell coefficient B. For squarefree B it gives
`#E_B(Z) << 2^rank` with an absolute constant. Includes separate AI audits,
1,285,032 additional residue checks, symbolic verification, and a comparison
with the already known rank-only bounds. Human review and novelty are open.

[Inert-prime refinement](research/2026-10-25-inert/README.md): a complete proof
draft of the bound `#E_d,n(Z) <<_d 2^(rank + omega_split(n))` for cube-free n,
using a local two-lattice classification and a global fibre count. Includes
exact verification and a literature audit; independent review and novelty
remain unresolved.

[October 25, 2026 research runs](research/2026-10-25/README.md): twenty exact
bounded-coordinate searches motivated by Levent Alpöge's integral-point work,
with reproducible data, proofs for the truncated problem, independent
verification, and an explicit account of the unresolved large-point tail.

No breakthrough or novelty is claimed.

[Deep-tail continuation](research/2026-10-25-tail/README.md): extends the direct
search to x = 134,217,728, measures mixed third moments, proves a growing-window
bound, and checks classical tripling constructions that produce points beyond
the enlarged cutoff.
