// Compute the cubic Gaussian periods of every prime p = 1 mod 3 in a range.
//
// For a in the coset g^i C of the cubes, G_p(a) = sum_x e(a x^3 / p) = 1 + 3 eta_i
// where eta_i = sum_{t in g^i C} cos(2 pi t / p).  Writes one fixed-size binary
// record per prime, sorted by p:
//   uint32 p, uint32 g, double eta0, double eta1   (eta2 = -1 - eta0 - eta1)
//
// Build: clang -O3 -march=native -fopenmp gauss_periods.c -o gauss_periods
// Usage: gauss_periods PMIN PMAX OUTFILE
#include <math.h>
#include <omp.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TBITS 14
#define TSIZE (1u << TBITS)
static double COS_T[TSIZE], SIN_T[TSIZE];
static const double TWO_PI = 6.283185307179586476925286766559;

typedef struct {
    uint32_t p, g;
    double eta0, eta1;
} rec_t;

static inline double cos_phase(uint64_t phi) {
    uint32_t i = (uint32_t)(phi >> (64 - TBITS));
    uint64_t rem = phi << TBITS;
    double d = (double)rem * (TWO_PI / 18446744073709551616.0 / (double)TSIZE);
    return COS_T[i] - d * (SIN_T[i] + 0.5 * d * COS_T[i]);
}

static uint64_t powmod(uint64_t b, uint64_t e, uint64_t m) {
    uint64_t r = 1;
    b %= m;
    while (e) {
        if (e & 1) r = r * b % m;
        b = b * b % m;
        e >>= 1;
    }
    return r;
}

static uint32_t primitive_root(uint32_t p) {
    uint32_t f[16], nf = 0, n = p - 1;
    for (uint32_t q = 2; (uint64_t)q * q <= n; q++)
        if (n % q == 0) {
            f[nf++] = q;
            while (n % q == 0) n /= q;
        }
    if (n > 1) f[nf++] = n;
    for (uint32_t g = 2;; g++) {
        int ok = 1;
        for (uint32_t i = 0; i < nf && ok; i++)
            if (powmod(g, (p - 1) / f[i], p) == 1) ok = 0;
        if (ok) return g;
    }
}

static void periods(uint32_t p, uint32_t g, double *eta0, double *eta1) {
    // Walk only half of each coset: -1 is a cube, and cos is even.
    uint32_t h = (uint32_t)powmod(g, 3, p);
    uint64_t hp = ((uint64_t)h << 32) / p;
    uint64_t M = UINT64_MAX / p;
    uint32_t t0 = 1, t1 = g % p;
    uint64_t n = (p - 1) / 6;
    double s0 = 0, s1 = 0;
    for (uint64_t j = 0; j < n; j++) {
        s0 += cos_phase((uint64_t)t0 * M);
        s1 += cos_phase((uint64_t)t1 * M);
        uint64_t q0 = (hp * t0) >> 32, q1 = (hp * t1) >> 32;
        uint32_t r0 = (uint32_t)((uint64_t)h * t0 - q0 * p);
        uint32_t r1 = (uint32_t)((uint64_t)h * t1 - q1 * p);
        t0 = r0 >= p ? r0 - p : r0;
        t1 = r1 >= p ? r1 - p : r1;
    }
    *eta0 = 2 * s0;
    *eta1 = 2 * s1;
}

int main(int argc, char **argv) {
    if (argc != 4) {
        fprintf(stderr, "usage: %s PMIN PMAX OUT\n", argv[0]);
        return 2;
    }
    uint32_t pmin = (uint32_t)strtoul(argv[1], 0, 10);
    uint32_t pmax = (uint32_t)strtoul(argv[2], 0, 10);
    if (pmin < 7) pmin = 7;
    for (uint32_t i = 0; i < TSIZE; i++) {
        COS_T[i] = cos(TWO_PI * i / TSIZE);
        SIN_T[i] = sin(TWO_PI * i / TSIZE);
    }
    uint8_t *comp = calloc((size_t)pmax + 1, 1);
    for (uint64_t i = 2; i * i <= pmax; i++)
        if (!comp[i])
            for (uint64_t j = i * i; j <= pmax; j += i) comp[j] = 1;
    size_t cnt = 0;
    for (uint32_t n = pmin; n <= pmax && n >= pmin; n++)
        if (!comp[n] && n % 3 == 1) cnt++;
    rec_t *r = malloc(cnt * sizeof(rec_t));
    size_t k = 0;
    for (uint32_t n = pmin; n <= pmax && n >= pmin; n++)
        if (!comp[n] && n % 3 == 1) r[k++].p = n;
    free(comp);
    double t0 = omp_get_wtime();
#pragma omp parallel for schedule(dynamic, 64)
    for (long long i = (long long)cnt - 1; i >= 0; i--) {
        r[i].g = primitive_root(r[i].p);
        periods(r[i].p, r[i].g, &r[i].eta0, &r[i].eta1);
    }
    FILE *f = fopen(argv[3], "wb");
    if (!f) return 1;
    fwrite(r, sizeof(rec_t), cnt, f);
    fclose(f);
    printf("primes=%zu seconds=%.1f\n", cnt, omp_get_wtime() - t0);
    return 0;
}
