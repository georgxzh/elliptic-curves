// Optional AVX-512 implementation of the SAME exact paired-coset sums.
// Each lane walks an independent subsequence and has its own histogram.
#ifdef CM_VECTOR
#include <immintrin.h>
static void sum_S_cm_vector(uint32_t p, uint32_t K, int64_t *S) {
    if (K%2 || p<=K) { sum_S_cm(p,K,S); return; }
    uint32_t g=sextic_root(p), h=sextic_pow(g,6,p), start=1;
    uint32_t h8=sextic_pow(h,8,p), width=K/2;
    uint64_t hp8=((uint64_t)h8<<32)/p, kp=((uint64_t)K<<32)/p;
    int64_t traces[6], hist[8*MAXK]={0};
    cm_traces(p,g,traces);
    int parity=p%12==1?1:-1;
    uint32_t classes=parity==1?6:3, length=(p-1)/(2*classes);
    __m512i vp=_mm512_set1_epi64(p), vh=_mm512_set1_epi64(h8);
    __m512i vr=_mm512_set1_epi64(hp8), vk=_mm512_set1_epi64(K);
    __m512i vkp=_mm512_set1_epi64(kp), last=_mm512_set1_epi64(K-1);
    __m512i offsets=_mm512_set_epi64(7*width,6*width,5*width,4*width,3*width,2*width,width,0);
    uint64_t starts[8];
    for (uint32_t i=0;i<classes;i++) {
        starts[0]=start;
        for (unsigned j=1;j<8;j++) starts[j]=starts[j-1]*h%p;
        __m512i t=_mm512_loadu_si512(starts), value=_mm512_set1_epi64(traces[i]);
        for (uint32_t j=0;j<length/8;j++) {
            __m512i q=_mm512_srli_epi64(_mm512_mul_epu32(vkp,t),32);
            __m512i r=_mm512_sub_epi64(_mm512_mul_epu32(vk,t),_mm512_mul_epu32(q,vp));
            q=_mm512_mask_add_epi64(q,_mm512_cmp_epu64_mask(r,vp,_MM_CMPINT_NLT),q,_mm512_set1_epi64(1));
            // p>K, hence p does not divide K*t: this q is floor((K*t-1)/p).
            __m512i mirror=_mm512_sub_epi64(last,q);
            __m512i index=_mm512_add_epi64(offsets,_mm512_min_epu64(q,mirror));
            __m512i contribution=value;
            if (parity<0)
                contribution=_mm512_mask_sub_epi64(value,_mm512_cmp_epu64_mask(q,mirror,_MM_CMPINT_GT),_mm512_setzero_si512(),value);
            __m512i old=_mm512_i64gather_epi64(index,hist,8);
            _mm512_i64scatter_epi64(hist,index,_mm512_add_epi64(old,contribution),8);
            __m512i estimate=_mm512_srli_epi64(_mm512_mul_epu32(vr,t),32);
            r=_mm512_sub_epi64(_mm512_mul_epu32(vh,t),_mm512_mul_epu32(estimate,vp));
            t=_mm512_mask_sub_epi64(r,_mm512_cmp_epu64_mask(r,vp,_MM_CMPINT_NLT),r,vp);
        }
        _mm512_storeu_si512(starts,t);
        // The first length%8 lanes are the remaining consecutive coset powers.
        for (uint32_t j=0;j<length%8;j++) {
            uint32_t bin=cm_bin(starts[j],K,p,kp), other=K-1-bin;
            hist[j*width+(bin<other?bin:other)] += bin<other?traces[i]:parity*traces[i];
        }
        start=(uint64_t)start*g%p;
    }
    int64_t bins[MAXK]={0}, prefix=0;
    for (unsigned k=0;k<width;k++) {
        for (unsigned j=0;j<8;j++) bins[k]+=hist[j*width+k];
        bins[K-1-k]=parity*bins[k];
    }
    for (uint32_t k=1;k<K;k++) S[k]=(prefix+=bins[k-1]);
}
#endif
