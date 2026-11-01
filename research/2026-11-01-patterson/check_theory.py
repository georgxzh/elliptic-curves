#!/usr/bin/env python3
"""Independent finite-field checks and coefficient/profile checks.

No prime-average conjecture is used as an oracle. Cusp output compares a
truncation with its proved leading asymptotic, not with a claimed finite-u
identity. Usage: python check_theory.py [output.json]
"""
import cmath
import json
import math
import sys
import numpy as np
from analyze_law import C, candidate


def root(n, k):
    r = int(n**(1/k))
    while (r+1)**k <= n: r += 1
    while r**k > n: r -= 1
    return r


def coefficients(N):
    """Generate b and c by the independent m^6 n^4 representations."""
    limit = root(N, 4)
    sf = [True]*(limit+1)
    for q in range(2, math.isqrt(limit)+1):
        # Removing all square divisors is enough; q need not be prime.
        for k in range(q*q, limit+1, q*q): sf[k] = False
    b, c = {}, {}
    for n in range(1, limit+1):
        if not sf[n]: continue
        weight = 2*C/n**(1/3)
        for m in range(1, root(N//n**4, 6)+1):
            a = m**6*n**4
            assert a not in b
            b[a] = weight
        if n % 3:
            for t, scale in [(3, 3**(-1/3)), (27, 1)]:
                for m in range(1, root(N//(t*n**4), 6)+1):
                    a = t*m**6*n**4
                    assert a not in c
                    c[a] = weight*scale
    return b, c


def finite_checks():
    count, error = 0, 0.
    for p in range(5, 101):
        if any(p % q == 0 for q in range(2, math.isqrt(p)+1)): continue
        leg = [0]+[1 if pow(t, (p-1)//2, p)==1 else -1 for t in range(1,p)]
        e = [cmath.exp(2j*math.pi*t/p) for t in range(p)]
        tau = sum(leg[t]*e[t] for t in range(p))
        mordell = [-sum(leg[(x**3+B)%p] for x in range(p)) for B in range(p)]
        quartic = [-sum(leg[(x**3+A*x)%p] for x in range(p)) for A in range(p)]
        for a in range(1,p):
            G = sum(e[(a*x**3)%p] for x in range(p))
            Q = sum(leg[x]*e[(a*x*x)%p] for x in range(p))
            G4 = sum(e[(a*x**4)%p] for x in range(p))
            G2 = sum(e[(a*x*x)%p] for x in range(p))
            h3 = sum(mordell[B]*e[(-a*B)%p] for B in range(p))
            h4 = sum(quartic[A]*e[(-a*A)%p] for A in range(p))
            error = max(error, abs(h3+leg[-a%p]*tau*G),
                        abs(h4+leg[-a%p]*tau*Q), abs(Q-(G4-G2)))
            count += 3
        if p % 3 == 1:
            alpha, beta = [1., -.7], [.3, .9]
            weight = [sum(alpha[a-1]*math.cos(2*math.pi*a*B/p)+
                          beta[a-1]*math.sin(2*math.pi*a*B/p) for a in (1,2)) for B in range(p)]
            lhs = sum(t*w for t,w in zip(mordell,weight))/p**(5/6)
            selected = alpha if p%12==1 else beta
            rhs = -sum(selected[a-1]*leg[a]*sum(e[(a*x**3)%p] for x in range(p)).real/p**(1/3) for a in (1,2))
            error = max(error, abs(lhs-rhs))
            count += 1
    assert error < 1e-9, error
    return count, error


def main(output):
    checks, error = finite_checks()
    b, c = coefficients(100000)
    for a in range(1,100001):
        value = candidate(a)
        eb = value if math.isqrt(a)**2==a else 0.
        ec = value if a%3==0 and math.isqrt(a//3)**2==a//3 else 0.
        assert abs(b.get(a,0)-eb)<1e-12
        assert abs(c.get(a,0)-ec)<1e-12
    N = 10**18
    b, c = coefficients(N)
    ab, ac = np.array(list(b),float), np.array(list(c),float)
    vb, vc = np.array(list(b.values())), np.array(list(c.values()))
    zeta2 = math.pi**2/6
    d = C/(12*zeta2)
    pref = (2*math.pi)**(5/6)/math.pi * d * 6/5 * math.gamma(1/6)
    K1 = pref*(1+math.sqrt(3)/2)*math.cos(math.pi/12)
    K7 = pref*(1-math.sqrt(3)/2)*math.sin(math.pi/12)
    tail = 2*C*(1+2/math.sqrt(3))*N**(-5/6)*((1+math.log(N)/4)/(5/6)+.25/(5/6)**2)
    rows = []
    for power in range(2,13):
        u = 10.**(-power)
        t = 2*math.pi*u
        F1 = -(np.dot(vb/ab,np.sin(t*ab))+np.dot(vc/ac,np.sin(t*ac)))/math.pi
        # 2*sin(t/2)^2 is stable for small t, unlike 1-cos(t).
        F7 = -(np.dot(vb/ab,2*np.sin(t*ab/2)**2)-np.dot(vc/ac,2*np.sin(t*ac/2)**2))/math.pi
        scale = u**(5/6)*math.log(1/u)
        rows.append(dict(u=u,F1=float(F1),F7=float(F7),
                         ratio1=float(F1/(-K1*scale)),ratio7=float(F7/(-K7*scale))))
    result = dict(finite_field_checks=checks,max_error=error,coefficient_checks=200000,
                  cutoff=N,b_terms=len(b),c_terms=len(c),K1=K1,K7=K7,
                  tail_bound_F1=tail/math.pi,tail_bound_F7=2*tail/math.pi,rows=rows,
                  note='Tail bounds exclude floating-point roundoff. Ratios converge slowly (logarithmic correction).')
    with open(output,'w') as fh: json.dump(result,fh,indent=2); fh.write('\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv)>1 else 'theory_checks.json')
