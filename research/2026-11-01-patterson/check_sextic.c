// Compare exact integer outputs, not floating-point aggregates.
#define main production_main
#include "mordell_direct.c"
#undef main
#include <assert.h>
int main(void) {
    const uint32_t limit = 10000;
    int32_t *T = malloc(limit*sizeof(*T));
    int8_t *leg = malloc(limit);
    int64_t old[MAXK], fast[MAXK];
    unsigned long checks = 0;
    for (uint32_t p = 7; p < limit; p += 6) {
        int prime = 1;
        for (uint32_t q = 2; q*q <= p; q++) if (p % q == 0) { prime = 0; break; }
        if (!prime) continue;
        for (uint32_t K = 2; K < MAXK; K += (K < 8 ? 1 : 7)) {
            sum_S(p, K, T, leg, old);
            sum_S_sextic(p, K, leg, fast);
            for (uint32_t k = 1; k < K; k++) { assert(old[k] == fast[k]); checks++; }
        }
    }
    printf("exact sextic/reference checks=%lu\n", checks);
    free(T); free(leg);
}
