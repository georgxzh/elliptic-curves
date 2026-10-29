"""Check the cubic-prime chord/lattice bridge and exact rational examples."""

from collections import Counter
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    "sixth_free",HERE.parent/"2026-10-25-inert/astra/verify_sixth_free.py")
prior=importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def main():
    counts=Counter()
    for p in (5,7,11,13,19):
        for B,x,y in prior.points(p,3):
            counts["point_samples"]+=1
            t=y*pow(x,-1,p**3)%p**3 if x%p else 0
            roots={w for w in range(p) if (w**3+B//p**3)%p==0}
            for z in range(t%p,p**3,p):
                value=z**4-6*x*z*z+8*y*z-3*x*x
                derivative=4*(z**3-3*x*z+2*y)
                valuation=prior.old.vp(value,p)
                counts["nonstandard_disk_residues"]+=1
                if valuation not in (2,4): continue
                k=valuation//2
                unit=value//p**(2*k)
                if pow(unit%p,(p-1)//2,p)!=1 or derivative%p**k: continue
                root=next(a for a in range(1,p) if a*a%p==unit%p)
                # q mod p^3 suffices to identify x_R/p modulo p.
                q=p**k*prior.old.lift_sqrt(unit,root,p,3-k)
                for sign in (1,-1):
                    xr=(z*z-x+sign*q)*pow(2,-1,p**3)%p**3
                    assert xr%p==0 and xr//p%p in roots
                    if x%p:
                        assert k==2
                        v=(z-t)//p%p
                        assert xr//p%p==(t*v)%p
                        counts["smooth_source_nonstandard_chords"]+=1
                    else:
                        assert k==1 and len(roots)==3
                        assert xr//p%p!=x//p%p
                        counts["singular_source_nonstandard_chords"]+=1
            # Unit-determinant, integral-slope case, both square-root signs.
            for z in range(p):
                value=z**4-6*x*z*z+8*y*z-3*x*x
                if value%p==0 or pow(value%p,(p-1)//2,p)!=1: continue
                root=next(a for a in range(1,p) if a*a%p==value%p)
                q=prior.old.lift_sqrt(value,root,p,3)
                for sign in (1,-1):
                    xr=(z*z-x+sign*q)*pow(2,-1,p**3)%p**3
                    if x%p:
                        assert xr%p
                    elif xr%p==0:
                        assert xr//p%p==x//p%p
                    counts["unit_determinant_chords"]+=1

            # Primitive first row (1,p^j), j=1,2: determinant is a unit,
            # but the normalized slope has negative valuation. Check both
            # square-root choices before dividing by the denominator.
            for j in (1,2):
                b=p**j
                value=1-6*x*b*b+8*y*b**3-3*x*x*b**4
                D=prior.old.lift_sqrt(value,1,p,2*j+3)
                statuses=[]
                for sign in (1,-1):
                    numerator=1-x*b*b+sign*D
                    valuation=prior.old.vp(numerator,p)-2*j
                    if valuation<0:
                        assert valuation==-2*j
                        statuses.append("nonintegral")
                    else:
                        assert numerator%b**2==0
                        xr=(numerator//b**2)*pow(2,-1,p**3)%p**3
                        if x%p: assert xr%p
                        else: assert xr%p==0 and xr//p%p==x//p%p
                        statuses.append("integral")
                    counts["denominator_chords"]+=1
                assert sorted(statuses)==["integral","nonintegral"]

    # These exact rational matrices exhibit nonstandard stabilizers as well
    # as a standard matrix with a nonzero chord component at a singular P.
    examples=[]
    for x,y,p,matrix in (
        (8,13,7,(13,1,-22,-13)),
        (154,-1911,7,(-13,1,-168,13)),
        (443,9324,11,(259,12,-5580,-259)),
    ):
        assert y*y==x**3-p**3
        a,b,c,d=matrix;D=a*d-b*c
        target=prior.old.transform(prior.old.coeffs(x,y),matrix)
        assert target==prior.old.coeffs(x,y)
        z=F(a,b);q=F(D,b*b)
        xr=(z*z-x+q)/2;yr=z*(xr-x)+y
        assert (xr,yr)==(p,0)
        assert prior.old.transform(prior.old.coeffs(x,y),(1,0,0,1))==prior.old.coeffs(x,y)
        assert prior.old.transform(prior.old.coeffs(x,y),(1,0,0,-1))==prior.old.coeffs(x,-y)
        counts["infinite_slope_signed_matrices"]+=2
        examples.append({"B":-p**3,"P":[x,y],"R":[p,0],
                         "matrix":list(matrix),"determinant":D,
                         "determinant_valuation":prior.old.vp(D,p)})
    assert counts["smooth_source_nonstandard_chords"]
    assert counts["singular_source_nonstandard_chords"]
    return {"counts":dict(counts),"rational_examples":examples,"status":"PASS",
            "scope":"Finite local chord-component checks at valuation three, denominator valuations one/two, and exact rational stabilizers and infinite-slope matrices. Does not replace the general written proof."}


if __name__=="__main__":
    rendered=json.dumps(main(),indent=2)+"\n"
    (HERE/"chord_lattice_results.json").write_text(rendered)
    print(rendered,end="")
