# Problem 2 — Counts that do not change

Let \(p>3\) be a prime. For an integer \(a\) and each
\(b\in\{0,1,\ldots,p-1\}\), let \(N_a(b)\) be the number of ordered
pairs \((x,y)\in\{0,1,\ldots,p-1\}^2\) satisfying
\[
y^2\equiv x^3+ax+b\pmod p.
\]
Determine all residue classes \(a\) modulo \(p\) for which
\[
N_a(0)=N_a(1)=\cdots=N_a(p-1).
\]

## Graduated hints

1. Count \(\sum_b N_a(b)\) by choosing \(x,y\) first.
2. To count \(\sum_b N_a(b)^2\), factor a difference of two squares.
   How does the answer depend on collisions of \(x^3+ax\)?
3. Show that the required condition is equivalent to \(x^3+ax\)
   permuting the residues. If a function permutes the residues, it preserves
   every sum of powers.
4. Expand \((x^3+ax)^k\), taking \(k=(p-1)/3\) when
   \(p\equiv1\pmod3\), and \(k=(p+1)/3\) otherwise.

## Elementary solution

The answer is **only \(a\equiv0\pmod p\) if \(p\equiv2\pmod3\)**,
and **no residue classes if \(p\equiv1\pmod3\)**.

Write \(\mathbb F_p\) for the residues modulo \(p\), with their usual
addition and multiplication. All counting equations below are equations of
ordinary integers; the power sums in the last part are congruences modulo
\(p\).

Put \(f(x)=x^3+ax\). Each pair \((x,y)\) determines one value
\(b=y^2-f(x)\), so
\[
\sum_bN_a(b)=p^2.
\]
If all the counts agree, they therefore all equal \(p\).

Let \(T\) be the number of ordered pairs \((x,z)\) with \(f(x)=f(z)\).
The sum \(\sum_bN_a(b)^2\) counts quadruples satisfying
\[
y^2-v^2=f(x)-f(z).
\]
For fixed \(x,z\), the substitution \((u,w)=(y-v,y+v)\) is invertible,
since 2 has an inverse modulo \(p\). If \(f(x)-f(z)\ne0\), the equation
\(uw=f(x)-f(z)\) has \(p-1\) solutions. If that difference is zero,
it has \(2p-1\) solutions. Thus
\[
\sum_bN_a(b)^2=(p-1)(p^2-T)+(2p-1)T=p^2(p-1)+pT. \tag{1}
\]
Equal counts make the left side \(p^3\), hence \(T=p\). The \(p\)
pairs \((x,x)\) already account for these collisions, so \(f\) is
one-to-one, and therefore a permutation of the residues. Conversely, if
\(f\) is a permutation, every \(y\) gives exactly one solution of
\(f(x)=y^2-b\). All counts then equal \(p\).

It remains to decide when \(f\) is a permutation. We use the elementary
power sums
\[
\sum_{x\in\mathbb F_p}x^r=
\begin{cases}
-1,&r=p-1,\\
0,&1\le r<2(p-1),\quad r\ne p-1.
\end{cases} \tag{2}
\]
Here is a proof. For \(1\le r<p-1\), the polynomial \(X^r-1\) has
at most \(r\) roots, so some nonzero \(c\) satisfies \(c^r\ne1\).
Multiplication by \(c\) permutes the residues; multiplying the sum by
\(c^r\) leaves it unchanged, forcing it to be zero. For \(r=p-1\),
Fermat's little theorem gives \(p-1=-1\) as the sum. The larger exponents
in (2) reduce to the first case by the same theorem. Fermat's theorem here
also follows by multiplying all nonzero residues: multiplication by any
nonzero \(c\) permutes them, giving \(c^{p-1}=1\).

If \(p\equiv1\pmod3\), put \(k=(p-1)/3\). In
\((x^3+ax)^k\) the leading term is \(x^{p-1}\), and all other
terms have positive degree below \(p-1\). Equation (2) gives
\(\sum_x f(x)^k=-1\), whereas a permutation would give
\(\sum_x f(x)^k=\sum_xx^k=0\). This is impossible.

If \(p\equiv2\pmod3\), put \(k=(p+1)/3\). The degrees in
\((x^3+ax)^k\) range from \(k\) to \(p+1<2(p-1)\). The
coefficient of \(x^{p-1}\) is \(ka\), from choosing \(ax\) in
exactly one factor. Equation (2) therefore gives
\(\sum_x f(x)^k=-ka\). A permutation forces this to be zero.
Since \(0<k<p\), we obtain \(a=0\).

Finally, if \(p\equiv2\pmod3\), the integer
\(e=(2p-1)/3\) satisfies \((x^3)^e=x^{2p-1}=x\) for every
residue \(x\). Thus cubing is one-to-one and is a permutation.
This proves the asserted answer. \(\square\)

## Optional elliptic-curve background

For most \((a,b)\), the equation being counted is the affine part of an
elliptic curve. Singular equations are intentionally included: omitting
them would change the problem and invalidate the simple average. The
projective point at infinity is not included in \(N_a(b)\).

Equation (1) can also be written
\[
\sum_b(N_a(b)-p)^2=p(T-p).
\]
So variation in these point counts measures precisely the collisions of
the cubic map. This elementary identity, rather than any estimate for
elliptic curves, explains the classification. Cubic permutation polynomials
and point-count moments are classical topics; see [prior art](PRIOR_ART.md).

## Design assessment and edge cases

Target: A3/A4; independent Astra assessment: approximately A4. The two
discoveries are the double count and the useful power-sum exponent. All
finite-field facts needed beyond arithmetic modulo a prime are proved
above. The original conic-counting route was replaced by the cleaner
power-sum route found during the independent attempt.

For \(p=5\), just \(a=0\) works; for \(p=7\), none works.
The hypothesis \(p>3\) matters: modulo 3, both \(a=0,1\) work,
and modulo 2 every \(a\) works. Zero values of \(x,y,a,b\) are
allowed throughout. No nonsingularity assumption is implicit.
