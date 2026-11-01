# Reproduction and exact sextic acceleration

Continuation, 1 November 2026. Numerical experiments are not proofs of prime
asymptotics. All paths below are relative to this directory.

## Reproduced baseline

On this environment (three visible CPUs, two-core quota, GCC, Python 3, NumPy 2.3.5, mpmath,
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

## Classical CM acceleration, with orientation fixed

The second acceleration uses classical complex multiplication of
E_1: y^2=x^3+1, together with exact sextic-coset counting. It is independent
of additive cubic Gauss sums and of any prime-bias conjecture.
The standard CM input is that Frobenius lies in the Eisenstein order,
has norm p and trace a_p(1), and its action on invariant differentials
is zero. This is classical CM theory for the j=0 curve, not a new result;
see, for example, Silverman, *Advanced Topics in the Arithmetic of
Elliptic Curves*, Chapter II (complex multiplication and reduction).
The explicit choice of generator and twist orientation used here follows.

Write p=a^2+3b^2 with b>0 and a=1 mod3, uniquely for p>3, p=1 mod3.
The curve E_1 has full rational 2-torsion and the rational point (0,1)
of order 3 over F_p. Its group order is divisible by 6. Of the six
possible CM traces

    +/-2a,  +/-(a+3b),  +/-(a-3b),

the last four are odd, because a and b have opposite parity.
The condition a_p(1)=p+1 mod3 selects 2a among the two even traces.
The existence and uniqueness of the representation, and these six
possibilities, follow from factorization of p and the six units in
the Euclidean Eisenstein ring. Thus the Frobenius element is one of
a +/- b sqrt(-3).

Choose the embedding into F_p by sqrt(-3) -> D=-a/b mod p. In this
embedding pi=a+b sqrt(-3) has zero differential, so it is Frobenius;
its conjugate reduces to 2a != 0. Put z=(1+D)/2, a primitive sixth
root of unity. If g is the primitive root used for the cosets and
d=g^((p-1)/6), then d is z or its inverse 1-z. Write s=1 in the
first case and s=-1 in the second. The ordered traces are

    t_0=2a, t_1=a+s*3b, t_2=-a+s*3b, t_{j+3}=-t_j.

To check the orientation, over the algebraic closure choose u^6=B.
The isomorphism (x,y)->(u^2 x,u^3 y) from E_1 to E_B transports
Frobenius to the composition of Frobenius on E_1 with the automorphism
(x,y)->(d^2 x,d^3 y), d=B^((p-1)/6).
This automorphism acts on the invariant differential by d^(-1).
For d=z its CM unit is (1-sqrt(-3))/2. Multiplying pi by that unit
and taking trace gives a+3b; its square gives -a+3b.
Conjugating the unit gives the other sign, and cubing gives -1.
This proves the formula used by cm_traces, including its sign convention.

The remaining optimization pairs B with -B. For p=1 mod12, -1 is a
sixth power, so half of each of six cosets suffices. For p=7 mod12,
-1 exchanges cosets j and j+3, so three entire cosets suffice.
The identity a_p(-B)=rho(-1)a_p(B) then gives both bin contributions.
Exactly (p-1)/2 steps are needed.

The bin reciprocal also uses exact integers: with
kp=floor(K*2^32/p), q=floor(kp*B/2^32), and r=K*B-q*p,

    floor((K*B-1)/p) = q + (r>p) - (r==0).

Since 0<B<p<2^32, q is either floor(K*B/p) or one less.
The formula includes p dividing K. The production CM limit is 30 million,
so a,b fit int16, products fit uint64, and totals fit int64.
Representation tables are initialized before the parallel read-only loop.

Use -DCM_FAST in place of -DSEXTIC:

    gcc -O3 -march=native -fopenmp -DCM_FAST mordell_direct.c -lm -o /tmp/mordell_cm
    OMP_NUM_THREADS=2 /tmp/mordell_cm 7 10000000 24 /tmp/direct_cm_1e7.csv
    gcc -O3 -march=native -fopenmp check_cm_large.c -lm -o /tmp/check_cm_large
    /tmp/check_cm_large

The updated small check compares all three algorithms on 166,803 exact
integer outputs. The large check compares CM to the character-sum
sextic method on 939 outputs at 32 spread-out primes through 30 million,
with K=7,24,63, plus 320,000 exact reciprocal-bin checks.
All passed. The 100,000-prime-limit benchmark CSVs from the CM and
sextic versions agree in every field; measured one-thread times under
contention were 1.3 and 5.2 seconds. They are not isolated speed benchmarks.
The slower 10-million sextic run was stopped after about 21 minutes
and replaced by the validated CM run; no completed result is attributed
to the interrupted job.
