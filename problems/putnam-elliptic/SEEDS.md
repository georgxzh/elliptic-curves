# Six seeds and selection record

Explored on 2026-11-08 with `gpt-6-astra`. These are problem proposals,
not research claims. The list records the developed pool, including
reformulation and rejection after testing and source checks.

## 1. A quartic that always has two zeros — selected

**Precise problem.** For real \(a,b\), not both zero, prove that
\(t^4-6at^2+8bt-3a^2\) has exactly two distinct real zeros.

**Key insight.** Divide by \(t\); the derivative becomes
\(3(t^2-a)^2/t^2\). The two half-lines each contribute one root.
Expected difficulty: A1/A2.

**Connection.** This is exactly the discriminant of the residual quadratic
for a line through a point on a Mordell cubic. The repository supplied the
expression, not an assumed theorem about its roots.

**Stress test.** Omitting “not both zero” makes the assertion false.
When \(a=0\), the zero at the origin needs separate treatment.
When \(a=r^2,b=r^3\), there is a triple root; “distinct” is essential.
The expression itself has an exact online precedent, disclosed in
[PRIOR_ART.md](PRIOR_ART.md). Retain the root-count formulation, not a claim
to have invented this quartic.

## 2. Constant point counts — selected

**Precise problem.** For prime \(p>3\), define
\(N_a(b)=\#\{(x,y)\bmod p:y^2=x^3+ax+b\}\). Determine all
\(a\bmod p\) for which this count is independent of \(b\bmod p\).

**Key insight.** A second-moment double count forces the cubic map to be
a permutation. Carefully chosen sums of powers then classify it.
Expected difficulty: A3/A4, settled editorially at A4.

**Connection.** Instead of estimating the number of points on one curve,
study when an entire family has no variation. Singular parameter values
must be retained. This is an elementary finite analogue of the repository's
interest in moments, with no dependence on its research bounds.

**Stress test.** The answer is \(a=0\) if \(p\equiv2\pmod3\), and
no classes otherwise. The primes 2 and 3 give different answers. An initial
quadratic-character conic argument was valid but less accessible; the
independent reviewer found the cleaner power-sum ending used in the final
solution. A stronger published variance theorem implies the result, so
originality is limited to the contest design and elementary presentation.

## 3. Polynomial square-value rigidity — selected

**Precise problem.** If \(P\in\mathbb R[t]\) and \(P(n)^3+1\) is
an integer square for every positive integer \(n\), prove that \(P\)
is constant.

**Key insight.** High finite differences of the integer square roots tend
to zero, so they eventually vanish exactly. Interpolation gives a polynomial
identity; a derivative and degree comparison finish it. Expected difficulty:
A5/A6 in exploration; independent assessment A4/A5. Final label: A5,
with the disagreement retained.

**Connection.** The impossible identity would give a nonconstant polynomial
tracing of \(Y^2=X^3+1\). This obstruction can be proved with derivatives
instead of algebraic geometry.

**Stress test.** Real coefficients may not be silently replaced by integers.
The square root is differentiated only on a positive tail. Constant zero
values and negative admissible constants are allowed. Testing any finite
prefix cannot prove the hypothesis: \(2+\prod_{j=1}^M(t-j)\) passes
the first \(M\) tests. The finite-difference square-value lemma has a
close published-online precedent and is not claimed as new.

## 4. Three consecutive quadratic residues — rejected as too familiar

**Precise problem.** For a prime \(p\equiv3\pmod4\), prove that
exactly \(\lfloor(p-3)/8\rfloor\) residues \(a\bmod p\) have
\(a-1,a,a+1\) all nonzero quadratic residues.

**Key insight.** Let \(\chi\) be 0 at zero, 1 on nonzero squares,
and -1 otherwise. Expand
\(\sum_a(1+\chi(a-1))(1+\chi(a))(1+\chi(a+1))\).
The single sums vanish; pair correlations are -1 by counting a difference
of squares; the cubic sum cancels under \(a\mapsto-a\).
Expected difficulty: A3/A4.

**Connection.** The cubic term is the point-count sum for
\(y^2=x^3-x\); its odd symmetry is the useful geometric feature.

**Stress test and result.** The expanded sum is \(p-3\), but it is
not yet eight times the desired count: \(a=1\) contributes
\(2(1+\chi(2))\). Thus \(8N=p-5-2\chi(2)\). Integrality
determines which sign is possible for each \(p\bmod8\), giving the
formula without quoting quadratic reciprocity. In particular \(p=3,7,11\)
must give 0,0,1. Bounded checks include these cases. Counting consecutive
residues is classical, and Putnam 1991 B5 already treats a related two-square
intersection count. The second selected seed has a stronger organizing idea.

## 5. Equal perimeter and area — rejected for close precedent and scope

**Precise problem.** Prove that infinitely many pairwise noncongruent
triangles have rational side lengths, perimeter 12, and area 6.

**Key insight sought.** Heron's formula translates this into positive
rational triples \(x+y+z=6,xyz=6\). Tangents and chords should produce
new points; positivity and infinitude require separate arguments.
Expected difficulty: A5/A6 if a sufficiently short proof is found.

**Connection.** The substitutions
\(u=12-24/z\), \(Y=24(x-y)/z\) give the cubic
\(Y^2=u^3-144u+576\).

**Stress test and rejection.** The exact non-right triangle
\((41/15,101/21,156/35)\) has the required perimeter and area, as checked
with rational arithmetic. But obtaining one more triangle proves neither
infinitude nor noncongruence. An exploration route used odd multiples on a
real component and denominator growth; it was not developed into a complete
elementary proof here and must not be treated as certified by this project.
More decisively, this exact triangle and the same geometric question appear
in teaching literature. Changing the numbers would not remedy the problem.

## 6. Two integral tangent steps — reserve, not a finalist

**Precise problem.** Let \(B\ne0\) be a squarefree integer and
\(P=(x,y)\) an integral point on \(Y^2=X^3+B\). Let \(Q\) be the
third intersection of the tangent at \(P\) with the cubic, and let \(R\)
be the third intersection of the tangent at \(Q\). Assume both tangents
are nonvertical and both \(Q,R\) have integer coordinates. Intersections
are counted with multiplicity and may coincide. Prove that \(B=1\) and
\(P\in\{(0,1),(0,-1),(2,3),(2,-3)\}\).

**Key insight.** Squarefreeness gives \(\gcd(x,y)=1\). The tangent
slope \(m=3x^2/(2y)\) has \(m^2=x(Q)+2x\in\mathbb Z\),
so \(m\in\mathbb Z\), forcing \(x\) even and \(|y|\in\{1,3\}\).
Apply the same argument at \(Q\). Expected difficulty: A2/A3.

**Connection.** The elementary remnant of torsion/integrality restrictions
is that successive tangents rarely preserve integral coordinates.

**Stress test and resolution.** The third ordinate is
\(y(Q)=y+m^3-3mx\). If \(|y|=1\), its absolute value is
\(|27x^6-36x^3+8|/8\); for even \(|x|\ge2\) this exceeds 3,
so \(x=0\) and \(B=1\). If \(|y|=3\), the absolute value is
\(|x^6-12x^3+24|/8\). For even \(x\le-2\) or \(x\ge4\)
it exceeds 3. Of the remaining \(x=0,2\), the first gives nonsquarefree
\(B=9\), and the second gives \(B=1\). All four claimed starting points
work, including the flex at \((0,\pm1)\). Requiring three distinct
intersections would incorrectly remove these cases. The statement has too
much geometric bookkeeping for its payoff compared with the selected trio.

## Additional discarded exploration

A second Astra explorer proposed: for every \(n\ge0\), find positive
pairwise coprime odd \(A,B,C\) with
\(A^3-C^2=2^{6n+1}B^6\). Tangent doubling from \((3,5)\) on
\(y^2=x^3-2\) suggests a denominator-doubling construction. This was
not promoted to a seventh main seed: its valuation condition feels
artificial, its mechanism is standard, and it does not improve the range
of the final set. No complete proof or independent audit is claimed here.
