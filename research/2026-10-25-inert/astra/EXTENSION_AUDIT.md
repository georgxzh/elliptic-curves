# Targeted audit of the exact local extension

2026-10-25. This separate AI audit checks the proposed local counts transmitted
by the research agent. It does not certify an entire new global manuscript.
Assume throughout `p>3`, `B=p^m u` with `u` a unit, an integral point
`P=(x,y)`, and a primitive integral matrix whose twisted transform of the
point quartic is integral, monic, and depressed. All lattices here are actual
row lattices. The proposed exact local counts for `1<=m<=5` pass this check.

## The case m=3 with x a unit

Put `t=y/x` and `h=B/x^2`. The original proof's expansion and derivative
identity still apply. Any nonstandard lattice has `z=a/b=t+s`, with
`r=v_p(s)>=1`. If `r>=2`, the constant term in the expansion has valuation
3 and is uniquely minimal, contradicting the requirement that `F(z)` be a
nonzero square. Thus `s=pS` with `S` a unit. Define

\[
 H(S)=p^{-3}F(t+pS).
\]

This polynomial is integral and has reduction

\[
 \overline H(S)=4tS^3+4u/x
                =4t(S^3+u/t^3)\quad\text{in }\mathbb F_p[S].
\]

The last equality uses `x=t^2 mod p`. An even valuation of `F(z)` forces
`H(S)=0 mod p`. Its roots correspond under `W=tS` to roots of
`W^3+u=0`; all are nonzero and simple. At any such residue, the exact
derivative expansion has uniquely minimal term `12t p^2 S^2`, so
`v_p(F'(z))=2`. Since `v_p(F(z))>=4`, the necessary inequalities give
`k=2`. The lattice is determined by `z=t+pS mod p^2`, so distinct roots
give distinct possible lattices.

Existence follows separately for every root: Hensel's lemma applied to
`H(S)-p` gives a lift with `H(S)=p`, hence `F(z)=p^4`. Its derivative is
divisible by `p^2`, so the construction below realizes the lattice.
Consequently the exact count is `1+rho`, where `rho` is the number of
roots of `W^3+u` over `F_p`, including the standard lattice.

## The case m=3 with x a nonunit

The curve equation forces `v_p(x)=1` and `v_p(y)>=2`: valuation at least
2 for `x` would make `v_p(y^2)=3`. For `x=pX` and any `z` in `p Z_p`,
the term `-3x^2` in `F(z)` alone has valuation 2. Thus

\[
 v_p(F(z))=2,\qquad p^{-2}F(z)\equiv-3X^2\pmod p.
\]

Necessarily `k=1`, with the unique possible nonstandard lattice
`Z_p(0,1)+Z_p(p,0)`, and it is possible only if `(-3/p)=1`.
Conversely, when this symbol is 1, choose `z=0` and
`q=x sqrt(-3)` in `Q_p`. Then `F(0)=q^2`, `v_p(q)=1`, and
`F'(0)=8y` is divisible by `p^2`. The construction below realizes it.
The exact count is therefore `1+1_{(-3/p)=1}`.

## Verification of the existence construction

For any `k>=1`, take `z` integral with `F(z)=q^2`, `v_p(q)=k`, and
`v_p(F'(z))>=k`. Let `T` have rows `(z,1),(p^k,0)`. Direct expansion
gives coefficients of `T_T f`, in descending degree of the first variable,

\[
 F(z)/p^{2k},\quad F'(z)/p^k,\quad F''(z)/2,\quad
 p^kF'''(z)/6,\quad p^{2k}.
\]

They are integral. Put `d=F'(z)/(4q)` and let `g` have rows
`(z,1),(zd-q,d)`. Then

\[
 \det g=q,\qquad
 g=\begin{pmatrix}1&0\\d&-q/p^k\end{pmatrix}T.
\]

The left factor lies in `GL_2(Z_p)`, so the transformed quartic is integral
and the row lattice is exactly that of `T`. Monicity and depression follow
directly from the two equations imposed on `F`. The invariants remain
`I=0,J=-1728B`. If the resulting coefficients are `1,0,A_2,A_3,A_4`,
then `I=0` gives `A_4=-A_2^2/12`; setting `x'=-A_2/6`, `y'=A_3/8`
recovers an integral point on the original curve. This validates the
construction as an actual transformation between point quartics.

## Other valuations checked

For `m=1,5`, a nonunit `x` is impossible: compare the valuations of
`x^3` and `B`; their minimum is odd, and they cannot be equal.
For a unit `x`, the repeated root is still `t mod p`. When `m=1`,
`F(t+s)` has valuation 1. When `m=5`, it has valuation 3 for `v_p(s)=1`
and valuation 5 for `v_p(s)>=2`. Each contradicts its being a nonzero
square. Thus only the standard lattice occurs.

For `m=2e` with `e=1,2`, necessity and uniqueness are proved in the
original local note. Sufficiency when `u` is square also checks:
if `x` is a unit, take `z=t`. Then `F(t)` has valuation `2e` and square
unit residue `4u/x`, while `F'(t)` has valuation `2e`. If `x` is a
nonunit, write `y=p^eY`, with `Y` a unit, and `x=p^eX`. The polynomial
`p^{-2e}F(p^eW)` has reduction `8YW-3X^2`. Hensel's lemma solves
`p^{-2e}F(p^eW)=1`, and `F'(p^eW)` has valuation `e`. The existence
construction applies in both cases. Thus the exact count is 2 when `u`
is square and 1 otherwise.

All arguments require `p>3`. No count at 2 or 3, no novelty claim, and
no average-rank conclusion is established by this targeted audit.
