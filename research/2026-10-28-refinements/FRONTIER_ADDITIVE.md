# Exact point-quartic lattices at all tame potentially good additive primes

Research proof draft, 2026-10-28. This extends the elementary local argument
from j=0 to general short Weierstrass curves. It does not establish novelty.
All existence assertions in the local theorem are over Z_p.

## 1. Statement

Let p>3 and let E: y^2=x^3+Ax+B be a minimal integral short model over Z_p,
with potentially good additive reduction. Put

    f_P(X,Y)=X^4-6xX^2Y^2+8yXY^3-(3x^2+4A)Y^4,
    F(Z)=f_P(Z,1),
    L(k,z)={(r,s) in Z_p^2 : r-zs is in p^k Z_p}.

Count actual row lattices Z_p^2 g of primitive integral matrices g with
nonzero determinant such that T_g f_P=(det g)^(-2)f_P((X,Y)g) is integral,
monic and depressed. The standard lattice always occurs. The table gives
**all** other lattices. For unit x put t=y/x. Write a=v_p(A), b=v_p(B),
allowing infinite valuations. The usual tame Kodaira conditions are included
to make the assertion independent of terminology.

| Type | Coefficient conditions | x unit | x nonunit |
|---|---|---|---|
| II | a>=1, b=1 | none | no such points |
| III | a=1, b>=2 | L(1,t) | none |
| IV | a>=2, b=2 | L(1,t) iff B/p^2 is a square mod p | L(1,0) |
| I0* | a>=2, b>=3, C separable | L(2,t+p v), one for each C(t v)=0 mod p | L(1,0) iff C splits completely |
| IV* | a>=3, b=4 | L(2,t) iff B/p^4 is a square mod p | L(2,A/(2y)) |
| III* | a=3, b>=5 | L(3,t-B/(t A)) | none |
| II* | a>=4, b=5 | none | no such points |

In the I0* row,

    C(T)=T^3+(A/p^2)T+B/p^3 over F_p.

In the nonunit IV and IV* rows the point equation forces B/p^b to be
a square. In nonunit IV*, v_p(y)=2 and v_p(A)>=3, so A/(2y) is integral.
The expression B/(t A) in III* is integral of valuation at least 2.
Only z modulo p^k matters in L(k,z).

Consequently the exact maximum, attained by every point with unit x, is

| Type | Maximum number lambda_p of lattices |
|---|---|
| II, II* | 1 |
| III, III* | 2 |
| IV, IV* | 1 + indicator(B/p^b is square mod p) |
| I0* | 1 + number of F_p roots of C |

Unit-x local points do exist: choose any nonzero t modulo p on the
cuspidal reduction and lift using the nonzero y derivative.

These statements include the earlier Mordell table. The shifted lattices
at nonunit IV* and at III* are additional phenomena when A is nonzero.

## 2. General quartic criterion

The primitive-first-row and determinant lemma used in the earlier notes
(Alpoge--Ho, Lemma 3.3 over the PID Z_p) applies to the general point quartic.
It gives a primitive first row and

    (det g)^2 divides disc(f_P)=2^8 Delta_E,
    Delta_E=-16(4A^3+27B^2).

If k=v_p(det g)>0, the second entry of the first row is a unit, since
f_P(X,Y) is monic. Normalize it to 1. Monicity and depression yield

    F(z)=q^2,     v_p(q)=k,     v_p(F'(z))>=k,                 (1)

and the lattice is L(k,z). Conversely (1) suffices: set

    d=F'(z)/(4q),       g=[[z,1],[zd-q,d]].                   (2)

The coefficients in the lattice basis with rows (z,1),(p^k,0) are

    F(z)/p^(2k), F'(z)/p^k, F''(z)/2, p^k F'''(z)/6, p^(2k).

They are integral. Changing to (2) is a GL_2(Z_p) basis change, proving
integrality of T_g f_P. Its invariants are I=-48A, J=-1728B.
If its coefficients are 1,0,c,d,e, then x'=-c/6, y'=d/8 are integral,
I=12e+c^2 forces e=-3x'^2-4A, and J forces y'^2=x'^3+Ax'+B.
Thus the construction gives another integral point quartic on E.

For every additive row, A=B=0 modulo p. If x is a unit, then t is a
unit, x=t^2 mod p and

    F(Z)=(Z-t)^3(Z+3t) mod p.

Conditions (1) force z=t+s with v_p(s)>=1. Set h=t^2-x=(Ax+B)/x^2.
Exact expansions, valid with nonzero A, are

    F(t+s)=s^4+4t s^3+6h s^2+4t h s+h^2+4B/x,
    F'(t+s)/4=s^3+3t s^2+3h s+t h.                           (3)

When x is nonunit, y is also nonunit and the only repeated root is z=0
mod p. We use F(z)=z^4-6xz^2+8yz-3x^2-4A directly.

A useful lifting observation will be applied repeatedly. If a candidate
z_0 has F(z_0) divisible by p^(2k) and v_p(F'(z_0))=k, changing z_0 by
p^k w preserves its lattice and changes F(z_0)/p^(2k) modulo p by an
affine function of w with unit linear coefficient, provided F''(z_0)=0
mod p. In all applications below z_0 is a repeated cusp root and this
last condition holds. Choose a nonzero square value. Then F(z) has a
p-adic square root of valuation k, establishing (1).

## 3. Unit-x proof

**II and II*.** In type II, v(h)>=1 and the term 4B/x in (3) has
valuation 1, strictly smaller than all others. In II*, v(h)>=4.
If v(s)=1, the cubic term has valuation 3; if v(s)>=2, the constant
4B/x has valuation 5. All these valuations are odd, excluding (1).

**III.** Here v(h)=1. The derivative in (3) has valuation exactly 1,
so k=1 is necessary. At z=t, F(t)=h^2+4B/x is divisible by p^2.
The lifting observation gives existence. Every candidate has z=t mod p,
so there is exactly one nonstandard lattice.

**IV.** Here v(h)>=2. For every v(s)>=1, F(t+s) has valuation 2 and

    F(t+s)/p^2 = 4(B/p^2)/x mod p.

Since x is a square mod p, the necessary and sufficient square condition
is the one in the table. Necessarily k=1 and z=t mod p. Taking z=t
works: its derivative has valuation at least 2.

**I0*.** Here v(h)>=2. Write s=p v, allowing v=0 mod p. Formula (3)
gives

    F(t+p v)/p^3 = (4/x) C(t v) mod p,
    F'(t+p v)/(4p^2) = (1/t) C'(t v) mod p.                  (4)

Initially F is divisible by p^3, so its square valuation requires k>=2.
The first equation forces C(t v)=0. Separability then makes the derivative
valuation exactly 2, hence k=2. For each root v, F(t+p v) is divisible
by p^4 and the lifting observation supplies a square at the same lattice.
Different residues v give different lattices.

**IV*.** Here v(h)>=3. If v(s)=1, F has valuation 3. If v(s)>=2,
F has valuation 4 with unit part 4(B/p^4)/x. Thus k=2, s=0 mod p^2,
and the same square condition as IV is necessary and sufficient. For
existence take z=t; its derivative has valuation at least 3.

**III*.** Here v(h)=3. If v(s)=1 then F has valuation 3. Hence
v(s)>=2. The derivative in (3) has valuation exactly 3; meanwhile F
is divisible by p^5, so (1) requires k=3. Write s=p^2 v. Reduction
modulo p^6 shows that F is divisible by p^6 precisely when

    s=-B/(t A) mod p^3.                                     (5)

Indeed the only possibly nonzero terms at valuation 5 are
4t h s+4B/x, and their sum is 4(t A s+B)/x modulo p^6.
Thus the table gives the sole possible lattice. At z_0=t-B/(t A)
one has F(z_0)=0 mod p^6 and derivative valuation 3; lift to a square
by the observation above.

## 4. Nonunit-x proof

**II and II*.** Type II would give v(y^2)=1. For II*, v(x)=1 gives
v(x^3+Ax+B)=3, and v(x)>=2 gives valuation 5. Both are impossible.

**III.** At any z divisible by p, -4A is the unique term of valuation
1 in F(z). Its valuation is odd, excluding a nonstandard lattice.

**IV.** The point equation forces v(y)=1 and B/p^2 square. At any
z divisible by p, F(z) is divisible by p^2 and F'(z) has valuation 1.
Thus k=1. At z=0 the lifting observation gives existence, yielding L(1,0).

**I0*.** Write x=p X. The point equation forces v(y)>=2 and C(X)=0
mod p. For z divisible by p,

    F(z)/p^2 = -(3X^2+4A/p^2) mod p.                        (6)

The right side is nonzero. Indeed the factorization

    C(T)=(T-X)(T^2+XT+X^2+A/p^2)

over F_p has quadratic discriminant -3X^2-4A/p^2; if it vanished, C
would have a repeated root. Hence F always has valuation 2. Condition
(1) holds exactly when this quadratic discriminant is a square, which
is exactly complete splitting of C. Take z=0 for existence: F'(0)=8y
has valuation at least 2. This gives only L(1,0).

**IV*.** The curve equation excludes v(x)=1 and forces v(x)>=2,
v(y)=2, and B/p^4 square. For every z divisible by p the derivative
F'(z) has valuation exactly 2, while F(z) is divisible by p^3.
Thus k=2. The only possible terms at valuation 3 are 8yz-4A, so

    F(z)=0 mod p^4 iff z=A/(2y) mod p^2.

This determines the asserted lattice. The lifting observation supplies
the required nonzero square.

**III*.** The curve equation excludes v(x)=1; hence v(x)>=2 and
v(y)>=3. At any z divisible by p, -4A is the unique term of valuation
3 in F(z). Again its odd valuation excludes all nonstandard lattices.

The zero determinant valuation gives only the standard lattice, completing
the exact local proof.

## 5. Global consequence with fully explicit bad-small-prime dependence

Let E: y^2=x^3+Ax+B over Z have nonzero discriminant and be minimal at
every p>3. Suppose every bad prime p>3 has potentially good reduction.
For p>3 use lambda_p above, with lambda_p=1 at good primes. Put

    K_p=floor(v_p(2^8 Delta_E)/2)  (p=2,3),
    N_p(K)=sum_{k=0}^K sum_{j=0}^k p^j.

The same rational-quartic-orbit, actual-row-lattice and homogeneous-Thue
argument as in the earlier global note proves

    #E(Z) <= 8 * 7^192 * N_2(K_2) * N_3(K_3)
                       * 2^rank(E(Q)) * product_{p>3} lambda_p.       (7)

There are at most 4*2^rank rational 2-descent orbits, at most 2*7^192
point quartics per occurring actual lattice, and localizations determine
each global lattice. Nothing here assumes simultaneous local attainment.
All p=2,3 dependence is displayed; no uniform bound at wild primes is
being imported without proof. On any family with bounded v_2(Delta_E)
and v_3(Delta_E), the leading factor is absolute for that family.

Thus the elementary refinement is not confined to constant j=0 families.
For example, every tame potentially good additive prime contributes at
most four, and primes of types II and II* contribute nothing even when
their number grows. Multiplicative and potentially multiplicative I_n*
primes are outside this local theorem.

### Fixing the reduction pattern removes every IV/IV* factor

Let S be any subset of the primes of types IV or IV* in (7), and prescribe
epsilon_p in {0,1} for each p in S. On the set of integral points satisfying
indicator(p divides x)=epsilon_p, inequality (7) holds with every factor
lambda_p for p in S omitted.

Here is a direct proof, which also extends the switching calculation in
[REDUCTION_PATTERNS.md](REDUCTION_PATTERNS.md). For a nonstandard lattice,
normalize g as in (2). Comparing the coefficient of X^2Y^2 gives

    x'=x-z^2+d^2,       d=F'(z)/(4q).                        (8)

For unit x in type IV, z=t mod p, v(q)=1 and v(F'(z))>=2.
For unit x in type IV*, z=t mod p^2, v(q)=2 and v(F'(z))>=3.
In both cases d is a nonunit and x-z^2 is divisible by p, so x' is
a nonunit. For nonunit x, the proofs above give v(F'(z))=v(q) and
p divides z. Thus d is a unit and x'=d^2 mod p is a unit. Therefore
every nonstandard lattice switches the reduction status. A standard
lattice preserves it, since an invertible change of variables modulo p
preserves the distinction between the triple-plus-simple root pattern of
a unit-x point quartic and the quadruple root of a nonunit-x point quartic.

Choose a base point in each rational orbit meeting the prescribed set.
Every transformation to another point of that set has standard lattice
at each p in S. The proof of (7) therefore uses only one lattice there.
In particular, when every bad p>3 is of type II, IV, IV* or II*, each
fixed reduction pattern has a bound C_{2,3}*2^rank with C_{2,3} exactly
the displayed small-prime factor in (7), independent of the number or
splitting of the additive primes. This includes the subset of points
with nonsingular reduction at every bad p>3.

## 6. Relationship to component counts and prior work

Let G be the rational component group at a tame potentially good additive
prime. The point-independent maxima in the table agree with

    (|G|+|G[2]|)/2.

Indeed the groups are trivial for II/II*, Z/2 for III/III*, either trivial
or Z/3 for IV/IV*, and trivial, Z/2 or (Z/2)^2 for I0*. The point-specific
counts also agree with unordered component pairs with sum equal to the
component of P: identity P for unit x and the appropriate nonzero component
for nonunit x. This is a numerical/geometric comparison, not a proof that
the actual lattice marking is identical to Sadek's model marking.

Sadek's classification of marked minimal genus-one models, and the
Cremona--Fisher--Stoll minimisation theory, remain close prior work.
Alpoge--Ho supplies the descent, primitive-matrix and Thue inputs, and
already refines local factors by root disks. The contribution established
here is a direct local proof with explicit lattice formulas and the
resulting inequality (7). Whether either formulation is already recorded
requires further literature checking. No general new rank-only phenomenon,
new minimisation theory, or new general component classification is claimed.

Primary source links and the previously inspected statements are recorded in
[the prior literature audit](../2026-10-25-inert/LITERATURE.md). The present
extension has not received independent human review or formal verification.
