# Extremal arithmetic images and the remaining integral-output question

Research note, 2026-10-29. Sections 1--2 are exact counterexamples proved
by rational arithmetic and certified full images. Section 3 is a bounded
computation. Section 4 states an unresolved target, not a theorem.

## 1. Simultaneous extremality really occurs

**Proposition.** For B=197225=5^2*7^3*23 the full component images are
H_2=F_2^2 at 7 and H_3=F_3 at 5. Consequently

\[
 A(H_2)=5/2=(2^2+1)/2,\qquad S(H_3)=2=(3^1+1)/2.
\]

Both bounds are attained simultaneously on this curve.

**Proof.** Direct substitution verifies P_1=(35,490) and P_2=(70,735).
At 7 the unit B/7^3 is 575=1 modulo 7. The roots of T^3+1 are
3,5,6, giving a two-dimensional binary component group. The two points
have distinct nonzero component labels x/7=5 and 3. They span that
whole ambient group, so this proves the full H_2, not just a subgroup.

At 5 the unit B/5^2=7889 is 4 modulo 5. The local group has order
three. Both points are singular there and give nonzero labels (choose
the square root 2; their signs are -1 and +1). Thus their components
span the entire ternary ambient group as well. No other primes are
retained. A subgroup of a product of groups of exponents two and three
is the product of its primary images: multiply by 3 and 4 to isolate
the two parts. Hence the entire mixed image is certified too.

For the full F_2^2 block, K_0 has size one and every other K_c has
size two. This gives A=1+3/2=5/2. The full F_3 has two supports. QED.

This refutes the proposed unconditional restriction that mixed binary
and ternary Mordell images must give a strict deficit from their two
dimension bounds. It does not refute a bound with an absolute prefactor
and an improved asymptotic base, or assert realization of arbitrary codes
in growing dimensions. No rank is computed, and no inequality s+h<=r
is assumed. The class-group theorem must be selective rather than
excluding every extremal image.

## 2. Integral matrices can realize both nonstandard choices together

On the same curve take

\[
 P=(-56,147),\quad R=(35,-490),\quad Q=(1120,-37485),
 \qquad g=\begin{pmatrix}-7&1\\-210&35\end{pmatrix}.
\]

All three points lie on E, g is primitive, and det(g)=-35. Direct
coefficient expansion gives

\[
                 (\det g)^{-2}f_P((X,Y)g)=f_Q(X,Y).
\]

Thus an actual integral point transformation has nonstandard row lattice
at both the binary prime 7 and the ternary prime 5. The chord formula
has z=-7, q=-35, d=35 and Q=P+2R. The standard-library checker expands
the transformed quartic exactly. This rules out the simple restriction
that one of these two local choices must always stay standard.

It does not show that every pair of outputs occurs for a fixed source.
The source has binary component 6 at 7, so there are two binary quotient
outputs; it has zero ternary component at 5, so there are two ternary
support outputs. The abstract count is four, while this example certifies
only the standard pair and the pair nonstandard at both primes.

## 3. A finite probe of the other two outputs

For this source P, the script `probe_integral_outputs.py` finds all 30
integral points with x<=100000, using the curve equation's lower bound
x>=-58. It also includes the two known points with x=22427440 and
y=+/-106211014035, constructed by doubling and addition.

For every target Q in this 32-point set, it determines exactly whether
Q-P has a rational half. For T=Q-P=(u,v) with T!=O, a half (a,b)
must satisfy

\[
 a^4-4ua^3-8Ba-4uB=0,\qquad
 b=(a^3-3ua^2-2B)/(2v).
\]

There is no rational nonzero 2-torsion, since -B is not a cube; hence
v!=0 and at most one rational half exists. The script factors the
quartic over Q using SymPy, checks every rational root, and verifies
the resulting point and doubling identity exactly. It finds six targets
in the source's rational 2-class, with x-coordinates

    -56, -56, 1120, 1120, 22427440, 22427440.

Their observed output pairs are only (standard,standard) and
(nonstandard,nonstandard), at primes (7,5). This is **not** a proof that
the other two outputs never occur. It exhausts only the stated finite
target set, not all integral points or all rational chords. In particular,
the coincidence of the two output indicators is a test question for
this curve, not an established arithmetic restriction.

Bennett--Ghadermarzi's published complete computation covers this B;
the relevant full data row has not been retrieved and checked here. A
verified use of that row, or an independent complete integral-point
calculation, could settle this fixed-curve test. It would still not prove
an exponential saving in rank.

## 4. A precise unresolved target for integral realizability

For each rational 2-class xi containing integral points, choose a base
point P_xi. Let M_xi count the distinct tuples of local row lattices at
the retained primes arising from **actual integral point transformations**
from P_xi. Set M_xi=0 for an empty class. If c is its binary component,
the audited bound is

\[
 M_\xi\le |H_2|\,S(H_3)/|K_c|,
 \qquad \sum_\xi M_\xi\le 2^{r+\tau_2}A(H_2)S(H_3).   \tag{1}
\]

**Unresolved lemma to investigate.** Do there exist absolute constants
K_0 and theta<1 such that base points can always be chosen with

\[
 \sum_\xi M_\xi\le K_0\theta^r
                2^{r+\tau_2}A(H_2)S(H_3)?              \tag{2}
\]

Such a statement, if proved in this form, would improve the exponential
base of the existing lattice argument. It might instead need additional
arithmetic hypotheses or fail outright. The finite probe above does not
supply an upper bound for its left side and cannot establish (2).
It merely makes a specific missing-output question available for a
complete calculation. Sparse actual 2-classes, local restrictions at
2 and 3, and global integrality of P+2R are possible mechanisms to test.

The proved advance of this run is the independent class-group restriction
and its explicit exclusions, not (2). The mixed extremal example explains
why dimension-only code estimates cannot settle the remaining question.
