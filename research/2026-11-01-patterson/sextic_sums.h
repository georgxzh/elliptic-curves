// Exact sextic-coset implementation. See COMPUTATION.md for the proof.
// Requires p > 3 prime, p == 1 mod 3, 2 <= K < MAXK, p < 2^31.
static uint32_t sextic_pow(uint64_t b, uint32_t e, uint32_t p) {
    uint64_t v = 1;
    for (; e; e >>= 1, b = b * b % p)
        if (e & 1) v = v * b % p;
    return (uint32_t)v;
}

static uint32_t sextic_root(uint32_t p) {
    uint32_t factors[16], nf = 0, n = p - 1;
    for (uint32_t q = 2; (uint64_t)q*q <= n; q++) {
        if (n % q) continue;
        factors[nf++] = q;
        do { n /= q; } while (n % q == 0);
    }
    if (n > 1) factors[nf++] = n;
    for (uint32_t g = 2;; g++) {
        uint32_t j = 0;
        while (j < nf && sextic_pow(g, (p-1)/factors[j], p) != 1) j++;
        if (j == nf) return g;
    }
}

// Reciprocal reduction: for t < p < 2^31 and h < p the estimate
// floor(floor(h*2^32/p)*t/2^32) differs from floor(h*t/p) by at most one.
static inline uint32_t sextic_step(uint32_t t, uint32_t h, uint64_t hp, uint32_t p) {
    uint64_t r = (uint64_t)h*t - ((hp*t) >> 32)*p;
    return (uint32_t)(r >= p ? r-p : r);
}

static void sum_S_sextic(uint32_t p, uint32_t K, int8_t *leg, int64_t *S) {
    memset(leg, -1, p);
    leg[0] = 0;
    uint64_t sq = 0, step = 1;
    for (uint32_t x = 1; x <= (p-1)/2; x++) {
        sq += step;
        if (sq >= p) sq -= p;
        step += 2;
        if (step >= p) step -= p;
        leg[sq] = 1;
    }
    uint32_t g = sextic_root(p), b[3] = {1, g, (uint64_t)g*g % p};
    uint32_t h = sextic_pow(g, 3, p), t = 1;
    uint64_t hp = ((uint64_t)h << 32)/p;
    int64_t traces[6] = {-leg[b[0]], -leg[b[1]], -leg[b[2]], 0, 0, 0};
    for (uint32_t j = 0; j < (p-1)/3; j++) {
        for (uint32_t i = 0; i < 3; i++) {
            uint32_t v = t + b[i];
            if (v >= p) v -= p;
            traces[i] -= 3 * leg[v];
        }
        t = sextic_step(t, h, hp, p);
    }
    for (uint32_t i = 0; i < 3; i++) traces[i+3] = -traces[i];
    int64_t bins[MAXK] = {0};
    h = sextic_pow(g, 6, p);
    hp = ((uint64_t)h << 32)/p;
    uint32_t start = 1;
    for (uint32_t i = 0; i < 6; i++) {
        t = start;
        for (uint32_t j = 0; j < (p-1)/6; j++) {
            // First included threshold is k=ceil(K*t/p).
            bins[((uint64_t)K*t-1)/p] += traces[i];
            t = sextic_step(t, h, hp, p);
        }
        start = (uint64_t)start*g % p;
    }
    int64_t prefix = 0;
    for (uint32_t k = 1; k < K; k++) S[k] = (prefix += bins[k-1]);
}
