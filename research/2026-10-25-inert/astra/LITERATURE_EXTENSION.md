# Literature check for the sixth-power-free extension

Checked 2026-10-25. This is a scoped search and comparison, not a certification
of priority. The proof imports descent, the primitive-matrix lemma and a
uniform homogeneous Thue bound; its local calculations are written out.

## Rank-only bounds are already known

[Gross--Silverman, *S-integer points on elliptic curves*, Pacific J. Math.
167 (1995), 263--288](https://msp.org/pjm/1995/167-2/pjm-v167-n2-p05-p.pdf)
give explicit rank-dependent bounds for quasi-minimal curves with integral
j-invariant. Their introduction recalls the earlier qualitative result of
Silverman. This applies to sixth-power-free Mordell coefficients, since j=0.
The general rank-only phenomenon is therefore established prior work.

[Bennett--Ghadermarzi, *Mordell's equation: a classical approach*, LMS J.
Comput. Math. 18 (2015), 633--646, Section 5.2](https://personal.math.ubc.ca/~bennett/BeGh-LMSJCM-2015.pdf)
explicitly states this consequence for sixth-power-free coefficients and
attributes it to Gross--Silverman. Both this section and the introduction of
the original Gross--Silverman paper were inspected. The older results do not
give the specific base-2 estimate from our displayed argument as an immediate
specialization of the statements inspected.

Thus the squarefree corollary must not be presented as the first rank-only
bound. The potential contribution to investigate is the base 2 together with
the explicit local factors in a direct refinement of the quartic-orbit method.
We have not proved that this combination is absent from the literature.

## Direct inputs and nearby minimal-model theory

[Alpoge--Ho, arXiv:1807.03761v3](https://arxiv.org/html/1807.03761v3)
is the principal input: Theorem 2.2 and Section 3.1 supply the rational
orbits, Lemma 3.3 works over a PID (including Z_p), and Theorem 3.5 supplies
the homogeneous Thue bound, also for reducible forms with at least three
distinct geometric roots. These statements were checked directly.
The original Evertse paper has not been separately verified in full text;
the precise version used is the one stated by Alpoge--Ho.

The [earlier literature audit](../LITERATURE.md) discusses Sadek and
Cremona--Fisher--Stoll. Established minimal-model classifications are close
to the local counts here. Actual row lattices carry more marking than an
isomorphism class of models; nevertheless, that distinction by itself is not
evidence of novelty. A comparison with the relevant rational component
configurations and their marking conventions remains necessary.

## Adjacent recent work

[Seokhyun Choi, *Number of integral points on quadratic twists of elliptic
curves*, arXiv:2509.03274v3](https://arxiv.org/abs/2509.03274v3)
states a bound of order 4^rank for sufficiently large positive squarefree
twist parameters in a fixed quadratic-twist family. Only the abstract was
inspected for this comparison. Quadratic twisting a fixed Mordell curve
varies its coefficient by D^3; that differs from varying squarefree B.
No result from that paper is used in our proof or to infer an average theorem.

## Review status and next questions

Two Astra agents supplied the extension and a separate local audit. The root
agent inspected their saved derivations, verified the quoted Alpoge--Ho inputs,
and added an independent finite modular checker. These are AI checks, not
independent human mathematical review or formal proof verification.

Useful next questions are whether the base-2 squarefree consequence is already
recorded, how the exact row-lattice counts compare with Sadek's classifications,
and whether global restrictions improve the product of local maxima. Local
attainment does not imply simultaneous global attainment. Nothing here proves
a bounded average on a thin family or bounds the ranks themselves.
