# A ternary component image gives a uniform 6^rank bound

Research derivation, 2026-10-28. This combines the fixed-pattern theorem
in `REDUCTION_PATTERNS.md` with an elementary local component calculation.
It uses the same imported descent and Thue theorems as the earlier global
proof. No novelty claim or independent human verification is asserted.

## The theorem for the original cubic-twist family

Fix a nonzero integer d. For every positive cube-free integer n, put

    E = E_{d,n}: y^2=x^3+dn^2,
    r = rank E(Q),
    S = {p : p divides n, p does not divide 6d, (d/p)=1},
    w = |S|.

At each p in S the nonsingular-reduction subgroup E_0(Q_p) has cyclic
quotient E(Q_p)/E_0(Q_p) of order three. Let

    H_3 = image(E(Q) -> product_{p in S} E(Q_p)/E_0(Q_p)),
    h = dim_F3 H_3.

The component groups, homomorphism and dimension are proved below. If
A_d is the explicit constant from `../2026-10-25-inert/GLOBAL_PROOF.md`,
then

    #E_{d,n}(Z) <= A_d 2^r min(2^w, (3^h+1)/2).           (1)

Moreover h<=r+tau_3, where tau_3=dim_F3 E(Q)[3]<=1. In particular

    #E_{d,n}(Z) <= 2 A_d 6^r.                             (2)

If E(Q)[3]=0, the constant 2 A_d in (2) can be replaced by A_d.
Both constants are independent of n, w and r. The precise displayed
integral model is intended; no change of model is made at primes
dividing 6d. Both signs of y are included.

The primitive subset satisfies the stronger bound

    #{(x,y) in E_{d,n}(Z): gcd(x,n)=1} <= A_d 2^r.         (3)

Here the stated gcd condition is the definition of primitive being
used; the same estimate holds for any one prescribed pattern of
divisibility of x by the primes dividing n outside 6d.

For reference, a deliberately crude explicit choice, inherited without
optimization from the original proof, is

    A_d = 8*7^192 * product_{p|6d} N_p(K_p),
    N_p(K) = sum_{k=0}^K sum_{j=0}^k p^j,
    K_p = floor((12 v_p(2)+3 v_p(3)+2 v_p(d)+8)/2).

## Elementary local component calculation

Let p>3, let e in {1,2}, and consider B=p^(2e)u with u a p-adic unit.
The nonsingular-reduction subgroup E_0(Q_p) consists of O, all points
with nonintegral coordinates, and all integral points with unit x.
The reduced affine cubic is y^2=x^3, with its sole singular point
(0,0). The subgroup and reduction homomorphism are standard: see
J. H. Silverman, *The Arithmetic of Elliptic Curves*, Chapter VII,
section 2, Proposition 2.1. The following proof needs no Kodaira-type
or Tate-algorithm classification.

For an integral point Q=(x,y) with nonunit x, valuation comparison in
y^2=x^3+B gives

    v_p(x)>=e,    v_p(y)=e,

and forces u to be square modulo p. If u is nonsquare modulo p there
are no such points, so E(Q_p)=E_0(Q_p).

Suppose now u is square modulo p. Hensel lifting gives b=p^e v with
b^2=B and v a p-adic unit. The point T=(0,b) has order three: its
tangent has slope zero and meets the cubic with multiplicity three,
or directly the doubling formula gives 2T=-T.

We show that all points lie in E_0(Q_p), T+E_0(Q_p), or -T+E_0(Q_p).
Only singular integral points Q need consideration. If x=0 then
Q=+/-T. Otherwise, write a=v_p(x)>=e. Since y/p^e is congruent to
one of v and -v modulo p, choose the sign of b so that

    v_p(y+b)=e.

The x-coordinate of Q-T is

    ((y+b)/x)^2-x.

Its valuation is zero when a=e, and 2(e-a)<0 when a>e. Thus Q-T
belongs to E_0(Q_p). This proves that there are at most three cosets.
There are exactly three: T and 2T=-T are both singular integral
points, hence neither belongs to E_0(Q_p), and their cosets are
distinct. Consequently

    E(Q_p)/E_0(Q_p) is isomorphic to Z/3Z.                 (4)

For integral points, the nonzero component condition is exactly
p|x. This includes e=2 without any additional argument.

In the original family, p does not divide 6d and p|n implies
B=dn^2=p^(2e)u with e=v_p(n) in {1,2}; the squareclass of u is
the squareclass of d. Thus the above cases are exactly the split
and inert primes occurring in the theorem.

## The image rank and the number of support patterns

Equation (4) shows that the global component map factors through
E(Q)/3E(Q). By the Mordell--Weil theorem,

    dim_F3 E(Q)/3E(Q) = r+dim_F3 E(Q)[3] = r+tau_3,

so h<=r+tau_3. Here tau_3<=1: the Weil pairing rules out all of E[3]
being Q-rational, since Q does not contain a primitive cube root of
unity. This uses only the standard nondegenerate, Galois-equivariant
Weil pairing (Silverman, Chapter III, section 8).

For h in H_3 define its support to be the subset of p in S at which
its component is nonzero. Every integral point produces exactly its
singular-reduction pattern as this support. There are at most 2^w
supports. Also, h and -h have the same support. The zero vector is
alone under this involution, and the other 3^h-1 vectors form
(3^h-1)/2 distinct two-element pairs. Therefore

    #{supports realized in H_3} <= min(2^w, (3^h+1)/2).    (5)

Different pairs can have the same support, and vectors whose cosets
contain no integral point can occur. Both phenomena only decrease
the number of realized integral patterns. No assertion that every
support is realized by an integral point is needed.

At primes p|n outside 6d with (d/p)=-1, the local calculation forces
x to be a unit, so there is only the nonsingular status. Thus (5)
also bounds the number of full patterns outside 6d. For each such
pattern, the fixed-pattern theorem gives at most A_d 2^r integral
points. Summing over the patterns proves (1).

Finally, r>=0 and h<=r+1 give

    2^r (3^h+1)/2
       <= 2^r (3^(r+1)+1)/2 <= 2*6^r.

If tau_3=0, replace r+1 by r and the final factor 2 disappears.
This proves (2). For (3), the primitive subset lies in the single
all-nonsingular pattern outside 6d; restrictions at the fixed bad
primes only reduce its cardinality.

## Scope and possible computation

The rank-only bound (2) requires neither computation of H_3 nor any
assumption on splitting or the number of factors of n. Keeping h in
(1) can give a substantially stronger estimate, and h=0 recovers
the base-two bound for the unrestricted integral point set.

To compute the exact H_3, one needs generators sufficient to determine
the global image, for example full Mordell--Weil generators modulo
3E(Q). A subgroup generated by some known points gives a lower bound
on h; unlike the weight saving in `GLOBAL_COMPONENT_CODE.md`, such a
lower bound cannot be substituted into (1) as an upper bound on the
number of patterns. The automatic upper bounds r+tau_3 and w are
always valid.

The primitive theorem (3) follows already from fixed patterns. The
additional step here is to bound the number of patterns globally by
the ternary component image, giving the unrestricted uniform 6^r
estimate. Prior rank-only bounds and component-group methods exist;
the priority and practical relevance of this particular constant base
require a separate literature assessment.
