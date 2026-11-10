# Q4 continuation: a balanced quadratic-twist estimate

Continuation of `c011f0c`, independently audited with Astra.

**Strongest new proved analytic statement (under GRH).** With
A=X^(3/5), B=X^(2/5), arbitrary bounded squarefree coefficients alpha_a
supported on Na asymptotic to A, and fixed smooth W supported in [1,2],

\[
 \sum_a\sum_{b\ {\rm primary\ prime}\atop B\le Nb\le2B}
 \alpha_a\chi_{-4}(N(ab))\widetilde g(ab)W(N(ab)/X)
                  \ll_W X^{5/6-\delta}\qquad(\delta>0).
\]

This follows from a proved GRH admissibility check and Dunn--Radziwill's
published broad Type II estimate. It is a result for composite
prime-factor blocks. **The prime-restricted estimate Q4 remains open
in this work.** No new nonzero progression bias or novelty is claimed.

[Q4_REPORT.md](Q4_REPORT.md) contains the theorem and proof, and also:

* The exact necessary and sufficient Q4 scale for separating mode one
  into classes 1 and 7 modulo 12, with the inert-prime contribution
  retained and normalization matched to [DR, (13.20)].
* A GRH counterexample showing the coefficient class C_eta is not
  generally preserved by a quadratic twist.
* An unconditional exact modulus-4 Fourier identity, including its sign
  and conductor, reducing the local twist to twelve additive twists.
* The precise unsupported long Type I transition in the published proof
  and the modulus mismatch in Yoshimoto's original functional equation.

[TAIL_REPORT.md](TAIL_REPORT.md) proves a smaller sufficient smoothing
cutoff using Jackson kernels and a weighted mean-square alternative to
uniform frequency bounds. Both still require additional arithmetic
estimates. Positivity and finite-field Parseval do not supply those.

[ASTRA_AUDIT.md](ASTRA_AUDIT.md) records the independent review and its
scope. [checks.json](checks.json) is produced by the standard-library-only
exact check script:

```sh
python research/2026-11-10-q4/check_q4.py
python research/2026-11-02-prime-audit/check_reductions.py
```

No large prime-average experiment was run. Finite checks verify the
identities and rational exponent arithmetic, not GRH or prime asymptotics.
The existing split-prime nonzero mean remains conditional on GRH;
the earlier w_* theorem remains a designed cancellation construction.

The remaining primary bottleneck is
Q(X;V)=o_V(X^(5/6)/log X). A route through [DR] requires a correctly
twisted long Type I transform, residue analysis and bounds uniform in
the short variable, plus checks for all coefficient blocks. The present
balanced theorem supplies one such block, not a complete adaptation.
