// Exact integer computation of S_p(X) = sum_{B=1}^{X} a_p(E_B), E_B: y^2 = x^3 + B,
// for X = floor(k p / K), k = 1..K-1, and every prime p = 1 mod 3 in a range.
// No Gauss sums and no floating point are used for S_p(X).
//
// Uses a_p(E_B) = -sum_x (x^3+B / p) and a prefix table T of Legendre symbols.
// Output CSV: one row per (dyadic bin, p mod 12, k) with
//   count of primes, sum S/p^(5/6), sum (S/p^(5/6))^2.
//
// Build: gcc -O3 -march=native -fopenmp mordell_direct.c -lm -o mordell_direct
// Add -DSEXTIC for the exact sextic-coset acceleration (see COMPUTATION.md).
// Usage: mordell_direct PMIN PMAX K OUT.csv
#include <math.h>
#include <omp.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXK 64
#define NBIN 40
#include "sextic_sums.h"

static void sum_S(uint32_t p, uint32_t K, int32_t *T, int8_t *leg, int64_t *S) {
    memset(leg, -1, p);
    leg[0] = 0;
    uint64_t sq = 0, step = 1;
    for (uint32_t x = 1; x <= (p - 1) / 2; x++) {
        sq += step;
        if (sq >= p) sq -= p;
        step += 2;
        if (step >= p) step -= p;
        leg[sq] = 1;
    }
    T[0] = 0;
    for (uint32_t n = 1; n < p; n++) T[n] = T[n - 1] + leg[n];
    // T[p-1] = 0 because the Legendre symbols sum to zero over a full period.
    uint32_t X[MAXK];
    for (uint32_t k = 1; k < K; k++) {
        X[k] = (uint32_t)((uint64_t)k * p / K);
        S[k] = 0;
    }
    uint64_t c = 0, d = 1, e = 6 % p;
    for (uint32_t x = 0; x < p; x++) {
        for (uint32_t k = 1; k < K; k++) {
            uint64_t top = c + X[k];
            if (top >= p) top -= p;
            S[k] -= (int64_t)T[top] - T[c];
        }
        c += d;
        if (c >= p) c -= p;
        d += e;
        if (d >= p) d -= p;
        e += 6;
        if (e >= p) e -= p;
    }
}

int main(int argc, char **argv) {
    if (argc != 5) {
        fprintf(stderr, "usage: %s PMIN PMAX K OUT\n", argv[0]);
        return 2;
    }
    uint32_t pmin = (uint32_t)strtoul(argv[1], 0, 10);
    uint32_t pmax = (uint32_t)strtoul(argv[2], 0, 10);
    uint32_t K = (uint32_t)strtoul(argv[3], 0, 10);
    if (pmin < 7) pmin = 7;
    if (K < 2 || K >= MAXK || pmax >= (1u << 31) || pmax < pmin) return 2;
    uint8_t *comp = calloc((size_t)pmax + 1, 1);
    for (uint64_t i = 2; i * i <= pmax; i++)
        if (!comp[i])
            for (uint64_t j = i * i; j <= pmax; j += i) comp[j] = 1;
    size_t cnt = 0;
    for (uint32_t n = pmin; n <= pmax; n++)
        if (!comp[n] && n % 3 == 1) cnt++;
    uint32_t *primes = malloc(cnt * sizeof(uint32_t));
    size_t m = 0;
    for (uint32_t n = pmin; n <= pmax; n++)
        if (!comp[n] && n % 3 == 1) primes[m++] = n;
    free(comp);

    static double sum1[NBIN][2][MAXK], sum2[NBIN][2][MAXK];
    static long long num[NBIN][2];
    double t0 = omp_get_wtime();
#pragma omp parallel
    {
        int32_t *T = malloc((size_t)pmax * sizeof(int32_t));
        int8_t *leg = malloc((size_t)pmax);
        int64_t S[MAXK];
#pragma omp for schedule(dynamic, 16)
        for (long long i = (long long)cnt - 1; i >= 0; i--) {
            uint32_t p = primes[i];
#ifdef SEXTIC
            sum_S_sextic(p, K, leg, S);
#else
            sum_S(p, K, T, leg, S);
#endif
            int bin = 31 - __builtin_clz(p);
            int cls = p % 12 == 1 ? 0 : 1;
            double norm = pow((double)p, 5.0 / 6.0);
#pragma omp critical
            {
                num[bin][cls]++;
                for (uint32_t k = 1; k < K; k++) {
                    double v = (double)S[k] / norm;
                    sum1[bin][cls][k] += v;
                    sum2[bin][cls][k] += v * v;
                }
            }
        }
        free(T);
        free(leg);
    }
    FILE *f = fopen(argv[4], "w");
    if (!f) return 1;
    fprintf(f, "bin,p_mod_12,k,K,count,sum,sum2\n");
    for (int b = 0; b < NBIN; b++)
        for (int c = 0; c < 2; c++)
            if (num[b][c])
                for (uint32_t k = 1; k < K; k++)
                    fprintf(f, "%d,%d,%u,%u,%lld,%.17g,%.17g\n", b, c ? 7 : 1, k, K, num[b][c],
                            sum1[b][c][k], sum2[b][c][k]);
    fclose(f);
    printf("primes=%zu seconds=%.1f\n", cnt, omp_get_wtime() - t0);
    return 0;
}
