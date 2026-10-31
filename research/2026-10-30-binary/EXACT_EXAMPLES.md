# Exact binary images and an essential exceptional-prime counterexample

Proof and certificate, completed 2026-10-31. These arguments use elementary
ideal arithmetic and the ordinary Hilbert class field theorem. They do not
require a class-number computation, GRH, rank, or a Mordell--Weil basis.
The associated [standard-library checker](verify_binary.py) verifies the
integer identities and residue certificates. It is not a formal proof of
class field theory. Astra's independent review is in [the audit](ASTRA_AUDIT.md).

## 1. A character in the cubic field of discriminant -90828

Let a³=58 and K=Q(a). The order Z[a] is maximal. Indeed the polynomial
discriminant is -27·58², so only 2,3,29 can divide its index. The
polynomial is Eisenstein at 2 and 29; the polynomial of a-1 is
T³+3T²+3T-57, Eisenstein at 3. An Eisenstein root generates the ring
of integers in each of these totally ramified local extensions. Thus
O_K=Z[a]. This also proves irreducibility and the asserted ramification.

Set

    alpha = 673+190a-94a²,     beta = 1+2a+3a².

Direct multiplication gives

    Norm(alpha) = 361,
    alpha-beta² = -24-336a-104a² ∈ 8 O_K.

At 19 the roots of T³-58 are 1,7,11. The corresponding residues of
alpha are 9,0,15. Since the norm is 19² and only the root-7 prime
P_7 divides alpha, unique ideal factorization gives (alpha)=P_7².
Every finite valuation of alpha is even.

Consequently L=K(sqrt(alpha)) is unramified at every odd prime: after
removing an even power of a uniformizer, adjoining a square root of a
unit gives an unramified or split extension in odd residue characteristic.
At the unique prime over 2, beta is a unit and alpha/beta²∈1+8O.
Strong Hensel at 1 applies since v(8)>2v(2), also in this ramified
completion; thus alpha is a local square. At the prime over 3, a has
residue 1 and alpha has residue 1, so unit-derivative Hensel also gives
a square. Both primes split in L.

There is one real embedding. Norm(alpha)>0 implies alpha is positive
there, since the other two embeddings contribute a positive absolute
square. Hence the real place splits too. At 5 the polynomial has the
single root 2, and alpha has residue 2, a nonsquare; L is nontrivial.

The Hilbert class field theorem now supplies an ordinary ideal-class
character, with all its hypotheses checked above:

    chi : Cl(K)/(2Cl(K)+<[q]:q|6>) → F₂.

The value is zero on split primes and one on primes inert in L/K.
In particular chi(P_5)=1. At 19, chi(P_1)=0 and chi(P_11)=1 by their
unit residues. Since P_1 P_7 P_11=(19), chi(P_7)=1. This use of the
principal ideal relation is essential if one has only the residues:
a zero residue of alpha does not determine its Frobenius.

As a separate direct check, the root-7 lift modulo 19³ is 5840;
alpha(5840)/19²≡10 mod19, a nonsquare. This division is understood
modulo 19³ and agrees with the principal-ideal calculation.

## 2. A nontrivial local group with zero rational image

For B=-58·5³=-7250, identify theta=5a. The only retained binary prime
is 5, whose normalized cubic T³-58 has one root. Thus V₂=F₂, and the
binary theorem maps its nonzero element to [P_5]. Since chi(P_5)=1,

    H₂=0,     A(H₂)=1,     H₃=0,     S(H₃)=1.

The nonzero local component really exists: the simple root 2 lifts to
b∈Q_5 with b³=58, and the local point (5b,0) is in it. It is excluded
globally by the character. In particular every integral point on this
curve has 5 not dividing x. We make no claim about existence or
completeness of integral points on this curve.

The binary factor drops from A(V₂)=3/2 to 1. The bound of the earlier
quotient theorem becomes #E_B(Z)≤(C/2)·2^r, with the same absolute
C=4·7^192·8178·1636, since the curve has no rational 2-torsion.
This single example is a constant-factor saving.

## 3. A certified full rational image in a split binary block

For B=-58·19³=-397822, identify theta=19a. The sole retained binary
block is V₂=F₂² at 19; the three nonzero elements have labels 1,7,11.
The character has values 0,1,1 on them. Thus H₂ lies in the line
{0,1}, where 1 denotes the root label, not a scalar coordinate.

The integral point

    P=(1463,55955),     55955²=1463³-397822,
    1463/19=77≡1 mod19,     55955=19²·155,

has exactly the nonzero root-1 component. It therefore spans the
character kernel. The upper and lower bounds together prove the full
image, not merely a known-point subgroup:

    H₂={0,root 1},     A(H₂)=3/2,     H₃=0.

Here A(V₂)=5/2. Thus the certified arithmetic restriction changes the
product A(H₂)S(H₃) from the ambient upper bound 5/2 to exactly 3/2,
a factor 3/5. This is a constant-factor improvement, not a new uniform
exponential base. The global bound is #E_B(Z)≤(3C/4)·2^r.
For every integral point with 19|x, one necessarily has x/19≡1 mod19.
All three nonzero components exist locally, using the three simple
cubic roots and the corresponding local 2-torsion points.

There is also an integral-transformation consequence. In the rational
2-class containing P, every source has component c=root 1. Every
rational chord point R has component in {0,c}. The local rule in
[BINARY_QUOTIENT.md, local equivalence relation](../2026-10-29-continuation/BINARY_QUOTIENT.md)
therefore allows only the standard row lattice at 19. The locally
admissible nonstandard lattice for this singular source cannot come
from an integral monic depressed quartic transformation over Q. This
statement includes stabilizing transformations; it imports the audited
rational-chord bridge and does not assume every abstract output occurs.
For a source in the zero component, the root-7 and root-11 output
lattices are likewise excluded. Existence of such an integral source
is not required or asserted.

## 4. Counterexample: one cannot simply omit the primes over 2

Let a³=11. Again O_K=Z[a]: only 3 and 11 can divide the index,
T³-11 is Eisenstein at 11, and the polynomial of a+1,
T³-3T²+3T-12, is Eisenstein at 3. Put delta=9-4a. Its norm is 25.
At 5 the only linear root of T³-11 is 1, and only that prime divides
delta, so (delta)=P_5². The lift of this root modulo 125 is 21,
and delta(21)/25≡2 mod5. Thus adjoining sqrt(delta) is unramified
but nonsplit at P_5.

All odd finite primes are unramified by the same even-valuation argument.
At 3, a has residue 2 and delta has residue 1, so the extension splits.
At 2 use the integral polynomial

    z²-z+(1-delta)/4 = z²-z+(a-2),

whose discriminant is exactly delta. Its reduction is z²+z+a.
Its derivative is a unit modulo 2, so the extension is unramified there.
The cubic modulo 2 factors as (T+1)(T²+T+1). At the linear prime,
z²+z+1 is irreducible over F₂. At the quadratic prime, the residue of
a has trace 1 from F₄ to F₂, so z²+z+a is irreducible over F₄.
Both primes above 2 are nonsplit. Positivity at the real place again
follows from the positive norm. Therefore Artin reciprocity gives

    chi_11 : Cl(K)/(2Cl(K)+<[q]:q|3>) → F₂,
    chi_11(P_5)=1,     chi_11(q)=1 for both q|2.

Now take E:y²=x³+11000, with 11000=11·(2·5)³ and theta=-10a.
The exact integral point (-10,100) has the nonzero component at 5:
x/5=-2 agrees with theta/5=-2a at the root a=1 mod5. This is the
only retained binary block, so the full H₂ is F₂. Mapping its nonzero
component to [P_5] in the quotient that kills 3 but omits 2 would give
a nonzero character value. Hence that stronger proposed containment
is false. Killing the primes above 2 removes this false obstruction.
This counterexample does not prove that every prime above 2 or 3 must
always be killed; the theorem uses a sufficient uniform quotient.

## 5. What has and has not been proved

The general class kernel, these exact images, and the exceptional-prime
counterexample are proved statements. The finite arithmetic verifier
checks their certificates independently of PARI/Sage. PARI was used
only to discover useful fields and elements. Neither a class-group
order nor a rank output from that search is used in a proof.
The integral-lattice exclusion depends on the previous bridge theorem.
No new descent principle or priority claim is made; see [the comparison](LITERATURE.md).
