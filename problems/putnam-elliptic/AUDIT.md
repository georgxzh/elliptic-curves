# Astra attempts, audits, and validation

Date: 2026-11-08. All agents named below actually ran using the explicitly
selected model `gpt-6-astra`, with high reasoning effort. This is an AI
review record, not human or formal verification.

Final reproduction and repository-preservation checks completed 2026-11-09.

## Separation of roles

`astra_explore` developed and tested the candidate pool after receiving a
summary of the repository inspection. `astra_hard_explore` independently
explored an additional construction and advised rejecting it. Neither was
used as the sole independent reviewer of a finalist.

Each finalist received a fresh reviewer with **no inherited conversation**
(`fork_turns="none"`). Its first prompt contained the statement, the
provisional difficulty target, and a request to solve and test it. It
explicitly prohibited reading the repository, other agents, or external
sources before completing that attempt. Each reviewer returned a solution
and confirmed it had used no files or sources. Only afterward was the
corresponding written solution file provided in a separate follow-up for
audit. Difficulty targets were visible, so the difficulty judgments were
not blind to the intended placement.

## Problem 1

Reviewer: `/root/astra_quartic_blind`.

**Statement-only attempt.** Independently divided the quartic by its
variable, found the perfect-square derivative, and proved strict
monotonicity on both half-lines. Treated \(a=0\) separately and classified
all multiple roots as \((t-r)^3(t+3r)\). No gap or ambiguity found.
Assessment: A1 quite plausible; A2 also reasonable.

**Separate solution audit.** Read `01-quartic.md` after the attempt.
Confirmed the limits, strictness, zero-parameter case, multiple roots,
chord discriminant, singular cubic distinction, and hints. Found one minor
expository mismatch: an integral was used to justify strictness while the
prerequisite list did not mention integration. We adopted the reviewer's
suggested monotonicity argument instead. No mathematical correction was
needed. The final wording change is that recommended argument.

## Problem 2

Reviewer: `/root/astra_counts_blind`.

**Statement-only attempt.** Independently found the second-moment count
and its equivalence with a cubic permutation. Then supplied a shorter
classification by sums of powers, replacing our provisional conic-counting
ending. Proved the elementary power-sum facts, handled zero, and identified
the exceptional answers at primes 2 and 3. Assessment: approximately A4;
A3 plausible; A5 would overstate it.

**Separate solution audit.** Read `02-counts.md`, including the adopted
power-sum ending. Confirmed all counting equations as integer equalities,
the later congruences, exponent bounds at \(p=5\), coefficient signs,
the inverse of cubing, singular cases, and hints. No gaps found. The
reviewer also directly enumerated every coefficient for primes through
43 and checked the variance identity. The ending benefits from the
reviewer's first-attempt contribution; the second pass is not represented
as a third independent proof discovery.

## Problem 3

Reviewer: `/root/astra_polynomial_blind`.

**Statement-only attempt.** Independently used eventual vanishing of high
integer finite differences to obtain a polynomial square-root identity.
Gave an explicit derivative numerator degree bound, interpolation recurrence,
and the coprime-divisibility contradiction \(H\mid P'\). Checked arbitrary
real coefficients, eventual positivity, zero values, and admissible
constants. Assessment: A4/A5, with A5 plausible; hesitant to call it A6.

**Separate solution audit.** Read `03-polynomial.md`. Explicitly checked
the derivative recurrence starting at \(j=0\), its degree bound, uniform
convergence on \([n,n+k]\), integrality and eventual vanishing, the
coefficient 1 that permits recurrence propagation, and the degree
contradiction. Confirmed the finite-prefix counterexample and the carefully
limited polynomial-parametrization background. No proof gaps found.

The author's exploratory A5/A6 target was revised to **A5 at the easier
end of that band**, with the A4/A5 disagreement printed in the final file.
No timed human solve was conducted, so no solve-time claims are made.

## Exact computational checks

Run from the repository root:

```sh
python problems/putnam-elliptic/verify.py
```

Python 3 and SymPy are required; the recorded run used Python 3.12.14 and
SymPy 1.14.0. This environment already supplied SymPy;
no package installation was needed. The default run compares freshly
computed data with [validation.json](validation.json). `--write` is an
explicit option for regenerating that record.

- **Quartic:** 3 symbolic identities and 467 exact parameter pairs,
  including the integer grid \([-10,10]^2\), rational triple-root cases,
  and the excluded origin. Distinct real roots were counted using the
  squarefree part and an exact symbolic root-counting routine, not
  floating-point root approximations.
- **Counts:** direct enumeration of every \((x,y)\), for all 1,161
  coefficient classes across primes at most 101. All classifications and
  odd-prime variance identities passed; primes 2 and 3 were checked too.
- **Polynomial:** eight arbitrary-length finite-prefix traps and three
  finite-difference examples checked symbolically. These illustrate why
  bounded computation cannot validate the infinite square-value condition.
  Its validation is the written proof and independent audit.
- **Reserves:** consecutive-residue counts for primes at most 199 with
  \(p\equiv3\pmod4\); exact triangle perimeter and Heron area;
  two-tangent integrality for squarefree \(-100\le B\le100\) and
  \(-50\le x\le100\). Only the four stated integral starting points
  survived that bounded tangent check.

The script does not formally verify calculus, establish any unbounded
Diophantine enumeration, or assess originality. No research-directory
claims or scripts were needed as proof inputs.

## Prior-art review is a separate check

The lead agent searched sources and compared Putnam statements; the blind
reviewers were not asked to certify originality. The last reviewer
explicitly limited its audit to mathematics, not linked source accuracy.
The actual sources, exact overlaps, unsuccessful searches, and corpus
coverage limits are in [PRIOR_ART.md](PRIOR_ART.md).
