// Compare exact integer outputs, not floating-point aggregates.
#define main production_main
#include "mordell_direct.c"
#undef main
#include <assert.h>
int main(void) {
    const uint32_t limit = 10000;
    uint8_t *comp = calloc(limit+1,1);
    for (uint32_t q = 2; q*q <= limit; q++)
        if (!comp[q]) for (uint32_t k = q*q; k <= limit; k += q) comp[k] = 1;
    init_cm(limit,comp);
    int32_t *T = malloc(limit*sizeof(*T));
    int8_t *leg = malloc(limit);
    int64_t old[MAXK], fast[MAXK], cm[MAXK];
    unsigned long checks = 0;
    for (uint32_t p = 7; p < limit; p += 6) {
        int prime = 1;
        for (uint32_t q = 2; q*q <= p; q++) if (p % q == 0) { prime = 0; break; }
        if (!prime) continue;
        for (uint32_t K = 2; K < MAXK; K += (K < 8 ? 1 : 7)) {
            sum_S(p, K, T, leg, old);
            sum_S_sextic(p, K, leg, fast);
            sum_S_cm(p,K,cm);
            for (uint32_t k = 1; k < K; k++) {
                assert(old[k] == fast[k] && old[k] == cm[k]); checks++;
            }
#ifdef CM_VECTOR
            sum_S_cm_vector(p,K,cm);
            for (uint32_t k=1;k<K;k++) assert(old[k]==cm[k]);
#endif
        }
    }
    printf("exact sextic/CM/reference checks=%lu\n", checks);
    free(T); free(leg); free(comp); free(cm_a); free(cm_b);
}
