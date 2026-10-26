# Sixth-power-free extension and Astra audits

The continuation gives a complete proof draft for every nonzero
sixth-power-free integer B:

\[
 \#\{(x,y)\in\mathbb Z^2:y^2=x^3+B\}
 \le C\,2^{\operatorname{rank}E_B(\mathbb Q)}
          \prod_{p>3}\lambda_p(B),
\]

where C is absolute. Write m=v_p(B) and u=B/p^m. The factors are:

| m | Local factor lambda_p(B) |
|---|---|
| 0, 1, 5 | 1 |
| 2, 4 | 2 if u is a square modulo p; otherwise 1 |
| 3 | 1 plus the number of roots of T^3+u modulo p |

In particular, for every nonzero squarefree B the product disappears and
the bound is `#E_B(Z) << 2^rank` with an absolute implied constant. More
generally the product is `2^(a+b+2c)` with a,b,c defined in the global proof.
The valuation-two/four cases recover the inert-prime mechanism in the
original fixed-d family. That earlier theorem also permits coefficients
which are not sixth-power-free at primes dividing the fixed integer d.

The exact local classification includes existence over Z_p of every listed
lattice. This is stronger than the earlier necessary-condition calculation.
It does not assert simultaneous global existence. The global bound uses only
an upper bound and the injection from actual global lattices to their
localizations.

Read the [local classification](LOCAL_SIXTH_FREE.md), the
[global theorem and squarefree corollary](GLOBAL_SIXTH_FREE.md), and the
[literature comparison](LITERATURE_EXTENSION.md). Rank-only bounds for
Mordell curves are already known; priority for the base-2 refinement and
these precise factors has not been established.

## Checks and their limits

The research Astra agent derived the extension; a separate Astra agent
audited the original proof and the local extension. Their saved reports are
[original proof audit](ORIGINAL_PROOF_AUDIT.md) and
[extension audit](EXTENSION_AUDIT.md). The root agent inspected the derivations
and added the finite and symbolic checks below. These are AI audits and
computational evidence, not independent human review or formal verification.

From the repository root:

```sh
python research/2026-10-25-inert/astra/verify_sixth_free.py
python research/2026-10-25-inert/astra/symbolic_extension.py
```

The first uses only the Python standard library and checks 1,285,032 residues
for 5,780 selected local points at p=5,7,11,13,19. It compares the exact
predicted lattice set with the set admitted by the square-value and derivative
conditions, at precision p^7. Every valuation case is exercised, including
all three cubic splitting types and both nonunit-x outcomes at valuation 3.
There were zero counterexamples; 106 truncated zero values and 356 other
square values were excluded by the derivative condition. The reproducible
output is [sixth_free_results.json](sixth_free_results.json).

The second requires SymPy. It verifies the determinant and basis change,
all five Taylor coefficients, monicity and depression, and recovery of a
point on the same curve, modulo the exact equation F(z)=q^2. All assertions
passed. Neither script verifies the imported descent or Thue theorems.

The constants displayed in the proof are deliberately very large. This is
an individual-curve theorem draft, not a bound on ranks or an average theorem.
