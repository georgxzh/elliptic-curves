# Reproduction and exact sextic acceleration

Continuation, 1 November 2026. Numerical experiments are not proofs of prime
asymptotics. All paths below are relative to this directory.

## Reproduced baseline

On this environment (three CPUs, GCC, Python 3, NumPy 2.3.5, mpmath,
cypari 2.5.7):

* `identity_check.py`: 76 primes, 13,882 Fourier-identity checks and 13,806
  PARI `ellap` comparisons; maximum absolute error `4.8489e-37`.
* `gauss_periods 7 2000000 ...`: 74,412 primes, 32.3 seconds before the
  other jobs started. The original analysis reproduces sum of squared
  standardized residuals 45.5 and maximum absolute residual 2.32.
* The original `mordell_direct 7 1000000 24 ...` reproduces all 759
  aggregate rows: counts and bin labels agree exactly, and the largest
  discrepancy in a sum or sum of squares divided by `max(1,abs(original))`
  is `6.904e-15`. Parallel floating-point accumulation explains these
  last-digit differences. The underlying character sums use integers.
* The committed direct-data comparison reproduces 27.3. These are
  descriptive diagnostics, **not calibrated chi-square statistics**.

The README's original `clang` command is not portable to this environment:
clang is absent, and GCC needs `-lm`. Use GCC commands below.

The 30-million Gauss-period computation has completed: 928,739 primes,
6,168.0 seconds with three threads (including contention with other jobs).
The binary file is 24 bytes per record. Its analysis is recorded separately.

## Exact acceleration (elementary lemma)

For a prime p=1 mod 3, choose a primitive root g. Write

    t_j = -rho(g^j) - 3 sum_{c in (F_p^*)^3} rho(c+g^j),  j=0,1,2.

Then `t_j=a_p(g^j)`. Cubing has three preimages on the nonzero cubes,
and the x=0 term is `-rho(g^j)`, proving the formula. Changing x to gx
in the original character sum gives

    a_p(g^3 B) = rho(g) a_p(B) = -a_p(B).

Changing x to d^2 x gives `a_p(d^6 B)=a_p(B)`. Thus the six sextic
cosets have traces `t_0,t_1,t_2,-t_0,-t_1,-t_2` in that order.
Walking them counts every nonzero B exactly once. B enters the first
threshold k satisfying `B <= floor(k*p/K)`, namely `ceil(K*B/p)`.
The code adds its integer trace to bin `floor((K*B-1)/p)` and takes
prefix sums. This proves equality to the original S_p for every threshold;
no Gauss sum, approximation to a trace, or rank information is used.

`sextic_sums.h` implements this lemma. The original algorithm is retained
as the default; `-DSEXTIC` selects the faster one. Time per prime becomes
O(p+K), in place of O(Kp). The modular reciprocal reduction is valid for
the enforced range p<2^31: its quotient estimate is at most one too small,
so a single subtraction suffices. Products use uint64; traces and sums
use int64.

## Exact cross-check and commands

```sh
gcc -O3 -march=native -fopenmp check_sextic.c -lm -o /tmp/check_sextic
/tmp/check_sextic
gcc -O3 -march=native -fopenmp -DSEXTIC mordell_direct.c -lm -o /tmp/mordell_sextic
OMP_NUM_THREADS=3 /tmp/mordell_sextic 7 10000000 24 /tmp/direct_1e7.csv
gcc -O3 -march=native -fopenmp gauss_periods.c -lm -o /tmp/gauss_periods
OMP_NUM_THREADS=3 /tmp/gauss_periods 7 30000000 /tmp/periods_3e7.bin
```

The check compares **166,803 exact integer outputs** for all eligible
primes below 10,000 and multiple K from 2 through 57, including K>p.
All passed. The test does not use the proposed bias law as an oracle.
The sextic algorithm is standard finite-field arithmetic; no algorithmic
novelty is claimed.
