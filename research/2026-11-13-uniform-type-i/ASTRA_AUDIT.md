# Independent Astra audit, 13 November 2026

Model: `gpt-6-astra`, agent `astra_uniform_audit`. Review was requested
after a concrete Euler-factor and dyadic de-completion argument was
ready. The agent worked read-only and inspected the relevant passages
of [DR v3](https://arxiv.org/html/2109.07463v3) directly.

The initial proof gave the unconditional U^(1/2)R^(1/4) bound and a
GRH U^(3/7)R^(2/7) bound. Astra proposed using the same absolute mass
lemma in a uniform strip interpolation and dividing by the completing
L-function. That strengthened the conditional exponent to
U^(1/3)R^(1/3). Both the primary agent and Astra checked the resulting
argument; the final report presents the stronger result as Theorem B.

## Checks of the decisive proof

The independent audit verified:

1. The exact theta/cusp support in (5.7), (5.13)--(5.14) and Appendix A.
   The squarefree and cube variables may share primes. The ramified
   factor has geometric ratio 3^(1/2-3sigma); the two exceptional cusp
   families together contribute the majorant 54 times 3^(4sigma).
2. The absolute local Ramanujan factor
   E_Q=[1+(Q-1)t+(Q-2)z]/(1-z). Its monotone envelope at
   t=1/Q,z=1/Q^2 equals exactly 2. The resulting product is bounded
   by a constant depending on sigma times 2^omega_O(r).
3. The general periodic transformation hypotheses at q=4r, the extra
   conjugated chi_4 factor, the vanishing completed residue, and the
   distinction between the entire completed series and its quotient.
4. The level-uniform Phragmen--Lindelof argument. Damping removes the
   preliminary horizontal-edge growth separately for each r, leaving
   boundary constants independent of r. Thus no hidden level constant
   enters the final strip bound.
5. The reciprocal completing factor, including (1+3^(-s))^(-1),
   its R^epsilon Euler-removal bound, and the fixed-character
   factorization L_K(s,kappa)=L(s,chi_-4)L(s,chi_12), including 2,3.
6. The unconditional shift to 1/2+a and conditional shift to 1/3+a,
   with no poles crossed. The auditor also suggested using only a
   polynomial reciprocal-L bound, proved by Borel--Caratheodory,
   rather than importing an unnecessarily sharp subpower statement.
   That weaker sufficient argument is now included explicitly.
7. Uniformity in bounded smooth weight families, and the edge cases
   r=1,U=1. The two-cutoff cross-check handles R>U^2 by the trivial bound.
8. The fair old-majorant interpolation thresholds 4/15 and 3/10,
   and the new thresholds 4/9 and 1/2.

## Actual decomposition block

The agent checked [DR, Definition 3.1 and (11.2)--(11.4)] against the
assembled block in Section 7. Primary generators and disjoint rough/
smooth prime supports give a unique factorization r=st. The rescaled
weights form a bounded smooth family. This validates
B(N)<<X^(4/3+epsilon)/N, the Case 1 exponent 47/60, its saving 1/20,
and the extension to N>=X^(1/2+delta).

Two minor hypotheses were made explicit at the auditor's request:
V_1,V_2,W must have compact support in (0,infinity), not just be
supported away from zero; and the general block statement assumes
X,N>=1 and C>0. Both are incorporated.

## Final checks and scope

The final written audit passed, including the weaker polynomial
reciprocal-L proof. The agent independently reran check_uniform.py
in memory with report writing intercepted:

* 882 local-mass/truncated-series checks;
* 26 prime Euler-factor checks;
* 18 quadratic cube-inversion checks;
* 5 exact exponent budgets.

All passed. The primary agent also reran the preceding exact
modulus-4 transformation verification. These computations establish
finite identities, not GRH or the analytic estimates by themselves.

The audit certifies the stated reasoning at research-review level;
it is not a formal proof of all imported theta-function theory.
The unconditional and GRH scopes remain separate. The remaining
balanced/short-variable blocks and full Q4 have not been proved.
No novelty claim was audited or established.
