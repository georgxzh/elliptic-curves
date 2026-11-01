// Integer cross-check of CM sums against character sums at large primes.
#define main production_main
#include "mordell_direct.c"
#undef main
#include <assert.h>

int main(void) {
    const uint32_t limit = 30000000;
    uint8_t *comp = calloc((size_t)limit+1,1);
    assert(comp);
    for (uint32_t q=2; (uint64_t)q*q<=limit; q++)
        if (!comp[q]) for (uint32_t k=q*q; k<=limit; k+=q) comp[k]=1;
    init_cm(limit,comp);
    int8_t *leg = malloc(limit);
    assert(leg);
    int64_t expected[MAXK], actual[MAXK];
    unsigned checks=0, primes=0;
    for (unsigned i=1; i<=32; i++) {
        uint32_t p=(uint64_t)i*limit/32;
        while (comp[p] || p%3!=1) p--;
        uint32_t K = i%3==0 ? 63 : i%3==1 ? 24 : 7;
        sum_S_sextic(p,K,leg,expected);
        sum_S_cm(p,K,actual);
        for (unsigned k=1; k<K; k++) {
            assert(expected[k]==actual[k]); checks++;
        }
        uint64_t kp=((uint64_t)K<<32)/p;
        // Deterministic spread of inputs checks the reciprocal bin operation.
        for (uint64_t j=1; j<=10000; j++) {
            uint32_t t=1+(j*104729)%(p-1);
            assert(cm_bin(t,K,p,kp)==((uint64_t)K*t-1)/p);
        }
        primes++;
    }
    printf("large_primes=%u exact_S_checks=%u reciprocal_checks=%u pmax=%u\n",
           primes,checks,primes*10000,limit);
    free(comp); free(leg); free(cm_a); free(cm_b);
}
