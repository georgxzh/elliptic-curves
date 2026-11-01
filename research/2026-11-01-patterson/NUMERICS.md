# Extended numerical tests

These are finite deterministic prime samples. The displayed standard errors
are descriptive sample standard deviations divided by the square root of the
sample size; they are not error bounds for a prime asymptotic. Frequencies
related by cubes coincide, progressions partition the same primes, and many
tests were inspected. No calibrated p-values or independent chi-square fit
are claimed.

## Gauss periods through 30 million

The run contains every one of the **928,739** rational primes p=1 mod3
between 7 and 30,000,000, last prime 29,999,989. The 22,289,736-byte
binary is not committed. Its SHA-256, full sieve check, and bitwise agreement
with all 74,412 records in the reproduced 2-million run are in
[the manifest](results/periods_manifest.json).
Runtime was 6,168 seconds with three threads and concurrent work.
The environment exposes three CPUs but has a **two-core CPU quota**.

[analyze_extended.py](analyze_extended.py) tests 510 frequencies: 1 through
400, mixed products of split primes 7,13,19,31,37,43 and inert primes
2,5,11,17,23,29, their specified square/cube multiples, and some powers.
The largest tested a is 53,621. Primes dividing a are excluded.
Both G and rho(a)G are tested, pooled and separately modulo 12, in
disjoint dyadic ranges and the pooled range p>=65536.

The [compressed CSV](results/extended_3e7.csv.gz) contains every row;
the [summary JSON](results/extended_3e7.csv.summary.json) gives selected
anchors and the largest standardized residuals.
In the pooled high range there are 925,480 primes, divided into
462,588 in class 1 and 462,892 in class 7 modulo 12.

| a | Mean G/p^(1/3) | Descriptive standard error | Candidate |
|---:|---:|---:|---:|
| 1 | 1.667645 | 0.022229 | 1.676379 |
| 2 | 1.328561 | 0.022250 | 1.330543 |
| 3 | 1.134371 | 0.022277 | 1.162336 |
| 4 | -0.013339 | 0.022306 | 0 |
| 7 | 0.876828 | 0.022268 | 0.876340 |
| 9 | -0.008185 | 0.022309 | 0 |
| 25 | 0.018318 | 0.022297 | 0 |
| 35 | 0.524872 | 0.022273 | 0.512487 |
| 77 | 0.386088 | 0.022272 | 0.394041 |
| 143 | 0.305292 | 0.022280 | 0.320573 |
| 323 | 0.253683 | 0.022292 | 0.244327 |

For a=1, the two progression means are 1.682039 +/- 0.031433 and
1.653259 +/- 0.031439. In the final range [2^24,30 million], they are
1.66610 +/- 0.05395 and 1.67464 +/- 0.05395.
The data do not suggest a persistent opposite progression offset here,
but this is not the direct sharp-window drift test.

The largest high-range standardized residual is for rho(91)G(91) in
class 7: mean 0.109435, error 0.031484, candidate zero, residual 3.476.
Its dyadic residual is 3.379 in [2^23,2^24], but 1.257 in the final
range; the latter mean is 0.06794 +/- 0.05406.
Another large residual is rho(199)G(199) in class 1, -3.425.
The pooled rho(77)G(77) residual is -3.070.
These are worth retaining for future tests, not evidence to discard or
calibrated discoveries after inspecting thousands of correlated rows.
This run produces no compelling numerical counterexample to the candidate
fixed-frequency means. It proves neither their limits nor the zero cases.

## Independent numerical and baseline checks

[check_periods.c](check_periods.c) checks the exact identity
G_0^2+G_1^2+G_2^2=6p numerically for every record, and recomputes 16
spread-out records with direct libm cosine instead of the production lookup.
The maximum relative second-moment discrepancy is 1.7661e-8;
the maximum sampled discrepancy in G/p^(1/3) is 2.9527e-7.
The [raw check log](results/period_check.log) records the values.
These checks are much smaller than the observed fluctuations; they are
not a rigorous floating-point error certificate.

The old analyze_law script assigned a cubic coset even when p divides a.
The exact value in that case is G_p(a)=p. The script is corrected;
the new extended script instead omits these finitely many primes.
The historical baseline JSON is preserved and the
[corrected baseline](results/law_2e6_corrected.json) is stored separately.
Both still round to the original descriptive squared-residual sum 45.5
and maximum absolute residual 2.32. Exact cube correlations require
excluding primes dividing the cube multiplier.

## Match the published smooth-weight convention

[normalization_check.py](normalization_check.py) uses the smooth bump
W(t)=exp(4-1/(4(t-1/2)(1-t))) on (1/2,1), zero elsewhere, and
V(t)=t^(1/6)W(t). At X=30 million the coefficient measured for

    sum_{p=1 mod3} G_p(1)/(2 sqrt(p)) V(p/X)

after dividing by X^(5/6)/log(X) times integral W is **0.433634**.
The consistently paired primary-prime convention predicts C/2=0.419095;
the literal rational-prime statement discussed in
[LITERATURE.md](LITERATURE.md) prints C=0.838189.
All five scales are in [the normalization JSON](results/normalization_3e7.json).
At the largest scale the W-weighted mean of G/p^(1/3) is
1.705223 +/- 0.049892.
This is a finite-data normalization check, not a refutation of an asymptotic
or of GRH. The later preprint already documents the factor-two issue.

## Reproduction

After generating periods_3e7.bin as in [COMPUTATION.md](COMPUTATION.md):

    python validate_periods.py periods_3e7.bin 30000000 periods_2e6.bin
    gcc -O3 -march=native -fopenmp check_periods.c -lm -o check_periods
    ./check_periods periods_3e7.bin
    python analyze_extended.py periods_3e7.bin extended_3e7.csv
    python normalization_check.py periods_3e7.bin normalization_3e7.json

The CSV archive uses Python gzip.compress with mtime=0. Floating-point
outputs may differ in their last digits on another platform.
