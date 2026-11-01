// Classical j=0 CM trace evaluation and paired sextic-coset counting.
// See COMPUTATION.md; independent of the cubic additive Gauss sums.
static int16_t *cm_a, *cm_b;

static void init_cm(uint32_t limit, const uint8_t *composite) {
    cm_a = calloc((size_t)limit+1, sizeof(*cm_a));
    cm_b = calloc((size_t)limit+1, sizeof(*cm_b));
    if (!cm_a || !cm_b) exit(1);
    for (uint32_t a = 1; (uint64_t)a*a < limit; a++) {
        for (uint32_t b = 1;; b++) {
            uint64_t p = (uint64_t)a*a + 3*(uint64_t)b*b;
            if (p > limit) break;
            if (composite[p] || p % 3 != 1) continue;
            cm_a[p] = a % 3 == 1 ? (int)a : -(int)a;
            cm_b[p] = b;
        }
    }
}

static void cm_traces(uint32_t p, uint32_t g, int64_t *traces) {
    int64_t a = cm_a[p], b = cm_b[p];
    if (!b || a*a+3*b*b != p) exit(1);
    uint32_t D = ((p-a)%p) * (uint64_t)sextic_pow(b,p-2,p) % p;
    uint32_t z = (uint64_t)(1+D)*((p+1)/2) % p;
    uint32_t d = sextic_pow(g,(p-1)/6,p);
    if (d != z && d != (p+1-z)%p) exit(1);
    int sign = d == z ? 1 : -1;
    traces[0] = 2*a;
    traces[1] = a+sign*3*b;
    traces[2] = -a+sign*3*b;
    for (int i = 0; i < 3; i++) traces[i+3] = -traces[i];
}

static inline uint32_t cm_bin(uint32_t t, uint32_t K, uint32_t p, uint64_t kp) {
    uint32_t q = (kp*t) >> 32;
    uint64_t r = (uint64_t)K*t-(uint64_t)q*p;
    return q+(r>p)-(r==0); // Exactly floor((K*t-1)/p), including p|K.
}

static void sum_S_cm(uint32_t p, uint32_t K, int64_t *S) {
    uint32_t g = sextic_root(p), h = sextic_pow(g,6,p), start = 1;
    uint64_t hp = ((uint64_t)h << 32)/p, kp = ((uint64_t)K << 32)/p;
    int64_t traces[6], bins[MAXK] = {0};
    cm_traces(p,g,traces);
    int parity = p % 12 == 1 ? 1 : -1;
    uint32_t classes = parity == 1 ? 6 : 3;
    uint32_t length = (p-1)/(2*classes);
    for (uint32_t i = 0; i < classes; i++) {
        uint32_t t = start;
        for (uint32_t j = 0; j < length; j++) {
            bins[cm_bin(t,K,p,kp)] += traces[i];
            bins[cm_bin(p-t,K,p,kp)] += parity*traces[i];
            t = sextic_step(t,h,hp,p);
        }
        start = (uint64_t)start*g % p;
    }
    int64_t prefix = 0;
    for (uint32_t k = 1; k < K; k++) S[k] = (prefix += bins[k-1]);
}
