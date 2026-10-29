# Completing the fibre count with actual row lattices

Research proof, 2026-10-25. This is a proposed refinement with a complete
argument written out below, conditional only on the explicitly cited standard
results. It has not received independent mathematical review. Novelty is a
separate question; see LITERATURE.md.

**Theorem.** Fix a nonzero integer d. For positive cube-free n, let

\[
 E_{d,n}:y^2=x^3+dn^2,\quad
 w_d(n)=\#\{p\mid n:p\nmid6d,\ (d/p)=1\}.
\]

There is a constant A_d, independent of n and the rank, such that

\[
 \#E_{d,n}(\mathbb Z)\leq A_d\,2^{\operatorname{rank}E_{d,n}(\mathbb Q)+w_d(n)}.
                                                        \tag{T}
\]

The proof does not require d to be nonsquare. The user's nonsquare case is
included. Integral points mean affine points on this precise model, with both
signs of y counted.

## 1. The rational orbits and their transformations

Write B=dn^2. Attach to each integral point P=(x,y) the quartic

\[
 f_P(X,Y)=X^4-6xX^2Y^2+8yXY^3-3x^2Y^4.
\]

It has invariants I=0, J=-1728B and discriminant

\[
 \Delta(f_P)=-2^{12}3^3B^2=2^8\Delta(E_{d,n})\ne0.       \tag{1}
\]

Alpoge--Ho, Theorem 2.2 and Section 3.1, identify its rational twisted
PGL_2 orbit with the image of P in E(Q)/2E(Q). There are at most 4*2^rank
such orbits. The point-to-quartic map is injective by its coefficients.

Fix an orbit containing an integral point and fix its quartic f=f_P.
Every other point quartic in it is T_g f, where

\[
 T_g f(X,Y)=(\det g)^{-2}f((X,Y)g).
\]

Represent g by a primitive integral matrix (gcd of all four entries is 1).
Such a representative exists and is unique up to sign. Alpoge--Ho,
Lemma 3.3 over Z, gives

\[
 \gcd(a,b)=1,\quad f(a,b)=D^2,\quad D^2\mid\Delta(f),    \tag{2}
\]

where (a,b) is its first row and D=det g. The integer-matrix hypotheses
hold because both f and T_g f are point quartics. Associate to g the actual
sublattice L_g=Z^2 g of Z^2; its index is |D|. The sign ambiguity does not
change this lattice.

We count these lattices first, then all point quartics that can arise from a
fixed lattice. No quotient of unmarked local models is used.

## 2. Bounding the number of global lattices

Let S be the finite set of primes dividing 6d. For p outside S:

* If p does not divide n, (1)--(2) give L_g tensor Z_p = Z_p^2.
* If p divides n, write e=v_p(n) in {1,2}. The local proposition in
  LOCAL_PROOF.md gives one possible lattice if (d/p)=-1, and at most two
  if (d/p)=1.

At p in S, define

\[
 K_p=\left\lfloor\frac{12v_p(2)+3v_p(3)+2v_p(d)+8}{2}\right\rfloor.
\]

Since n is cube-free, (1)--(2) give 0<=v_p(D)<=K_p. The number of all
sublattices of Z_p^2 of index p^k is sum_{j=0}^k p^j (Hermite normal
form). We may overcount by allowing all of them, including nonprimitive
ones. Thus put

\[
 M_d=\prod_{p\mid6d}\left(\sum_{k=0}^{K_p}\sum_{j=0}^k p^j\right).
\]

The local-to-global map on actual finite-index sublattices

\[
 L\longmapsto(L\otimes\mathbb Z_p)_p
\]

is injective: L equals the set of v in Z^2 belonging to every local
lattice. For example this follows by applying localization to the finite
group Z^2/L. Therefore the number of lattices arising from the matrices g
is at most

\[
 M_d\,2^{w_d(n)}.                                      \tag{3}
\]

Only injectivity is required. There is no existence or simultaneous gluing
claim to check, and no need to control stabilizers of abstract local models.

## 3. Uniformly many depressed monic forms per lattice

Fix one lattice L which actually occurs, and choose a Z-basis matrix T
for L. Every g with L_g=L has the form g=UT, U in GL_2(Z). Set F=T_T f.

This F is integral. To see this without a divisibility assumption on the
basis T, choose one occurring g_0=U_0 T. Its point quartic is integral,
and F=T_{U_0^{-1}}(T_{g_0}f). The twisted action of GL_2(Z) preserves
integrality, since its determinants are +/-1. Here the action convention
is T_U(T_T f)=T_{UT}f. The discriminant of F is the same nonzero number
as that of f, so F has four distinct geometric roots.

If T_U F is monic and the first row of U is (a,b), then

\[
 F(a,b)=1.                                             \tag{4}
\]

Apply the homogeneous Thue--Mahler bound stated as Alpoge--Ho Theorem
3.5, with K=Q, Sigma={infinity}, and degree 4. It bounds pairs satisfying
F(a,b) in Z^* modulo common multiplication by Z^*={+/-1} by

\[
 H=7^{4^3(1+2)}=7^{192}.
\]

This bound allows reducible F: the hypothesis is at least three distinct
geometric roots, not irreducibility. Our pairs satisfying (4) form a subset.

For each pair modulo common sign there are at most two depressed monic
forms, one for each determinant of U. Indeed, fix the first row and fix
det U=epsilon in {+/-1}. Any two possible second rows differ by a rational
multiple lambda(a,b), since their determinants with (a,b) agree. Changing
the second row by lambda(a,b) adds 4lambda to the X^3Y coefficient of the
already monic transformed quartic. Depression therefore forces lambda=0.
Replacing U by -U changes neither its determinant nor the quartic.

Thus the number of point quartics obtainable from a fixed actual lattice
is at most 2H. Counting transformations instead would be an unnecessary
overcount; any stabilizers can only reduce the number of quartics.

The determinant sign is retained explicitly. The first row alone does not
always determine a unique transformation: diag(1,1) and diag(1,-1) send
f_P to f_P and f_{-P}. This constant factor is harmless but must be counted.

## 4. Conclusion

Multiply (3) by 2H and then by the at most 4*2^rank rational orbits. One
valid, deliberately crude explicit choice is

\[
 A_d=8\,7^{192}M_d.
\]

This proves (T) from the quoted descent and Thue--Mahler results and the
local proposition. If every prime dividing n outside 6d is inert, then

\[
 \#E_{d,n}(\mathbb Z)\leq A_d\,2^{\operatorname{rank}E_{d,n}(\mathbb Q)}.
\]

This is an individual-curve result. It does not establish a bounded or zero
average on a thin inert-supported subfamily, since that would require rank
statistics in that particular sampling family.

References: [Alpoge--Ho, Sections 2--3](https://arxiv.org/html/1807.03761),
specifically Theorem 2.2, Section 3.1, Lemma 3.3, and Theorem 3.5.
All local-lattice classification and global-lattice counting steps used here
are supplied in these notes; no further minimal-model theorem is assumed.
