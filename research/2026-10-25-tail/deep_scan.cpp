#include <algorithm>
#include <cmath>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

using i64=int64_t;
using i128=__int128_t;
using u64=uint64_t;

i64 floor_sqrt(i128 n) {
    if(n<0) throw std::runtime_error("negative square root");
    i64 r=static_cast<i64>(std::sqrt(static_cast<long double>(n)));
    while(i128(r+1)*(r+1)<=n) ++r;
    while(i128(r)*r>n) --r;
    return r;
}
i64 floor_div(i128 n,i64 d) {
    i128 q=n/d,r=n%d;
    if(r<0) --q;
    return static_cast<i64>(q);
}
i64 ceil_div(i128 n,i64 d) { return -floor_div(-n,d); }
u64 cube(u64 n) {return n*n*n;}
struct Moments {
    u64 one=0,two=0,three=0,bearing=0;
    void add(u64 old,u64 increment) {
        const u64 now=old+increment;
        one+=increment; two+=now*now-old*old; three+=cube(now)-cube(old);
        bearing+=old==0;
    }
};
int main(int argc,char**argv) {
    if(argc!=4) throw std::runtime_error("usage: deep_scan T maximum_L output_directory");
    const int t=std::stoi(argv[1]);
    const i64 max_l=std::stoll(argv[2]);
    if(t<1||t>32||max_l<256||max_l>4194304) throw std::runtime_error("input outside checked arithmetic range");
    const std::string out=argv[3]; std::filesystem::create_directories(out);
    const i64 amax=i64(t)*t,bmax=amax*t,width=2*bmax+1,base_x=256*t,max_x=max_l*t;
    const size_t size=static_cast<size_t>((2*amax+1)*width);
    std::vector<uint16_t> counts(size,0),tail_counts(size,0);
    Moments full,tail;
    u64 mixed_base2_tail=0,mixed_base_tail2=0;
    u64 no_base_tail_points=0;
    i64 sing_r=0;
    while(3*(sing_r+1)*(sing_r+1)<=amax && 2*(sing_r+1)*(sing_r+1)*(sing_r+1)<=bmax) ++sing_r;
    const u64 models=size-static_cast<size_t>(1+2*sing_r);
    const std::string suffix="_T"+std::to_string(t)+".csv";
    std::ofstream pts(out+"/tail_points"+suffix);
    pts<<"A,B,x,y_nonnegative\n";
    std::ofstream sum(out+"/deep_summary"+suffix);
    sum<<"T,L,X,models,points,S2,S3,point_bearing,tail_points,tail_S2,tail_S3,tail_bearing,mixed_3_base2_tail,mixed_3_base_tail2,tail_points_on_models_with_no_baseline,mean_N,mean_N3,mean_tail,mean_tail3\n";
    auto record=[&](i64 a,i64 b,i64 x,i64 y) {
        if(a < -amax||a>amax||b < -bmax||b>bmax) throw std::runtime_error("invalid coefficient");
        if(4*a*a*a+27*b*b==0) return;
        if(i128(y)*y!=i128(x)*x*x+i128(a)*x+b) throw std::runtime_error("invalid point");
        const size_t idx=static_cast<size_t>((a+amax)*width+b+bmax);
        const u64 step=y?2:1,old=counts[idx];
        if(old+step>65535) throw std::runtime_error("point count overflow");
        full.add(old,step);
        if(x>base_x) {
            const u64 ot=tail_counts[idx],base=old-ot;
            tail.add(ot,step);
            mixed_base2_tail+=3*base*base*step;
            mixed_base_tail2+=3*base*((ot+step)*(ot+step)-ot*ot);
            if(!base) no_base_tail_points+=step;
            tail_counts[idx]=static_cast<uint16_t>(ot+step);
            pts<<a<<','<<b<<','<<x<<','<<y<<'\n';
        }
        counts[idx]=static_cast<uint16_t>(old+step);
    };
    // There are no points with x < -2T. Handle the short negative range by A.
    for(i64 x=-2*t;x<0;++x) for(i64 a=-amax;a<=amax;++a) {
        const i128 center=i128(x)*x*x+i128(a)*x;
        if(center+bmax<0) continue;
        const i128 low=std::max<i128>(0,center-bmax),high=center+bmax;
        i64 y=floor_sqrt(low); if(i128(y)*y<low) ++y;
        for(;i128(y)*y<=high;++y) record(a,static_cast<i64>(i128(y)*y-center),x,y);
    }
    // At x=0, B=y^2 and every A in range is possible.
    for(i64 y=0;y*y<=bmax;++y) for(i64 a=-amax;a<=amax;++a) record(a,y*y,0,y);
    std::vector<i64> cutoffs={256};
    for(i64 l=1024;l<=max_l;l*=4) cutoffs.push_back(l);
    if(cutoffs.back()!=max_l) cutoffs.push_back(max_l);
    size_t next=0;
    u64 baseline_three=0;
    for(i64 x=1;x<=max_x;++x) {
        const i128 x3=i128(x)*x*x;
        const i128 low=std::max<i128>(0,x3-i128(amax)*x-bmax),high=x3+i128(amax)*x+bmax;
        i64 y=floor_sqrt(low); if(i128(y)*y<low) ++y;
        for(;i128(y)*y<=high;++y) {
            const i128 offset=i128(y)*y-x3;
            const i64 amin=std::max(-amax,ceil_div(offset-bmax,x));
            const i64 ahi=std::min(amax,floor_div(offset+bmax,x));
            for(i64 a=amin;a<=ahi;++a) record(a,static_cast<i64>(offset-i128(a)*x),x,y);
        }
        if(x==cutoffs[next]*t) {
            const i64 l=cutoffs[next];
            if(l==256) baseline_three=full.three;
            if(full.three!=baseline_three+mixed_base2_tail+mixed_base_tail2+tail.three) throw std::runtime_error("moment decomposition failed");
            sum<<std::setprecision(17)<<t<<','<<l<<','<<x<<','<<models<<','<<full.one<<','<<full.two<<','<<full.three<<','<<full.bearing<<','<<tail.one<<','<<tail.two<<','<<tail.three<<','<<tail.bearing<<','<<mixed_base2_tail<<','<<mixed_base_tail2<<','<<no_base_tail_points<<','<<static_cast<long double>(full.one)/models<<','<<static_cast<long double>(full.three)/models<<','<<static_cast<long double>(tail.one)/models<<','<<static_cast<long double>(tail.three)/models<<'\n';
            sum.flush();
            std::cout<<"T="<<t<<" L="<<l<<" X="<<x<<" points="<<full.one<<" M3="<<std::setprecision(10)<<static_cast<long double>(full.three)/models<<" new_points="<<tail.one<<" tail_M3="<<static_cast<long double>(tail.three)/models<<std::endl;
            ++next;
            if(next==cutoffs.size()) break;
        }
    }
    std::ofstream curves(out+"/tail_curves"+suffix);
    curves<<"A,B,N_baseline,N_tail\n";
    std::map<std::pair<int,int>,u64> hist;
    std::vector<std::pair<int,size_t>> leaders;
    for(size_t idx=0;idx<size;++idx) {
        const int n=counts[idx],nt=tail_counts[idx];
        if(!n) continue;
        ++hist[{n,nt}];
        if(nt) {
            const i64 a=static_cast<i64>(idx/width)-amax,b=static_cast<i64>(idx%width)-bmax;
            curves<<a<<','<<b<<','<<n-nt<<','<<nt<<'\n';
        }
        if(leaders.size()<100||n>=leaders.back().first) {
            leaders.push_back({n,idx});
            std::sort(leaders.begin(),leaders.end(),[](auto a,auto b){return a.first!=b.first?a.first>b.first:a.second<b.second;});
            if(leaders.size()>100) leaders.resize(100);
        }
    }
    std::ofstream h(out+"/joint_hist"+suffix);
    h<<"N_full,N_tail,models\n0,0,"<<models-full.bearing<<'\n';
    for(auto [key,n]:hist) h<<key.first<<','<<key.second<<','<<n<<'\n';
    std::ofstream top(out+"/deep_top"+suffix);
    top<<"A,B,N_full,N_tail\n";
    for(auto [n,idx]:leaders) top<<static_cast<i64>(idx/width)-amax<<','<<static_cast<i64>(idx%width)-bmax<<','<<n<<','<<tail_counts[idx]<<'\n';
}
