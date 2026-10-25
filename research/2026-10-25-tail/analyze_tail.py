"""Exact verification, tail moment decomposition, and integral tripling runs."""
from __future__ import annotations

import bisect
import csv
import gzip
import hashlib
import json
import math
import os
import random
import shutil
from collections import Counter
from fractions import Fraction
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/elliptic-tail-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp

ROOT=Path(__file__).resolve().parent
DATA=ROOT/"data"
OLD=ROOT.parent/"2026-10-25"/"data"
SCALES=(4,8,16,32)
LEVELS=(256,1024,4096,16384,65536,262144,1048576,4194304)
MASK16=(1<<16)-1


def data_open(path):
    if path.exists():
        return path.open(newline="")
    return gzip.open(str(path)+".gz","rt",newline="")


def rows(path):
    with data_open(path) as f:
        return list(csv.DictReader(f))


def add(p,q,a):
    if p is None: return q
    if q is None: return p
    x,y=p; u,v=q
    if x==u and y==-v: return None
    slope=Fraction(3*x*x+a,2*y) if p==q else Fraction(v-y,u-x)
    xr=slope*slope-x-u
    return xr,-y+slope*(x-xr)


def triple(p,a):
    return add(add(p,p,a),p,a)


def old_moments(t):
    h=rows(OLD/f"hist_T{t}_L256.csv")
    return [sum(int(r['models'])*int(r['N'])**k for r in h) for k in (1,2,3)]


def direct_slices(t,xs):
    amax,bmax=t*t,t**3
    found=set()
    for x in sorted(xs):
        for a in range(-amax,amax+1):
            center=x**3+a*x
            low=max(0,center-bmax); high=center+bmax
            if high<0: continue
            y=math.isqrt(low)
            if y*y<low: y+=1
            while y*y<=high:
                b=y*y-center
                if 4*a**3+27*b*b:
                    found.add((a,b,x,y))
                y+=1
    return found


def analyze_scale(t):
    summary=rows(DATA/f"deep_summary_T{t}.csv")
    baseline=old_moments(t)
    assert [int(summary[0][k]) for k in ('points','S2','S3')]==baseline
    assert [int(r['L']) for r in summary]==list(LEVELS)
    last=summary[-1]; models=int(last['models']); width=2*t**3+1
    states={}
    with data_open(DATA/f"tail_curves_T{t}.csv") as f:
        for a,b,nb,nt in list_reader(f):
            idx=(a+t*t)*width+b+t**3
            assert idx not in states and nt>0 and nt%2==0
            states[idx]=nb | (nt<<128)
    # Baseline count in low 16 bits, seven bin counts in the next 112 bits,
    # expected tail count in bits 128..143, and last x above bit 143.
    rng=random.Random(20261025+t)
    xs={256*t+1}
    for l in LEVELS:
        for offset in (-1,0,1):
            x=l*t+offset
            if 256*t<x<=LEVELS[-1]*t: xs.add(x)
    xs.update(rng.randint(256*t+1,LEVELS[-1]*t) for _ in range(64))
    # Include known-hit slices as well as uniformly chosen slices.
    anchors=[]
    with data_open(DATA/f"tail_points_T{t}.csv") as f:
        for i,row in enumerate(list_reader(f)):
            if i<12 or i%100003==0: anchors.append(row[2])
    for x in anchors:
        xs.update(z for z in (x-1,x,x+1) if 256*t<z<=LEVELS[-1]*t)
    observed_slices=set(); dense_t4=set()
    row_count=0; last_global_x=0; match_counters={l:[0,0,0] for l in (256,65536,1048576)}
    bin_ends=[l*t for l in LEVELS[1:]]
    max_point=None
    with data_open(DATA/f"tail_points_T{t}.csv") as f:
        for a,b,x,y in list_reader(f):
            assert -t*t<=a<=t*t and -t**3<=b<=t**3 and 256*t<x<=LEVELS[-1]*t
            assert y>0 and y*y==x**3+a*x+b and 4*a**3+27*b*b
            assert x>=last_global_x
            last_global_x=x
            idx=(a+t*t)*width+b+t**3
            state=states[idx]
            assert x>(state>>144), 'duplicate or unsorted point on a model'
            j=bisect.bisect_left(bin_ends,x)
            assert ((state>>(16*(j+1)))&MASK16)<65533
            state=(state&((1<<144)-1))+(2<<(16*(j+1)))
            states[idx]=state | (x<<144)
            if x in xs: observed_slices.add((a,b,x,y))
            if t==4 and x<=65536: dense_t4.add((a,b,x,y))
            square=b>0 and math.isqrt(b)**2==b
            marked_tripling=bool(square and a and x*a**4==8*b*(a**3+8*b*b))
            for l,counts in match_counters.items():
                if x>l*t:
                    counts[0]+=1; counts[1]+=square; counts[2]+=marked_tripling
            max_point=(a,b,x,y)
            row_count+=1
    expected=direct_slices(t,xs)
    assert expected==observed_slices, (t,expected-observed_slices,observed_slices-expected)
    if t==4:
        assert direct_slices(t,range(1025,65537))==dense_t4

    sums=[[0]*7 for _ in LEVELS]
    tail_hist=Counter(); baseline_probe_models=[]
    for idx,state in states.items():
        nb=state&MASK16
        bins=[(state>>(16*j))&MASK16 for j in range(1,8)]
        nt=sum(bins)
        assert nt==((state>>128)&MASK16)
        tail_hist[nb+nt,nt]+=1
        prefix=0
        for j,acc in enumerate(sums):
            r=nt-prefix; c=nb+prefix
            acc[0]+=r; acc[1]+=r*r; acc[2]+=r**3
            acc[3]+=3*c*c*r; acc[4]+=3*c*r*r
            acc[5]+=r>0
            acc[6]+=r if c==0 else 0
            if j<7: prefix+=bins[j]
        if len(baseline_probe_models)<20: baseline_probe_models.append((idx,nb))
    for idx,nb in baseline_probe_models:
        a=idx//width-t*t; b=idx%width-t**3
        points=direct_one_curve(a,b,256*t)
        assert sum(2 if y else 1 for x,y in points)==nb

    hist=rows(DATA/f"joint_hist_T{t}.csv")
    assert sum(int(r['models']) for r in hist)==models
    assert {(int(r['N_full']),int(r['N_tail'])):int(r['models']) for r in hist if int(r['N_tail'])}==dict(tail_hist)
    for key,power in (('points',1),('S2',2),('S3',3)):
        assert sum(int(r['models'])*int(r['N_full'])**power for r in hist)==int(last[key])
    r1,r2,r3,c1,c2,support,no_base=sums[0]
    assert [r1,r2,r3,support,no_base]==[int(last[k]) for k in ('tail_points','tail_S2','tail_S3','tail_bearing','tail_points_on_models_with_no_baseline')]
    assert c1==int(last['mixed_3_base2_tail']) and c2==int(last['mixed_3_base_tail2'])
    assert baseline[0]+r1==int(last['points'])
    assert baseline[1]+sum(int(r['models'])*(int(r['N_full'])**2-(int(r['N_full'])-int(r['N_tail']))**2) for r in hist)==int(last['S2'])
    assert baseline[2]+c1+c2+r3==int(last['S3'])
    assert 2*row_count==r1
    # Same first tail boundary, but use observed marginal moments to test independence.
    independence_increment=3*baseline[1]*r1/models**2+3*baseline[0]*r2/models**2+r3/models
    actual_increment=(c1+c2+r3)/models
    estimates=[]
    for l,acc in zip(LEVELS,sums):
        estimates.append(dict(L=l,upper_X=int(last['X']),tail_points=acc[0],mean_tail=acc[0]/models,
                              mean_tail3=acc[2]/models,tail_bearing=acc[5],
                              mean_mixed_3_C2R=acc[3]/models,mean_mixed_3_CR2=acc[4]/models,
                              no_C_tail_points=acc[6]))
    result=dict(T=t,models=models,baseline_M3=baseline[2]/models,deep_M3=int(last['S3'])/models,
                deep_points=int(last['points']),upper_X=int(last['X']),tail_nonnegative_rows=row_count,
                mean_tail=r1/models,mean_tail3=r3/models,mean_M3_increase=actual_increment,
                mixed_fraction_of_M3_increase=(c1+c2)/(c1+c2+r3),
                independence_predicted_M3_increase=independence_increment,
                actual_over_independence_prediction=actual_increment/independence_increment,
                tail_point_share_with_no_baseline=no_base/r1,
                exact_coordinate_slices_checked=len(xs),baseline_models_independently_checked=len(baseline_probe_models),
                full_independent_T4_range=[1025,65536] if t==4 else None,
                marked_tripling_diagnostics={str(k):v for k,v in match_counters.items()},
                largest_searched_hit=max_point,finite_tail_estimates=estimates)
    print(f"Verified T={t}: {row_count:,} tail rows; M3={result['deep_M3']:.9f}",flush=True)
    return result


def list_reader(f):
    reader=csv.reader(f); next(reader)
    for row in reader: yield tuple(map(int,row))


def direct_one_curve(a,b,bound):
    result=[]
    for x in range(-bound,bound+1):
        v=x**3+a*x+b
        if v>=0:
            y=math.isqrt(v)
            if y*y==v: result.append((x,y))
    return result


def tripling_family():
    results=[]
    with (DATA/'constructed_tripling.csv').open('w',newline='') as f:
        out=csv.writer(f);out.writerow(['T','A','B','b','x_3P','y_3P','beyond_direct_search'])
        for t in SCALES:
            admissible=missed=0;largest=None
            for b in range(1,math.isqrt(t**3)+1):
                for a in range(-t*t,t*t+1):
                    if not a or 4*a**3+27*b**4==0: continue
                    xnum=8*b*b*(a**3+8*b**4)
                    integral=xnum%a**4==0
                    assert integral==((8*b**3)%(a*a)==0)
                    if not integral: continue
                    x=xnum//a**4
                    y=Fraction(b*(3*a**6+96*a**3*b**4+512*b**8),a**6)
                    assert y.denominator==1
                    y=int(y)
                    assert y*y==x**3+a*x+b*b
                    assert triple((Fraction(0),Fraction(b)),a)==(x,y)
                    beyond=abs(x)>LEVELS[-1]*t
                    out.writerow([t,a,b*b,b,x,y,int(beyond)])
                    admissible+=1;missed+=beyond
                    if largest is None or abs(x)>abs(largest['x']):
                        largest=dict(A=a,B=b*b,b=b,x=x,y=y)
            results.append(dict(T=t,admissible_models=admissible,constructed_models_beyond_direct_cutoff=missed,
                                additional_signed_points_beyond_direct_cutoff=2*missed,largest_point=largest))
    # A symbolic identity checks the formulas independently of numerical examples.
    a,b=sp.symbols('A b',nonzero=True)
    x=8*b*b*(a**3+8*b**4)/a**4
    y=b*(3*a**6+96*a**3*b**4+512*b**8)/a**6
    assert sp.cancel(y*y-x**3-a*x-b*b)==0
    return results


def triple_old_catalog():
    known={}
    for source in (OLD/'points_T8.csv',DATA/'tail_points_T8.csv'):
        with data_open(source) as f:
            for a,b,x,y in list_reader(f): known[a,b,x]=y
    generated={};tested=finite=0
    with data_open(OLD/'points_T8.csv') as f:
        for a,b,x,y in list_reader(f):
            tested+=1
            fval=y*y
            psi=3*x**4+6*a*x*x+12*b*x-a*a
            if not psi: continue
            finite+=1
            q=x**6+5*a*x**4+20*b*x**3-5*a*a*x*x-4*a*b*x-8*b*b-a**3
            num=x*psi*psi-8*fval*q;den=psi*psi
            if num%den: continue
            xr=num//den
            v=xr**3+a*xr+b;assert v>=0
            yr=math.isqrt(v);assert yr*yr==v
            actual=triple((Fraction(x),Fraction(y)),a)
            assert actual is not None and actual[0]==xr and abs(actual[1])==yr
            if abs(xr)<=33554432:
                assert known[a,b,xr]==yr
            generated[a,b,xr]=yr
    extras=[(*key,y) for key,y in generated.items() if abs(key[2])>33554432]
    extras.sort(key=lambda r:abs(r[2]),reverse=True)
    with (DATA/'tripled_T8_catalog_beyond_search.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['A','B','x','y_nonnegative']);writer.writerows(extras)
    return dict(nonnegative_input_points=tested,finite_triples_tested=finite,
                distinct_integral_triples=len(generated),distinct_points_beyond_direct_search=len(extras),
                largest_examples=extras[:10])


def make_plot(scales):
    fig,axes=plt.subplots(1,3,figsize=(14,4.4))
    for t in SCALES:
        ss=rows(DATA/f'deep_summary_T{t}.csv')
        axes[0].plot([int(r['L']) for r in ss],[float(r['mean_N3']) for r in ss],'o-',label=f'T={t}')
    axes[0].set_xscale('log',base=4)
    axes[0].set(title='Third moments continue rising',xlabel='Coordinate multiplier L',ylabel='Mean N³')
    axes[0].legend()
    positions=list(range(len(scales)))
    tail=[s['mean_tail3'] for s in scales]
    cross=[s['mean_M3_increase']-s['mean_tail3'] for s in scales]
    axes[1].bar(positions,tail,label='New points alone')
    axes[1].bar(positions,cross,bottom=tail,label='Mixed terms with baseline')
    axes[1].set_xticks(positions,[s['T'] for s in scales])
    axes[1].set(title='Mixed terms dominate the increase',xlabel='Coefficient scale T',ylabel='Increase in mean N³ beyond L=256')
    axes[1].legend(fontsize=8)
    for s in scales:
        rr=s['finite_tail_estimates'][:-1]
        axes[2].loglog([r['L'] for r in rr],[r['mean_tail3'] for r in rr],'o-',label=f"T={s['T']}")
    axes[2].set(title='Third moment of the finite tail',xlabel='Lower coordinate multiplier L',ylabel='Mean number of tail points cubed')
    axes[2].legend()
    for ax in axes:ax.grid(alpha=.2)
    fig.suptitle('Upper search bound is finite: L = 4,194,304; unseen points still exist',fontsize=12)
    fig.tight_layout();fig.savefig(ROOT/'tail_results.png',dpi=170);plt.close(fig)


def compress_large_artifacts():
    for path in DATA.glob('*.csv'):
        if path.stat().st_size>500000:
            with path.open('rb') as src,gzip.GzipFile(filename=str(path)+'.gz',mode='wb',mtime=0) as dst:
                shutil.copyfileobj(src,dst)
            path.unlink()


def main():
    results=[analyze_scale(t) for t in SCALES]
    family=tripling_family();catalog=triple_old_catalog()
    output=dict(scales=results,tripling_family=family,tripled_T8_catalog=catalog,
                scope='Exact finite-coordinate censuses and exact constructed points; no completeness claim beyond cutoffs.')
    (ROOT/'analysis.json').write_text(json.dumps(output,indent=2)+'\n')
    make_plot(results)
    compress_large_artifacts()
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(DATA.iterdir()) if p.is_file()}
    (ROOT/'data_sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps({'tripling_family':family,'tripled_T8_catalog':catalog},indent=2),flush=True)


if __name__=='__main__': main()
