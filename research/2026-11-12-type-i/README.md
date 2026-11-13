# Completed Type I: exact modulus-4 transform and zero residue

**Continuation:** [uniform bounds after Mobius inversion](../2026-11-13-uniform-type-i/README.md)
now replace the conservative level loss and prove a GRH saving for the
actual long Type I block. The remaining prime-decomposition blocks and
Q4 remain open in this work.

Continuation of `8e72e3d`, 12 November 2026 (Toronto).

**Proved unconditionally, using the published general theta transform:**
for every odd squarefree primary r, including r=1, the correctly
cube-completed quadratic-twisted Type I series is entire. Its possible
residue at s=5/6 is zero. The corresponding smooth transformation has
no polar term. This is an all-moduli result, not a solution of Q4.

With q=4r, psi=kappa conjugate(chi_r), and DR's finite-transform
normalization, the decisive identity is

\[
 \widetilde\psi(v)=16\chi_r(\lambda^2)\overline{g(r)}
                   \kappa(v)\overline{\chi_4(v)}c_r(v).
\]

The extra conjugated cubic character at 2 matters. The completed sum
contains **both** kappa(u) and kappa(d); its theta normalization includes
psi(lambda)=-conjugate(chi_r(lambda)). These factors are retained in the
explicit functional equation and smooth Voronoi formula.

* [RANGES.md](RANGES.md) specifies the short-variable ranges, cube cutoff,
  and error budget required by the prime decomposition before estimates
  are proposed.
* [TRANSFORM.md](TRANSFORM.md) proves the finite transform, residue theorem,
  full smooth transformation, exact Mobius de-completion, and the uniform
  bound C_r(Y) <<_(b,W) sqrt(R) phi(r) (R^2/Y)^b, R=Nr.
* [ASTRA_AUDIT.md](ASTRA_AUDIT.md) records independent verification of
  phases, conductor hypotheses, constants, contour shifts, and limitations.
* [checks.json](checks.json) records exact cyclotomic checks at 1,824
  Fourier residues and 173 metaplectic evaluations, including inert and composite
  odd squarefree r. No floating-point or prime-average experiment is used.

Run:

```sh
python research/2026-11-12-type-i/check_transform.py
python research/2026-11-10-q4/check_q4.py
```

The bound is rapid decay for each fixed r. Its level dependence is too
weak at the edge of the required range: Y/R^2 can be X^(-3/5), before
epsilon losses. The next missing result is a sharper, uniform estimate
after Mobius de-completion, such as (TI) in RANGES.md, followed by the
remaining coefficient-block and prime-decomposition checks. The zero
all-moduli residue does not exclude a main term on primes.

GRH is retained in earlier prime-average results and in the proposed
adaptation of the Mobius bounds. No novelty is claimed for this
specialization of published machinery.
