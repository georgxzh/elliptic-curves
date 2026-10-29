# Rational chords control the entire tuple of local lattices

Research proof draft, 2026-10-28. The argument below adds a global
compatibility restriction to the exact Mordell local classification.
It uses the descent and Thue inputs already stated in the earlier notes.
It is not a novelty claim or independent human verification.

## Theorem

Let B be a nonzero sixth-power-free integer, E:y^2=x^3+B, and r=rank E(Q).
At p>3 with v_p(B)=2 or 4 and square unit part, retain the local quotient
G_p=E(Q_p)/E_0(Q_p), of order 3. At p>3 with v_p(B)=3, retain the
nontrivial quotient G_p of order 2 or 4. Let H be the image of E(Q) in
the product of all these quotients. Write H_2,H_3 for its projections
to the order-two-power and order-three parts, and s=dim_F2 H_2,
h=dim_F3 H_3. These quotients and their elementary descriptions are proved
in [the binary component note](GLOBAL_COMPONENT_CODE.md) and
[the ternary component note](GLOBAL_PATTERN_IMAGE.md).

With C=4*7^192*8178*1636 from the sixth-free theorem,

\[
 \#E(\mathbb Z)\le C\,2^r
      \min\left\{\prod_{p>3}\lambda_p(B),\ |H|\right\},
 \qquad |H|=2^s3^h.                                      \tag{1}
\]

Consequently,

\[
                 \#E(\mathbb Z)\le 6C\,12^r.             \tag{2}
\]

If no p>3 has v_p(B) in {2,4}, the bound improves to 2C*4^r.
If no p>3 has v_p(B)=3, it improves to 3C*6^r; the support-pattern
argument gives a slightly better constant in that case. For squarefree B,
all retained quotients are absent and (1) recovers the earlier C*2^r bound.

The component-weight theorem can also be combined with (1): replace its
first alternative by (product lambda_p) W(H_2). Since both are bounds
for the whole point set with the same C, their minimum is valid.

## 1. The rational chord attached to a matrix

Fix an integral base point P=(x,y) and its quartic f_P. Let g be a
primitive integer matrix taking f_P to another integral point quartic
f_Q. Write its first row (a,b), determinant D, and first assume b!=0.
Scaling the whole matrix by 1/b does not change its twisted action.
By monicity and depression its normalized form is

\[
 \begin{pmatrix}z&1\\zd-q&d\end{pmatrix},\qquad
 z=a/b,\quad q=D/b^2,\quad F(z)=q^2,\quad d=F'(z)/(4q).
\]

Here F(Z)=Z^4-6xZ^2+8yZ-3x^2 and q!=0. Define rational points

\[
 u=(z^2-x+q)/2,\quad v=(z^2-x-q)/2,
\]
\[
 R=(u,z(u-x)+y),\qquad S=(v,z(v-x)+y).
\]

Substitution, using q^2=F(z), proves that R and S lie on E. They are
the other intersections, with multiplicity, of the line through P of
slope z. Since u-v=q!=0, they are distinct. The chord law gives

\[
 R+S=-P,\qquad Q=R-S=P+2R.                              \tag{3}
\]

For the second identity, the slope from R to -S is
(z(u+v-2x)+2y)/q=(z^3-3xz+2y)/q=d. Thus its x-coordinate is
d^2-u-v=x-z^2+d^2, exactly the transformed quartic's point coordinate.
Direct expansion of its XY^3 coefficient gives the same y-coordinate.
The signs, both curve equations, and both group-law identities are checked
in [symbolic_chord.py](symbolic_chord.py).

The essential fact is that R is one rational point over Q. Its components
at different primes therefore belong to the global image H.

## 2. Primes with coefficient valuation two or four

At each such split prime, write c for the component of P and a_R for
the component of R in G_p=Z/3Z. Equation (3) gives the component
of Q as c+2a_R. Integral points have singular reduction exactly when
their component is nonzero. By the switching lemma in
[REDUCTION_PATTERNS.md](REDUCTION_PATTERNS.md), the row lattice is standard
if P and Q have the same status and is the unique nonstandard lattice
otherwise. Thus the component of R determines the row lattice. At nonsplit
primes the earlier theorem gives only the standard lattice.

## 3. Valuation three, integral normalized slope

Fix p>3 with B=p^3u_0, u_0 a unit, and assume b is a p-adic unit.
Then z and q are integral, and k=v_p(q)=v_p(D). The coordinates u,v
of R,S and their y-coordinates are integral as well. The nonzero local
component labels are the roots of T^3+u_0 modulo p: a singular integral
point U has label x(U)/p mod p. All these groups have exponent two.

If k=0, u-v=q is a unit, so at least one of R,S has unit x and lies
in E_0. Their component sum is -c=c, where c is the component of P.
Therefore their unordered component pair is {0,c}. If P is smooth,
both components are zero; if P is singular, the component of R is
either zero or c.

If k>0 and P is smooth, the exact local theorem gives k=2 and
z=t+p v_0, where t=y/x is a unit and (t v_0)^3=-u_0 mod p.
Since t^2-x=B/x^2 has valuation three and q has valuation two,

\[
 x(R)/p=(z^2-x+q)/(2p)\equiv t v_0\pmod p.              \tag{4}
\]

This is a nonzero component label. It determines v_0 modulo p and
hence the unique lattice L(2,t+p v_0). The zero component gives the
standard lattice. Thus the component of R determines the lattice.

If k>0 and P is singular, the local theorem gives k=1, complete splitting
of T^3+u_0, and the unique lattice L(1,0). Write X=x/p mod p and
q_0=q/p mod p. Then X^3=-u_0, q_0^2=-3X^2, and the labels of R,S are

\[
 (-X+q_0)/2,\qquad (-X-q_0)/2.                           \tag{5}
\]

They are precisely the other two roots of T^3+u_0. They are distinct
from each other and from X, since p>3 and X,q_0 are units. Hence
the nonstandard lattice corresponds to either of the two components
outside {0,c}. The standard case was shown to have the component of R
in {0,c}. These possibilities exhaust all admissible matrices.

## 4. Denominator and infinity cases

Still assume b!=0, but now p|b. Primitive-first-row implies p does not
divide a. Monicity gives D^2=f_P(a,b), a unit modulo p, so the original
primitive matrix has unit determinant and standard row lattice at p.
Let j=v_p(b)>0. The normalized quantities satisfy

\[
 v_p(z)=-j,\quad v_p(q)=-2j,\quad
 u+v=z^2-x,\quad uv=x^2+xz^2-2yz.
\]

The sum has valuation -2j, and the product has valuation at least -2j.
It follows that exactly one of u,v has valuation -2j and the other
is integral (possibly zero). For if their valuations were equal and
negative, the product valuation would be less than -2j; if unequal,
the smaller valuation equals that of the sum and the product bounds
the larger one below by zero. Thus one of R,S is nonintegral and
belongs to E_0, while the other has component -c. In the order-two
groups the pair is {0,c}, just as in the standard case above. In the
order-three groups, the component of R is zero or -c, and c+2a_R
has the same zero/nonzero status as c. Therefore the component rules
already given assign the standard lattice in this case too.

Finally, if b=0, primitive-first-row gives a=+/-1 and monicity gives
D=+/-1. Every local lattice is standard. Assigning the global point
R=O encodes this standard tuple: at every retained prime the component
rules for a_R=0 give the standard lattice. We do not need (3) for
this exceptional assignment, since only the row lattice is being counted.

## 5. Global count and the rank-only consequence

For each fixed base point P, Sections 2--4 show that the complete tuple
of local row lattices at p>3 is a function of the component tuple of
a single rational point R. Primes with valuation zero, one or five allow
only the standard lattice. Thus there are at most |H| possible tuples
away from 2 and 3, instead of the unrestricted product of local maxima.
The argument counts actual row lattices and does not require any freeness
of the action: nonstandard stabilizing matrices are allowed.

At 2 and 3 retain the earlier bound M=N_2(11)N_3(6)=8178*1636. Actual
global sublattices are determined by their localizations, so each rational
orbit has at most M|H| occurring global lattices. The earlier Thue bound
gives at most 2*7^192 point quartics per lattice. There are at most
2*2^r rational 2-orbits. Multiplying proves (1) with the stated C.

The finite component target has exponent dividing six. Its global image
is the product of its two primary images: multiplication by 3 isolates
the order-two part, and multiplication by 4 isolates the order-three
part. Consequently |H|=|H_2||H_3|=2^s3^h. The maps factor through
E(Q)/2E(Q) and E(Q)/3E(Q), respectively, so

\[
 s\le r+\dim E(\mathbb Q)[2]\le r+1,\qquad
 h\le r+\dim E(\mathbb Q)[3]\le r+1.
\]

The first torsion bound follows because X^3+B has at most one rational
root. The second follows from the Weil pairing, since Q has no primitive
cube root of unity. Therefore 2^r|H|<=6*12^r, proving (2) and the
two stated subfamily bounds when one primary image is absent.

One can sharpen |H| further to |H_2| times the number of supports in H_3:
the even-valuation lattice depends only on the singular-reduction pattern
of Q, while the valuation-three lattice depends only on the component
of R in H_2. This is bounded by
2^s min(2^w,(3^h+1)/2), where w is the number of retained order-three
primes. This sharpening is optional for the rank-only conclusions above.

## Limits and evidence

Known points give only a subgroup of H. Its size must not replace |H|
as an upper bound without proving that the image is complete. The
automatic bounds s<=r+1,h<=r+1 require no generator computation.
The separate component-weight theorem has the opposite monotonicity
and does allow savings certified from a known subgroup.

The [finite chord checker](verify_chord_lattices.py) examines valuation-three
component labels and actual rational stabilizing matrices; its
[results](chord_lattice_results.json) do not substitute for the denominator
or infinity arguments. The [literature note](LITERATURE_AND_STATUS.md)
records the already known rank-only phenomenon and unresolved quantitative
comparison. No best-known-bound or novelty assertion is made.
