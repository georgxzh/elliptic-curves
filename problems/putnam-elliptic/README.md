# Putnam-style problems inspired by elliptic curves

Three self-contained undergraduate problems, developed on 2026-11-08 and
finalized on 2026-11-09.
This is a problem-design project, not new elliptic-curve research.

Start with the [statement-only sheet](STATEMENTS.md). Each solution file
contains graduated hints, a complete elementary proof, edge-case checks,
and a separately labeled optional elliptic-curve explanation.

| Problem | Main insight | Placement | Hints and complete proof |
| --- | --- | --- | --- |
| Two zeros | A monotone quotient reveals a perfect-square derivative | A1/A2 | [Problem 1](01-quartic.md) |
| Counts that do not change | A double count turns constant counts into a permutation | A3/A4, probably A4 | [Problem 2](02-counts.md) |
| Squares at every integer | Integer finite differences tending to zero vanish exactly | A5; independent reviewer said A4/A5 | [Problem 3](03-polynomial.md) |

The third problem is at the easier end of the requested A5/A6 band. We do
not claim it deserves A6. The three problems emphasize different methods:
real calculus, finite-field combinatorics, and discrete polynomial rigidity.

## Development and evidence

- [Six seeds, stress tests, and rejected candidates](SEEDS.md).
- [Repository inspection and separation from research claims](REPOSITORY_NOTES.md).
- [Astra statement-only attempts and subsequent solution audits](AUDIT.md).
- [Prior-art checks, citations, and originality limits](PRIOR_ART.md).
- [Exact check script](verify.py) and [recorded results](validation.json).

Fresh `gpt-6-astra` reviewers independently solved each finalist from its
statement before seeing the written solution, then audited that solution
in a separate pass. No substantive proof gaps were found. The only requested
wording correction and the difficulty disagreements are recorded. Every
indispensable nonstandard lemma is proved elementarily in the solution.

The exact checks cover 467 quartic parameter pairs and all coefficient
classes for primes through 101, plus tests of informative rejected seeds.
They support the proofs; they do not replace them. Reproduce with Python 3
and SymPy:

```sh
python problems/putnam-elliptic/verify.py
```

## Originality and scope

These are newly assembled contest formulations of established mathematics.
The quartic expression has an exact prior appearance; the finite-field
result follows from a known stronger variance formula; and the hard
problem's main square-value lemma has a close methodological precedent.
Those sources are cited rather than hidden. The exact combined formulations
were not located in the limited Putnam/source search, which does **not**
establish novelty. The rational-triangle seed was rejected after its exact
example was found in teaching literature.

No theorem from the repository's unverified research drafts is assumed.
Changes are confined to this directory on branch `problems/putnam-elliptic`,
in the separate worktree `/workspace/problems/putnam-elliptic`, starting
from `2e8e859`. Existing work and research files are preserved. Work is
committed locally; no push, merge, or pull request is part of this task.
