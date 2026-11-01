# Cubic Gauss sum bias in Mordell Frobenius traces

Started 2026-11-01. Unfinished. The identity below is elementary and checked.
The limiting law is an **empirical conjecture**, not a theorem. No novelty or
breakthrough is claimed, and no targeted prior-art search has been done.

## Setup

For a prime p = 1 mod 3, put a_p(B) = -sum_x (x³+B / p), the Frobenius trace of
E_B: y² = x³+B, and G_p(a) = sum_x e(a x³/p), which is real. Let
C = (2π)^(2/3) / (3 Γ(2/3)) = 0.838189.

**Exact identity.** With ρ the Legendre symbol mod p,

    a_p(B) = -(2/√p) Σ_{a=1}^{(p-1)/2} ρ(a) G_p(a) cos(2π a B/p)   if p = 1 mod 4,
    a_p(B) = -(2/√p) Σ_{a=1}^{(p-1)/2} ρ(a) G_p(a) sin(2π a B/p)   if p = 3 mod 4.

Proof: substitute u = x³+B in the discrete Fourier transform of B ↦ a_p(B).
`identity_check.py` confirms it for all 76 primes 5 ≤ p < 400 and all B mod p
(13,882 checks, maximum error 5·10⁻³⁷), and confirms a_p against PARI's `ellap`
(13,806 checks).

**Conjectural law.** Write a = a₁a₂²a₃³ with a₁, a₂ squarefree and coprime. Then
the mean of G_p(a)/p^(1/3) over primes p = 1 mod 3 tends to

    μ(a) = 2C a₁^(-1/3)   if a₂ = 1,      μ(a) = 0   otherwise.

**Consequence of the law, assuming the means may be taken term by term.** With
X = floor(up) and S_p(X) = Σ_{B=1}^X a_p(B), the mean of S_p(X)/p^(5/6) tends to

    p = 1 mod 12:  -(1/π) Σ_a m₁(a) sin(2π a u)/a,
    p = 7 mod 12:  -(1/π) Σ_a m₇(a) (1-cos 2π a u)/a,

where m₁ = μ on squares and on 3·squares, m₇ = μ on squares and -μ on 3·squares,
and both vanish elsewhere.

## Evidence

| Test | Data | Result |
|---|---|---|
| Law for a ≤ 60 ([law_2e6.json](law_2e6.json)) | 74,412 primes up to 2·10⁶ | chi² 45.5 on 60 rows, max z 2.32, no fitted parameters |
| Exact integer S_p(X), no Gauss sums ([direct_1e6.csv](direct_1e6.csv)) | primes in [2¹⁶, 10⁶] | chi² 27.3 on 46 grid points, max z 1.56 |

Rows are not independent. In the first test a and ac³ give identical values. In
the second, u and 1-u are exact mirrors and neighbouring u are correlated. Read
the chi² values as "no visible disagreement", not as calibrated fits. In the
second test the measured p = 1 mod 12 values lie slightly below the prediction
in size and the p = 7 mod 12 values slightly above it, which may be a
finite-size effect and has not been investigated.

## A prediction that failed

The first prediction used only the stationary-phase term ∫e(a t³/p)dt, giving
mean C a^(-1/3). It is wrong: the a = 1 constant is 2C, a = 4, 9, 25 vanish, and
G_p(ac³) = G_p(a) is an exact identity it ignores. `analyze_periods.py` still
prints that failed prediction, so [twisted_2e6.json](twisted_2e6.json) has chi²
1999 by design. The factor 2 is not explained.

## Reproduce

```sh
pip install numpy mpmath cypari
python identity_check.py
clang -O3 -march=native -fopenmp gauss_periods.c -o gauss_periods
clang -O3 -march=native -fopenmp mordell_direct.c -o mordell_direct
./gauss_periods 7 2000000 periods_2e6.bin
./mordell_direct 7 1000000 24 direct_1e6.csv
python analyze_law.py periods_2e6.bin 60
python compare_direct.py direct_1e6.csv 16
```

The binary periods file is not committed. On 16 threads it took 7 seconds.
