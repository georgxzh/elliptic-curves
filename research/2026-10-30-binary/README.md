# Binary ideal-class restrictions and exact component images

Continuation of merged PR #4, begun October 30 and completed October 31,
2026. The result is an explicit structural refinement with exact examples,
independently audited by Astra. No novelty or new universal rank base is
claimed.

For sixth-power-free B, work in the maximal order of the cubic étale
algebra K=Q[T]/(T³+B). There is a linear map

    Psi₂ : V₂ → Cl(K)/(2Cl(K)+<[q]:q|6>),
    H₂ ⊆ ker(Psi₂),

sending each nonzero root-labelled component at a valuation-three prime
to the class of its corresponding linear prime. The proof treats all
other prime valuations, rational denominators, nonmaximal monogenic
orders, and reducible algebras. In the reducible case the class target
is zero; the rational 2-torsion point must be treated separately.

The strongest exact example is

    E: y²=x³-397822,     P=(1463,55955).

The local binary group at 19 has four elements. An explicit unramified
quadratic character in Q(cuberoot(58)) restricts the full rational image
to one line; P spans that line. Thus A(H₂)S(H₃)=3/2, improving the
ambient bound 5/2 by a factor 3/5. Moreover only the standard row lattice
at 19 can occur from integral transformations in P's rational 2-class.
A second curve, B=-7250, has a nontrivial local group and zero rational
image. Neither conclusion uses a rank or complete Mordell--Weil basis.

On B=11000 the point (-10,100) proves that omitting primes above 2 from
the exceptional-prime quotient would give a false statement. Its class
character has an independent exact certificate in Q(cuberoot(11)).

## Proofs and scope

- [Binary theorem and all-prime valuation proof](ASTRA_BINARY.md).
- [Exact examples and the counterexample](EXACT_EXAMPLES.md).
- [Independent Astra audit](ASTRA_AUDIT.md), including the preceding
  ternary class-group theorem, component signs, and absolute constants.
- [Quantitative combination with the ternary restriction](QUANTITATIVE.md).
  The concrete savings are constant factors; a growing rank saving
  requires additional dimension deficits, explicitly stated there.
- [Literature comparison](LITERATURE.md): classical 2-descent already
  provides the norm/class-group machinery. The possible contribution is
  its explicit component and integral-lattice application; priority is open.

The previous ternary proof required no correction under its stated
hypotheses. The binary construction is a necessary constraint, not a
general equality with the rational image. The new exact examples have
matching upper and lower certificates. No assumption that binary and
ternary dimensions add to at most the rank is used.

## Reproduction

From the repository root, with Python 3 and its standard library only:

```sh
python research/2026-10-30-binary/verify_binary.py
python research/2026-10-29-arithmetic/verify_arithmetic.py
```

The first command recomputes and compares [binary_results.json](binary_results.json).
It checks norms, Eisenstein certificates, residue characters, Hensel
lifts, exact point identities, rational doubling, the single-block A
values, and 6,613 bounded singular valuation cases. Use `--write` only
when intentionally updating the recorded result. The second rechecks
the previous ternary and extremal-image certificates.

These finite checks support the written proofs; they are not a formal
verification of class field theory or a proof of rank or point-list
completeness. PARI was used for discovery only. Human review remains open.

Final focused review: Astra separately checked the exact-example note,
quantitative ratios, fixed-field limitation, and verifier against the
committed JSON, finding no substantive issue. The prior 113,950-case
component-quotient verifier was also rerun successfully. These are
independent AI checks, not independent human or formal verification.
