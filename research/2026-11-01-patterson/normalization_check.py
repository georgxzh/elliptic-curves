#!/usr/bin/env python3
"""Match the smooth prime-weight convention used in the literature audit."""
import json
import math
import sys
import mpmath as mp
import numpy as np
from analyze_law import REC, C


def main(path, output):
    mp.mp.dps = 40
    integral = float(mp.quad(lambda t: mp.exp(4-1/(4*(t-mp.mpf('.5'))*(1-t))),
                             [mp.mpf('.5'),mp.mpf('.75'),1]))
    r = np.fromfile(path,dtype=REC)
    rows = []
    for X in [2000000,4000000,8000000,16000000,30000000]:
        p = r['p'].astype(float)
        use = (p > X/2) & (p < X)
        p = p[use]
        t = p/X
        w = np.exp(4-1/(4*(t-.5)*(1-t)))
        h = (1+3*r['eta0'][use])/np.cbrt(p)
        mean = float(np.dot(w,h)/w.sum())
        err = float(np.sqrt(np.dot(w*w,(h-mean)**2))/w.sum())
        # V(t)=t^(1/6)W(t). Both numerator expressions must agree.
        numerator = float(np.sum((1+3*r['eta0'][use])/(2*np.sqrt(p))*t**(1/6)*w))
        assert abs(numerator-.5*X**(-1/6)*float(np.dot(w,h))) < 1e-8
        coeff = numerator/(X**(5/6)/math.log(X)*integral)
        rows.append(dict(X=X,primes=len(p),weighted_mean=mean,descriptive_stderr=err,
                         measured_coefficient=coeff,paired_coefficient=C/2,
                         literal_printed_coefficient=C))
    result=dict(W='exp(4-1/(4*(t-1/2)*(1-t))) on (1/2,1), zero elsewhere',
                V='t^(1/6) W(t)',integral_W=integral,rows=rows,
                note='Finite data do not prove an asymptotic or refute GRH. No calibrated significance interpretation.')
    with open(output,'w') as fh: json.dump(result,fh,indent=2); fh.write('\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__': main(sys.argv[1],sys.argv[2])
