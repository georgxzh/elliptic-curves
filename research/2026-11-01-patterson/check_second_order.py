#!/usr/bin/env python3
"""Numerical checks of SECOND_ORDER_CUSP.md, independent of prime averages."""
import json
import math
import sys
import mpmath as mp
from analyze_law import C
from check_theory import coefficients


def main(output):
    mp.mp.dps=60
    alpha=mp.mpf(1)/6
    zeta2=mp.zeta(2); zp=mp.diff(mp.zeta,2); R=mp.sqrt(3)/2
    CC=(2*mp.pi)**(mp.mpf(2)/3)/(3*mp.gamma(mp.mpf(2)/3))
    base=10*mp.euler-8*zp/zeta2
    eta1=base-R*mp.log(3)/(1+R)+mp.digamma(alpha)-mp.pi/2*mp.tan(mp.pi/12)+mp.mpf(6)/5-mp.log(2*mp.pi)
    eta7=base+R*mp.log(3)/(1-R)+mp.digamma(alpha)+mp.pi/2*mp.cot(mp.pi/12)+mp.mpf(6)/5-mp.log(2*mp.pi)
    d=CC/(12*zeta2)
    K1=(2*mp.pi)**(1-alpha)/mp.pi*d*(1+R)*mp.gamma(alpha)*mp.cos(mp.pi/12)/(1-alpha)
    K7=(2*mp.pi)**(1-alpha)/mp.pi*d*(1-R)*mp.gamma(alpha)*mp.sin(mp.pi/12)/(1-alpha)
    kb=CC/(2*zeta2)
    lb=CC/zeta2*(5*mp.euler-3-4*zp/zeta2)
    kc=R*kb; lc=R*lb-R*mp.log(3)*kb
    # Independently expand the Euler factors near the double pole.
    def regular_b(s):
        return 2*CC*((s-alpha)*mp.zeta(6*s))*((s-alpha)*mp.zeta(4*s+mp.mpf(1)/3))/mp.zeta(8*s+mp.mpf(2)/3)
    eps=mp.mpf('1e-15')
    numerical_d=(regular_b(alpha+eps)+regular_b(alpha-eps))/2
    numerical_e=(regular_b(alpha+eps)-regular_b(alpha-eps))/(2*eps)
    assert abs(numerical_d-d)<mp.mpf('1e-25')
    assert abs(numerical_e-(kb+alpha*lb))<mp.mpf('1e-25')
    cutoff=10**18
    b,c=coefficients(cutoff)
    summatory=[]
    for power in range(4,19,2):
        x=10**power
        for name,seq,k,l in [('b',b,float(kb),float(lb)),('c',c,float(kc),float(lc))]:
            actual=math.fsum(v for a,v in seq.items() if a<=x)
            model=x**(1/6)*(k*math.log(x)+l)
            summatory.append(dict(sequence=name,x=x,actual=actual,two_term=model,
                                  error=actual-model,error_over_scale=(actual-model)/(x**(2/21)*math.log(x))))
    tail=2*C*(1+2/math.sqrt(3))*cutoff**(-5/6)*((1+math.log(cutoff)/4)/(5/6)+.25/(5/6)**2)
    profiles=[]
    for power in range(2,13):
        den=10**power; u=1/den
        # Exact integer argument reduction for these rational u, before floats.
        sinb=math.fsum(v/a*math.sin(2*math.pi*(a%den)/den) for a,v in b.items())
        sinc=math.fsum(v/a*math.sin(2*math.pi*(a%den)/den) for a,v in c.items())
        cosb=math.fsum(v/a*2*math.sin(math.pi*(a%den)/den)**2 for a,v in b.items())
        cosc=math.fsum(v/a*2*math.sin(math.pi*(a%den)/den)**2 for a,v in c.items())
        for r,value,K,eta,err in [(1,-(sinb+sinc)/math.pi,float(K1),float(eta1),tail/math.pi),
                                 (7,-(cosb-cosc)/math.pi,float(K7),float(eta7),2*tail/math.pi)]:
            scale=K*u**(5/6)
            observed=value/(-scale)-math.log(1/u)
            profiles.append(dict(residue=r,u=u,profile=value,two_term=-scale*(math.log(1/u)+eta),
                                 observed_secondary=observed,predicted_secondary=eta,
                                 secondary_error=observed-eta,secondary_truncation_bound=err/scale))
    result=dict(eta1=str(eta1),eta7=str(eta7),K1=str(K1),K7=str(K7),
                kb=str(kb),lb=str(lb),kc=str(kc),lc=str(lc),
                double_pole_and_simple_pole_checks=True,cutoff=cutoff,
                summatory=summatory,profiles=profiles,
                note='Numerical checks, not interval arithmetic. Tail bounds exclude roundoff. The theorem does not identify prime averages.')
    with open(output,'w') as f: json.dump(result,f,indent=2); f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('summatory','profiles')},indent=2))
    print('last profile checks',profiles[-2:])


if __name__=='__main__': main(sys.argv[1] if len(sys.argv)>1 else 'results/second_order_checks.json')
