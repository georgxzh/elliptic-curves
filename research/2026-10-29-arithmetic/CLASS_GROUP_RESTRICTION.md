# A class-group restriction on ternary component images

Follow-up: the [independent Astra audit](../2026-10-30-binary/ASTRA_AUDIT.md)
checks this statement, denominators, small and ramified primes, signs, and
uniformity of C. No correction was required under the stated hypotheses.
The [binary continuation](../2026-10-30-binary/README.md) supplies its
cubic-algebra counterpart and exact component-image certificates.

Research proof, 2026-10-29. This supplies a concrete arithmetic restriction
missing from the arbitrary-code estimates. Its norm-descent mechanism is
classical; novelty of the particular lattice-count consequence is unestablished.
The proof and exact certificates below do not require a rank calculation,
Mordell--Weil generators, or a completeness claim for a point search.

## 1. The restriction

Let B be a nonzero, nonsquare, sixth-power-free integer. Write B=d k^2,
where d is squarefree, k>0, and L=Q(sqrt(d)). Let C_L be its ordinary
ideal class group, written additively. Define the F_3-vector space

\[
 \overline C_L=C_L/(3C_L+\langle[\mathfrak q]:\mathfrak q\mid6\rangle).
                                                               \tag{1}
\]

Retain the primes p>3 with v_p(B)=2e_p in {2,4} and square unit part.
These primes split in L. Choose a prime ideal \(\mathfrak p\) above each p,
equivalently choose the sign of sqrt(d) in Q_p. Normalize its component
coordinate c_p in F_3 by giving the local point (0,k sqrt(d)) label +1.
For a singular integral point, this is the sign of y/(k sqrt(d)) modulo p;
points in E_0 have label zero. These are the component homomorphisms
proved in the earlier [ternary note](../2026-10-28-refinements/GLOBAL_PATTERN_IMAGE.md).

Let V_3=F_3^w be the product of these local groups, and H_3 its full
rational-point image. Define

\[
 \Psi:V_3\longrightarrow\overline C_L,\qquad
 (c_p)_p\longmapsto\sum_p e_p c_p[\mathfrak p].          \tag{2}
\]

**Theorem.** H_3 is contained in ker(Psi). In particular, if
kappa=rank(Psi), then

\[
 \dim H_3\le\min\{r+\dim E_B(\mathbb Q)[3],\ w-\kappa\}.\tag{3}
\]

Changing the chosen prime above p negates both its ideal class and its
component coordinate, so the restriction is independent of this choice.
The target is the quotient by 3C_L, not just a list of elements of order
three; those are different descriptions unless a suitable identification
has been supplied. The classes over 2 and 3 must be killed unless their
contributions have been analyzed separately.

## 2. Proof by ideal valuations

For an affine rational point P=(x,y), set alpha=y+k sqrt(d). This is a
nonzero element of L and

\[
                   \operatorname{Norm}_{L/\mathbb Q}(\alpha)=x^3. \tag{4}
\]

It defines a fractional principal ideal; rational denominators are allowed.
Fix p>3. If P is nonintegral at p, write v_p(x)=-2j and v_p(y)=-3j
with j>0. These valuations follow directly from the integral curve equation.
The y term dominates k sqrt(d) at every prime above p. Its ideal valuation
is -3j times the ramification index, hence divisible by three.

Now suppose P is integral at p. The following cases exhaust the
sixth-power-free valuations m=v_p(B).

* If m=0, alpha and its conjugate cannot both vanish at a prime above p,
  since their difference is 2k sqrt(d), a unit. At a split prime any
  positive valuation of one factor is therefore 3v_p(x). At an inert
  prime the norm equation gives \(2v_{\mathfrak p}(\alpha)=3v_p(x)\), also forcing
  divisibility by three. There is no ramification here for p>3.
* If m>0 and x is a unit, the norm is a unit and all ideal valuations
  are zero.
* For m=1 or 5 there is no integral point with p dividing x, by valuation
  comparison in y^2=x^3+B: for m=1 the right side has valuation one;
  for m=5 it has valuation three when v_p(x)=1 and five otherwise.
* For m=3 and p dividing x, v_p(x)=1 and v_p(y)>=2. The prime is
  ramified in L. At its unique prime ideal the terms y and k sqrt(d)
  have valuations at least four and exactly three. Thus alpha has
  ideal valuation three.
* For m=2e in {2,4} and p dividing x, valuation comparison gives
  v_p(x)>=e and v_p(y)=e, and forces the unit part of B to be square.
  This is precisely a retained split prime. If c_p=+1, the valuation
  of alpha at the chosen prime is e, while its valuation at the
  conjugate prime is 3v_p(x)-e. For c_p=-1 these valuations are exchanged.
  Modulo three the pair is therefore (e c_p,-e c_p).

Consequently the fractional ideal of alpha has the shape

\[
 (\alpha)=\mathfrak a^3\mathfrak j
       \prod_{p\ {
m retained}}
          (\mathfrak p/\overline{\mathfrak p})^{e_pc_p},  \tag{5}
\]

where \(\mathfrak j\) is supported above 2 and 3, and \(\mathfrak a\) is a
fractional ideal. Exponents c_p can be represented by 0,+1,-1; altering
them by three changes only \(\mathfrak a\). Taking classes in (1) eliminates
the left side, \(\mathfrak a^3\), and \(\mathfrak j\). Since
\([\overline{\mathfrak p}]=-[\mathfrak p]\), the result is 2Psi(c)=0. Multiplication
by two is invertible over F_3, proving Psi(c)=0. The point at infinity
has zero component vector and is covered as well. This proves the theorem.

## 3. Consequence for the integral-point bound

Let S(J) count the distinct supports of a ternary subspace J, and put
J=ker(Psi). The earlier chord/quotient argument now gives

\[
 \#E_B(\mathbb Z)\le C\,2^r A(H_2)
      \min\left\{S(J),\frac{3^{r+\tau_3}+1}{2}\right\}, \tag{6}
\]

where tau_3=dim E_B(Q)[3] and C is the previous absolute constant.
This uses H_3 subset J, which makes support-count inclusion valid;
it does not replace the full image by a subgroup generated by known points.
One may further bound S(J) by min(2^w,(3^(w-kappa)+1)/2).

**Injective-class criterion.** Suppose d is squarefree and nonsquare,
n is positive cube-free and coprime to 6d, and B=d n^2. If the classes
\([\mathfrak p]\) for the split primes p dividing n are linearly independent
in (1), then H_3=0. There are no valuation-three primes in this family,
so H_2=0 as well, and

\[
                     \#E_{d,n}(\mathbb Z)\le C\,2^r.   \tag{7}
\]

The constant is absolute and independent of d,n. Here B is sixth-free:
primes dividing d have valuation one, and primes dividing n have valuation
two or four. The coefficients e_p in (2) are nonzero modulo three, so
independence makes Psi injective even when v_p(n)=2.

In this injective case there is also a direct route avoiding the new
chord argument: every integral point has nonsingular reduction at every
retained prime, so the earlier fixed-pattern theorem allows only the
standard row lattice there. Valuation-one primes dividing d also allow
only the standard lattice. The original lattice/Thue count then gives
(7), with its absolute bounds at 2 and 3.

This criterion removes all 2^w split-prime factors. It is a structural
condition for a base-two estimate, not a universal improvement for Mordell
curves. If w is proportional to r in a collection satisfying the criterion,
the saving against the local-product estimate is exponential in r. No
existence of such a collection with unbounded rank is assumed or proved.
For fixed d, w is bounded by the dimension of (1); it would be misleading
to present this as an unbounded-prime assertion for that fixed d.

## 4. Exact examples

### One excluded split component

Let B=-3475=-139*5^2. The discriminant -139 has precisely the reduced
primitive positive definite forms

    (1,1,35), (5,1,7), (5,-1,7).

Thus its class group has order three, and a prime above 5 represents a
nonzero class. The primes 2 and 3 are inert: -139 is 5 modulo 8 and
2 modulo 3. Their unique prime ideals are principal, so (1) is C_3.
The sole column of Psi is nonzero, proving H_3=0.

The local group at 5 really has order three. For example x=5 gives
y^2=-3350=25*(-134), and -134 is a unit square in Q_5 by Hensel's
lemma. This is a singular local point, excluded from the rational image.
We make no assertion that this curve has a nontrivial rational point.

### Two independent exclusions on a curve with integral points

Let

\[
 B=-196682707=-4027(13\cdot17)^2.
\]

The discriminant -4027 has nine reduced primitive positive definite
forms. The class representatives P=(13,9,79), Q=(17,11,61) have order
three and generate all nine classes. A complete product table is

| i | j | Reduced representative of P^i Q^j |
|---|---|---|
| 0 | 0 | (1,1,1007) |
| 0 | 1 | (17,11,61) |
| 0 | 2 | (17,-11,61) |
| 1 | 0 | (13,9,79) |
| 1 | 1 | (19,1,53) |
| 1 | 2 | (29,-27,41) |
| 2 | 0 | (13,-9,79) |
| 2 | 1 | (29,27,41) |
| 2 | 2 | (19,-1,53) |

The script independently enumerates all reduced forms and produces these
products by lifting discriminant roots, the Chinese remainder theorem,
and unimodular reduction. It also verifies P^3=Q^3=1. The standard
ideal-class/binary-quadratic-form correspondence therefore certifies
C_L=C_3^2 and independence of the two prime classes, up to harmless
choices of inverse classes. Again 2 and 3 are inert and principal.
Thus Psi:F_3^2 -> C_3^2 is an isomorphism and H_3=0.

Both local groups are nontrivial, but every rational point has identity
component at both primes. In particular, every integral point satisfies
gcd(x,221)=1. The curve is nonempty: direct integer arithmetic verifies

\[
                 (1691,68108),\qquad (2027,90176).
\]

The checker also constructs singular Q_13 and Q_17 points by Hensel
lifting, so these exclusions are genuinely global. None of these
certificates uses analytic rank, a GRH-dependent class-group computation,
or a bounded search as a proof of completeness.

## 5. Status and remaining arithmetic question

The additional standard inputs have the following hypotheses here.
The maximal order of a number field is Dedekind, so nonzero fractional
ideals factor uniquely and principal ideals have zero class; L is a
quadratic number field because B is nonsquare. The norm valuation formula
uses residue degrees (two at an inert prime, one at a split or ramified
prime). For the example certificates, both discriminants are negative,
squarefree, and 1 modulo 4, hence fundamental: primitive reduced positive
definite forms give all ordinary ideal classes, with leading coefficient
at most sqrt(|D|/3). The enumerator uses exactly this finite range.
The chosen prime roots are unramified and lift uniquely. The local
point certificates use Hensel only at nonzero square roots modulo p,
whose derivative 2r is a unit. No class-number estimate or heuristic
distribution of prime classes is imported.

The norm identity and class-group descent are standard. The concrete
advance in this repository is a proved component-image constraint,
its combination with the lattice bound, and fully checkable exclusions
of locally admissible components. See [the literature comparison](LITERATURE.md).
No novelty claim is made for the norm-descent principle.

This does not resolve the universal exponential-base problem. The
[mixed-image counterexample](EXTREMAL_AND_INTEGRAL.md) shows that both
code estimates can be attained on a Mordell curve. Moreover, class-group
restrictions can be vacuous. Any further uniform saving must address
such cases, or prove a deficit in actual integral transformations.
