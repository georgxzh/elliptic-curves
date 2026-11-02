# Cubic Gauss-sum bias in Mordell traces

Continuation, 1 November 2026. The rational theta specialization and a
two-term logarithmic cusp for the candidate profiles are proved below.
The required twisted-prime means and sharp-interval prime limit remain
conjectural. Both enlarged computations are complete. No breakthrough
or novelty is claimed.

## Exact identity and candidate means

For p=1 mod3, put a_p(B)=-sum_x (x^3+B / p), for E_B: y^2=x^3+B,
and G_p(a)=sum_x exp(2pi i a x^3/p), which is real.
Let C=(2pi)^(2/3)/(3 Gamma(2/3))=0.83818940294056...
With rho the quadratic character,

    a_p(B) = -(2/sqrt(p)) sum_{a=1}^{(p-1)/2} rho(a) G_p(a) cos(2pi a B/p), p=1 mod4,
    a_p(B) = -(2/sqrt(p)) sum_{a=1}^{(p-1)/2} rho(a) G_p(a) sin(2pi a B/p), p=3 mod4.

Substitution t=x^3+B proves the Fourier identity. The singular parameter
B=0 is included as a character sum, with value zero.
The reproduced check covers 13,882 Fourier identities and 13,806 PARI
trace comparisons over 76 primes; maximum Fourier error was 4.849e-37.

Write a=a_1 a_2^2 a_3^3, with a_1,a_2 squarefree and coprime. Define

    mu(a) = 2C a_1^(-1/3) if a_2=1; 0 otherwise.

[THEORY.md](THEORY.md) proves that mu(a)/(2C) is exactly a rational
specialization of Patterson's cubic theta coefficient, including the
ramified prime 3 and inert primes. This identifies the arithmetic shape;
it does not prove a prime-restricted mean.
The conjecture is that the mean of G_p(a)/p^(1/3) tends to mu(a).

## Conditional theorem and the missing hypotheses

For S_p(X)=sum_{B=1}^X a_p(B), the candidate sharp-interval profiles are

    F_1(u) = -(1/pi) sum_a m_1(a) sin(2pi a u)/a,
    F_7(u) = -(1/pi) sum_a m_7(a) (1-cos(2pi a u))/a,

where m_1=mu on squares and three times squares, m_7=mu on squares
and -mu on three times squares, and both are zero elsewhere.
These profiles require more than the untwisted law: quadratic-character
twists, progression restrictions modulo 12, and an averaged Fourier-tail
estimate are all needed.

The strongest conditional prime-average theorem here is for a fixed
trigonometric polynomial in B/p. Its exact finite Fourier identity and
every required JTP hypothesis appear in [THEORY.md](THEORY.md).
There is no infinite tail in that theorem. Arbitrary smooth weights do
not have finite Fourier support. GRH alone is not shown to imply JTP.

## Proved coefficient/profile results

[COEFFICIENT_CUSP.md](COEFFICIENT_CUSP.md) corrects the original heuristic:

    sum mu(a)/a^s = 2C zeta(3s) zeta(s+1/3) / zeta(2s+2/3).

This has a zero, not a double pole, at s=1/6. The double poles occur
after selecting squares and three times squares. They give a proved
logarithmic cusp for the defined candidate profiles.

[SECOND_ORDER_CUSP.md](SECOND_ORDER_CUSP.md) strengthens it to

    F_r(u) = -K_r u^(5/6) (log(1/u) + eta_r + o(1)).

| r | K_r | eta_r |
|---:|---:|---:|
| 1 | 0.75270166404949 | 2.43107867716781 |
| 7 | 0.01448038915639 | 16.32567319151816 |

An elementary hyperbola decomposition gives a two-term coefficient
summatory estimate with error O(x^(2/21)log x). Explicit tail estimates
justify the oscillatory transfer. The larger eta_7 quantifies slow
convergence of the candidate cusp; it is not a theorem about finite-prime
drift or an integral-point count.

## Completed computations and the drift question

| Computation | Coverage | Finding |
|---|---|---|
| Reproduced Gauss baseline | 74,412 primes through 2 million | Original descriptive diagnostic 45.5 reproduced |
| Reproduced direct baseline | All eligible primes through 1 million | Original descriptive diagnostic 27.3 reproduced |
| Extended Gauss sums | 928,739 primes through 30 million; 510 frequencies | No compelling counterexample; twists, progressions and dyads retained |
| Exact direct sums | 332,194 primes through 10 million; 23 thresholds | Pooled drift decreases; class-7 offset reverses sign |

These squared standardized residual sums are **not calibrated chi-square
tests**. Frequencies related by cubes coincide; grid points are correlated
and mirrored. Sample standard errors are descriptive.

For a=1 and p>=65536, the enlarged Gauss mean is 1.667645 +/- 0.022229,
against candidate 1.676379. Mixed split/inert products, square factors
and quadratic twists are included. The largest high-range standardized
residual is 3.476 and is smaller in the final dyadic range.

For the direct comparison, the descriptive amplitude ratios change from
0.9696 to **0.9919** in class 1, and from 1.0509 to **0.9826** in class 7.
Thus both pooled absolute offsets shrink; the class-7 offset reverses.
Dyadic behavior is not monotone. No fitted correction is applied.
The new pooled maximum absolute standardized residuals are 0.975 and 1.153.
The candidate-series truncation error is below 3.3e-14, excluding roundoff.

[NUMERICS.md](NUMERICS.md) records all results, outliers, checks, data,
and the normalization experiment. The old p-dividing-a coset bug is
corrected and its tiny baseline effect is documented.
[COMPUTATION.md](COMPUTATION.md) proves the exact CM acceleration and
records independent integer comparisons. The direct run uses no
additive Gauss sums or bias conjecture.

## Literature and unsuccessful predictions

[LITERATURE.md](LITERATURE.md) records targeted searches and exact
hypotheses. Dunn–Radziwill's printed rational-prime coefficient and
primary-prime convention have a factor-two mismatch under conjugate
pairing. A September 2026 preprint already documents this issue and
claims an unconditional first moment. We did not audit its entire
proof or run its formalization; it is not a newly certified input here.
Fixed angular twists are not automatically the JTP assumptions above.

Under the explicitly normalized primary-prime hypothesis TP-a, the
factor 2 in mu comes from the density 1/2 of split rational primes.
The theta specialization is proved; this prime-twist transfer remains
an extra hypothesis.

The original stationary-phase-only prediction C a^(-1/3) disagrees
with the computations and ignores G_p(ac^3)=G_p(a) when p does not
divide c. The old analyze_periods.py retains that failed prediction,
explaining the historical diagnostic 1999. A numerical limiting
constant is not described here as proved.

## Extensions and wider survey

[EXTENSIONS.md](EXTENSIONS.md) separates exact identities from heuristic
transfers. Sixth-power-free parameters admit exact Mobius inversion,
but a growing-divisor tail is unresolved. The j=1728 transform is
quartic **minus quadratic**; omitting the quadratic term is wrong.
The proposed exponent 3/4 is not proved here. Root-number weighting
and conductor ordering require a different setup. No integral-point
explanation of the logarithm is established.

The [survey report](../../reports/Tractable%20elliptic%20curve%20open%20problems.md)
synthesizes all four supplied notes and rechecks rank records above 29.
Announcements, lower bounds, conditional equalities and finite
certificates are kept distinct.

## Reproduce

Python needs numpy and mpmath; the independent PARI check additionally
needs cypari2 and PARI. GCC needs -lm. Run from this directory:

    python identity_check.py
    gcc -O3 -march=native -fopenmp gauss_periods.c -lm -o /tmp/gauss_periods
    OMP_NUM_THREADS=2 /tmp/gauss_periods 7 30000000 /tmp/periods_3e7.bin
    python analyze_extended.py /tmp/periods_3e7.bin /tmp/extended_3e7.csv
    python normalization_check.py /tmp/periods_3e7.bin /tmp/normalization_3e7.json
    gcc -O3 -march=native -fopenmp -DCM_FAST mordell_direct.c -lm -o /tmp/mordell_cm
    OMP_NUM_THREADS=2 /tmp/mordell_cm 7 10000000 24 /tmp/direct_1e7.csv
    python analyze_direct_extended.py /tmp/direct_1e7.csv 10000000 /tmp/direct_1e7.json
    python check_theory.py /tmp/theory_checks.json
    python check_second_order.py /tmp/second_order_checks.json

[COMPUTATION.md](COMPUTATION.md) also gives the original baseline
commands and optional, much faster AVX-512 direct implementation.
Binary Gauss periods are not committed; their hash and coverage check
are archived with the compressed analysis CSV. Direct aggregate data
and comparison JSON are committed.

## Candid final status

* **Proved:** Fourier identities, rational theta specialization, corrected
  coefficient Dirichlet series, and the two-term cusp of the candidate profiles.
* **Conditional:** the finite-mode prime theorem under explicit JTP assumptions.
* **Numerical:** both reproduced baselines, Gauss tests through 30 million,
  and exact direct sums through 10 million. Pooled drift shrinks without
  monotone convergence across dyads.
* **Unknown:** JTP in the needed form, the sharp-window averaged tail,
  sixth-power-free transfer, quartic and root-number limits, and a link
  to integral points.
* **Novelty:** established Fourier, CM, theta and hyperbola machinery is
  used throughout. The normalization warning is prior work. Priority
  for the specialized coefficient/profile formulas is not established.
