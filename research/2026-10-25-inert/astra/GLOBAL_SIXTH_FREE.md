# A rank bound with explicit local factors for sixth-power-free B

Research proof draft, 2026-10-25. The inputs are the local classification
in `LOCAL_SIXTH_FREE.md` and the descent/lattice/Thue argument audited in
`../GLOBAL_PROOF.md`. This is an explicit refinement of established
methods, with novelty unassessed.

## Theorem

For every nonzero sixth-power-free integer B, let E_B be the precise
affine model y^2=x^3+B, and let r=rank E_B(Q). For p>3 write
m_p=v_p(B) and u_p=B/p^(m_p), and set

\[
 \lambda_p(B)=
 \begin{cases}
 1,&m_p=0,1,5,\\
 1+\mathbf1_{(u_p/p)=1},&m_p=2,4,\\
 1+\#\{w\in\mathbb F_p:w^3=-u_p\},&m_p=3.
 \end{cases}
\]

There is an absolute constant C such that

\[
 \#E_B(\mathbb Z)\leq C\,2^r\prod_{p>3}\lambda_p(B).        \tag{1}
\]

One explicit, deliberately large choice is

\[
 C=4\,7^{192}\,8178\,1636=53\,516\,832\cdot7^{192}.
\]

The product is a power of 2. Let a count primes p>3 with m_p in {2,4}
and (u_p/p)=1; let b count primes with m_p=3,p=2 mod 3; and let c
count primes with m_p=3,p=1 mod 3 for which -u_p is a cube modulo p.
Then the right side is C 2^(r+a+b+2c).

## Proof and fixed-prime constants

For each P in E_B(Z), use the point quartic f_P in the local note.
Alpoge--Ho Theorem 2.2 and Section 3.1 identify its rational twisted
PGL_2 orbit with the image of P in E_B(Q)/2E_B(Q). For Mordell curves
over Q, the polynomial X^3+B has at most one rational root. Therefore
|E_B(Q)[2]|<=2, and there are at most 2*2^r such orbits. This slightly
improves the general bound 4*2^r used in the preceding proof draft.

Fix a base point quartic in an occurring orbit. Each other point
quartic in that orbit is T_g f_P for a primitive integer matrix g,
defined up to sign. The associated actual row lattice is independent
of that sign. Lemma 3.3 of Alpoge--Ho gives

\[
 (\det g)^2\mid\Delta(f_P)=-2^{12}3^3B^2.                   \tag{2}
\]

At p>3 the local note bounds the number of row lattices by lambda_p(B).
At p=2, (2) gives v_2(det g)<=6+v_2(B)<=11; at p=3 it gives
v_3(det g)<=1+v_3(B)<=6. For K>=0 define

\[
 N_p(K)=\sum_{k=0}^K\sum_{j=0}^k p^j.
\]

Hermite normal form counts all sublattices of index p^k in Z_p^2 as
sum_{j=0}^k p^j. This deliberately allows lattices which cannot arise.
In particular N_2(11)=8178 and N_3(6)=1636.

An actual finite-index sublattice L of Z^2 is determined by its
localizations L tensor Z_p: an integral vector lies in L precisely
when its class in the finite group Z^2/L vanishes at every prime.
Thus the total number of possible global lattices is at most

\[
 N_2(11)N_3(6)\prod_{p>3}\lambda_p(B).                       \tag{3}
\]

Each occurring lattice contributes at most 2*7^192 point quartics.
For completeness, choose an integer row basis T for it. Since some
g_0=U_0T with U_0 in GL_2(Z) occurs, F=T_T f_P is integral: it equals
T_(U_0^(-1))(T_(g_0)f_P). Its discriminant is nonzero. Any other g=UT
has U in GL_2(Z), and monicity gives F(a,b)=1 for the first row
(a,b) of U. Alpoge--Ho Theorem 3.5, the homogeneous Thue--Mahler
bound, gives at most 7^192 such pairs modulo common sign; it applies
to reducible forms as well, since F has four distinct geometric roots.
For a fixed signed first row and fixed det U in {1,-1}, all second
rows differ by a multiple of the first; depression fixes that multiple
uniquely. Common negation leaves the quartic unchanged. Hence the
factor 2*7^192.

Multiply this by (3) and the number of rational orbits. This proves
(1) with the displayed constant.

## Corollary: squarefree Mordell coefficients

For every nonzero squarefree integer B,

\[
 \#\{(x,y)\in\mathbb Z^2:y^2=x^3+B\}
       \leq36\,144\cdot7^{192}\,2^{\operatorname{rank}E_B(\mathbb Q)}.
                                                               \tag{4}
\]

Indeed, every p>3 has m_p=0 or 1, so the product in (1) is 1.
Here (2) sharpens to v_2(det g)<=7 and v_3(det g)<=2, giving
N_2(7)=502 and N_3(2)=18. The same argument yields the stated
constant 4*7^192*502*18. All signs of B and both signs of y are included.
For squarefree |B|>1, E_B(Q)[2] is trivial, so the displayed constant
can be halved if desired.

More generally, the product in (1) is 1 whenever every p>3 dividing B
has valuation 1 or 5, or has valuation 2 or 4 with nonsquare unit
part, or has valuation 3 with T^3+u_p irreducible modulo p. In all
these cases the bound is absolute C 2^r. The squarefree corollary is
the cleanest special case.

## Limitations and relationship to earlier results

Sixth-power-freeness is essential to the uniform fixed-prime argument
and to the finite list of local cases. No assertion for arbitrary
nonminimal integral models is intended. The constants are explicit
but far too large to estimate practical point counts. These are bounds
for individual curves; no averaging assertion or rank statistic on a
thin subfamily follows automatically.

The local counts resemble the rational component configurations in
established minimal-model theory. The proof is useful as a direct
row-lattice derivation, and must not be described as new minimisation
theory. Even the clean squarefree consequence needs a wider literature
audit before any priority claim. See `EXTENSION_AUDIT.md` for the separate
AI check of the local argument, and `LITERATURE_EXTENSION.md` for prior work.

Reference: [Alpoge--Ho, Theorem 2.2, Lemma 3.3, Theorem 3.5](https://arxiv.org/html/1807.03761).
