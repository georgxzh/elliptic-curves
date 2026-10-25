# Local classification of transformations between point quartics

Research proof, 2026-10-25. The argument below is algebraic; finite checks are
separate evidence. No claim of novelty is made.

Let p > 3, let B = p^(2e) u with u in Z_p^* and e in {1,2}, and let
P = (x,y) in Z_p^2 satisfy y^2 = x^3 + B. Put

\[
 f_P(X,Y)=X^4-6xX^2Y^2+8yXY^3-3x^2Y^4.
\]

Use row vectors and the twisted action
T_g f(X,Y) = (det g)^(-2) f((X,Y)g). Suppose g has entries in Z_p,
at least one entry is a unit, and T_g f_P is integral, monic and depressed
(its X^3 Y coefficient is zero). Write the rows as (a,b), (c,d_0),
write D = det g and k = v_p(D), and let L_g be their Z_p-span.

**Proposition.** If k > 0, then u is a square modulo p, k = e, and

\[
 L_g=\{(r,s)\in\mathbb Z_p^2:r-z_0s\in p^e\mathbb Z_p\},\qquad
 z_0=\begin{cases}y/x& p\nmid x,\\0&p\mid x.\end{cases}
\]

Consequently there is only the standard lattice when u is nonsquare, and
at most two lattices altogether when u is square. Existence of the second
lattice is not asserted.

## 1. Necessary equations, including the derivative

Alpoge--Ho, Lemma 3.3, applied over Z_p, gives (a,b) = Z_p. Their
integer-matrix hypothesis is automatic because 2 and 3 are units.
Monicity and depression say

\[
 f_P(a,b)=D^2,\qquad
 f_{P,X}(a,b)c+f_{P,Y}(a,b)d_0=0.                 \tag{1}
\]

For k > 0, b must be a unit: otherwise a is a unit and f_P(a,b) is a
unit. Set z = a/b and F(Z) = f_P(Z,1). Euler's identity in (1) gives

\[
 F(z)=(D/b^2)^2,\qquad F'(z)=4d_0D/b^3.         \tag{2}
\]

Thus v_p(F(z)) = 2k and v_p(F'(z)) >= k. In particular z is a repeated
root modulo p. The second condition cannot be omitted.

## 2. A unit x

Here y and t = y/x are units, x is a square modulo p, and
h = t^2-x = B/x^2 has valuation 2e. Reduction modulo p gives

\[
 F(Z)\equiv (Z-t)^3(Z+3t)\pmod p.
\]

The roots t and -3t are distinct, and only t is repeated. Hence z=t+s
with r=v_p(s)>=1 (allow r=infinity). The exact identity is

\[
 F(t+s)=s^4+4ts^3+6hs^2+4ths+h(4x+h).          \tag{3}
\]

If 3r < 2e, its valuation is 3r. For e in {1,2}, this is possible only
when (e,r)=(2,1), and the valuation is odd, contrary to (2). Equality
3r=2e is impossible. Thus 3r>2e; for these two e this implies r>=e.
Equation (3) now has valuation 2e, so k=e, and

\[
 p^{-2e}F(z)\equiv 4u/x\pmod p.
\]

The left side is a unit square by (2). Since x is a square modulo p, u
must be square modulo p as well. We have also proved z=t mod p^e.

## 3. A nonunit x

First v_p(x)>=e and v_p(y)=e. Indeed, if 3v_p(x)<2e, the only possible
case is e=2, v_p(x)=1, which would make v_p(y^2)=3. Equality
3v_p(x)=2e is impossible. Reducing the curve equation after division by
p^(2e) shows that u is square modulo p. This also covers x=0 using
v_p(0)=infinity.

Since F(Z)=Z^4 mod p, the repeated-root condition gives v_p(z)>=1.
If e=2 and v_p(z)=1, the term 8yz in F(z) has valuation 3, strictly
smaller than all the other terms, again contradicting (2). Therefore
v_p(z)>=e in both cases. Now

\[
 v_p(F(z))\geq 2e,\qquad
 F'(z)=4(z^3-3xz+2y),\qquad v_p(F'(z))=e.
\]

The last equality follows because the first two terms have valuation at
least 3e and 2e respectively, while 2y has valuation e. Equations (2)
give k>=e and k<=e, hence k=e. Here z=0 mod p^e.

## 4. Identifying the lattice

Because b is a unit, the first row can be replaced by (z,1). Subtracting
d_0(z,1) from the second row gives (-D/b,0). Thus

\[
 L_g=\mathbb Z_p(z,1)+\mathbb Z_p(p^e,0).
\]

Only z mod p^e matters. The congruences already proved identify a single
possible nonstandard lattice. When k=0, L_g=Z_p^2.

For B=d n^2 and p not dividing 6d, the unit u is d times a unit square.
Thus the condition that u be square is exactly (d/p)=1. This proves the
proposed inert-prime exclusion and the stronger local lattice count.

Source: [Alpoge--Ho, Sections 2--3, especially Lemma 3.3 and (11)](https://arxiv.org/html/1807.03761).
The classification in this note is
derived explicitly rather than assumed from general minimal-model theory.
