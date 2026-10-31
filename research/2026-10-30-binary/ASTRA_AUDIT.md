# Independent audit of the class-group restrictions

Audit date: 2026-10-30. Starting revision: `c0f8eba` on
`research/inert-prime-fibres`. This is a separate mathematical and code
review of the ternary restriction and the proposed binary analogue. It is
not a human review or a claim of novelty. No rank computation, generator
completeness assumption, or class-number heuristic is used.

**Verdict.** The theorem and injective-class corollary in
[`CLASS_GROUP_RESTRICTION.md`](../2026-10-29-arithmetic/CLASS_GROUP_RESTRICTION.md)
are valid under their stated hypotheses and the lattice/Thue inputs
identified in the preceding notes. The proposed binary class-group
restriction is also valid, provided it uses the maximal order of the
cubic étale algebra, labels valuation-three primes using `theta/p`, and
treats the rational 2-torsion point separately when the algebra is
reducible. No counterexample or necessary correction to the ternary
statement was found. The binary statement needs the qualifications
spelled out below.

## 1. Ternary descent: denominators, ramification, and signs

Let `B=d k^2` with `d` squarefree and nonsquare, and work in the maximal
order of the quadratic **field** `L=Q(sqrt(d))`. The nonsquare hypothesis
ensures that `alpha=y+k sqrt(d)` is nonzero, including when `y=0`.
Its norm is exactly `x^3`. Fractional ideals, rather than integral ideals
only, are essential for the full rational-point image.

At a prime `p>3`, a nonintegral rational point has
`v_p(x)=-2j`, `v_p(y)=-3j` for an integer `j>0`. At every prime ideal
above `p`, the integral term `k sqrt(d)` has nonnegative valuation,
whereas `y` has valuation `-3j e(P/p)`. The latter dominates, so every
ideal exponent is divisible by three, including at ramified primes.
There is no omitted denominator contribution.

For integral points, the following checks exhaust the possibilities:

| `m=v_p(B)` | Singular integral point behavior | Ideal exponents away from 3-divisible terms |
|---|---|---|
| 0 | The two conjugate factors cannot both vanish | All exponents divisible by 3 |
| 1 or 5 | No point with `p` dividing `x` | None |
| 2 or 4 | `m=2e`, `v_p(x)>=e`, `v_p(y)=e`; the unit part is a square | At the split pair: `(e c,-e c)` modulo 3 |
| 3 | `v_p(x)=1`, `v_p(y)>=2`, allowing `y=0` | The unique ramified-prime exponent is exactly 3 |

For `m=0`, the inert norm formula is `2 v_P(alpha)=3 v_p(x)`,
which does force divisibility by three. At split primes, conjugate
factor coprimality gives the same conclusion. At `m=3`, the normalized
ideal valuations of `y` and `k sqrt(d)` are respectively at least 4 and
exactly 3; there is no cancellation. If `x` is a unit, the integral
norm is a unit and all exponents vanish in every case.

The sign convention is consistent. At the chosen split prime, choose
the local square root `b=k sqrt(d)` and label `(0,b)` by `+1`.
For component `+1`, `y/b=1` modulo `p`, so `y+b` has valuation
exactly `e`, not the complementary valuation. The conjugate exponent
is `3 v_p(x)-e`. Thus the ideal class equation is

\[
 0=2\sum_p e_p c_p[\mathfrak p]
 \quad\text{in }C_L/(3C_L+\langle[\mathfrak q]:\mathfrak q\mid6\rangle).
\]

Multiplication by 2 is invertible in this quotient. Swapping the chosen
prime swaps the component sign and negates the prime class, preserving
the map. This checks the potential sign ambiguity explicitly.

The quotient by prime classes above 2 and 3 is sufficient: all untreated
valuations are supported there. It must not silently be omitted, and
ordinary ideal classes are the correct classes for this argument, also
when `d>0`. No positivity or narrow-class condition is used. Likewise,
`C_L/3C_L` should not be replaced canonically by the subgroup `C_L[3]`.

## 2. The absolute constant and the exact examples

For `B=d n^2`, with `d` squarefree and `n` cube-free and coprime to
`6d`, primes dividing `d` have valuation 1 and those dividing `n` have
valuation 2 or 4. Thus `B` is sixth-power-free, and there are no
valuation-three binary factors. Linear independence of the retained
prime classes makes the ternary map injective because its coefficients
`v_p(n)` are 1 or 2 modulo 3. Consequently `H_3=H_2=0`.

The uniform constant follows from the **sixth-free** lattice theorem,
not merely from the older bound with a constant `A_d`. In
[`GLOBAL_SIXTH_FREE.md`](../2026-10-25-inert/astra/GLOBAL_SIXTH_FREE.md),
the determinant caps at 2 and 3 are uniformly 11 and 6, giving
`N_2(11)=8178` and `N_3(6)=1636`. Primes dividing `d` outside 6
contribute only the standard lattice. With every retained prime also
standard, the same absolute

\[
 C=4\,7^{192}\,8178\,1636
\]

works independently of both `d` and `n`. This conclusion inherits the
stated rational descent and homogeneous Thue inputs; the class-group
argument introduces no additional dependence. Inclusion of support
sets under `H_3 subset ker(Psi)` is valid, as is the displayed
dimension/support-count bound. There is no assertion that known points
generate the full image.

I reran the exact class-certificate and Hensel functions from
[`verify_arithmetic.py`](../2026-10-29-arithmetic/verify_arithmetic.py)
without rewriting its result file. For discriminants `-139` and
`-4027`, they produce respectively 3 and 9 reduced classes and exactly
the displayed product tables, including the cube relations. The
enumeration range is sufficient since reduced positive forms satisfy
`a<=sqrt(|D|/3)`; the boundary convention selects one proper class
representative. The lifting/CRT construction consistently multiplies
the chosen prime ideals, with only a harmless global choice of inverse
class. Both discriminants are fundamental; 2 and 3 are inert, so their
unique ideals are principal. The Hensel witnesses have unit derivative.
Both displayed integral points on `B=-196682707` satisfy the equation
exactly and have `gcd(x,221)=1`.

These certificates establish the claimed exclusions. They do not
establish a rank or completeness of integral points, and the note does
not use them for either purpose. Fixed `d` bounds the number of
independent retained prime classes, exactly as the note acknowledges.

## 3. Correct binary statement

Let `B` be any nonzero sixth-power-free integer and put

\[
 K=\mathbb Q[T]/(T^3+B),\qquad \theta=T\bmod(T^3+B),
 \qquad \mathcal O_K=\prod_i\mathcal O_{K_i}.
\]

The polynomial is separable because `B!=0`, so `K` is an étale algebra.
Its class group is the product of the ordinary ideal class groups of
its field factors. Define

\[
 \overline C_K=\operatorname{Cl}(\mathcal O_K)/
 \bigl(2\operatorname{Cl}(\mathcal O_K)
       +\langle[\mathfrak q]:\mathfrak q\mid6\rangle\bigr).
\]

At a prime `p>3` with `v_p(B)=3`, set `u=B/p^3` and `eta=theta/p`.
The element `eta` is integral, and `T^3+u` has discriminant `-27u^2`,
a `p`-adic unit. It follows that

\[
 \mathcal O_K\otimes\mathbb Z_p=\mathbb Z_p[\eta],
\]

an unramified étale algebra. In particular, its prime ideals correspond
to the irreducible factors of `T^3+u` over `F_p`.

For each linear root `r`, let `P_{p,r}` be the corresponding prime of
norm `p`. Map the nonzero component with root label `r` to
`[P_{p,r}]` in `overline C_K`, and map the identity component to zero.
This defines a linear map `Psi_2:V_2 -> overline C_K`:

* If there is one root, the component block is `F_2`, so linearity is
  immediate.
* If there are three roots, the three nonzero components add to zero,
  and the three prime classes also add to zero because their product
  is `(p)`.
* If there are no roots, the component group is trivial.

Then the full rational component image satisfies

\[
                         H_2\subseteq\ker\Psi_2.
\]

The equivalent parity formulation in the proposed analogue is correct:
component `r` has parity zero at `P_{p,r}` and parity one at all other
primes over `p`. Taking classes, this complementary sum equals
`-[P_{p,r}]=[P_{p,r}]` modulo 2. At splitting type `(1,2)`, the
degree-two prime occurs **once** in this ideal-class sum; its residue
degree is used in the norm formula, not as an ideal exponent.

## 4. Binary valuation proof and the index issue

First suppose the descent element `alpha=x-theta` is invertible in `K`.
Its norm is `x^3+B=y^2`. The fractional-ideal parity analysis is:

* For a nonintegral point, `v_p(x)=-2j` dominates the integral `theta`
  in every factor. Thus `v_P(alpha)=-2j e(P/p)` is even.
* For integral points with unit `x` at `p|B`, all valuations are zero.
* If `p` does not divide `6B`, the algebra is unramified and generated
  by `theta`. Only a linear residue factor can have `theta=x` modulo
  a prime. There is at most one such factor, and its ideal valuation
  equals `v_p(y^2)`, which is even; all other valuations vanish.
* At `m=1` or `m=5`, singular integral points are impossible.
* At `m=2` or `m=4`, the Newton slope has denominator 3, so the local
  cubic is a totally ramified degree-three field. Normalized ideal
  valuation gives `v_P(theta)=m`, while
  `v_P(x)=3v_p(x)>=3m/2>m`. Hence `v_P(alpha)=m`, which is even.
* At `m=3`, a singular point has `v_p(x)=1`, `v_p(y)>=2`. Write
  `z=x/p`. In the unramified algebra generated by `eta`,
  `alpha=p(z-eta)`. All factors except the matching linear root
  have valuation 1. At that root, the norm formula gives
  `v_P(z-eta)=2v_p(y)-3`, an odd integer. Its valuation in `alpha`
  is therefore even.

These cases give a square fractional ideal times the prescribed parity
ideals times an ideal supported over 2 and 3. Taking classes proves
the inclusion. Infinity has zero component vector.

The maximal-order requirement is substantive. `Z[theta]` is not locally
maximal at a valuation-three prime: `theta` reduces to a multiple root,
whereas `theta/p` gives the correct unramified factorization. Factoring
`T^3+B` directly modulo such a prime would lose the root labels.
At `m=2,4`, a nonmaximal monogenic order may also occur, but the
ramification/normalized-valuation argument above takes place in the
maximal order and does not use unique ideal factorization in that
smaller order. No extra quotient by index primes outside 2 and 3 is
needed once these local cases are treated correctly.

## 5. Reducible algebra and vanishing descent element

The only reducible case is `B=-a^3` for a nonzero integer `a`; sixth-free
`B` makes `a` squarefree up to sign. Then

\[
 K\simeq\mathbb Q\times\mathbb Q(\zeta_3),\qquad
 \theta\longmapsto(a,a\zeta_3),\qquad
 \mathcal O_K=\mathbb Z\times\mathbb Z[\zeta_3].
\]

Both factors have class number one, so `overline C_K=0`. The binary
class-group restriction is therefore valid but completely vacuous for
this entire subfamily, including its rational 2-torsion.

At the rational point `T=(a,0)`, `x-theta` has zero rational component
and is not invertible in `K`. It has no nonzero fractional principal
ideal of the type used in the proof. Applying the ordinary norm/ideal
argument to this element would be an error. The simplest repair is to
handle `T` separately: its image lies in the kernel because the target
is zero. All other affine rational points have `y!=0`, and the descent
element is invertible, so the preceding proof applies. At primes
`p>3` dividing `a`, the point `T` has the nonzero root label `a/p`;
it must not be assigned the smooth label zero.

If an everywhere-defined standard 2-descent representative is desired,
replace the vanishing rational coordinate at `T` by the derivative:

\[
 \delta(T)=(3a^2,\ a(1-\zeta_3)).
\]

Its norm is `9a^4=(3a^2)^2`. At `p>3` dividing `a`, its rational
valuation is 2 and each quadratic-factor prime valuation is 1, exactly
the required complementary parity. This alternative is consistent,
but unnecessary for the class-group containment because the entire
target already vanishes.

## 6. Checks, scope, and consequences

In addition to the exact ternary certificates, I manufactured integral
points from every `-60<=x<=60`, `0<=y<=700` by setting `B=y^2-x^3`,
discarded zero/non-sixth-free coefficients, and checked the singular
valuation alternatives at `p=5,7,11,13,17,19`. This exercised 5,582
valuation-two cases, 875 valuation-three cases, and 156 valuation-four
cases with no failure. In split binary blocks, the complementary
three-bit parity vectors satisfy exactly the `F_2^2` addition law.
The finite check is corroboration only; the exhaustive valuation proof
is what establishes the theorem for all rational points.

The binary result supplies a necessary class-group constraint, not a
description of the full component image. It can be vacuous even for an
irreducible cubic field, and unit/squareclass conditions can impose
additional restrictions not detected by ideal classes. A nonzero map
or an injective map requires an actual class-group/prime-class
certificate. Known point subgroups cannot certify an upper bound for
the full image by themselves.

If `D=dim V_2` and `kappa_2=rank Psi_2`, then the valid automatic bound
is `dim H_2<=min(r+dim E(Q)[2],D-kappa_2)`. Inserting this into the
existing dimension bound for `A(H_2)` is justified. Replacing
`A(H_2)` directly by a different subspace statistic requires its own
monotonicity argument; the class-group containment alone should not
be treated as that argument. The injective case immediately forces
`H_2=0` and `A(H_2)=1`.

No universal rank-base improvement, infinite family with growing rank,
or novelty conclusion follows from this audit.

## 7. Independent check of the explicit binary obstruction certificate

After the preceding review, the root agent supplied a certificate in
`K=Q(a)`, `a^3=58`. I checked its integer identities independently and
audited its local and class-field hypotheses. It is valid.

The polynomial discriminant is `-27*58^2=-90828`, so only 2, 3, and 29
can divide the index of `Z[a]` in the maximal order. The polynomial is
Eisenstein at 2 and 29. At 3, the polynomial of `a-1` is
`T^3+3T^2+3T-57`, which is Eisenstein. Each of these completions is
totally ramified of degree three, with the specified element a
uniformizer and residue field the prime field; its integer ring is
generated by that uniformizer over `Z_p`. Since `Z[a-1]=Z[a]`, the
index is one at every possible index prime. Thus `O_K=Z[a]`.

Put

\[
 \alpha=673+190a-94a^2,\qquad \beta=1+2a+3a^2.
\]

Exact resultant and polynomial reduction give

\[
 N(\alpha)=361,\qquad
 \alpha-\beta^2=-24-336a-104a^2\in8\mathcal O_K.
\]

At 19 the roots of `T^3-58` are `1,7,11`, and the respective residues
of `alpha` are `9,0,15`. Only the root-7 prime divides `alpha`, so
`(alpha)=P_7^2`. Every finite ideal valuation is therefore even.
At every odd residue characteristic, adjoining the square root of
such an element is unramified or split.

The prime over 2 requires a separate argument. Here `a` has zero
residue and `beta` has residue 1, so `beta` is a unit and
`alpha/beta^2` belongs to `1+8O_{K_2}`. The strong Hensel criterion
at the approximate root 1 gives a square root: the valuation of the
error is at least `3v(2)>2v(2)`, the strict bound needed for derivative
2. This remains valid in the ramified completion. At 3, `a` has
residue 1 and `alpha` has residue 1; the usual unit-derivative Hensel
lemma gives a square root there as well. Hence every prime over 2
and 3 splits in `K(sqrt(alpha))/K`.

The cubic field has one real embedding. Its norm identity is the real
value of `alpha` times a positive complex absolute square; since the
norm is positive, `alpha` is positive at that real embedding. Thus
the quadratic extension also splits at the real place. At the
degree-one prime over 5, `a=2` in the residue field and `alpha=2`,
a nonsquare modulo 5. This certifies that the quadratic extension is
nontrivial.

Global Artin reciprocity for an abelian extension unramified at every
finite prime and split at every real place therefore gives a
nontrivial character of the **ordinary** ideal class group, factoring
through

\[
 \operatorname{Cl}(K)/(2\operatorname{Cl}(K)
                   +\langle[\mathfrak q]:\mathfrak q\mid6\rangle)
 \longrightarrow\mathbb F_2.
\]

At 19 the root-1 prime has character zero because 9 is a square,
and the root-11 prime has character one because 15 is a nonsquare.
The root-7 prime then has character one from the principal ideal
relation `P_1 P_7 P_11=(19)`. This last step legitimately avoids
trying to read a Frobenius value from a zero residue of `alpha`.
At the sole degree-one prime over 5 the character is one, by the
nonsquare residue 2.

For `B=-58*19^3=-397822`, the only binary block is the split block at
19, and the character kernel is the line whose nonzero root label
is 1. The exact identity

\[
 55955^2-1463^3=-397822,\qquad 1463/19=77\equiv1\pmod{19}
\]

provides a rational point with this nonzero component. Thus the full
`H_2` is exactly that line: containment gives the upper bound and
the point supplies the matching lower bound. Consequently
`A(H_2)=3/2`, compared with `A(V_2)=5/2`. For
`B=-58*5^3=-7250`, the sole binary block has dimension one and its
nonzero component has nonzero character. Hence `H_2=0`.
In both cases the remaining coefficient primes have valuation one,
so there are no ternary blocks. These image conclusions require no
rank or generator-completeness calculation.

This certificate imports the standard Hilbert-class-field/Artin
reciprocity theorem in addition to the elementary norm and Hensel
arguments. Its applicability has been checked above. It proves the
required nonzero quotient and character values without computing the
full class group or assuming GRH.

## 8. Counterexample to omitting the primes above 2

Additional audit, 2026-10-31. The root agent supplied the following
counterexample, which I checked independently. It proves that the
binary theorem cannot in general retain the prime classes above 2 in
its target, even if it still kills those above 3.

Let `K=Q(a)`, where `a^3=11`. The polynomial discriminant is
`-27*11^2=-3267`, so only 3 and 11 can divide the index of `Z[a]`.
The polynomial is Eisenstein at 11. The element `a+1` has polynomial
`T^3-3T^2+3T-12`, which is Eisenstein at 3. The same local
uniformizer argument as in Section 7 proves `O_K=Z[a]`.

Set `delta=9-4a`. Exact arithmetic gives `N(delta)=25`. Modulo 5,
`T^3-11` has the unique linear root 1; the remaining factor is
irreducible quadratic. The element `delta` vanishes only at that
linear prime `P_5`, so

\[
                         (\delta)=\mathfrak P_5^2.
\]

Consequently all its finite ideal valuations are even. At every odd
prime the quadratic extension `M=K(sqrt(delta))` is therefore
unramified or split. At `P_5`, more is known: the root 1 lifts to
`a=21` modulo 125, since `21^3=11` modulo 125. Thus

\[
 \delta/25\equiv(9-4\cdot21)/25=-3\equiv2\pmod5.
\]

Here 5 is a uniformizer at this unramified degree-one prime, so
dividing by its square is legitimate. The nonsquare unit residue 2
proves that `M/K` is unramified and nonsplit at `P_5`. Its quadratic
Artin character has `chi(P_5)=1`.

At 2, use the integral generator `z=(1+sqrt(delta))/2`, which satisfies

\[
                         z^2-z+a-2=0.
\]

Its discriminant is `delta`, a unit at 2, so this quadratic algebra
is étale there. Moreover,

\[
 T^3-11\equiv(T+1)(T^2+T+1)\pmod2.
\]

At the degree-one prime over 2, `a=1` in the residue field and the
quadratic reduces to `z^2+z+1`, irreducible over `F_2`. At the
degree-two prime, the residue of `a` lies in `F_4` and satisfies
`a^2+a+1=0`, so `Tr_{F_4/F_2}(a)=1`. The characteristic-two
quadratic `z^2+z+a` is therefore irreducible over `F_4`. I also
checked all its residue values directly. Hence `M/K` is unramified
and nonsplit at **both** primes above 2; their character values are
both 1. This is compatible with their sum being the principal
ideal class of `(2)`.

At the unique prime over 3, `a=2` and `delta=1` in the residue field.
The ordinary Hensel lemma, with derivative 2 a unit, gives a local
square root of `delta`, so that prime splits. Finally, `K` has one
real embedding; the positive norm 25 implies that `delta` is positive
there. The real place therefore splits as well.

The resulting nontrivial extension is quadratic, unramified at every
finite prime, and split at the real place. Artin reciprocity gives a
character

\[
 \chi:\operatorname{Cl}(K)/
 \bigl(2\operatorname{Cl}(K)+
       \langle[\mathfrak q]:\mathfrak q\mid3\rangle\bigr)
 \longrightarrow\mathbb F_2
\]

with `chi(P_5)=1`. It does **not** factor through the further quotient
by primes over 2. No class-number computation is needed for these
conclusions.

Now take the sixth-power-free coefficient

\[
 B=11000=2^3\,5^3\,11,
 \qquad E:y^2=x^3+11000.
\]

Identify its cubic étale algebra with `K` by `theta=-10a`. The only
retained binary prime `p>3` is 5. At this prime,
`eta=theta/5=-2a` has polynomial `T^3+88`, whose sole linear root
modulo 5 is `-2`. This is precisely the prime `P_5`, where `a=1`.
The exact integral point

\[
                         P=(-10,100)
\]

has `v_5(x)=1`, `v_5(y)=2`, and nonzero component label
`x/5=-2`. Thus it realizes the entire one-dimensional binary block,
and `H_2=F_2`. A proposed class map with the primes over 2 omitted
from the quotient would send this realized component to `[P_5]`,
whose character is 1, and would falsely exclude it. This is an exact
counterexample to that strengthened statement. It does not show that
every individual prime above 2 or the primes above 3 are separately
indispensable in every field.

## 9. Lattice consequence for the root-1 line at 19

For `B=-397822` and `P=(1463,55955)`, Section 7 proves that the full
binary image is `H_2={0,c}`, where `c` is the nonzero root-1 component
at 19. The source point `P` itself has this component. Components are
constant throughout its rational 2-class because the component group
has exponent two.

In the exact local lattice rule at a split valuation-three prime, a
source with nonzero component `c` has the standard row lattice
precisely for chord components in `{0,c}`. The other two local
components give the unique nonstandard lattice. Every rational chord
point has its component in the **full** global image `H_2={0,c}`.
Therefore every transformation from `P` to an integral point quartic
in its rational 2-class has the standard row lattice at 19.

Equivalently, there is just one retained binary block and

\[
 D_c=\langle c\rangle=H_2,\qquad
 H_2/(H_2\cap D_c)=0.
\]

The identity transformation realizes the standard lattice, so the
single possible output is indeed the standard one. The previously
proved denominator and infinite-slope cases obey the same local rule.
This conclusion concerns the 19-adic row lattice; it makes no claim
that only one global lattice occurs after including primes 2 and 3.
