// Check lookup-based periods against libm cos at spread-out records.
// Also verifies every record's exact second-moment identity numerically.
#define main production_main
#include "gauss_periods.c"
#undef main
#include <assert.h>

int main(int argc, char **argv) {
    if (argc != 2) return 2;
    FILE *f = fopen(argv[1], "rb");
    assert(f);
    assert(fseek(f, 0, SEEK_END) == 0);
    long bytes = ftell(f);
    assert(bytes > 0 && bytes % sizeof(rec_t) == 0);
    size_t count = bytes/sizeof(rec_t);
    rewind(f);
    rec_t *r = malloc(bytes);
    assert(r && fread(r, sizeof(*r), count, f) == count);
    fclose(f);
    double moment = 0, error = 0, normalized = 0;
    for (size_t i = 0; i < count; i++) {
        assert(r[i].p % 3 == 1 && (!i || r[i].p > r[i-1].p));
        double a = 1+3*r[i].eta0, b = 1+3*r[i].eta1, c = -a-b;
        double delta = fabs((a*a+b*b+c*c)/(6.0*r[i].p)-1);
        if (delta > moment) moment = delta;
    }
    unsigned samples = 16;
    for (unsigned i = 0; i < samples; i++) {
        rec_t v = r[(count-1)*i/(samples-1)];
        uint32_t h = powmod(v.g, 3, v.p), t0 = 1, t1 = v.g;
        double s0 = 0, s1 = 0;
        for (uint32_t j = 0; j < (v.p-1)/6; j++) {
            s0 += cos(TWO_PI*t0/v.p);
            s1 += cos(TWO_PI*t1/v.p);
            t0 = (uint64_t)h*t0 % v.p;
            t1 = (uint64_t)h*t1 % v.p;
        }
        // eta2 is inferred, so also check its accumulated difference.
        double d0 = v.eta0-2*s0, d1 = v.eta1-2*s1;
        double d = 3*fmax(fmax(fabs(d0),fabs(d1)),fabs(d0+d1));
        if (d > error) error = d;
        if (d/cbrt(v.p) > normalized) normalized = d/cbrt(v.p);
    }
    printf("records=%zu libm_samples=%u max_relative_second_moment=%.17g max_G_difference=%.17g max_normalized_difference=%.17g\n",
           count, samples, moment, error, normalized);
    assert(moment < 1e-6 && normalized < 1e-5);
    free(r);
}
