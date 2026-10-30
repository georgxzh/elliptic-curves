# Audit of the rational chord bridge and binary quotient average

Research audit, 2026-10-29. This is an independent AI check of the written
arguments, including a direct inspection of the specified primary source.
It is not independent human verification or a novelty assessment.

**Verdict.** No counterexample or substantive gap was found in
[CHORD_GLOBAL.md](../2026-10-28-refinements/CHORD_GLOBAL.md) or
[BINARY_QUOTIENT.md](../2026-10-29-continuation/BINARY_QUOTIENT.md).
Their stated bounds follow from the cited inputs and the supplied local
classification. In particular, determinant signs, nonstandard stabilizers,
denominator slopes, empty rational classes, and averaging fibers do not
invalidate the argument. The additional torsion restriction below improves
constants, but does not change the exponential base or resolve the main
integral-realizability question.

## 1. Primary-source check of the imported results

The source checked was Alpöge–Ho,
[*The second moment of the number of integral points on elliptic curves is bounded*,
arXiv:1807.03761v3](https://arxiv.org/html/1807.03761v3), dated 3 November 2022.

Theorem 2.2 supplies the point/quartic correspondence; **Section 3.1** supplies
the identification of rational twisted-PGL2 orbits with rational classes
modulo 2. The latter assertion is not Theorem 2.2 alone.

Lemma 3.3 assumes a PID, a primitive matrix representative, and monic depressed
integer-matrix source and target quartics. It concludes primitive first row
and determinant-square divisibility by the quartic discriminant.

Theorem 3.5 assumes a homogeneous polynomial over the specified ring of
S-integers with at least three distinct geometric projective roots. It does
not require irreducibility. Its unit-value solutions are counted modulo
simultaneous unit scaling. Degree four, Q, and the singleton infinite place
give exponent 4^3(1+2)=192.

These are the precise imported statements used here. The application checks
and additional calculations below are performed on the present notes.

## 2. Application hypotheses and the count per actual lattice

For an integral point P=(x,y), the polynomial

\[
 f_P=X^4-6xX^2Y^2+8yXY^3-3x^2Y^4
\]

is monic and depressed. Its X^3Y and XY^3 coefficients belong to 4Z;
its X^2Y^2 coefficient belongs to 6Z. Thus it is integer-matrix in the
source's convention, including at 2 and 3. The same statements hold for
every target f_Q. A rational invertible matrix has a primitive integral
representative unique up to common sign. This is precisely enough to apply
the determinant lemma over Z. Localization at p>3 also satisfies its
hypotheses: Z_p is a PID, some matrix entry remains a unit, and 4 and 6
are units. No unproved minimal-model assumption is being substituted.

Direct substitution into the quartic invariants gives

\[
 I=0,\quad J=-1728B,\quad
 \Delta(f_P)=-2^{12}3^3B^2\ne0.
\]

The twisted action preserves this discriminant. The divisor bound therefore
gives v_2(D)<=11 and v_3(D)<=6 for sixth-power-free B, and the proposed
counts N_2(11)=8178 and N_3(6)=1636 are correct. Allowing every sublattice
with these indices is an upper bound; first-row primitivity does not need
to be imposed on this deliberately enlarged set.

There is no left/right-action error in the passage from matrices to row
lattices. With the convention in the notes,

\[
 T_U(T_T f)=T_{UT}f.
\]

If the lattice with row basis T occurs via g_0=U_0T, then
F=T_T f=T_{U_0^{-1}}f_{Q_0} is integral. It need not itself be monic or
depressed, and the Thue input does not require those properties. Nonzero
discriminant gives four distinct geometric roots, including a possible
root at infinity. Reducible F causes no problem.

For g=UT with U in GL_2(Z), monicity imposes F(a,b)=1 on its first row.
After fixing this row and det(U)=epsilon, any other second row differs by
lambda(a,b). The substitution changes the X^3Y coefficient by 4lambda,
so depression permits at most one second row. Common negation of U has
no effect on a quartic; the two determinant signs must still be retained.
For example, diagonal matrices (1,1) and (1,-1) send f_P to f_P and
f_{-P}. Thus **2*7^192**, rather than 7^192, is the justified uniform
bound per lattice. The notes retain this factor correctly.

Finally, actual finite-index sublattices of Z^2 are determined by their
localizations. This gives an injection, which is all the upper bound uses.
Surjectivity of any local-to-global construction and freeness of an action
are unnecessary. A point quartic occurring through several lattices is
merely counted several times.

## 3. Chord formula, signs, and exceptional slopes

Normalize a matrix with b!=0 by dividing all its entries by b. The
twisted action is unchanged. Monicity and depression give

\[
 g/b=\begin{pmatrix}z&1\\zd-q&d\end{pmatrix},\quad
 q^2=F(z),\quad d=(z^3-3xz+2y)/q,\quad q\ne0.
\]

The other two intersections of the line through P of slope z have
abscissae u,v satisfying

\[
 u+v=z^2-x,\qquad uv=x^2+xz^2-2yz,\qquad u-v=q.
\]

Together with ordinates z(u-x)+y and z(v-x)+y, they give the stated R,S.
The line meets the cubic with its intersection multiplicities, so R+S=-P
also covers a tangent at P. Since u!=v, the addition of R and -S uses
an ordinary nonvertical secant. Its slope is d, and comparison of both
coordinates gives Q=R-S=P+2R with the signs as printed. No implicit
choice Q versus -Q is harmless here; the displayed XY^3 coefficient
check verifies the actual choice.

Replacing q by -q swaps R and S and changes the target from Q to -Q.
At a binary prime their component vectors differ by c, which belongs to
D_c; their binary lattice outputs coincide. At a ternary prime Q and -Q
have the same support. Thus the subsequent lattice counting is compatible
with this sign change as well.

When p divides b, primitive first row forces a to be a unit, and
f_P(a,b)=D^2 forces D to be a unit. Hence the original lattice is standard.
For j=v_p(b)>0, v_p(z)=-j and v_p(q)=-2j. The sum u+v has valuation
-2j and the product uv has valuation at least -2j. If u,v had the same
negative valuation t, their sum would give t<=-2j, while their product
would have valuation 2t<=-4j, a contradiction. If the valuations differ,
the smaller is -2j and the larger is nonnegative. This also allows one
coordinate to be zero. Exactly one of R,S is therefore nonintegral and
in E_0. If the other abscissa is integral, its ordinate is integral by
the curve equation. The component pair is {0,-c}, yielding precisely
the standard-lattice rules in both primary groups.

For b=0, primitivity gives a=+/-1 and monicity D=+/-1. Every lattice
is standard. Assigning R=O is legitimate for this counting argument:
it encodes the output, and no chord identity for that assignment is
needed. In particular this case includes the transformation to -P.

## 4. Local component rules

The supplied component calculations use the standard subgroup E_0 of
nonsingular reduction. For p>3 and the given coefficient valuations,
they prove the quotient directly, without importing a table of Kodaira
types. Their torsion representatives are outside E_0, and distinct
representatives give distinct cosets. In the cubic-valuation case the
labels x/p are roots, not field elements to be added directly; identifying
three roots with the three nonzero vectors of F_2^2 supplies the group
operation. The argument respects this distinction.

At valuations two and four, the previously proved switching lemma says
that the unique nonstandard lattice occurs exactly when P and Q have
different singular-reduction statuses. Since the ternary component of Q
is c+2a_R, this status and therefore the lattice are functions of a_R.
For a fixed P, passing to supports of Q is legitimate: adding the fixed
c and multiplying by 2 permutes H_3.

At valuation three and b a unit, q and z are integral, hence R,S are
integral. If q is a unit, u-v is a unit, so one component is zero and
the other is c. This gives exactly the standard outputs.

If P is smooth and q is not a unit, the exact classification forces
k=2 and z=t+pv. Then x(R)/p=tv modulo p labels the nonstandard lattice
L(2,t+pv); distinct roots give distinct lattices. If P is singular,
the nonstandard case forces k=1 and complete splitting. The two labels
(-X+q_0)/2 and (-X-q_0)/2 are the two roots different from X. The
conditions q_0^2=-3X^2 and p>3 make all these labels distinct. This
exhausts the local cases rather than presuming every global output is
realized.

Nonstandard stabilizers are allowed. For example, the checked matrix
with rows (13,1),(-22,-13) stabilizes the point quartic of (8,13) on
B=-343 and has determinant -147. Its chord point is (7,0). This is
consistent with the component rule, and refutes any attempted proof
that a stabilizing transformation must have standard lattice. Neither
audited proof uses that false assertion.

## 5. Exact binary quotient and averaging

For a fixed source component c, the local output map is exactly the
quotient by span(c_p). When c_p=0 it is injective on the local component
group. When c_p!=0, its fibers are the pairs {a_p,a_p+c_p}. Restriction
to the actual global image H therefore has kernel

\[
 K_c=H\cap\prod_p\langle c_p\rangle,
\]

and exactly |H|/|K_c| abstract outputs, each with |K_c| preimages.
This is an equivalence relation on component vectors, not a quotient
by a matrix stabilizer. Actual integral transformations form a subset,
so only an upper bound by this number is claimed.

Write N=2^(r+tau_2), where tau_2=dim E(Q)[2]. The map from E(Q)/2E(Q)
onto H is a homomorphism, and all its fibers have N/|H| elements.
It is valid to include classes containing no integral point with the
prescribed nonnegative bound. Thus the sum of binary contributions is

\[
 \frac N{|H|}\sum_{c\in H}\frac{|H|}{|K_c|}=N A(H).
\]

There is no extra |H| factor, no claim that occurring classes are uniformly
distributed, and no dependence on a choice of integral point in an empty
class. Multiplication by S(H_3) is valid even if the actual binary and
ternary outputs are dependent. At the abstract group level the full
global image is the product of its primary images, since multiplication
by 3 and 4 isolates them. This does not assert simultaneous integral
realizability.

For c!=0, K_c contains {0,c}; for c=0, it is zero. This proves
A(H)<=(2^s+1)/2, including s=0. Pairing nonzero ternary vectors under
negation proves S(H_3)<=(3^h+1)/2. Both are upper estimates on the full
image. Substituting an incompletely generated subgroup for H would be
invalid, as the notes correctly warn.

## 6. Arithmetic torsion restriction: a constant-factor refinement

The simultaneous worst torsion shifts s<=r+1 and h<=r+1 in the previous
rank-only estimate cannot occur with both component images nontrivial.
This gives an arithmetic refinement, albeit only of constants.

**Lemma.** For nonzero sixth-power-free integer B:

1. If E_B(Q)[2]!=0, then H_3=0.
2. If E_B(Q)[3]!=0, then H_2=0. More precisely, B is a positive square
   or B=-432; in the exceptional case both retained images are zero.

For the first assertion, a nonzero rational 2-torsion point has the form
(a,0), with a an integer and B=-a^3. Sixth-freeness forces a to be
squarefree, so v_p(B) is zero or three. There are no retained ternary
primes.

For the second, let T=(u,v) have order three. Here v!=0, and comparing
the x-coordinates of 2T and -T using the tangent slope 3u^2/(2v) gives

\[
 u(u^3+4B)=0.
\]

If u=0, then B=v^2 is a positive rational square and hence an integer
square. All prime valuations of B are even, so H_2=0. If u!=0, then
v^2=3u^3/4. Set t=2v/(3u); this yields u=3t^2 and

\[
 B=-27t^6/4=-432(t/2)^6.
\]

For every prime ell, sixth-freeness imposes
0<=v_ell(-432)+6v_ell(t/2)<=5. Since the valuations of -432 are
4 at 2, 3 at 3, and zero elsewhere, v_ell(t/2)=0 for every ell.
Thus t/2=+/-1 and B=-432, whose prime support is {2,3}.

Consequently, if H_2 and H_3 are both nonzero, there is no rational
2- or 3-torsion, and

\[
 \#E_B(\mathbb Z)
 \le\frac C2\,2^r A(H_2)S(H_3)
 \le\frac C8\,2^r(2^r+1)(3^r+1).                 \tag{A}
\]

There is **no assertion s+h<=r**. Reduction modulo 2 and modulo 3 of
the same free Mordell–Weil generators can independently have full rank.

For completeness a uniform torsion-aware envelope, also covering the
one-primary cases, is

\[
 \#E_B(\mathbb Z)\le\frac C2\,2^r
 \max\left\{
 \frac{(2^r+1)(3^r+1)}4,\quad
 2^{r+1}+1,\quad
 \frac{3^{r+1}+1}2
 \right\}.                                             \tag{B}
\]

These three terms correspond respectively to no rational 2/3-torsion,
rational 2-torsion, and rational 3-torsion without rational 2-torsion.
If both torsion groups are nontrivial, the lemma forces B=1 and the
retained images vanish; this is covered by the second term. For r>=3
the first term in the maximum dominates the other two, so (A)'s final
right side is then a valid uniform bound. For r=0,1,2 the maximum
in (B) is respectively 3,5,14.

The leading exponential rate in (A) and (B) remains 12^r. This lemma
does not constrain torsion-free extremal codes or prove a deficit in
the integral transformations realizing their outputs. It must not be
presented as an improvement of that rate.

## 7. Verification and remaining scope

### Additional standard inputs (root-agent application check)

The nonsingular-reduction subgroup is the standard E_0 of Silverman,
*The Arithmetic of Elliptic Curves*, VII.2, Proposition 2.1; the primary
text was inspected in the preceding continuation. At every retained p>3,
v_p(B)<6 makes the short Mordell model minimal, and its reduction is
the cuspidal cubic. Integral points are in E_0 precisely when x is a
unit; nonintegral points reduce to its nonsingular point at infinity.
The local quotient sizes used here are then proved by explicit torsion
translations in the component notes, not imported without checking.

Mordell--Weil applies because B!=0 makes the projective completion a
smooth genus-one curve over Q with the rational point O. It gives the
finite quotient sizes n^r*|E(Q)[n]| used for n=2,3. The Weil-pairing
bound on rational 3-torsion applies in characteristic zero: two independent
rational 3-torsion points would force a primitive cube root of unity
in Q. Rational 2-torsion is bounded directly by the number of rational
roots of X^3+B. Thus neither image-dimension bound assumes that a list
of known points generates E(Q), and the two bounds are separate.

The standard ideal-factorization, Hensel, and quadratic-form inputs for
the new arithmetic certificates are checked separately in
[CLASS_GROUP_RESTRICTION.md](CLASS_GROUP_RESTRICTION.md), Section 5.
They are not part of the imported quartic/descent argument.

The symbolic chord checker passed, including both curve equations and
the actual transformed ordinate. The finite chord/lattice checker passed
1,290 local point samples at p=5,7,11,13,19, including 5,160 denominator
checks and explicit nonstandard stabilizers. These support the general
written proof; they do not replace it or check all p-adic points.

The binary quotient checker separately verifies the exact fiber relation
and averaging identity in all its tested ambient dimensions through six.
The imported descent and Thue theorems were checked against the primary
paper, not inferred from those finite computations. No search over
bounded rational points establishes full Mordell–Weil generators,
saturation, rank, or integral completeness.

The substantive remaining arithmetic question is whether actual integral
transformations uniformly occupy fewer outputs than these component bounds
allow, or whether another arithmetic argument bounds integral points with
a smaller exponential base. Neither the audit nor the torsion lemma settles
that question.
