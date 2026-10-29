# Exact local row lattices for sixth-power-free Mordell coefficients

Research derivation, 2026-10-25. This extends the valuation-two and
valuation-four calculation in `../LOCAL_PROOF.md`. Local existence below
means existence over Z_p, and does not assert a rational or global integral
transformation. No novelty claim is made.

Let p>3, B=p^m u with u in Z_p^*, 0<=m<=5, and let
P=(x,y) in Z_p^2 satisfy y^2=x^3+B. Write

\[
 f_P(X,Y)=X^4-6xX^2Y^2+8yXY^3-3x^2Y^4,\qquad F(Z)=f_P(Z,1).
\]

For a matrix g over Z_p with some unit entry, nonzero determinant, and
integral monic depressed T_g f_P, count its actual row lattice
L_g=Z_p^2 g. The action is T_g f=(det g)^(-2)f((X,Y)g).
All such transformed forms are point quartics on the same local curve.

## The exact classification

The standard lattice Z_p^2 always occurs. The complete list of other
lattices is as follows; t=y/x is used only when x is a unit.
The notation L(k,z) means

\[
 L(k,z)=\{(r,s)\in Z_p^2:r-zs\in p^k Z_p\}.
\]

| m | Condition on P or u | All nonstandard lattices |
|---|---|---|
| 0,1,5 | any | none |
| 2e, e=1 or 2 | u nonsquare modulo p | none |
| 2e, e=1 or 2 | u square modulo p, x unit | L(e,t) |
| 2e, e=1 or 2 | x nonunit | L(e,0) |
| 3 | x unit | L(2,t+p v), one for each v mod p with (t v)^3=-u mod p |
| 3 | x nonunit, -3 square modulo p | L(1,0) |
| 3 | x nonunit, -3 nonsquare modulo p | none |

In the nonunit-x row with m even, the curve equation forces u to be a
square. In the nonunit-x row with m=3, it forces v_p(x)=1,
v_p(y)>=2, and (x/p)^3=-u modulo p.

Consequently, a bound independent of P is

\[
 N_p(P)\leq\lambda_p(B):=
 \begin{cases}
 1,&m=0,1,5,\\
 1+\mathbf1_{(u/p)=1},&m=2,4,\\
 1+\#\{w\in\mathbb F_p:w^3=-u\},&m=3.
 \end{cases}                                                   \tag{1}
\]

For m=3, this bound is attained by every local point with unit x. For
m=2,4 it is attained by every local point. The three possibilities for
the last line of (1) are 1,2,4. More explicitly, it is 2 for p=2 mod 3;
for p=1 mod 3 it is 4 if -u is a cube and 1 otherwise.

## 1. Necessary equations and a sufficient construction

Write the rows of g as (a,b),(c,d), its determinant as D, and
k=v_p(D). Alpoge--Ho Lemma 3.3 over the PID Z_p gives (a,b)=Z_p and
D^2 dividing the discriminant of f_P. Its integer-matrix hypotheses
hold because 2 and 3 are units. If k>0, b is a unit: otherwise a is a
unit and monicity f_P(a,b)=D^2 is impossible modulo p.

Monicity, depression, and Euler's identity give, for z=a/b,

\[
 F(z)=(D/b^2)^2,\qquad F'(z)=4dD/b^3.                         \tag{2}
\]

Thus F(z) is a nonzero square of valuation 2k and v_p(F'(z))>=k.
In particular, z is a repeated root modulo p. Row reduction gives
L_g=L(k,z), so only z modulo p^k matters.

Conversely, suppose z in Z_p and q in Q_p^* satisfy

\[
 F(z)=q^2,\quad k=v_p(q)\geq1,\quad v_p(F'(z))\geq k.
\]

Set d=F'(z)/(4q) and

\[
 g=\begin{pmatrix}z&1\\zd-q&d\end{pmatrix}.                  \tag{3}
\]

This matrix is integral and primitive, has determinant q, and gives
monicity and depression. To check every remaining coefficient, use
the basis matrix T with rows (z,1),(p^k,0). The coefficients of T_T f_P
are

\[
 \left(F(z)/p^{2k},\;F'(z)/p^k,\;F''(z)/2,
                \;p^kF'''(z)/6,\;p^{2k}\right),              \tag{4}
\]

all integral. The matrices g and T have the same row lattice, and
g=U T with U in GL_2(Z_p). Therefore T_g f_P is integral as well.

Finally, write this monic depressed quartic as
X^4+A X^2Y^2+C XY^3+E Y^4. The invariant I=0 gives E=-A^2/12.
Set x'=-A/6 and y'=C/8. Both are integral, the constant term is -3x'^2,
and the unchanged invariant J=-1728B gives y'^2=x'^3+B. Thus (3)
really gives a point quartic, not merely an integral quartic.

## 2. Unit x

If m>0 and x is a unit, so are y and t=y/x. Put h=t^2-x=B/x^2.
Modulo p, x=t^2 and y=t^3. In particular x is a square modulo p.
One has

\[
 F(Z)\equiv(Z-t)^3(Z+3t)\pmod p,
\]

so (2) forces z=t+s, with r=v_p(s)>=1. The exact expansions are

\[
\begin{aligned}
 F(t+s)&=s^4+4ts^3+6hs^2+4ths+h(4x+h),\\
 F'(t+s)/4&=s^3+3ts^2+3hs+th.                     \tag{5}
\end{aligned}
\]

If 3r differs from m, the first expansion has valuation min(3r,m).

For m=1 this valuation is 1. For m=5 it is 3 when r=1 and 5 when
r>=2. These are odd, excluding (2).

For m=2e in {2,4}, equality 3r=2e is impossible. The only possibility
3r<2e is e=2,r=1, again with odd valuation. Hence r>=e and
v_p(F(z))=2e. Furthermore

\[
 p^{-2e}F(z)\equiv4u/x\pmod p.
\]

This is square precisely when u is square modulo p. Necessarily k=e
and L_g=L(e,t). Conversely, if u is square, take z=t. Then F(t) has
valuation 2e and square unit part, and v_p(F'(t))=2e. Every p-adic
unit with square reduction has a square root, so construction (3)
realizes L(e,t).

For m=3, values r>=2 give odd valuation 3. Thus r=1. Write s=pv
with v a unit. The derivative in (5) has valuation exactly 2. By (2),
k<=2; since v_p(F)>=3, the square condition forces k=2. Reduction of
the first expansion gives

\[
 p^{-3}F(t+pv)\equiv4t v^3+4u/x
       =\frac4x\bigl((tv)^3+u\bigr)\pmod p.                 \tag{6}
\]

This proves the claimed list of at most rho lattices, with
rho=#{w:w^3=-u}. Conversely, take any residue v satisfying (6), and
choose a lift z_0=t+pv. Then p^4 divides F(z_0) and
v_p(F'(z_0))=2. For z=z_0+p^2 w, Taylor expansion gives

\[
 \frac{F(z)}{p^4}\equiv
 \frac{F(z_0)}{p^4}+\frac{F'(z_0)}{p^2}w\pmod p.             \tag{7}
\]

The coefficient of w is a unit. Choose w modulo p so that this is any
chosen nonzero square. Then F(z) is a square of valuation 4 and
v_p(F'(z))=2; (3) realizes the specified L(2,z_0). Distinct v modulo
p give distinct lattices. No square-condition loss remains here,
because changing z modulo p^3 preserves the lattice and permits (7).

## 3. Nonunit x

For m=1 there are no such points: x^3+B would have odd valuation 1.
For m=5, v_p(x)=1 gives valuation 3, whereas v_p(x)>=2 gives valuation
5. Thus these cases again have no such points.

For m=2e in {2,4}, the curve equation forces v_p(x)>=e and
v_p(y)=e. The only possible smaller valuation is e=2,v_p(x)=1,
which would give odd valuation 3. Equality 3v_p(x)=2e is impossible.
Dividing the curve equation by p^(2e) shows that u is square modulo p.

The only repeated root of F modulo p is zero. Thus v_p(z)>=1.
When e=2,v_p(z)=1, the term 8yz has valuation 3, strictly smaller
than every other term in F(z). This is excluded by the square
condition. Therefore v_p(z)>=e. Now v_p(F)>=2e, while

\[
 v_p(F'(z))=v_p(4(z^3-3xz+2y))=e.
\]

Equation (2) forces k=e. For existence, write x=p^e X,y=p^e Y and
z=p^e Z. Here Y is a unit, and

\[
 F(p^e Z)/p^{2e}\equiv8YZ-3X^2\pmod p.
\]

This affine function of Z takes every residue. Choose it to be a
nonzero square and use (3). The lattice is always L(e,0).

For m=3, write a=v_p(x). If a>=2, x^3+B has odd valuation 3.
Thus a=1. The equation then requires v_p(y)>=2, and with X=x/p
one has X^3=-u modulo p. Again z must be divisible by p, and now

\[
 F(z)/p^2\equiv-3X^2\pmod p.                               \tag{8}
\]

Thus v_p(F)=2 and k=1, and the square condition is exactly that -3
be square modulo p. The derivative has valuation at least 2, so
when that condition holds z=0 and (3) realize L(1,0). When it fails
there is no nonstandard lattice. For p>3, (-3/p)=1 is equivalent to
p=1 mod 3. In that case the existing root X of T^3+u implies all
three roots exist. Thus the point-independent bound (1) also covers
this branch (its exact count is 2, while the maximum is 4).

## 4. Unit B and scope

For m=0, the discriminant -2^12 3^3 B^2 is a p-adic unit.
The determinant divisibility in Alpoge--Ho Lemma 3.3 forces k=0.
This completes all six valuations.

The sole imported algebraic input above is the primitive-first-row and
determinant lemma. The local construction proves attainment over Z_p;
it does not prove simultaneous global realization of these lattices.
The global bound requires only their upper count.

Reference: [Alpoge--Ho, Lemma 3.3 and invariant conventions in Section 2](https://arxiv.org/html/1807.03761).
