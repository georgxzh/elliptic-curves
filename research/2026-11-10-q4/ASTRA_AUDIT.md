# Independent Astra audit, 10 November 2026

Model: `gpt-6-astra`, separate agent `astra_q4_audit`. The audit was
requested only after the balanced-block proof, counterexample, and
local identity were concrete. The agent did not edit or commit files.
This record summarizes its findings; it is not a claim of formal
verification or an independent proof of all imported analytic machinery.

## Primary argument

The auditor independently read [Dunn--Radziwill v3](https://arxiv.org/html/2109.07463v3),
Definition 3.1, Lemma 6.1 through (6.5), Proposition 10.1, and the
relevant transitions in Sections 8 and 11. Its conclusion was that
the balanced composite bilinear theorem passes under the stated GRH
and Proposition 10.1, and does not establish Q4.

It checked:

1. The extra quadratic factor leaves every cubic/angular test
   nonprincipal. The R=1 contour argument retains the required
   uniformity in k,ell,t; the extra conductor has bounded norm factor.
   For u!=1, prime support leaves at most one term and B/Nu is in
   [1/2,1], verifying the divisibility part of C_eta.
2. All six error exponents, including the ||alpha||_2 factor. It
   independently obtained 49/75, 5/6-rho/2,
   41/60+3epsilon/10, 91/120+epsilon/2,
   7/10+2eta/5+epsilon/2, and 4/5+epsilon/2.
   The choice delta=min(rho/4,1/100) is valid.
3. The model main term O_W(X^(19/30)log^2 X), uniformly in arbitrary
   bounded alpha. In fact B^2>10A eventually, so at most one prime
   divisor of each a lies in the b-range; the exclusion costs only
   O(X^(13/30)).
4. The C_eta nonclosure example with psi=(4/.)_3. It supplied the
   explicit primary witness -2+3omega of norm 19, where psi=omega^2;
   the post-twist test counts asymptotically B/log B primary primes.
5. Every value of the local Fourier identity by exact integer
   arithmetic, and the proof using the twelve units modulo 4.
   It also supplied the primary norm-7 witness for kappa.
6. The stated gap in the cubic Voronoi/long Type I transition: both
   the u character and the cube variable change after twisting.

Precision changes requested and incorporated: retain a smooth cutoff
equal to one on [1,2] with sharp prime endpoints in Lemma 1; retain
the fixed 3-adic primary-generator convention; restrict the modulus-4r
discussion to odd r; call the new character noncubic (its order is
two when its cubic part is trivial, six otherwise). The coefficient
nonclosure assertion concerns families with constants uniform in B.

## Final report and secondary tail argument

The same agent then read Q4_REPORT.md and TAIL_REPORT.md. It checked
the Jackson normalization, first and second moments, degree-2L
attenuation, endpoint/BV sampling conventions, physical X^(2/3)/L
threshold, and both maximum and weighted mean-square criteria.
It checked the exact finite-field energy formulas and ran the new
script's assertions in memory with output-file writing disabled.
It also confirmed the exact inert correction, both progression
normalizations, Q4's necessity given P, and Yoshimoto's original
degree-one prime-modulus hypothesis directly from Theorem 2.

It requested two small presentation fixes: distinguish Eisenstein
residue arithmetic from Gaussian-integer Fourier values; write the
P(X;V) asymptotic additively for general signed V, whose Mellin integral
can be zero. Both are corrected.

The primary theorem depends on GRH. The local identities and tail
inequalities do not. The auditor did not certify Q4, the sharp-interval
arithmetic hypotheses, or novelty.
