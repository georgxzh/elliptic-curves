# Independent binary component restriction

Research proof draft, 2026-10-30. The cubic étale norm gives an arithmetic
restriction on the binary component image, with quantitative consequences
for the quotient factor. The norm/class-group mechanism is standard;
no novelty or universal improvement of the rank exponent is asserted.

## 1. The maximal-order statement

Let B be a nonzero sixth-power-free integer, E:y²=x³+B, and

    K=Q[t]/(t³+B),    theta=image of t.

This is an étale cubic algebra: either a cubic field or Q×Q(sqrt(-3)).
Use the maximal order O_K and its ordinary ideal class group, interpreted
factorwise in the product case. Define

    Cbar_K=Cl(O_K)/(2Cl(O_K)+<[q]:q divides 6>).

This is an F₂-vector space. Killing primes above 2 and 3 is part of the
statement, not an assumption that those classes vanish.

Retain the primes p>3 with v_p(B)=3 and at least one root of
T³+B/p³ in F_p. The earlier local component proof gives
V_p=E(Q_p)/E_0(Q_p), with nonzero elements labelled by these roots.
It has dimension one for splitting type 1+2 and dimension two for
splitting type 1+1+1. Write V₂=product V_p and H₂ for the image of
all rational points. For a root w, let P_{p,w} be the degree-one prime
of O_K above p with theta/p=w in its residue field.

These primes are well defined in the maximal order. Indeed write
B=b³d with d signed cube-free and b>0. At a retained prime,
theta/p=(b/p)eta, eta³=-d, and p does not divide 3d. The separable
polynomial for eta describes prime decomposition at p. Locally the bases
(1,theta,theta²) and (1,theta/p,(theta/p)²) have determinant ratio p³,
so the local index of Z_p[theta] in the maximal order is exactly p³.

**Theorem.** The assignments

    psi_p(0)=0,    psi_p(component labelled w)=[P_{p,w}]

are linear maps V_p→Cbar_K. Define

    Psi₂(c)=sum_p psi_p(c_p),    J₂=ker(Psi₂),
    n₂=dim V₂,    kappa₂=rank Psi₂.

Then

    H₂ subset J₂,
    dim H₂ ≤ min(r+tau₂,n₂-kappa₂),

where tau₂=dim E(Q)[2]. In the irreducible case tau₂=0.

At a fully split prime the three prime classes add to zero since their
product is (p). The three nonzero elements of V_p also add to zero, so
the assignment is linear. The one-dimensional case is automatic. Root
permutations simply relabel coordinates. An irreducible cubic residue
polynomial gives no binary block.

One may replace Cbar_K by **any certified F₂ quotient or family of
characters** of it. The resulting possibly larger kernel still contains
H₂. Thus a single class-field character can give an exact useful
obstruction without computing the full ideal class group.

## 2. Parity at every prime greater than three

First suppose K is a field. For P=(x,y) rational, put alpha=x-theta.
It is nonzero, and Norm(alpha)=x³+B=y². Its nonzero fractional
principal ideal is defined even when the point has denominators.
Fix p>3 and m=v_p(B), with 0≤m≤5.

**Nonintegral P.** The integral curve equation implies
v_p(x)=-2j, v_p(y)=-3j for j>0. Since theta is integral, x dominates
at every q above p and v_q(alpha)=-2j e(q/p), which is even. The
component is zero.

Now suppose x,y are p-integral.

* If m=0, the polynomial discriminant -27B² is a p-adic unit. A prime
  q dividing x-theta must have theta reducing to the scalar x, hence
  has residue degree one. There is at most one such prime because the
  roots are distinct. The norm formula gives v_q(alpha)=2v_p(y).
  All other valuations are zero.
* If m>0 and x is a unit, theta has positive valuation at every prime
  over p, so v_q(alpha)=0. These points have nonsingular reduction.
* If m=1 or 5 and x is a nonunit, no point exists: the valuation of
  x³+B is one for m=1, and either three or five for m=5.
* If m=2 or 4 and x is a nonunit, p is totally ramified in K, with
  e=3 and f=1: the cube-free radicand has valuation prime to three.
  The curve equation gives v_p(x)≥1 for m=2 and v_p(x)≥2 for m=4.
  Hence v_q(x)>v_q(theta)=m, and v_q(alpha)=m is even. This argument
  works in the maximal order and does not assume Z[theta] is maximal.
* If m=3 and x is a nonunit, then v_p(x)=1 and v_p(y)=n≥2. The
  residue w=x/p is a root of T³+B/p³. At the matching degree-one
  prime P=P_{p,w}, one has v_P(alpha)=2n-2; at every other prime
  q over p, one has v_q(alpha)=1. Indeed p is unramified, and
  x/p-theta/p is a unit at each nonmatching prime. Those primes have
  total residue degree two, so the norm identity gives the matching
  valuation 2n-2. In splitting type 1+2 this is one other prime of
  residue degree two; in type 1+1+1 it is two degree-one primes.
  With irreducible reduction there is no root and no such point.

Thus the only odd valuations outside 2 and 3 occur at the nonmatching
primes of a retained block with nonzero component. Their total ideal
class in Cbar_K is

    sum_{q above p,q != P} [q] = -[P] = [P],

since p is unramified and (p)=product_{q above p}q. Consequently

    (alpha)=a² j product_{p:c_p != 0} product_{q above p,q != P_{p,c_p}}q,

where a is a fractional ideal and j is supported above 2 and 3,
allowing negative exponents. Taking classes gives Psi₂(c)=0.
Infinity has zero component and is covered separately. This proves the
field case, including all primes, denominators, and nonmaximal orders.

## 3. Reducibility and the vanishing norm element

If K is reducible, B=-a³ with a a nonzero integer, and

    K=Q×Q(zeta_3),    theta=(a,a zeta_3).

Q has trivial class group and the Eisenstein integers are norm-Euclidean.
Thus Cl(O_K)=0, so this particular class-group restriction is vacuous
for every reducible cubic. It cannot exclude rational 2-torsion.

For P other than O and T=(a,0), x-theta is invertible and the preceding
ideal argument applies factorwise. At T it has a zero coordinate, so
one must not form its nonzero principal fractional ideal. The corrected
standard value is

    delta(T)=(3a²,a(1-zeta_3)),    Norm(delta(T))=(3a²)².

At p>3 dividing a, the first-coordinate valuation is two and the
valuations in the quadratic factor are one. This matches the parity
pattern for the component of T. Assign delta(O)=1. These corrections
explain compatibility with torsion; containment in the zero class-group
target is already tautological in this reducible case.

## 4. Safe quantitative consequences for A(H₂)

For a block subspace H recall

    D_c=product_p <c_p>,    K_c(H)=H intersect D_c,
    A(H)=sum_{c in H} 1/|K_c(H)|.

We do **not assume** monotonicity of A under subgroup inclusion. The
previous warning that a subgroup generated by known points cannot simply
replace the full image does not prove nonmonotonicity: it is compatible
with A increasing under inclusion. Establishing general monotonicity
would be a separate combinatorial theorem.

Let J₂ be any certified kernel above, j=dim J₂, and
d=min(r+tau₂,j). The established dimension inequality gives

    A(H₂) ≤ (2^d+1)/2.                                    (4.1)

For j=0 the factor is exactly one. For j>0 there is also the stronger
kernel-sensitive safe alternative

    A(H₂) ≤ max{A(J₂),(2^(j-1)+1)/2}.                     (4.2)

Proof: either H₂=J₂, or it is proper and has dimension at most j-1.
Take the minimum of (4.1) and (4.2). Both use a class-group matrix and
rank upper bound, with no requirement for complete Mordell--Weil
generators. If known points already span J₂, containment proves
H₂=J₂ and permits the exact value A(J₂).

A finer computable bound uses the distribution of intersections inside
J₂. For a possible image dimension s≤d and each nonzero c in J₂, set

    k_c=dim(J₂ intersect D_c),
    w_s(c)=2^(-max(1,s+k_c-j)).

For s-dimensional H⊂J₂ containing c, the subspace dimension inequality
and c∈K_c(H) give dim K_c(H)≥max(1,s+k_c-j). Therefore A(H) is at
most one plus the sum of the largest 2^s-1 numbers w_s(c). The maximum
of this explicitly computable expression over 0≤s≤d is another valid
kernel-only bound. At s=0 the sum is empty; at s=j it equals A(J₂).
No claim is made that maximizing subsets are linear or arithmetically
realizable.

Combining a certified bound U₂ with the preceding ternary class kernel
J₃ gives, with the constant C of the component-quotient theorem,

    #E_B(Z) ≤ C 2^r U₂ min{S(J₃),(3^(r+tau₃)+1)/2}.

When the quadratic field construction is unavailable, use the original
full ternary ambient space instead of J₃. If the cubic is irreducible,
tau₂=0 and the previous normalization permits C/2. This provides a
quantified arithmetic refinement of A(H₂)S(H₃). It assumes neither
s+h≤r nor completeness of a subgroup generated by known points.

**Injective-class criterion.** If Psi₂ is injective, then H₂=0 and
U₂=1. If the ternary map is injective too, or there are no retained
ternary primes, this gives #E_B(Z)≤C 2^r. No uniform injectivity or
unbounded-rank family with this property is asserted.

## 5. Concrete example supplied by the parallel certificate computation

The root investigation constructs an unramified quadratic character for
K=Q(a), a³=58, using alpha=673+190a-94a². Its certificate checks
Norm(alpha)=19², (alpha)=P_7², splitting over 2 and 3, and a nonsquare
residue at the degree-one prime over 5. At 19 the roots are 1,7,11 and
the character takes values 0,1,1. Full details and exact checks belong
to the companion root certificate; they are not substituted by an
uncertified numerical class-group order here.

The [exact certificate](EXACT_EXAMPLES.md), independently checked in
[the audit](ASTRA_AUDIT.md), establishes these hypotheses. The consequences
of the theorem are immediate and require no rank or saturation computation:

* For B=-58·5³=-7250, the sole binary block is one-dimensional and
  the character is nonzero on it. Thus H₂=0 and A(H₂)=1.
* For B=-58·19³=-397822, the character kernel in the split binary
  block is the line labelled by root 1. The exact rational point
  P=(1463,55955) has that nonzero component: 1463=19·77 and
  77≡1 mod19. Hence H₂ equals the line and A(H₂)=3/2, improving the
  full split-block factor 5/2. Both curves have H₃=0 because the
  remaining prime valuations are one.

The point identity 55955²=1463³-397822 is checked directly. A verified
character suffices: no computation of the entire class group is needed.
Both conclusions are unconditional arithmetic statements, using the
standard class-field theorem specified in the companion certificate.

## 6. Status and imported facts

The all-prime parity proof and quantitative kernel inequalities above
are complete derivations. The global point count imports the same
rational descent, local component classification, and Thue bound as the
previously audited quotient theorem. Additional standard inputs are
unique ideal factorization in maximal orders, the norm valuation formula,
prime decomposition at primes of unit polynomial discriminant, total
ramification of cubic radicals whose valuation is prime to three, and
the norm-Euclidean property of the Eisenstein integers. The example
character needs the separate class-field certificate. This research
draft should receive independent human review before publication.
