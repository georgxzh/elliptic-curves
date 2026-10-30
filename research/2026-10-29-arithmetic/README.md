# Arithmetic restrictions after the component-code bound

Research continuation of draft PR #3, 2026-10-29. The deliverable is a
proved class-group restriction with exact arithmetic certificates, together
with a counterexample to an unconditional strict-deficit route. No general
improvement of the exponential base for all Mordell curves is claimed.

## Proved arithmetic refinement

For nonsquare sixth-free B, the full ternary component image is contained
in the kernel of an explicit map to

\[
 \operatorname{Cl}(\mathbb Q(\sqrt B))\big/
 \left(3\operatorname{Cl}(\mathbb Q(\sqrt B))+
             \langle[\mathfrak q]:\mathfrak q\mid6\rangle\right).
\]

The [proof](CLASS_GROUP_RESTRICTION.md) identifies its columns as weighted
classes of split primes. Independent columns force those component choices
to vanish globally. In the squarefree-d, coprime cube-free-n family B=dn^2,
injectivity of this map gives an absolute C*2^rank bound, removing every
split-prime factor. This is a structural criterion, with no assumption
that it holds on families of unbounded rank.

Two exact examples are certified:

- B=-3475: the local order-three component at 5 is absent globally.
- B=-196682707: the local order-three components at both 13 and 17 are
  absent globally. Every integral point has gcd(x,221)=1. The points
  (1691,68108) and (2027,90176) show that the curve is nonempty.

The certificates enumerate reduced quadratic forms for discriminants -139
and -4027 and check their ideal-class products. They require neither
Mordell--Weil generators nor analytic/conditional class-group calculations.

## Counterexamples and unresolved work

On B=197225, two known points span the entire ambient component groups,
certifying H_2=F_2^2 and H_3=F_3. Both code bounds are attained:
A=5/2 and S=2. An explicit primitive integral matrix of determinant -35
also realizes nonstandard lattices at both retained primes simultaneously.
See [the counterexamples and integral-output probe](EXTREMAL_AND_INTEGRAL.md).

A bounded target search on this curve observes only two of four possible
outputs for one source. It does not prove the other outputs absent. A
precise proposed inequality that would give an exponential saving from
actual integral realizability is stated separately as unresolved.

## Audit, prior work, and novelty

[Astra's completed audit](AUDIT.md) found no gap in the rational-chord
bridge or rational 2-class averaging. It checks the imported Alpoge--Ho
hypotheses and records a torsion refinement that improves constants only.
This is independent AI review, not independent human verification.

The [quantitative literature comparison](LITERATURE.md) extracts base 24
from the published Chi--Lai--Tan proof; its prefactor is far smaller than
the present draft's. Choi's base 4 applies to a fixed quadratic-twist
family with its stated threshold, and already covers that particular
rank-only phenomenon. Classical norm descent supplies the class-group
mechanism. The potentially new combination with actual quartic lattice
counts remains subject to a broader literature comparison; no priority
claim is made.

Astra completed the audit file and communicated the class-group mechanism
and first example. Its literature and arithmetic runs did not finish their
files before the usage limit. The root agent completed the proofs and
comparison, found the two-prime certificate, and wrote the independent
checkers. The new class-group proof has not received a separate completed
audit. It is presented in full so that it can be checked independently.

## Verification

From the repository root:

```sh
python research/2026-10-29-arithmetic/verify_arithmetic.py
python research/2026-10-29-arithmetic/probe_integral_outputs.py
```

The first uses the standard library and verifies the complete reduced-form
certificates, local Hensel data, explicit points, full-image witnesses,
and the transformed quartic identity. The second uses SymPy for exact
rational polynomial factorization and checks only its stated finite set.
Both passed and write JSON records alongside their source.

The existing symbolic chord checker, chord/lattice checker, and 113,950-case
quotient checker were also rerun successfully for the audit. PARI/GP 2.17.2
was used to discover the two-prime example, but the saved certificate does
not depend on PARI. No ranks or complete integral-point lists are asserted.
