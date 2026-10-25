#include <algorithm>
#include <cmath>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

using i64 = int64_t;
i64 isqrt(i64 n) {
    if (n < 0) throw std::runtime_error("negative square root");
    i64 r = static_cast<i64>(std::sqrt((long double)n));
    while ((__int128)(r+1)*(r+1) <= n) ++r;
    while ((__int128)r*r > n) --r;
    return r;
}
int mobius(int n) {
    int m = 1;
    for (int p=2; p*p<=n; ++p) if (n%p==0) {
        n/=p; m=-m;
        if (n%p==0) return 0;
        while (n%p==0) n/=p;
    }
    return n>1 ? -m : m;
}
i64 nonsingular_models(i64 a, i64 b) {
    i64 r=0;
    while (3*(r+1)*(r+1)<=a && 2*(r+1)*(r+1)*(r+1)<=b) ++r;
    return (2*a+1)*(2*b+1)-(1+2*r);
}
bool minimal(i64 a, i64 b, int t) {
    // Testing composite integers as well as primes is harmless and keeps this exact.
    for (i64 p=2; p*p<=t; ++p) {
        i64 p4=p*p*p*p, p6=p4*p*p;
        if (a%p4==0 && b%p6==0) return false;
    }
    return true;
}
int main(int argc, char** argv) {
    if (argc!=3) throw std::runtime_error("usage: scan T output_directory");
    int t=std::stoi(argv[1]);
    if (t<1 || t>32) throw std::runtime_error("supported exhaustive range: 1 <= T <= 32");
    std::string out=argv[2]; std::filesystem::create_directories(out);
    i64 amax=(i64)t*t, bmax=amax*t, width=2*bmax+1;
    size_t size=(2*amax+1)*width;
    std::vector<uint16_t> counts(size, 0);
    std::vector<uint8_t> torsion(size, 0);
    i64 total=nonsingular_models(amax,bmax), mintotal=0;
    for (i64 n=1; n*n<=t; ++n) {
        i64 n4=n*n*n*n, n6=n4*n*n;
        mintotal+=mobius(static_cast<int>(n))*nonsingular_models(amax/n4,bmax/n6);
    }
    std::ofstream points;
    if(t==8) {
        points.open(out+"/points_T8.csv"); points << "A,B,x,y_nonnegative\n";
    }
    std::ofstream summary(out+"/summary_T"+std::to_string(t)+".csv");
    summary << "T,L,models,minimal_models,point_bearing,multi_x,points,ordered_distinct_x_pairs,mean_N,mean_N2,mean_N_log2_5,mean_N2_49,mean_N2_75,mean_N3,minimal_mean_N,minimal_mean_N3,new_points_since_previous_cutoff\n";
    const double exponents[]={1,2,std::log2(5.),2.49,2.75,3};
    int previous=0; i64 previous_points=0;
    for (int l : {4,16,64,256}) {
        int bound=l*t;
        for (i64 a=-amax; a<=amax; ++a) {
            // No points exist at x < -2T: x^3 + A*x + B < 0 there.
            for (i64 x=-2*t; x<=bound; ++x) {
                if (previous && std::abs(x)<=previous) continue;
                i64 center=x*x*x+a*x, high=center+bmax;
                if(high<0) continue;
                i64 low=std::max<i64>(0,center-bmax);
                i64 ylo=isqrt(low); if(ylo*ylo<low) ++ylo;
                i64 yhi=isqrt(high);
                for(i64 y=ylo; y<=yhi; ++y) {
                    i64 b=y*y-center;
                    size_t idx=(a+amax)*width+b+bmax;
                    if(counts[idx]>65532) throw std::runtime_error("count overflow");
                    counts[idx]=static_cast<uint16_t>(counts[idx]+(y ? 2 : 1));
                    if(!y) ++torsion[idx];
                    if(t==8 && 4*a*a*a+27*b*b!=0) points << a << ',' << b << ',' << x << ',' << y << '\n';
                }
            }
        }
        long double sums[6]={}, minsums[6]={};
        i64 bearing=0, multi=0, npoints=0, pairs=0;
        std::map<int,i64> histogram, minhist;
        // Fractions of the moment lying above each threshold of this PARTIAL prime count.
        long double local_moment[4][3]={};
        std::vector<std::pair<int,size_t>> leaders;
        for(size_t idx=0; idx<size; ++idx) {
            int n=counts[idx]; if(!n) continue;
            i64 a=(i64)(idx/width)-amax, b=(i64)(idx%width)-bmax;
            i64 disc=-16*(4*a*a*a+27*b*b);
            if(!disc) continue;
            bool is_minimal=minimal(a,b,t);
            ++histogram[n]; if(is_minimal) ++minhist[n];
            ++bearing; npoints+=n;
            int nx=(n+torsion[idx])/2;
            if(nx>=2) ++multi;
            pairs+=(i64)nx*(nx-1);
            for(int j=0;j<6;++j) {
                long double value=std::pow((long double)n,exponents[j]);
                sums[j]+=value; if(is_minimal) minsums[j]+=value;
            }
            if(l==256) {
                int omega=0;
                for(i64 p : {5,7,11,13,17,19,23,29,31}) omega+=disc%(p*p)==0;
                for(int k=0;k<4;++k) if(omega>=k) {
                    local_moment[k][0]+=n;
                    local_moment[k][1]+=(long double)n*n;
                    local_moment[k][2]+=(long double)n*n*n;
                }
            }
            if(leaders.size()<100 || n>=leaders.back().first) {
                leaders.push_back({n,idx});
                std::sort(leaders.begin(),leaders.end(),[](auto x, auto y) {return x.first!=y.first ? x.first>y.first : x.second<y.second;});
                if(leaders.size()>100) leaders.resize(100);
            }
        }
        summary<<std::setprecision(16)<<t<<','<<l<<','<<total<<','<<mintotal<<','<<bearing<<','<<multi<<','<<npoints<<','<<pairs;
        for(auto s:sums) summary<<','<<s/total;
        summary<<','<<minsums[0]/mintotal<<','<<minsums[5]/mintotal<<','<<npoints-previous_points<<'\n';
        summary.flush();
        std::ofstream hist(out+"/hist_T"+std::to_string(t)+"_L"+std::to_string(l)+".csv");
        hist<<"N,models,minimal_models\n0,"<<total-bearing<<','<<mintotal-std::accumulate(minhist.begin(),minhist.end(),(i64)0,[](i64 s,auto kv){return s+kv.second;})<<'\n';
        for(auto [n,c]:histogram) hist<<n<<','<<c<<','<<minhist[n]<<'\n';
        std::ofstream top(out+"/top_T"+std::to_string(t)+"_L"+std::to_string(l)+".csv");
        top<<"A,B,N,torsion_points,short_scaling_minimal\n";
        for(auto [n,idx]:leaders) {
            i64 a=(i64)(idx/width)-amax,b=(i64)(idx%width)-bmax;
            top<<a<<','<<b<<','<<n<<','<<(int)torsion[idx]<<','<<minimal(a,b,t)<<'\n';
        }
        if(l==256) {
            std::ofstream local(out+"/local_T"+std::to_string(t)+".csv");
            local<<"at_least_k_prime_squares_among_5_through_31,share_M1,share_M2,share_M3\n";
            for(int k=0;k<4;++k) local<<std::setprecision(16)<<k<<','<<local_moment[k][0]/sums[0]<<','<<local_moment[k][1]/sums[1]<<','<<local_moment[k][2]/sums[5]<<'\n';
        }
        std::cout<<std::setprecision(8)<<"T="<<t<<" L="<<l<<" curves="<<total<<" points="<<npoints<<" M1="<<sums[0]/total<<" M2="<<sums[1]/total<<" M3="<<sums[5]/total<<" max="<<leaders.front().first<<std::endl;
        previous=bound; previous_points=npoints;
    }
}
