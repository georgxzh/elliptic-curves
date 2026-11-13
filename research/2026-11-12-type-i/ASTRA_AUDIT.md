# Independent Astra audit

Model: `gpt-6-astra`, agent `astra_type_i_audit`, requested after the
finite transform, completed-series identity, residue calculation and
smooth-transform constants had been derived. The agent worked read-only.
This is a research audit, not formal verification of the imported
theta-function theory or proof of Q4.

The auditor directly inspected [DR v3](https://arxiv.org/html/2109.07463v3),
(5.17), (5.21)--(5.25), (5.44)--(5.48), the coefficient calculation
around (5.62), and the relevant Type I setup. Its core verdict was:
the completed transform, vanishing residue, and conservative uniform
bound pass.

The independently checked points were:

1. The general periodic-transform theorem permits q=4r. Its hypothesis
   is support of hat(psi) on units, which follows from primitivity;
   squarefreeness of q is not required.
2. CRT gives the factor 16, the phase chi_r(lambda^2), and the
   **conjugated** chi_4(v). The two local -4 factors and the two CRT
   phases cancel as in TRANSFORM.md. The auditor separately checked all
   sixteen local classes and supplied an independent orthogonality proof.
3. The normalization D_r=3^(5/2+3s)psi(lambda)F_r, with
   psi(lambda)=-conjugate(chi_r(lambda)), is correct. Both quadratic
   factors in the completed sum and the exact Mobius inversion survive.
4. The possible completed residue is zero. Entirety is proved for F_r;
   regularity of R_r at 5/6 uses the nonzero completing L-factor at 2.
   Entirety or rapid decay is not asserted for the uncompleted quotient.
5. The smooth prefactor is [3^(7/2)psi(lambda)(2pi)^2]^(-1), and its
   kernel argument is (2pi)^4 YN(mu)/(6912 R^2).
6. Absolute convergence of the dual series at 1+b yields
   O_(b,W)(sqrt(R)phi(r)(R^2/Y)^b), uniformly in r,Y for fixed b>0.
7. The conditional error-budget arithmetic is correct: hypothetical
   pointwise errors sum to X^(5/6-rho) and
   X^(1/12+epsilon)R^(3/2+O(epsilon)), the latter at most
   X^(91/120+O(epsilon)) when R<=X^(9/20).

The auditor requested an explicit vertical-growth argument: the theta
Mellin representation alone initially bounds the gamma-divided series
exponentially. TRANSFORM.md now supplies Phragmen--Lindelof between the
right absolute-convergence line and the left functional-equation line;
the gamma quotient on Re(s)=-b has size O_b((1+|t|)^(2+4b)). This
justifies the smooth contour shift, not merely the formal identity.

In the final written audit the agent read TRANSFORM.md, RANGES.md and
the complete check_transform.py, rechecked the ranges against Sections
8, 11 and 13, and independently reran all six finite cases in memory
without writing files. All 1,824 Fourier residue checks and 173
metaplectic evaluations passed. The latter count is evaluations, not
distinct classes: a few selected inputs repeat. No blocking corrections
remained.

The stronger uniform pointwise Type I estimate remains unproved.
Neither the residue theorem nor this audit establishes cancellation
in the prime-restricted Q4 sum or a novelty claim.
