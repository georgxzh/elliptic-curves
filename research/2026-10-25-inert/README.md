# Inert-prime refinement of the integral-point bound

The candidate now has a complete proof draft of the stronger estimate

\[
 \#E_{d,n}(\mathbb Z)\ll_d
 2^{\operatorname{rank}E_{d,n}(\mathbb Q)+\omega_{\rm split}(n)},
 \qquad E_{d,n}:y^2=x^3+dn^2,
\]

for fixed nonzero integer d and positive cube-free n. Here omega_split
counts p dividing n with p not dividing 6d and (d/p)=1. In particular,
inert primes contribute no varying prime-count factor. This draft has not
received independent mathematical review, and no novelty is claimed.

The improvement over the earlier candidate outline is the global fibre
argument: count actual row sublattices of Z^2, rather than equivalence
classes of abstract local models. Each inert prime allows one local lattice,
each split prime at most two, and each actual global lattice contributes
uniformly many point quartics by the homogeneous Thue bound.

Read the argument in this order:

1. [Local proof](LOCAL_PROOF.md): determinant valuation, repeated-root disk,
   square-value obstruction, and classification of the possible lattices.
2. [Global proof](GLOBAL_PROOF.md): local-to-global injection, fixed-prime
   constants, determinant signs, and the uniform bound per lattice.
3. [Sharpness examples](SHARPNESS.md): the second lattice actually occurs
   at a split prime, for both cube-free valuation cases.
4. [Literature audit](LITERATURE.md): precise dependencies and close overlap
   with Sadek's established minimal-model classification.

Reproduce the finite checks from the repository root:

```sh
python local_quartic_checks.py
python research/2026-10-25-inert/verify.py
python research/2026-10-25-inert/symbolic_checks.py
```

The first script reproduces the original 215,892 repeated-root residue checks.
The new script checks 1,050,696 residues across 13,872 selected p-adic points,
including 7,264 nonunit-x cases, and 106 admissible signed matrices between
point quartics. It verifies 77 changes of basis within actual row lattices.
All assertions passed, with zero counterexamples. Exact scope and sample
examples are in [results.json](results.json); finite tests are not proofs.

The last script verifies four symbolic identities: the split-prime example
family, the quartic discriminant, and the determinant and depression equations
used to reconstruct transformation matrices.

The finite verifier uses only Python's standard library. The original and
symbolic scripts require SymPy. These checks do not compute complete
integral-point sets, certify a rank bound, or certify novelty.

The conclusion here is an individual-curve bound. No new average theorem or
rank distribution on an inert-supported thin family is established.
