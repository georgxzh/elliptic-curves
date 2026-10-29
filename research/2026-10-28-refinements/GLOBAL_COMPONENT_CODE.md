# A component-code saving in the sixth-power-free lattice bound

Research derivation, 2026-10-28. This is a proved refinement of the bound in
`../2026-10-25-inert/astra/GLOBAL_SIXTH_FREE.md`, conditional on the same
imported descent and Thue bounds used there. No novelty claim is made.

## Statement

Let B be a nonzero sixth-power-free integer, r the rational Mordell rank,
and lambda_p(B) the exact point-independent factors in the earlier note.
Let S consist of the primes p>3 for which v_p(B)=3 and

    rho_p = #{w in F_p : w^3 = -B/p^3} > 0.

Put d_p=log_2(1+rho_p), which is 1 or 2. Let E_0(Q_p) denote the subgroup
of points with nonsingular reduction on y^2=x^3+B, including infinity.
There is a component homomorphism

    alpha: E_B(Q)/2E_B(Q) -> V = product_{p in S} E_B(Q_p)/E_0(Q_p),

where each factor is an F_2-vector space of dimension d_p. Write H for
its image, s=dim_F2 H, and define its block-support enumerator

    W(H) = (1/|H|) sum_{h in H} 2^{-wt(h)},
    wt(h) = #{p in S : h_p != 0}.

Then, with exactly the absolute constant C of the earlier global note,

    #E_B(Z) <= C 2^r (product_{p>3} lambda_p(B)) W(H).       (1)

In particular, writing c=#{p in S:d_p=2} and
q=min(c,floor(s/2)),

    W(H) <= (5/8)^q (3/4)^(s-2q).                         (2)

This is a genuine group-theoretic invariant and a dimension-only saving,
rather than a sum whose input requires enumerating the integral points.
It is strictly smaller than the old bound whenever H is nonzero.

If the global component map is surjective and b=#{p in S:d_p=1}, then

    W(H) = (3/4)^b (5/8)^c.

Consequently the combined valuation-three contribution changes from
2^b 4^c to (3/2)^b (5/2)^c under that hypothesis. No surjectivity is
asserted in general. If s=1 and the unique nonzero vector of H has
support t, the exact saving is W(H)=(1+2^{-t})/2.

## Elementary identification of the local quotient

Fix p>3, B=p^3u with u a p-adic unit. The standard nonsingular-reduction
subgroup E_0(Q_p) consists of O, points with nonintegral coordinates,
and integral points with x a unit. Indeed the reduced affine cubic is
y^2=x^3, whose sole singular point is (0,0). We use the standard fact
that nonsingular reduction defines a subgroup; see J. H. Silverman,
*The Arithmetic of Elliptic Curves*, Chapter VII, section 2, Proposition
2.1 (the reduction map and its kernel). No Tate-algorithm table or
component-group classification is required below.

Every integral point Q=(x,y) with x nonunit has v_p(x)=1 and
v_p(y)>=2, by the valuation calculation in the local note. Its residue
X=x/p solves X^3=-u modulo p. Each root lifts uniquely to w in Z_p
with w^3=-u, since 3w^2 is a unit. Set T_w=(pw,0), a nonzero local
2-torsion point. If Q=T_w, its coset is already represented by T_w.
Otherwise, write n=v_p(y)>=2. Since X=w modulo p,

    v_p(x^2+pw x+p^2w^2)=2,
    y^2=(x-pw)(x^2+pw x+p^2w^2),

and hence v_p(x-pw)=2n-2. The addition slope y/(x-pw) has valuation
2-n. The x-coordinate of Q+T_w is

    (y/(x-pw))^2-x-pw.

It is a unit if n=2, and has negative valuation if n>2. Thus Q+T_w
belongs to E_0(Q_p), proving Q belongs to T_w+E_0(Q_p).

Distinct roots give distinct cosets: the difference of distinct nonzero
local 2-torsion points is another nonzero local 2-torsion point, with
nonunit integral x, and so is outside E_0(Q_p). We have proved that
E(Q_p)/E_0(Q_p) has exactly 1+rho_p elements, all represented by
2-torsion. It is therefore an elementary abelian 2-group, and
2E(Q_p) is contained in E_0(Q_p). This proves that alpha is well-defined.

For clarity, when rho_p=1, p=2 modulo 3 and d_p=1; when rho_p=3,
p=1 modulo 3 and d_p=2. The unused rho_p=0 case has trivial quotient.

## Orbit weights and the global count

Rational point quartics in one rational twisted-PGL_2 orbit correspond
to one class in E_B(Q)/2E_B(Q), so their local component labels agree.
Choose an integral point P in an occurring orbit. At p in S:

* If alpha(P)_p=0, then x(P) is a unit and the exact number of local
  row lattices is 1+rho_p=lambda_p(B).
* If alpha(P)_p is nonzero, then x(P) is nonunit. The exact local count
  is 1 when d_p=1, and 2 when d_p=2, by the earlier local theorem.
  In both cases this is lambda_p(B)/2.

The other local factors and the uniform bound per global lattice are
unchanged. Therefore the number of integral points in an occurring
global 2-class xi is at most

    K (product_{p>3} lambda_p(B)) 2^{-wt(alpha(xi))},

where K=2*7^192*N_2(11)*N_3(6) is the earlier per-orbit constant.
Include also the global 2-classes having no integral points, which can
only increase this upper bound. If tau=dim_F2 E_B(Q)[2]<=1, then
|E_B(Q)/2E_B(Q)|=2^(r+tau), and every fiber over H has size
2^(r+tau-s). Thus the sum is exactly bounded by

    K 2^(r+tau) (product lambda_p(B)) W(H).

Using 2^tau<=2 proves (1) with C=2K. If rational 2-torsion is absent,
one can use C/2 instead, just as in the earlier argument.

## Proof of the dimension-only estimate

This is a purely finite-linear-algebra statement. Order the blocks
V_1,...,V_m, each of dimension at most 2. Let H_i be the projection of
H onto its first i blocks, and let

    k_i = dim H_i - dim H_{i-1} in {0,1,2}.

For a uniform element of H_i, conditioned on its first i-1 blocks, the
last block is uniform in an affine subspace of V_i of dimension k_i.
The average of f(v)=1 for v=0 and f(v)=1/2 otherwise over any such
affine subspace is at most

    a_k = (1+2^{-k})/2,
    a_0=1, a_1=3/4, a_2=5/8.

Integrating the final block first, then repeating, gives
W(H)<=product_i a_{k_i}. If n_2 counts the indices with k_i=2, then
sum k_i=s and n_2<=min(c,floor(s/2)). Moreover
a_2/a_1^2=10/9>1. Consequently

    product_i a_{k_i}
      = (5/8)^{n_2}(3/4)^{s-2n_2}
      <= (5/8)^q(3/4)^{s-2q}.

This proves (2). It is sharp among abstract subspaces with these block
dimensions: take H supported on q full two-dimensional blocks and
s-2q one-dimensional subspaces of distinct unused blocks. Sharpness for abstract codes
does not assert realization by Mordell curves over Q.

## Computability and limitations

Given generators of E_B(Q) modulo 2E_B(Q), H is obtained by finite-field
linear algebra. At each p in S, a rational point has zero label when
it is nonintegral or has unit x; otherwise its label is the residue x/p,
a root of T^3+u. For a split block, label two root components by a basis
of F_2^2 and the third by their sum. Global rational 2-torsion must be
included among the generators.

Generators only for a subgroup G give H_G contained in H. Both the exact
weight W(H_G) and the dimension bound using s_G=dim H_G give valid,
possibly weaker, upper bounds without any saturation or completeness
claim about G. Indeed, expanding the factors in the definition gives
the additional exact formula

    W(H) = 2^{-|S|} sum_{T subset S} 2^{-dim pi_T(H)},       (3)

where pi_T denotes projection onto the blocks in T. To see this, use
2^{-wt(h)}=2^{-|S|} product_{p in S}(1+1_{h_p=0}), and average each
expanded term: the probability that h vanishes on T is
|ker(pi_T|H)|/|H|=2^{-dim pi_T(H)}. Since projection dimensions can only
increase on enlarging H, formula (3) proves W(H)<=W(H_G).

Thus even one known rational point with nonzero component at t primes
of S certifies the unconditional saving (1+2^{-t})/2 in (1). Several
known points certify their full code weight, regardless of whether they
generate the Mordell--Weil group. For example, if B=-a^3 is sixth-power
free, the rational 2-torsion point (a,0) is nontrivial at every p>3
dividing a, and gives this saving with t=#{p>3:p divides a}.

For a concrete example without rational 2-torsion, take

    B = 67,821,390 = 2 * 3^2 * 5 * 7^3 * 13^3,
    P = (91, 8281).

The identity 8281^2-91^3=B verifies the point and the factorization
verifies sixth-power-freeness. The point P has nonzero component at
both 7 and 13. Each is a split two-dimensional block, since
B/p^3=-(91/p)^3 modulo p and p=1 modulo 3. Thus the old product at
these two primes is 4*4=16. The subgroup generated by P has component
image {0,alpha(P)}, whose exact weight is (1+1/4)/2=5/8. Therefore

    #E_B(Z) <= (C/2) 2^r * 10.

The factor C/2 is available because -B is not a rational cube, so
E_B(Q)[2]=0; retaining C is also valid. No rank or saturation calculation
is needed for the factor 10, compared with 16 in the previous bound.
For an arithmetic consistency check, 2P=(-719/4,-62999/8) has unit
x-coordinate at both 7 and 13, as required by the component calculation.

No uniform lower bound on s is claimed. If all rational points have
trivial local components at these primes, W(H)=1 and this argument gives
no gain. The theorem does not remove the valuation-two/four factors.
It improves only the valuation-three factors by using global component
compatibility. These statements remain proof drafts pending independent
human review; the finite-code check verifies only the combinatorial step.

## Reproducible finite checks

Run `python research/2026-10-28-refinements/global_verify_component_code.py`
from the repository root. It exhaustively checks 12,668 subspace/layout
pairs across all 16 unordered one-/two-dimensional block layouts of
total dimension at most six. It verifies (2), attainment of its abstract
maximum at every tested dimension, (3), and subgroup monotonicity for
the tested codimension-one subspaces. It also checks the exact rational
arithmetic of the displayed Mordell point and its double. All checks
passed; they do not prove the imported global descent and Thue results.
Pass `--json` to emit the counts and exact example as a machine-readable
JSON record instead of the human-readable output.
