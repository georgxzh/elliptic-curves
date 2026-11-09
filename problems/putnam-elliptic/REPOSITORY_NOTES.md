# Repository inspection and scope

Inspected 2026-11-08. This project is problem design, not a claim of new
elliptic-curve theorems.

The new branch `problems/putnam-elliptic` starts at
`2e8e859` (the existing `work` checkout's HEAD). Its separate worktree is
`/workspace/problems/putnam-elliptic`. The original checkout was clean.
No existing branch was checked out, reset, merged, or rewritten. No root or
nested `AGENTS.md` was found in the inspected checkout.

## Ideas taken from the repository

- The root [README](../../README.md) explicitly distinguishes proof drafts,
  bounded searches, AI audits, and unresolved questions. In particular it
  disclaims breakthrough and novelty claims.
- [CHORD_GLOBAL.md](../../research/2026-10-28-refinements/CHORD_GLOBAL.md),
  section 1, gives a useful elementary identity: the discriminant of the
  residual intersection quadratic for a line of slope `z` through `(x,y)`
  on `Y²=X³+B` is `z⁴−6xz²+8yz−3x²`.
- [The chord audit](../../research/2026-10-29-arithmetic/AUDIT.md), section 3,
  checks the signs and exceptional cases in that calculation. For this
  project the identity is rederived directly; that audit is not an assumed
  theorem.
- [The binary research index](../../research/2026-10-30-binary/README.md)
  supplies a useful warning about exceptional primes and the difference
  between necessary local conditions and global sufficiency.

## What is and is not established here

Elementary algebraic identities, calculus, integer divisibility, and finite
double counts can be proved independently and used. Finite computations
establish only the cases actually checked. The research directory's rank
bounds, class-group restrictions, local lattice classifications, and claims
about full rational images remain outside the prerequisites of every problem.
Their existing AI audit labels are not inherited as validation of this work.

Every finalist must have a complete elementary proof in this directory.
Optional elliptic-curve explanations are motivation only.
