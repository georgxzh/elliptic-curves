# Combining binary and ternary restrictions: precisely when a saving follows

Completed 2026-10-31. The underlying bound is

    #E_B(Z) ≤ C 2^r A(H₂) S(H₃),   C=4·7^192·8178·1636,

for a nonzero sixth-power-free integer B. If the cubic is irreducible,
C/2 suffices. These constants are absolute across all such coefficients;
computing a field or a character does not change the constant. The
[prior audit](../2026-10-29-arithmetic/AUDIT.md) checks the rational-chord
bridge and averaging, and [the new audit](ASTRA_AUDIT.md) checks the
class-group hypotheses and uniformity.

Let J₂ be a kernel certified by the binary theorem (possibly using only
some class characters), and J₃ a kernel certified by the preceding
quadratic-field ternary theorem. If the latter field construction is
unavailable, set J₃ equal to the full ternary ambient space. Write

    D=dim V₂, j=dim J₂, kappa=D-j,
    d₀=min(r+tau₂,D), d=min(r+tau₂,j),
    e=min(r+tau₃,dim J₃), w=number of ternary coordinates.

Here tau_l=dim E(Q)[l]. The valid separate dimension bounds never imply
that the binary and ternary dimensions add to at most r.

## 1. A safe computable product bound

Define

    U₂=(2^d+1)/2,
    U₃=min{S(J₃), (3^e+1)/2, 2^w}.

Then A(H₂)S(H₃)≤U₂U₃. Support count is monotone under inclusion,
which justifies S(H₃)≤S(J₃). We do not need or assume monotonicity of A.
For j>0 one may further replace U₂ by its minimum with

    max{A(J₂), (2^(j-1)+1)/2}.

Indeed either H₂=J₂ or its dimension is at most j-1. The histogram
bound in [the binary theorem](ASTRA_BINARY.md)
is another valid option. If known points span J₂, then H₂=J₂ and its
exact A-value may be used. Without that upper-bound certificate,
known points alone cannot be substituted for H₂.

## 2. Dimension savings and their limits

Compared with the old binary dimension estimate (2^d₀+1)/2, the
new one saves the exact factor

    (2^d₀+1)/(2^d+1).

For Delta=d₀-d≥0 this lies between 2^(Delta-1) and 2^Delta (and is
exactly one if Delta=0). Therefore the dimension estimate improves
strictly precisely when j<d₀. A nonzero class map alone is insufficient:
if j≥r+tau₂, the rank cap already gives the same dimension estimate.
The kernel's block structure can still give extra information through
the preceding alternatives or an exact-image certificate.

A deficit Delta≥epsilon r would give a saving at least
2^(epsilon r-1) **relative to the binary dimension estimate**. A
simultaneous ternary dimension deficit gives the analogous ratio
(3^e₀+1)/(3^e+1), where e₀ is its previous cap. These are conditional
inequalities, not assertions that curves of unbounded rank satisfying
such deficits have been constructed. Nor do they automatically beat
every other available local or published estimate; take the minimum
with those estimates when making a numerical comparison.

For a fixed cubic field K, kappa≤dim(Cl(K)/2Cl(K)) is bounded.
Since Delta≤kappa, this source of *dimension* saving is at most a
field-dependent factor 2^kappa. Thus we do not obtain a growing
exponential saving just by varying valuation-three primes in a fixed
cubic field. A growing class-map deficit would require varying fields
with sufficiently many independent surviving classes and suitable
prime columns. This is a necessary condition for this route, not a
realization theorem for Mordell images or ranks.

If J₂=0, the binary factor is exactly one. If also J₃=0, the product
is one and the absolute C·2^r bound follows. These are arithmetic
criteria; no assertion of their universal validity is made.

## 3. Actual stronger estimates and excluded outputs

The exact certificates give:

| B | V₂ | Full H₂ | S(H₃) | A(V₂) | A(H₂)S(H₃) |
|---|---|---|---|---|---|
| -7250 | F₂ | 0 | 1 | 3/2 | 1 |
| -397822 | F₂² | root-1 line | 1 | 5/2 | 3/2 |
| 11000 | F₂ | F₂ | 1 | 3/2 | 3/2 |

For these single blocks the ambient A-values are also the dimension
bounds. The first two rows are strict, certified constant-factor savings.
The third is the counterexample to an overstrong exceptional-prime
quotient. No rank calculation is required for any row.

For B=-397822, the nonzero rational 2-classes at 19 have only the
standard 19-adic output lattice. The other locally admissible output
is arithmetically impossible. Thus the result supplies an actual
integral-transformation exclusion as well as a smaller averaged factor.
It does not claim to count the remaining global outputs exactly.

## 4. Open direction, without a novelty claim

The class kernel forgets units, squareclasses at 2 and 3, and full
Selmer local conditions. Determining when those further conditions
shrink its component projection is a precise next target. This run
already supplies the requested structural refinement and exact examples;
no unproved additional shrinking lemma is needed for its conclusions.
