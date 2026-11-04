# Elliptic-curve research

Research notes, proof drafts, exact arithmetic certificates, and reproducible
computations on integral points on elliptic curves. The work follows two
connected directions: bounded-coordinate searches motivated by Levent
Alpöge's integral-point work, and local-to-global lattice methods for
rank-sensitive bounds on Mordell curves `E_B: y² = x³ + B`.

**No breakthrough or novelty is claimed.** Rank-only bounds for Mordell curves
are already known. The proof drafts include AI audits and computational
checks; independent human review and a broader novelty assessment remain
open. The searches are exhaustive only within their stated coordinate bounds,
and the full large-point tail remains unresolved.

## Where to start

- **Latest arithmetic results:** [binary ideal-class restrictions](research/2026-10-30-binary/README.md)
  and [ternary class-group restrictions](research/2026-10-29-arithmetic/README.md).
- **Proof development:** begin with the [inert-prime refinement](research/2026-10-25-inert/README.md),
  then follow the sixth-power-free, global-component, and exact-quotient
  continuations below.
- **Search data and the moment problem:** begin with the [October 25 research runs](research/2026-10-25/README.md),
  then read the [deep-tail continuation](research/2026-10-25-tail/README.md).

## Arithmetic restrictions and global component bounds

Listed newest first. Each research index links to its proofs, certificates,
checks, literature comparison, and limitations.

### Binary ideal-class restrictions and exact images · October 30–31, 2026

[Research index](research/2026-10-30-binary/README.md)

A maximal-order cubic class-group map restricts the full binary component
image. Exact character certificates determine a restricted image at 19 and
exclude a locally admissible integral-quartic lattice. Includes an
exceptional-prime counterexample, Astra's independent AI audit of both the
binary and ternary class restrictions, and a quantitative and literature
comparison. The certified savings are constant factors; no new universal
exponential base is claimed.

### Arithmetic restrictions and completed chord audit · October 29, 2026

[Research index](research/2026-10-29-arithmetic/README.md)

A class-group kernel restricts the full ternary component image, with exact
one- and two-prime exclusion certificates and a criterion for an absolute
base-two bound. Also records an arithmetic extremal-code counterexample,
an integral-output experiment, the completed AI chord audit, and numerical
comparisons with published bounds.

### Exact component quotients and method limits · October 29, 2026

[Research index](research/2026-10-29-continuation/README.md)

Averaging the actual binary quotients improves the chord bound's prefactor.
An equality criterion using intersecting codes shows that dimension-only
estimates cannot further lower its exponential base. Includes exhaustive
finite checks, an exact arithmetic example, and the audit status at that
stage; the arithmetic follow-up above completes the separate chord audit.

### Global component continuation · October 28, 2026

[Research index](research/2026-10-28-refinements/README.md)

Rational chords constrain the tuple of local lattices. The resulting proof
drafts give an absolute bound of order `12^rank` for sixth-power-free Mordell
coefficients, a bound of order `6^rank` for the fixed-d cubic-twist family
(with constant depending on d), and `2^rank` within each reduction pattern.
Includes component-code savings, a general additive extension, reproducible
checks, and explicit review and novelty limits.

## Local lattice foundations

### Sixth-power-free continuation

[Research index](research/2026-10-25-inert/astra/README.md)

An Astra-derived proof draft with explicit local factors for every nonzero
sixth-power-free Mordell coefficient B. For squarefree B it gives
`#E_B(Z) << 2^rank` with an absolute constant. Includes separate AI audits,
1,285,032 additional residue checks, symbolic verification, and a comparison
with already known rank-only bounds. Human review and novelty remain open.

### Inert-prime refinement

[Research index](research/2026-10-25-inert/README.md)

A complete proof draft of `#E_d,n(Z) <<_d 2^(rank + omega_split(n))` for
`E_d,n: y² = x³ + dn²`, with fixed nonzero d and positive cube-free n.
Here `omega_split(n)` counts primes p dividing n, outside 6d, for which d is
a quadratic residue modulo p. The argument uses a local two-lattice
classification and a global fibre count. Includes exact verification and
a literature audit; independent human review and novelty remain unresolved.

## Bounded-coordinate searches and the large-point tail

### Deep-tail continuation

[Research index](research/2026-10-25-tail/README.md)

Extends the direct search to `x = 134,217,728`, measures mixed third moments,
and proves a growing-window bound. Classical tripling constructions certify
points beyond the enlarged cutoff, so the full large-point tail is still open.

### October 25, 2026 research runs

[Research index](research/2026-10-25/README.md)

Twenty exact bounded-coordinate searches motivated by Levent Alpöge's
integral-point work, with reproducible data, proofs for the truncated problem,
independent verification, and an explicit account of the unresolved
large-point tail. These are finite-range counts, not complete integral-point
enumerations or a solution of the full third-moment problem.

## Reproducing the checks

Run commands from the repository root. For the latest binary and ternary
arithmetic certificates, only Python 3 and its standard library are needed:

```sh
python research/2026-10-30-binary/verify_binary.py
python research/2026-10-29-arithmetic/verify_arithmetic.py
```

For other checks and the original searches, follow the commands and dependency
requirements in the relevant research index. Some symbolic checks require
SymPy; the search programs require a C++20 compiler. Each index describes
the scope of its checks and links to recorded results. Finite and symbolic
checks support the written arguments; they do not constitute formal
verification, certify complete point lists, or establish novelty.
