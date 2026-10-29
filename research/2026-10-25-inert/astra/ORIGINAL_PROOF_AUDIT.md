# Audit of the original local and global proofs

2026-10-25. Scope: `LOCAL_PROOF.md` and `GLOBAL_PROOF.md`, read in full.
This is a separate AI audit, not independent human certification or a novelty
assessment. No substantive mathematical gap was found in these two arguments.
The conclusions below use the established descent and Thue results cited in
the notes; this audit does not reprove those results.

## Local argument

* **Primitivity.** Alpöge–Ho Lemma 3.3 applies to the PID `Z_p`. Both
  quartics satisfy its integer-matrix hypothesis when `p>3`, since 4 and 6
  are units. A primitive integral matrix therefore has primitive first row.
  Monicity then forces `b` to be a unit whenever `p | det(g)`.
* **Derivative identity.** With rows `(a,b),(c,d_0)`, `z=a/b`, and
  `D=ad_0-bc`, the gradient equation is
  `b^3[(c-zd_0)F'(z)+4d_0F(z)]=0`. Since `c-zd_0=-D/b`, it gives exactly
  `F'(z)=4d_0D/b^3`. In particular the claimed valuation inequality and
  repeated-root restriction follow with the correct powers of `b`.
* **Unit x.** The expansion about `t=y/x` is correct. If `3r<2e`, the
  `4ts^3` term alone has least valuation. For `e=1,2`, the only such case
  is `e=2,r=1`, producing odd valuation 3. Otherwise `r>=e` and the
  constant term alone has valuation `2e`. Its normalized residue is
  `4u/x`. Since `x=t^2 mod p`, the square obstruction is exactly that
  asserted in the proposition. The case `s=0` is covered as well.
* **Nonunit x.** The curve equation forces `v_p(x)>=e` and `v_p(y)=e`.
  For `e=2,v_p(z)=1`, the `8yz` term alone has valuation 3. Once
  `v_p(z)>=e`, the derivative has valuation exactly `e`, including when
  `x=0` or `z=0`. Combining this with the valuation of `F` forces `k=e`.
* **Lattice.** Dividing the first row by the unit `b` and eliminating the
  second coordinate of the second row gives `(z,1),(-D/b,0)`.
  Consequently the stated residue of `z` determines a unique possible
  nonstandard lattice. The proposition makes no unsupported existence claim.

For complete formality, the opening sentence could explicitly state
`g in GL_2(Q_p)`; invertibility is already implicit in the definition of
the twisted action. This is a presentation improvement, not a proof gap.

## Global argument

* **Action and orbits.** The convention is internally consistent:
  `T_U(T_T f)=T_(UT)f`. The point quartic has the stated invariants and
  discriminant. Its coefficients recover `(x,y)`, including the sign of
  `y`. The rational orbit count used is a valid upper bound.
* **Normalization.** A rational projective matrix has an integral
  representative primitive in all four entries, unique up to sign. This
  is primitive over every `Z_p`. Lemma 3.3 applies over `Z` because both
  endpoint quartics are integer-matrix forms. Its determinant divisibility
  applies to the discriminant of this actual model; minimality is unnecessary.
* **Fixed primes.** The exact valuation of the quartic discriminant is
  `12v_p(2)+3v_p(3)+2v_p(d)+4v_p(n)`. Cube-freeness gives the final
  contribution at most 8, so the displayed `K_p` is valid and independent
  of `n`. The number of index-`p^k` sublattices of `Z_p^2` is
  `1+p+...+p^k`; allowing all such lattices is a legitimate overcount.
* **Global injection.** For a finite-index lattice `L`, the finite group
  `Z^2/L` is detected by its p-primary components. Thus an integral vector
  lying in every completed lattice lies in `L`. This proves the required
  injection for actual lattices, without a gluing or stabilizer assumption.
* **A fixed lattice.** Every basis matrix is related to an occurring
  matrix by left multiplication in `GL_2(Z)`. Therefore `F=T_T f` is
  integral, with unchanged nonzero discriminant. Its leading coefficient
  may vanish in the chosen coordinates, but as a homogeneous binary quartic
  it still has degree 4 and four distinct projective roots, which is what
  the cited theorem requires.
* **Thue bound and signs.** The quoted theorem applies to reducible forms
  and to roots at infinity. Its specialization gives `7^192` classes of
  unit representations modulo simultaneous sign. For a fixed first row
  and determinant sign, equal determinants make the second-row difference
  a multiple of the first row. The resulting cubic coefficient changes by
  exactly four times that multiple, so depression forces uniqueness.
  The additional factor 2 for the two determinant signs is necessary and
  sufficient. No further factor from sign representatives is required.

The resulting constant `A_d=8*7^192*M_d` follows. The proof remains an
individual-curve estimate and supplies no rank average for an inert-supported
sampling family.

## Source verification and limits

I inspected the exact statements and relevant proofs in
[Alpöge–Ho, arXiv:1807.03761v3](https://arxiv.org/html/1807.03761): Theorem
2.2, Section 3.1, Lemma 3.3, and Theorem 3.5. In particular, Lemma 3.3
has the primitive-first-row and determinant-divisibility conclusions used
here. Theorem 3.5 requires at least three distinct projective roots and
does not impose irreducibility. Its displayed exponent specializes to 192.
The notes correctly retain the determinant-sign multiplicity rather than
depending on the first-row injectivity assertion in the surrounding source
argument.

The underlying Evertse reference is
[On equations in S-units and the Thue–Mahler equation, Invent. Math. 75
(1984), 561–584](https://doi.org/10.1007/BF01388644), Theorem 3. Its
bibliographic identity was verified, but the publisher exposed only a
subscription preview and EuDML returned HTTP 403. Accordingly, verification
of that theorem's exact formulation stops at its explicit statement in
Alpöge–Ho; I did not inspect Evertse's original proof. This is a source-audit
limit, not an identified mathematical defect in the notes.

No changes to the two audited proof files were made. No finite numerical
test is used to justify this audit's conclusions.
