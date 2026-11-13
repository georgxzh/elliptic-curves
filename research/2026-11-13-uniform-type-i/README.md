# A uniform twisted Type I bound and a completed long block

Continuation of `fb4273e`, 13 November 2026. Independently audited with
Astra. No novelty or complete Q4 theorem is claimed.

For odd squarefree primary r, R=Nr, and fixed smooth W supported away
from zero and infinity, write

\[
 T_r(U)=\sum_{u\equiv1(3)}\chi_{-4}(Nu)\widetilde g(ur)W(Nu/U).
\]

**Proved uniformly in growing r and U>=1:**

\[
 T_r(U)\ll_{\varepsilon,W}(UR)^\varepsilon U^{1/2}R^{1/4}
                 \quad\text{unconditionally},
\]
\[
 \boxed{\ T_r(U)\ll_{\varepsilon,W}(UR)^\varepsilon U^{1/3}R^{1/3}
                 \quad\text{under fixed-character GRH}.\ }
\]

The conditional input is GRH for L_K(s,kappa), equivalently for the
two Dirichlet L-functions of characters chi_-4 and chi_12. The proof
checks the reciprocal factor, including the removed Euler factors;
it does not assume Mobius cancellation at a growing conductor.

The new absolute dual-mass lemma retains the Ramanujan factor against
the actual theta support. Each prime ideal dividing r costs at most 2,
replacing the previous worst-case phi_O(r) loss by
2^omega_O(r)<<_epsilon R^epsilon. A uniform strip interpolation and
Mellin-space Mobius inversion then give the displayed bounds.

**Contribution to the prime decomposition.** A short-variable sum with
R<=X^(1/2-delta) saves a power under GRH. The actual rough/smooth
factorization in the long Type I block is unique, so its multiplicities
introduce no new loss. Its dyadic contribution satisfies

\[
 B(N)\ll X^{4/3+\varepsilon}/N.
\]

Thus [DR, Section 11, Case 1], N>=X^(11/20), contributes
O(X^(47/60+epsilon)), with exponent saving **1/20**. The estimate
extends to all N>=X^(1/2+delta). Unconditionally the corresponding
short-variable range is R<=X^(4/9-delta).

[UNIFORM_BOUND.md](UNIFORM_BOUND.md) contains the proofs, all normalizations,
the earlier-bound comparison, the actual block calculation, and source
and novelty limits. [ASTRA_AUDIT.md](ASTRA_AUDIT.md) records independent
review. [checks.json](checks.json) records exact local and exponent checks.

```sh
python research/2026-11-13-uniform-type-i/check_uniform.py
python research/2026-11-12-type-i/check_transform.py
```

**Remaining gap:** the new bound alone gives no power saving at
N=X^(1/2), or for smaller N. Those ranges and the remaining twisted
coefficient/bilinear comparisons must still be proved and assembled
before Q4 follows. The earlier prime-supported balanced-block theorem
does not automatically cover all those coefficients. Sharp-interval
tails remain separate. No prime-restricted main term has been excluded
merely by the completed zero residue.
