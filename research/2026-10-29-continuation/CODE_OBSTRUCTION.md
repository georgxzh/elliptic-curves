# What component-code counting can and cannot improve

Research note, 2026-10-29. The statements here are finite linear algebra.
They do not assert that arbitrary codes occur as component images of
Mordell curves. They delimit the information used by the current proof.

## Exact equality criterion for the binary estimate

Use A(H) and K_c from [the quotient theorem](BINARY_QUOTIENT.md).
For a vector a in H, let its block support consist of the local primes
where a_p is nonzero. For c!=0,

\[
 |K_c|>2\quad\Longleftrightarrow\quad
 c=a+b\text{ for nonzero }a,b\in H
 \text{ having disjoint block supports}.                \tag{1}
\]

Indeed, an a in K_c other than 0,c has a_p either 0 or c_p. Thus
b=c+a is nonzero and has disjoint block support from a. Conversely,
disjointness implies a_p is either 0 or c_p, hence a in K_c.

It follows that

\[
 A(H)=\frac{2^s+1}{2}
 \quad\Longleftrightarrow\quad
 \text{every two nonzero vectors of H have intersecting block supports}.
                                                               \tag{2}
\]

For H={0} both sides are true, with the right side vacuous. More precisely,

\[
 A(H)=\frac{2^s+1}{2}
       -\sum_{0\ne c\in H}\left(\frac12-\frac1{|K_c|}\right). \tag{3}
\]

If N(H) is the number of nonzero c admitting the decomposition in (1),
then |K_c|>=4 for each such c, so

\[
               A(H)\le (2^s+1)/2-N(H)/4.               \tag{4}
\]

This gives a usable certificate from partial information: exhibit m
distinct component vectors, each a sum of two known nonzero vectors
with disjoint block supports. Then N(H)>=m. If s<=s_max is certified,
(4) yields A(H)<=(2^s_max+1)/2-m/4. This uses the partial image only
to certify these witnesses, not as a replacement for the full H.

There is also an exact factorization. If the full image splits as
H=H^(1) direct-sum ... direct-sum H^(t), with these summands supported
on disjoint sets of blocks, then

\[
 A(H)=\prod_i A(H^{(i)})
       \le\prod_i (2^{s_i}+1)/2.                         \tag{5}
\]

The assertion of a decomposition of the full image needs proof; merely
finding points with disjoint supports does not establish it.

### An arithmetic example with a certified complete image

Take B=-55^3=-166375 and the rational points

\[
 T=(55,0),\qquad P=(130,1425),\qquad P+T=(176,-2299).
\]

The only retained primes are 5 and 11. Both are 2 modulo 3, so each
component group is F_2. The displayed x-coordinates give

\[
 \alpha(T)=(1,1),\quad\alpha(P)=(1,0),
 \quad\alpha(P+T)=(0,1).
\]

These known points already span the entire ambient F_2^2; hence H_2
is proved to be the full product without a rank or saturation computation.
Also H_3 is trivial. The vector (1,1) has |K_c|=4, while the other
two nonzero vectors have |K_c|=2. Consequently

\[
 A(H_2)=1+1/2+1/2+1/4=9/4<5/2.
\]

The quotient bound gives #E(Z)<=C*2^r*(9/4), compared with the factor
5/2 from dimension alone. This agrees with the previously available
full-product weight bound; its purpose is to demonstrate a strict
arithmetic instance of (4), not to claim a new bound for this example.
The checker verifies the curve equations, exact addition, and labels.

## Relation to established coding theory

For one-dimensional blocks, K_c consists of the codewords supported
inside the support of c. Condition |K_c|=2 says that c is a minimal
codeword. The equivalence with an intersecting binary code is standard:
see Ashikhmin--Barg, *Minimal Vectors in Linear Codes*, IEEE Transactions
on Information Theory 44(5), 2010--2017 (1998), Section II.A,
Lemma 2.1(5) and the following intersecting-code example.
[Primary text](https://user.eng.umd.edu/~abarg/reprints/MinimalVectors98.pdf).
The definition and this equivalence were inspected directly.

Two-dimensional blocks reduce to the same theory. Expand (u,v) to the
three binary coordinates (u,v,u+v); leave one-dimensional blocks alone.
For this injective linear expansion iota,

\[
 a_p\in\langle c_p\rangle\ \text{for every p}
 \quad\Longleftrightarrow\quad
 \operatorname{supp}\iota(a)\subseteq\operatorname{supp}\iota(c).
\]

Every nonzero expanded two-dimensional block has weight two, so distinct
nonzero blocks have distinct supports of the same size. This proves the
equivalence. Thus (2) is a standard minimal-code condition after this
expansion; we do not claim to have discovered that coding-theory concept.

## Binary codes attain the bound in every dimension

Let U=F_2^s. Index coordinates by all nonzero linear functionals ell on U
and embed v as the word (ell(v))_ell. This is the binary simplex code.
The map is injective. If the support of a is contained in that of a
nonzero c, then every functional vanishing on c vanishes on a. Linear
duality implies a belongs to span(c), hence a=0 or c. Therefore

\[
                    A(H)=(2^s+1)/2                     \tag{6}
\]

for every s, with one-dimensional blocks only. Equivalently, two
distinct nonzero vectors admit a functional taking value one on both,
so their supports intersect. For s=0 use the empty code.

The unaveraged number of pairs consisting of a source c and a quotient
output is |H|*A(H)=(4^s+2^s)/2. This differs from the averaged factor
A(H) in the point bound, and must not be substituted for it.

## Ternary supports attain their bound too

For U=F_3^h, index coordinates by the one-dimensional subspaces of U*,
choosing one nonzero functional in each. Send v to its evaluations on
these functionals. Two nonzero vectors give equal supports exactly
when the functionals annihilating them are the same, which is equivalent
to their spanning the same line in U. Each line has two nonzero vectors.
Including the zero vector gives exactly

\[
                          S(H_3)=(3^h+1)/2.             \tag{7}
\]

The empty code covers h=0. All these constructions are elementary;
the checker verifies (6) through s=8 and (7) through h=6.

## Precise limit of the obstruction

At the abstract level the binary and ternary codes can be chosen
independently. With s=h=r, their contribution to the current bound is

\[
 2^r A(H_2)S(H_3)
       =2^r(2^r+1)(3^r+1)/4\ \ge\ 12^r/4.              \tag{8}
\]

Thus no uniform bound O(k^r) with k<12 can hold for this expression
over all abstract codes of dimensions at most r. The analogous binary
expression 2^r A(H_2) attains order 4^r, and the ternary expression
2^r S(H_3) attains order 6^r. This is an obstruction to improving those
expressions using only dimension and arbitrary-code inequalities.

It is **not** a lower bound for integral points, a realization theorem
for elliptic component images, or an obstruction to an arithmetic proof
with a smaller exponential base. In particular, it remains possible
that arithmetic restricts the simultaneous binary and ternary images,
that most rational 2-classes contain no integral points, or that actual
integral transformations occupy few of the allowed abstract outputs.

The next substantive target is consequently an arithmetic restriction
on these images or on integral realizability. Repeating dimension-only
estimates cannot resolve that target. Rank-only bounds themselves were
already classical; see the [existing literature comparison](../2026-10-28-refinements/LITERATURE_AND_STATUS.md).
