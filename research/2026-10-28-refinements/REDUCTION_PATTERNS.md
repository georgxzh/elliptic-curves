# Removing the split factors within a fixed reduction pattern

Research proof draft, 2026-10-28. This builds on the exact local classification
in [the sixth-free note](../2026-10-25-inert/astra/LOCAL_SIXTH_FREE.md).
It does not assert novelty or independent human verification.

## Local switching lemma

Let p>3, B=p^(2e)u with e in {1,2}, and let P=(x,y), Q=(x',y')
be integral p-adic points on y^2=x^3+B. Suppose a primitive integral
matrix g sends f_P to f_Q under the twisted action. Then

\[
 p\mid\det g\quad\Longleftrightarrow\quad
 \mathbf1_{p\mid x}\ne\mathbf1_{p\mid x'}.
 \tag{1}
\]

In particular, a transformation between two points with the same
singular/nonsingular reduction status has unit determinant.

**Proof.** First suppose the determinant has positive valuation. The earlier
local classification gives k=v_p(det g)=e and a unit second entry in the
first row. Scale the whole matrix by that unit's inverse, without changing
its twisted action. The normalized matrix has rows (z,1),(zd-q,d), where

\[
 F(z)=q^2,\qquad d=F'(z)/(4q),\qquad v_p(q)=e.
\]

Expanding the X^2Y^2 coefficient gives

\[
 -6x'=\tfrac12 F''(z)-6d^2,
 \qquad x'=x-z^2+d^2.                           \tag{2}
\]

If x is a unit, put t=y/x and h=B/x^2. The earlier proof gives
z=t+s with v_p(s)>=e. Since

\[
 F'(t+s)/4=s^3+3ts^2+3hs+th,
\]

the derivative is divisible by p^(2e), so d is divisible by p^e.
Also x-z^2=-h-2ts-s^2 is divisible by p^e. Equation (2) implies
p^e divides x'. In fact the curve equation then gives v_p(y')=e.

If x is a nonunit, the earlier proof gives v_p(x)>=e,
v_p(y)=e, v_p(z)>=e, and v_p(F'(z))=e. Thus d is a unit and
(2) gives x'=d^2 mod p, a unit. This proves that a nonstandard
lattice switches the status.

If the determinant is a unit, g reduces to an invertible linear change of
variables over F_p. For unit x, the reduction of f_P has a triple root and
a distinct simple root: (X-tY)^3(X+3tY). For nonunit x, y is also a
nonunit and the reduction is X^4, with one quadruple root. An invertible
change of variables preserves geometric root multiplicities. The status
therefore cannot change when the determinant is a unit. This proves (1).

## Bound for any prescribed pattern

Let B be nonzero and sixth-power-free, let S be any set of primes p>3
with v_p(B) in {2,4}, and prescribe epsilon_p in {0,1} for p in S.
Write

\[
 E_B(\mathbb Z;\epsilon)=
 \{(x,y)\in E_B(\mathbb Z):\mathbf1_{p\mid x}=\epsilon_p
       \text{ for every }p\in S\}.
\]

With the same absolute constant C as in the
[sixth-free global theorem](../2026-10-25-inert/astra/GLOBAL_SIXTH_FREE.md),

\[
 \#E_B(\mathbb Z;\epsilon)
 \le C\,2^{\operatorname{rank}E_B(\mathbb Q)}
          \prod_{\substack{p>3\\p\notin S}}\lambda_p(B).
 \tag{3}
\]

To prove this, choose the base point separately in each rational orbit
meeting the prescribed set. Every transformation to another point in that
set has standard row lattice at every p in S by (1). The existing global
argument now counts only one local lattice at these primes. All other
local counts, the fixed-prime constants, the Thue bound per actual lattice,
and the number of rational orbits are unchanged. Empty orbit intersections
contribute nothing. No existence of a point in a prescribed pattern is assumed.

Taking S to contain every valuation-two/four prime leaves only the
valuation-three factors. In particular, if no p>3 has v_p(B)=3, every
individual reduction pattern has an absolute bound of order 2^rank.
This includes the set of points with gcd(x,B)=1, but also every other
prescribed pattern.

## Original cubic-twist family

Fix nonzero d and let n be positive and cube-free. Put
S={p:p divides n, p does not divide 6d}. For every prescribed pattern
epsilon on S,

\[
 \#\{(x,y)\in E_{d,n}(\mathbb Z):
              \mathbf1_{p\mid x}=\epsilon_p\ (p\in S)\}
       \ll_d 2^{\operatorname{rank}E_{d,n}(\mathbb Q)}.
 \tag{4}
\]

The proof is the same, using the original d-dependent bounds at primes
dividing 6d. It does not require dn^2 to be sixth-power-free at those fixed
primes. As a useful special case,

\[
 \#\{(x,y)\in E_{d,n}(\mathbb Z):\gcd(x,n)=1\}
       \ll_d 2^{\operatorname{rank}E_{d,n}(\mathbb Q)}.       \tag{5}
\]

Here the primitive condition is explicitly gcd(x,n)=1; no alternative
definition of a primitive integral point is intended. Primes dividing 6d
impose further restrictions on this subset and do not enlarge its bound.

The unrestricted point set may meet several patterns, so (4) does not
remove the split-prime factor from the unrestricted theorem. At inert
primes only the nonsingular pattern occurs; at split primes there are at
most two status choices. Summing (4) over them recovers the earlier factor.

## Status

The new ingredient in this note is the explicit status-switching equation
(2) and its use to bound each reduction pattern. The descent, lattice count
and Thue inputs are inherited from the earlier draft. Related component
geometry and primitive-point techniques predate this calculation. The
exact formulation's priority remains unassessed.
