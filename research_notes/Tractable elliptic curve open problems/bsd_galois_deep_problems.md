# BSD, Galois images and adjacent deep problems: status at November 2026 and which sub-questions are computationally testable

Status tags used throughout. **[T]** theorem, published or accepted. **[T*]** theorem claimed in an arXiv preprint with no journal reference found (not refereed as far as I could verify). **[C]** conditional theorem. **[Cj]** conjecture. **[N]** numerics, not proof. **[A]** announced, no paper found. Theorem statements for arXiv 2409.01350, 2312.09301, 2106.11141, 2507.17967, 1010.2431 and 2608.10919 were read from the extracted PDF text. Most others were read through a summarising fetch, so check wording against the source before quoting.

Search date: 1 Nov 2026. Workstation assumed: 16 cores, PARI/GP, Python, C, no Magma.

## Q1. BSD: what is proved in rank 0 and 1, proportions, numerical verification, and the situation for rank >= 2

### Takeaway
The rank 0/1 theory is now close to complete prime by prime: p-converses and p-parts of the formula are known for almost all p, with the residual gaps at p = 2, at p = 3, and at some additive, Eisenstein and non-semistable cases. Full BSD is known for all curves of rank <= 1 and conductor < 5000 and for infinite twist families, while for rank >= 2 not one curve is known to have finite Sha, and Sha_an is not known to be rational for a single curve. Computation can prove finite statements (the formula for one curve in rank <= 1, Sha[p] = 0 for one pair (E,p) in higher rank) but cannot touch the Clay statement.

### Cited Findings

**Rank 0/1, the classical implication**
- [T] The implication ord_{s=1} L = r <= 1 implies rank = r and Sha finite is credited to Gross-Zagier, Kolyvagin and Rubin — [Burungale-Skinner-Tian-Wan, arXiv:2409.01350](https://arxiv.org/abs/2409.01350); analytic-rank-0/1 equality attribution also in [LMFDB analytic rank knowl](https://www.lmfdb.org/knowledge/show/ec.q.analytic_rank).
- [T] Miller: for r_an <= 1 there are algorithms computing both E(Q) and Sha; "It is worthy to note" that Sha_an "is not even known to be a rational number for a single curve" with r_an > 1 — [Miller, arXiv:1010.2431](https://arxiv.org/pdf/1010.2431).

**p-converse and p-part of the formula**
- [T] Wei Zhang (Cambridge J. Math. 2014): indivisibility of derived Heegner points (Kolyvagin 1991 conjecture) for good ordinary p >= 5 with local ramification conditions, giving a rank one p-converse and the p-part of the refined BSD formula in rank one — [Zhang](https://math.mit.edu/~wz2113/math/online/Kconj.pdf). Hypotheses restated as p not dividing 6N, surjective mod p, ramification conditions — [BCGS, arXiv:2312.09301](https://arxiv.org/abs/2312.09301).
- [T] Rank one p-part for semistable curves, p >= 5 good, E[p] irreducible — [arXiv:1512.06894](https://arxiv.org/html/1512.06894v1). Split multiplicative p-converse in rank 1 — [arXiv:1407.1816](https://arxiv.org/pdf/1407.1816). Supersingular p > 3, semistable, rank one p-converse (Castella-Wan) — [par.nsf.gov](https://par.nsf.gov/servlets/purl/10549768). CM rank one p-converse at good ordinary p (Burungale-Tian) — [Caltech record](https://authors.library.caltech.edu/records/va3nw-phx39).
- [T*] Burungale-Skinner-Tian-Wan, "Zeta elements for elliptic curves and applications", arXiv:2409.01350v2 (11 Sep 2024, no journal listed) — [abs](https://arxiv.org/abs/2409.01350). Exact statements from the PDF:
  - Thm 1.3: E/Q semistable, p > 2 supersingular (a_3 = 0 if p = 3). Kobayashi's signed main conjecture holds: (L_p^o(E)) = xi(X^o(E)) for o = +,-, also for quadratic twists by discriminants coprime to Np divisible only by primes of ordinary reduction. First non-CM cases.
  - Thm 1.5: same hypotheses, r_an <= 1 implies the p-part of the BSD formula.
  - Thm 1.6: same hypotheses, corank Sel_{p^inf} = 0 implies L(1,E) != 0.
  - Thm 1.7: for E one of 46a1, 62a1, 66b1, 69a1, 77c1, 94a1, 105a1, 106d1, 114b1, 115a1, 118c1, 118d1, 141b1, 141c1, 141e1, 142c1, and squarefree M > 1 coprime to N with L(1,E^M) != 0 and E ordinary at primes dividing M, the full BSD conjecture holds for E^M; infinitely many such M exist. Authors state this is the first infinite family of non-CM curves with full BSD (previously only finitely many, by theory plus computation).
  - Thm 1.9: p not dividing 2N ordinary, mod p absolutely irreducible, and (ram) some l || N with rho-bar ramified at l. If r_an = 1 then the p-part holds.
  - Thm 1.10: p not dividing 2N ordinary, rho-bar surjective, (ram). Corank 1 implies r_an = 1.
  - Thm 1.13: Perrin-Riou's conjecture on Beilinson-Kato elements for all p not dividing 2N (with a_3 = 0 if p = 3 supersingular).
- [T, to appear Cambridge J. Math per arXiv comment] Burungale-Castella-Grossi-Skinner, arXiv:2312.09301v2 (18 Jan 2026) — [abs](https://arxiv.org/abs/2312.09301). Thm A: p odd good ordinary, K imaginary quadratic with Heegner hypothesis, D_K odd and not -3, E(K)[p] = 0, p split in K, and the rational anticyclotomic main conjecture: the Heegner point Kolyvagin system is nonzero. Unconditional in two cases: rational p-isogeny with kernel F_p(phi), phi|G_p != 1, omega; or p > 3 with E[p] irreducible. Cor A: ord(kappa^Heeg) = max(r^+, r^-) - 1 for arbitrary Selmer coranks. Thm B: p > 3, surjective, integral main conjecture, p-optimal parametrisation: M_inf = sum_{l|N} ord_p(c_l) (Zhang's refined conjecture). Thm C: non-vanishing of Kato's Kolyvagin system for non-CM E, p odd good ordinary, E(Q_p)[p] = 0, with Cor C: ord(kappa^Kato) = corank of the fine Selmer group.
- [T] Inputs to the above: Castella-Grossi-Skinner, Mazur's main conjecture at Eisenstein primes, Math. Ann. 393 (2025); Burungale-Castella-Skinner, Base change and Iwasawa main conjectures for GL2, IMRN 2025 — bibliography of [arXiv:2312.09301](https://arxiv.org/abs/2312.09301). Sweeting's patched Euler systems relaxed Zhang's hypotheses — [arXiv:2012.11771](https://arxiv.org/pdf/2012.11771).
- [T*] Burungale-Tian, arXiv:2506.03465v2: for E/K with CM by an order of the imaginary quadratic K and any prime p (including p = 2 and non-ordinary p), corank Sel_{p^inf}(E/K) = 0 implies ord_{s=1} L(s,E/K) = 0. With Smith's 2^inf-Selmer distributions this gives the first instance of even parity Goldfeld, for y^2 = x^3 - x — [arXiv:2506.03465](https://arxiv.org/html/2506.03465v2).
- Burungale-Castella-Skinner-Tian, "p^inf-Selmer groups and rational points on CM elliptic curves", Ann. Math. Que. 46 (2022) 325-346 exists — [BSTW bibliography](https://arxiv.org/abs/2409.01350). I did not read its statement (see Gaps).
- [T*] Smith, arXiv:2503.17619 (22 Mar 2025): for every E/Q, 50% of quadratic twists have 2^inf-Selmer corank 0 and 50% corank 1, so BSD implies Goldfeld; the 2-Selmer rank distribution differs from Poonen-Rains where previously unknown — [abs](https://arxiv.org/abs/2503.17619).

**Proportions**
- [T*, arXiv only] Bhargava-Skinner-Zhang, arXiv:1407.1826: at least 66.48% of curves by height satisfy the rank conjecture and have finite Sha; at least 16.50% are rank 0 and 20.68% rank 1 (algebraic and analytic). Rank 0 uses Skinner-Urban and Skinner at p = 5; rank 1 uses Zhang and Skinner-Zhang at p = 5; averages of p-Selmer for p <= 5 come from Bhargava-Shankar and Bhargava-Skinner. Conditional improvements reach 79.7%. Extending Selmer averages to infinitely many primes would give 100% — [arXiv:1407.1826](https://arxiv.org/html/1407.1826). The page shows no journal reference.

**Full BSD numerics and proofs for specific curves**
- [T] Miller: for E of rank <= 1 and N < 5000, BSD(E,p) holds for all p with E[p] irreducible, and for reducible E[p] except 11 pairs, giving 16714 of the 16725 isogeny classes. Tools: Kolyvagin bounds, four independent 2-descents, 3-descent for 31 optimal curves, and the Stein-Wuthrich algorithm for 20 of those — [arXiv:1010.2431v3](https://arxiv.org/pdf/1010.2431). The arXiv v1 figure 16706 differs from v3 — [search record](https://web3.arxiv.org/pdf/1010.2431v1).
- [T] Creutz-Miller, J. Algebra 372 (2012): complete verification for all curves of rank <= 1 and conductor < 5000, using second isogeny descents at p = 5, 7; Miller-Stoll isogeny descents were also used — [arXiv:1105.4018](https://arxiv.org/pdf/1105.4018).
- [T] Grigorov-Jorza-Patrikis-Stein-Tarnita (Math. Comp. 2009): for non-CM curves of conductor <= 1000 and rank <= 1, the formula holds up to odd primes dividing Tamagawa numbers or degrees of rational cyclic isogenies — [record](https://ctarnita.scholar.princeton.edu/document/95).
- [N/T] LMFDB covers all curves of conductor < 500,000, all 7-smooth conductors, and all prime conductors up to 3 x 10^8: 3,824,372 curves in 2,917,287 classes — [Completeness](https://www.lmfdb.org/EllipticCurve/Q/Completeness). Ranks: 36.73% rank 0, 49.34% rank 1, 12.90% rank 2, 0.98% rank 3, 2,086 rank 4, 19 rank 5; largest listed Sha_an 75^2 — [stats](https://www.lmfdb.org/EllipticCurve/Q/stats).
- [N] LMFDB reliability: r_an is rigorous for r_an <= 3 and N <= 500,000; for r_an >= 4 "we cannot compute the exact value" and a claimed r_an = 4 is only known to lie in {2, 4}. Sha_an is exact in rank 0; in rank 1 exact computation has only been done for conductors below 5000; for rank > 1 only a floating point approximation exists since the value is not known to be rational — [Reliability](https://www.lmfdb.org/EllipticCurve/Q/Reliability); [Sha knowl](https://www.lmfdb.org/knowledge/show/ec.q.analytic_sha_order). The analytic-rank knowl has an apparent typo on ranks 2 and 3 — [knowl](https://www.lmfdb.org/knowledge/show/ec.q.analytic_rank).
- [N] Large Sha: Broadhurst obtained analytic |Sha| = 1937832^2 > 3.755 x 10^12 in rank 0 from twists of Frey curves of good abc triples — [arXiv:2111.07794](https://arxiv.org/abs/2111.07794v1).

**Sha in rank >= 2**
- Finiteness for rank >= 2: "not known in a single case" (Stein problem list, 2006) — [MSRI problems](https://wstein.org/msri06/problems/html/node42.html). Reaffirmed Sept 2026: "totally open", no single example of unconditional finiteness — [Banwait, arXiv:2609.08431](https://arxiv.org/abs/2609.08431). Over function fields some cases of analytic rank > 1 are known — [Hamacher-Yang-Zhao, arXiv:2207.11904](https://ar5iv.labs.arxiv.org/html/2207.11904).
- [T] Stein-Wuthrich (Math. Comp. 82, 2013): Sha(E/Q)[p] = 0 for 1,534,422 pairs (E,p): E non-CM, conductor <= 30,000, rank >= 2, p good ordinary, 5 <= p < 1000, rho-bar surjective — [AMS](https://www.ams.org/mcom/2013-82-283/S0025-5718-2012-02649-4/); [paper page](https://www.wstein.org/papers/shark/). The method gives no group structure or elements of Sha — [search record](https://www.wstein.org/papers/shark/). Applicable for p != 2, non-additive, image GL2(F_p) or Borel — [Miller](https://arxiv.org/pdf/1010.2431).
- [T*] Banwait, arXiv:2609.08431 (8 Sep 2026), partly formalised in Lean: for E/Q rank 2 with CM by the maximal order, L(E,1) = 0, w = +1 (analytic rank not assumed), p >= 5 split good outside an explicit set S_E: if the normalised second Taylor coefficient of the MTT p-adic L-function is a p-adic unit, then Sha[p^inf] = 0, Selmer corank 2 and lambda_an = 2. It is equivalent to the cyclotomic p-adic regulator being a unit together with Sha[p^inf] = 0, and to a valuation condition on three critical Hecke L-values of weight 2p-1. Numerics [N]: regulators for y^2 = x^3 - Dx, D = -14, 17, -33, -34, -39, at all 8,052 split good p < 30,000; non-units at only 3 of 8,050 non-excluded primes (p = 37 for D = -33; p = 5, 15289 for D = -39), against about 3.8 expected at random; heuristically about (1/2) log log X failing split primes below X. Resolves p = 577 for D = -34, left open by Coates-Liang-Sujatha. Scope is vertical only: no rank 2 curve gets finite Sha — [arXiv:2609.08431](https://arxiv.org/html/2609.08431).

**Non-square Sha**
- For elliptic curves the Cassels pairing is alternating, so finite Sha has square order; for principally polarised abelian varieties the order is a square or twice a square (Poonen-Stoll) — [arXiv:math/9911267](https://arxiv.org/abs/math/9911267v1). Neither-square-nor-twice-a-square occurs for non-principal polarisations (Stein) — [paper](https://williamstein.org/papers/nonsquaresha/final2.pdf); Keil found k times a square for several k — [arXiv:1206.1822](https://arxiv.org/pdf/1206.1822).
- All Sha_an values computed in LMFDB are integer squares so far — [knowl](https://www.lmfdb.org/knowledge/show/ec.q.analytic_sha_order).

**Rank records (context)**
- Elkies-Klagsbrun 2024: rank >= 29, exactly 29 under GRH; coefficients over 60 digits — [Simons Collaboration](https://simonscollab.icerm.brown.edu/2024/08/record-breaking-elliptic-curve/).

### Inferences
- "Non-square Sha computation" is a non-question for elliptic curves over Q: a non-square Sha_an in rank <= 1 would disprove BSD outright, and rationality fails to be known in higher rank. The live version is rank 0/1 exact Sha_an, or abelian surfaces.
- Open finite verification, rank >= 2: there is no statement "Sha_an checked to a bound" beyond floating point agreement with a square. The only provable finite statements are of the form Sha[p^inf] = 0 for one p. Each such statement also needs a nonzero p-adic regulator, which is itself a computed quantity.
- Since 2012 the theorems available have grown a lot (BSTW Thms 1.5, 1.9, BCGS Thm B, Castella-Grossi-Skinner at Eisenstein primes), while the published verified range stayed at N < 5000 as far as I could find. LMFDB says the same for exact rank 1 Sha. Pushing full BSD beyond 5000 is therefore a real gap between theory and table. Most of the remaining labour is at p = 2, 3 and reducible p.
- Nothing here implies feasibility of the Clay statement. Finite verification proves the formula for listed curves of rank <= 1, where finiteness of Sha and the rank equality were already theorems.

### Gaps
- Could not find any paper extending full BSD verification past conductor 5000. Absence of evidence only; a spoken or unpublished project may exist.
- Did not read Burungale-Castella-Skinner-Tian (2022). From memory it concerns the CM p-converse at some primes, unverified.
- Exact Stein-Wuthrich hypotheses (role of Kato's divisibility and the regulator) were not read: the paper server returned 522 at fetch time.
- Publication status of BSZ and BSTW could not be established beyond the arXiv pages.
- Could not fetch the Wiles Clay PDF; the [Clay page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/) gives only an informal statement.
- Rubin-Silverberg survey and AIM problem lists were not retrieved. An AimPL-specific search returned nothing.
- 2608.25975 ("Introduction to the BSD conjecture") is introductory with questionable arithmetic (a 62.5% claim); not used.

## Q2. Serre uniformity and Mazur's Program B: l-adic images, adelic images, non-split Cartan, and what remains

### Takeaway
As of November 2026 the prime-power picture has shrunk to one genus 3 quartic at 7 (rank 3, resisting Chabauty), X_ns^+(25) (genus 14), X_ns^+(121) (genus 511), and X_ns^+(p) for p >= 19, with p = 19, 23 announced but not published. The most concrete open object is a single explicit plane quartic whose four known points would complete the 7-adic classification. Serre uniformity itself remains open and is not a finite computation.

### Cited Findings

**Prime level**
- [T] For p > 37, non-CM E/Q: rho-bar_{E,p} is surjective or lies in the normaliser of a non-split Cartan; Zywina showed a non-surjective image is the full normaliser or an index 3 subgroup G(p); Le Fourn-Lemos excluded G(p) for p > 1.4 x 10^7; Furio-Lombardo exclude G(p) for every p > 5 — [arXiv:2305.17780](https://arxiv.org/abs/2305.17780) (v2 25 Nov 2025, to appear in Algebra & Number Theory).
- [Cj] rho_{E,l} surjective for non-CM E/Q for all l > 37, and an absolute index bound — [RSZB](https://arxiv.org/pdf/2106.11141). Zywina's explicit form: for l > 13 surjective except (17, -17^2·101^3/2), (17, -17·373^3/2^17), (37, -7·11^3), (37, -7·137^3·2083^3) — [arXiv:2206.14959](https://arxiv.org/html/2206.14959v2).
- The cursed curve X_ns^+(13) (genus 3): rational points are 7 CM points, settled in [BDM+19], and X_ns^+(17) (genus 6) in [BDM+23] — [Hashimoto-Lido-Lombardo-Mascot-Parent, arXiv:2608.10919](https://arxiv.org/html/2608.10919); [BDMTV, arXiv:2101.01862](https://arxiv.org/pdf/2101.01862).
- [A] "the case N = 19 has recently been announced" — [arXiv:2608.10919](https://arxiv.org/html/2608.10919). "recently N = 19, 23 have been announced by Balakrishnan-Muller-Vonk" — [Leonhardt-Rendell, arXiv:2610.30703](https://arxiv.org/html/2610.30703) (22 Oct 2026). Mayle-Rouse (Jan 2026) still list X_ns^+(l), l in {19, 23, 29, 31}, as unknown — [arXiv:2601.17202](https://arxiv.org/html/2601.17202v2).
- X_ns^+(19): genus 8, 15 quadrics in P^7, 7 rational CM points, no others with integer coordinates up to 10,000 — search snippet attributed to [arXiv:1805.06873](https://arxiv.org/pdf/1805.06873).
- Rank = genus for X_ns^+(N) is verified only for primes below 100 (Chen isogeny plus Kolyvagin-Logachev) — [arXiv:2608.10919](https://arxiv.org/html/2608.10919).
- Love-Studnia-Vonk compute arithmetic intersections of CM divisors on non-split Cartan curves when p is inert (8 Apr 2026) — [arXiv:2604.06963](https://arxiv.org/abs/2604.06963). This is theory towards heights, not a points result.

**Method papers 2026**
- [T*] Hashimoto-Lido-Lombardo-Mascot-Parent, arXiv:2608.10919 (11 Aug 2026): equationless geometric quadratic Chabauty for X_ns^+(N), N >= 13 prime, using moduli interpretation and Makdisi-Mascot arithmetic (O(g^3) ring operations, O(g^2) space). Re-derives X_ns^+(13) only. Assumes r = g and rho > 1. Finiteness statement r < g + rho - 1 in general. Code mixes PARI/GP and Magma — [arXiv:2608.10919](https://arxiv.org/html/2608.10919).
- [T*] Leonhardt-Rendell, arXiv:2610.30703: algorithms for de Rham bases and Hodge filtration matrices using modular forms only; first time any step of QC is done for X_ns^+(25) (g = 14) and X_ns^+(29) (g = 24). Timings on 56 cores, 256 GB, total seconds including Zywina's q-expansions, as read from a hard-to-parse table: N = 13: 103; 17: 3,831; 19: 11,909; 23: 90,248; 25: 83,635; 29: 1,034,853. Own steps cost only 2.5 to 884 s. Frobenius step still needs equations, and the local height and finite set steps are not done. Equation-based QC "has yet been unable to compute" X_ns^+(25) or N >= 29 — [arXiv:2610.30703](https://arxiv.org/html/2610.30703).

**Prime power level: RSZB and successors**
- [T] Rouse-Sutherland-Zureick-Brown, Forum Math. Sigma 10 (2022), arXiv:2106.11141v6 (20 Jan 2025): Thm 1.1.6: for non-CM E/Q exactly one holds: (i) X_H is P^1 or rank one elliptic; (ii) X_H has exceptional rational point, H in Table 1; (iii) H in N_ns(3^3), N_ns(5^2), N_ns(7^2), N_ns(11^2), or N_ns(l) for l >= 19; (iv) H in 49.147.9.1 or 49.196.9.1. 22 exceptional images, 20 non-CM j. Table 2 lists curves with unknown X_H(Q): 27.243.12.1 (g 12), 25.250.14.1 (g 14), 49.1029.69.1 (g 69), 49.147.9.1, 49.196.9.1 (g 9), 121.6655.511.1 (g 511), each with rank = genus, rational CM points, no rational cusps — [PDF](https://arxiv.org/pdf/2106.11141).
- [T*] Balakrishnan-Betts-Hast-Jha-Muller, arXiv:2501.07833 (14 Jan 2025): X_ns^+(27) has no non-CM points, via Q(zeta_3)-points of a plane quartic quotient with Jacobian rank 6, using QC over number fields. This completes the 3-adic classification — [abs](https://arxiv.org/abs/2501.07833).
- [T] Furio-Lombardo, arXiv:2507.17967v2 (15 Sep 2025); PLMS DOI 10.1112/plms.70193 per a [citation index](https://www.citedrive.com/en/discovery/on-7adic-galois-representations-for-elliptic-curves-over-q/): Thm 1.4: X_ns^+(49) has exactly 7 rational points, all CM. Cor 1.5: for non-CM E/Q the 7-adic image is the full inverse image of the mod 49 image. Method avoids Chabauty on genus 69: j-map gives a generalised Fermat equation a^2 + 28b^3 = 27c^7 of signature (2,3,7), solved by modularity, level lowering (Poonen-Schaefer-Stoll style) and rational points on twists of the Klein quartic (2-descent, Mordell-Weil sieve, Coleman), in Magma — [arXiv:2507.17967](https://arxiv.org/html/2507.17967v2); scripts at [github.com/DavideLombardoMath/7-adic-representations](https://github.com/DavideLombardoMath/7-adic-representations).
- [Cj] Furio-Lombardo Conjecture 1.6 (the single remaining 7-adic object): C: x^4 + 3x^3y - 3x^2yz - 3x^2z^2 + 6xy^3 - 6xy^2z + 3xyz^2 - 2xz^3 + 4y^4 + 2y^3z - 5yz^3 = 0 has C(Q) = {[0:0:1], [1:1:1], [2:0:1], [-1:0:1]}. Thm 1.7 [C]: under this, the 7-adic classification is complete, since 49.147.9.1 and 49.196.9.1 (their X_ns^#(49), X_sp^#(49)) reduce to a^2 + 196b^3 = 27c^7 — [PDF](https://arxiv.org/pdf/2507.17967).
- Properties of C = X_{E_3} from their section 6.5: rk J(Q) = 3 with the four points giving rank 3, J(Q) torsion-free; bitangents defined over a field of degree 28; J(F_p) has a 7-torsion point for all p <= 500 with p = +-1 mod 7, suggesting a 7-torsion point over Q(zeta_7)^+ (etale cover of genus 15); endomorphisms defined over the degree 336 splitting field of x^8 - 2x^7 + 7x^4 - 14x^2 + 8x + 5; End(J) trivial over Q; End over Q(sqrt(-7)) tensor Q = Q(sqrt(-7)), which is not Rosati-symmetric, so QC gets no input from it (Remark 6.7). They note it suffices to treat c = -z^2, with extra j-denominator constraints — [PDF](https://arxiv.org/pdf/2507.17967).
- Furio-Lombardo on extensions: for X_ns^+(25) the equation f(x,y) = kz^5 with f quadratic may have infinitely many solutions, so the method does not apply directly; X_ns^+(121) maps to the rank 1 elliptic curve X_ns^+(11), which makes it harder. [C] Under abc, X_ns^+(7) x X_ns^+(p) has only CM points for large p — [arXiv:2507.17967](https://arxiv.org/html/2507.17967v2).
- X_ns^+(25): point search over height <= 1000 on X_ns^+(5) took about 6 hours and found only 8 CM points; no map to a genus 2 curve found. X_ns^+(121): no model computed; a Mordell-Weil sieve shows a non-CM point has height of j roughly 10^(7.92·10^202) or larger — [RSZB section 9](https://arxiv.org/pdf/2106.11141).
- Genus 2 rank 2 curves 25.50.2.1 and 25.75.2.1 are "handled by Balakrishnan et al." — [RSZB](https://arxiv.org/pdf/2106.11141); contradicted in tone by Derickx et al., who write 25.75.2.a.1 "(conjecturally) has exactly two rational points" — [arXiv:2602.20964](https://arxiv.org/html/2602.20964v2). Unresolved discrepancy.

**Adelic (composite level)**
- [C, Cj] Zywina, arXiv:2206.14959v2 (22 Mar 2024): classification up to Serre uniformity and rational points on finitely many explicit curves of genus >= 2; Conjecture 1.3: index <= 2736 for non-CM E/Q (attained at j = -7·11^3, -7·137^3·2083^3); index lies in an explicit set of 48 integers — [arXiv:2206.14959](https://arxiv.org/html/2206.14959v2).
- [C] Derickx-Hashimoto-Najman-Shnidman, arXiv:2602.20964v2 (9 Mar 2026): assuming Conjecture 4.7 (equivalent to Serre uniformity in explicit form plus Zywina's exceptional list), 160 pairs (K_i, M_i) parameterise all non-CM images up to twist: 138 twist parameterised, 22 twist isolated; 41 twist-isolated j-invariants; every rational point on every modular curve is "explained by geometry" — [arXiv:2602.20964](https://arxiv.org/html/2602.20964v2).
- Count conflict: Zywina's text gives 53 groups and 81 exceptional j-invariants — [v2](https://arxiv.org/html/2206.14959v2); Derickx et al. say Zywina listed 77 — [arXiv:2602.20964](https://arxiv.org/html/2602.20964v2). Possibly different definitions; not resolved.
- [T*] Mayle-Rouse, arXiv:2601.17202v2 (Jan 2026): construct maps X_G -> E with E rank 0. For level <= 70 with -I in G and surjective determinant: of 804,450 groups, 797,591 map to a rank 0 elliptic curve; all rational points determined for all but ten: 58.812.61.a.1, 58.812.61.b.1, 58.2436.175.a.1, 57.1026.67.a.1, 57.1026.72.c.1, 69.1518.104.a.1, 69.1518.115.b.1, 46.1518.104.a.1, 62.930.63.a.1, 55.3300.239.a.1. All but the last map to X_ns^+(l), l in {19, 23, 29, 31}. Their minimal covers of level <= 70 have no non-CM points. 6,859 groups fall outside the method: 2,137 genus 0, 1,401 genus 1 of positive rank, 3,321 with finitely many points. Cost: about 79 CPU hours, desktop 128 GB, up to 33 GB; largest genus 54 about 9 hours; 58.812.61.a.1 ran out of memory (degree 280 map; largest run 126). Requires Magma V2.29-2 and Zywina's Magma code; code at [github.com/rouseja/ModCrvToEC](https://github.com/rouseja/ModCrvToEC) — [arXiv:2601.17202](https://arxiv.org/html/2601.17202v2); [listing](https://arxiv.org/abs/2601.17202).

### Inferences
- Updated open list at prime power level. 3-adic: closed (preprint). 5-adic: X_ns^+(25). 7-adic: quartic C only. 11-adic: X_ns^+(121). Prime level: X_ns^+(p), p >= 19 (with 19, 23 announced). Note 2-adic, 13, 17 are done per [arXiv:2507.17967](https://arxiv.org/html/2507.17967v2).
- Quartic C is the sharpest finite problem in the whole survey, but it is a mathematical problem rather than a compute problem. r = g = 3 and End_Q trivial gives rho(Q) = 1 (NS tensor Q is the Rosati-symmetric part of End), so r < g + rho - 1 fails and plain QC has no finiteness guarantee, consistent with Remark 6.7.
- My hand character computation, to be double-checked: take G = PGL2(7), and NS tensor Q over Q-bar = 1 + chi_8, with chi_8 the irreducible 8-dimensional character (inner values 8, 0, -1, 0, 1 on orders 1, 2, 3, 4, 7; outer values 2, -1, 0 on orders 2, 6, 8; its norm checks to 1). Then the invariants of chi_8 vanish on PSL2(7), the Borel 7:6 and S_4, and are 1-dimensional on the dihedral groups of orders 16 and 12. So the smallest field carrying a non-scalar Rosati-symmetric endomorphism has degree 21 (next 28, matching the bitangent field). QC over number fields as in 2501.07833 used a quadratic field. A degree 21 instance looks very expensive. Better bets are the c = -z^2 restriction, the conjectural 7-torsion cover, or direct work on the genus 9 curves.
- Candidate low-risk project: triage the 3,321 finite-point curves in the Mayle-Rouse list for local obstructions and low-rank maps with Python plus PARI, using LMFDB models. New output would be a smaller residual list, plausibly a short note.
- Not for this workstation: X_ns^+(23), (25), (29) via QC. Two groups have announcements or partial code, Magma is needed for Frobenius lifts, and q-expansion time alone runs from a day to many days on 56 cores.
- Ten Mayle-Rouse curves: finite and rank-0 in principle, but Magma-based, genus 61 to 239, and memory-limited. Reimplementing Zywina's machinery in PARI is a large project. The result would be new entanglement theorems, without resolving X_ns^+(l).

### Gaps
- No paper found for X_ns^+(19) or (23). I treat them as open pending publication.
- Why 55.3300.239.a.1 alone does not map to X_ns^+(l) is not explained in what I read. Whether a rank 0 map exists explicitly is implied, not stated.
- Whether any group outside Furio-Lombardo has attacked Conjecture 1.6 since Sept 2025: none found.
- Could not retrieve Sutherland's current pages. LMFDB modular curve status of the labels above not checked live.
- Current publication status of 2501.07833 not verified.

## Q3. Hilbert's tenth problem over rings of integers: what elliptic curve input was used

### Takeaway
Hilbert's tenth problem is now negative for every infinite finitely generated ring, via rank-stable abelian varieties in quadratic extensions, in two independent proofs. The input is existence of positive rank with no growth, proved by 2-descent or isogeny Selmer methods plus additive combinatorics or sieving. There is no interesting open computational question left here.

### Cited Findings
- [T*] Koymans-Pagano, arXiv:2412.01768v3 (revised Nov 2025): Thm 1.1: H10 is negative for every infinite finitely generated ring. Thm 1.2: Z is Diophantine over O_K for every number field K (Denef-Lipshitz). Thm 2.4: if K has at least 32 real places and L = K(i), there is E/K with rk E(K) = rk E(L) > 0. Cor 2.5 reduces to K containing Q(sqrt 5, sqrt 7, sqrt 11, sqrt 13, sqrt 17, sqrt 19) with a real place. Eisentrager's thesis gives Thm 1.2 implies Thm 1.1 — [arXiv:2412.01768](https://arxiv.org/html/2412.01768v3).
- Method: curves with full rational 2-torsion, combining additive combinatorics (Green-Tao) with 2-descent; unconditional, where Mazur-Rubin needed finiteness of Sha — [arXiv:2412.01768](https://arxiv.org/pdf/2412.01768). Expository article: [arXiv:2602.04468](https://arxiv.org/abs/2602.04468) (4 Feb 2026), explaining Poonen's criterion reducing the problem to elliptic curves.
- [T*] Alpoge-Bhargava-Ho-Shnidman, arXiv:2501.18774 (30 Jan 2025): for any quadratic extension K/F of number fields there is an abelian variety A/F of positive rank with no rank growth over K, hence H10 negative for O_K — [abs](https://www.arxiv.org/abs/2501.18774). Their approach uses l-isogeny Selmer groups of Jacobians of hyperelliptic curves — [search record](https://export.arxiv.org/pdf/2501.18774).
- [T*] Zywina, arXiv:2505.16960: for any quadratic L/K there are infinitely many E/K with rank E(K) = rank E(L) = 1, unconditional. Method: specialise the rank 1 family y^2 = x^3 + 4T(T+1)x^2 + 2T(T+1)^2(T-1)x over Q(T), explicit 2-isogeny descent, and Kai's number field Green-Tao-Ziegler. Mazur-Rubin rank 0 existence is cited; their rank 1 corollary assumed finiteness of the 2-part of Sha — [arXiv:2505.16960](https://arxiv.org/html/2505.16960v1).

### Inferences
- Q is not finitely generated over Z, so these results say nothing on H10 over Q.
- Explicit rank-stable examples for small L/K are cheap to find with PARI, but they answer no open question. No finite problem here changes the status of anything.

### Gaps
- Publication status of the Koymans-Pagano and Alpoge et al. papers not confirmed; I saw no journal references.
- Whether ABHS also supply elliptic curves in general: the abstract speaks of abelian varieties. Did not read the body.

## Q4. Effective Mordell, abc, Szpiro ratio and Hall ratio records

### Takeaway
Effective Mordell exists only conditionally (Alpoge-Lawrence), abc is unproved in the mainstream view, and records remain at Szpiro about 9.02, Hall 46.60, abc quality 1.6299. Record searches are well defined and feasible, but they yield data, not theorems.

### Cited Findings
- [C] Alpoge-Lawrence, arXiv:2408.11653: a Turing machine that on input a number field K and a smooth projective hyperbolic curve C outputs C(K) if it terminates; Hodge, Tate and Fontaine-Mazur imply termination. The authors expect it to be too slow for practical use — [arXiv:2408.11653](https://arxiv.org/pdf/2408.11653).
- abc status: Mochizuki's proof remains unaccepted; Scholze-Stix objection stands in dispute; Joshi claims are self-assessed; the LANA Lean project was announced in March 2026, with Mochizuki's April 2026 progress report — [Mochizuki et al. PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Formalization%20of%20IUT%20(2026-04).pdf); [Joshi, arXiv:2403.10430](https://arxiv.org/pdf/2403.10430). A claim that Lean confirmed a gap came only from an aggregator — [zeli.app](https://zeli.app/es/story/48963019) — so treat as unconfirmed.
- Szpiro: top ten table headed by 9.01996, then 8.90370, 8.84313, 8.81194 — [Bennett-Yazdani](https://personal.math.ubc.ca/~bennett/BeYa.pdf). Largest known about 9.02 for conductor 2·7·13·19·29·127 — [arXiv:2012.12475](https://arxiv.org/pdf/2012.12475) as read in a search summary. Szpiro's conjecture is nearly equivalent to abc — [same](https://arxiv.org/pdf/2012.12475).
- Hall: best ratios r = sqrt(x)/|y^2 - x^3| are 46.60 (x = 5853886516781223, Elkies), 16.53, 10.65, 10.18, 6.50, 5.65. List complete for x <= 10^29 (44 entries). Strong form not believed; weak form follows from abc — [Wikipedia](https://en.wikipedia.org/wiki/Hall%27s_conjecture).
- Aanderaa-Kristiansen-Ruud (Math. Comp. 2018): nine new good examples; all good examples with x < 10^29 found — [AMS](https://www.ams.org/journals/mcom/2018-87-314/S0025-5718-2018-03298-7). Preliminary cost data: C/GMP run with q_max = 10^4 (x_max = 10^24) took 57 processor-days; q_max = 2 x 10^4 (x_max = 64 x 10^24) took 441 processor-days — [arXiv:1401.4345](https://arxiv.org/pdf/1401.4345).
- abc: best quality 1.6299 (Reyssat); ABC@Home finished all triples with c < 10^18 in 2011, 23.8M triples by 2015 — [Wikipedia](https://www.wikipedia.org/wiki/Abc_conjecture); [arXiv:1409.2974](https://arxiv.org/pdf/1409.2974).
- Goldfeld-Szpiro ratio G = |Sha|/sqrt(N): three curves with G > 150 — [arXiv:2111.07794](https://arxiv.org/abs/2111.07794v1).

### Inferences
- From the AKR figures, time scales as x^(1/2) (x up by 64, time up by 7.7). That implies about 18,000 processor-days (2014 speed) for all x < 10^29. Extending to 2 x 10^29 adds about 7,500 processor-days. Assuming 16 cores at 3 times 2014 per-core speed, that is about 155 days. With 44 examples up to 10^29, roughly 1.5 per decade, expect about 0.45 new good examples in that window. Reaching 10^30 is about 2 years on the same assumptions. Honest reading: possible, low yield, and new only as a record list. The 2018 code may be faster than these 2014 figures.
- Szpiro records: cheap sweeps over Frey curves of the public abc triples, plus isogenous curves and twists. Beating 9.02 would be a record. No theorem follows.
- No computation bears on abc or effective Mordell. Numerics neither test IUT nor supply a height bound.

### Gaps
- No 2025-2026 Szpiro or Hall record found; LMFDB top Szpiro not checked directly. Bennett-Yazdani is old.
- Exact final cost of the 10^29 run not obtained; the Math. Comp. paper itself was not read.
- The LANA interim report was not read from a primary source.

## Q5. Modularity: real quadratic, imaginary quadratic, abelian surfaces

### Takeaway
Modularity is known over Q, real quadratic, totally real cubic and quartic fields without sqrt(5); over imaginary quadratic fields it is known when X_0(15) has rank 0 over F; and a positive proportion of abelian surfaces over Q are modular. These are neighbouring results, and the residual cases are theoretical rather than compute-limited.

### Cited Findings
- [T] Freitas-Le Hung-Siksek, Invent. Math. 201 (2015): every elliptic curve over a real quadratic field is modular, using mod 3 and mod 5 modularity lifting plus rational points on modular curves — [arXiv:1310.7088](https://ar5iv.arxiv.org/html/1310.7088).
- [T] Derickx-Najman-Siksek, Algebra Number Theory 14 (2020): totally real cubic fields — [arXiv:1901.03436](https://arxiv.org/abs/1901.03436). [Journal not verified] Box: totally real quartic fields not containing sqrt(5), via quartic points on four modular curves — [arXiv:2103.13975](https://arxiv.org/pdf/2103.13975).
- [T*, journal not verified] Caraiani-Newton, arXiv:2301.10509: if X_0(15) has rank 0 over imaginary quadratic F then every elliptic curve over F is modular; covers infinitely many F, including Q(sqrt(-d)) for d = 1, 2, 3, 5 — [arXiv:2301.10509](https://arxiv.org/pdf/2301.10509). Quanta describes this as about half of imaginary quadratic fields — [Quanta](https://www.quantamagazine.org/elliptic-curves-yield-their-secrets-in-a-new-number-system-20230706/). The arXiv abstract page and journal reference were not checked.
- Allen-Khare-Thorne: positive proportion over imaginary CM fields — [arXiv:1910.12986](https://arxiv.org/pdf/1910.12986v1.pdf).
- [T*] Boxer-Calegari-Gee-Pilloni, arXiv:2502.20645 (28 Feb 2025): modularity of a positive proportion of abelian surfaces over Q, for surfaces ordinary at 3 and 3-distinguished with big image of the 3-torsion — [abs](https://web3.arxiv.org/abs/2502.20645). Earlier potential modularity [arXiv:1812.09269](https://arxiv.org/abs/1812.09269v3); overview by Gee [arXiv:2510.02756](https://arxiv.org/html/2510.02756v1).

### Inferences
- Over F = Q(sqrt(-d)), X_0(15) rank 0 is a rank question for 15a and its twist by -d, so a table of proven d is a cheap PARI run. It reproduces what the theorem gives and is not a new result.
- Consequence for BSD: modularity over F feeds into analytic continuation of L(E/F,s), which is a prerequisite for BSD over F, not progress on it.

### Gaps
- Totally real quintic and quartic containing sqrt(5): no result found; search did not cover this directly.
- Smith's 100% claim for X_0(15) rank 0 cited in secondary work is unverified.

## Q6. Heegner points, Euler systems, Stark-Heegner points, p-adic BSD, Iwasawa invariants

### Takeaway
Kolyvagin's conjecture is now essentially a theorem at good ordinary non-Eisenstein primes, so numerics now test refinements rather than the conjecture. Rationality of Stark-Heegner points is still open in general, with numerics and genus-field results only. On Iwasawa invariants, no counterexample to Greenberg's mu = 0 with E[p] irreducible is known. Public tables stop around p = 50 (LMFDB) or p < 1000 for rank >= 2 up to conductor 30,000, so large-p data is new in coverage, but scientifically interesting only at exceptional pairs.

### Cited Findings

**Heegner points and Kolyvagin classes**
- Jetchev-Lauter-Stein, arXiv:0707.0032 (2007): full algorithm for Kolyvagin classes via Heegner points over ring class fields; evidence for Kolyvagin's conjecture for specific rank 2 curves; non-trivial Sha elements — [abs](https://arxiv.org/abs/0707.0032). A later Stein grant text says they "came close in exactly one case" of conductor 389 — [proposal](https://www.williamstein.org/grants/2010-ant/project_description.pdf). Conflict on how complete that verification was.
- BCGS Thm A, Cor A, Thm B and Thm C as in Q1, and M_inf >= ord_p(c_l) by Jetchev — [arXiv:2312.09301](https://arxiv.org/abs/2312.09301). Kurihara's analytic delta_n in modular symbols satisfy the same divisibility index under hypotheses, confirming Kim's conjecture — [same](https://arxiv.org/abs/2312.09301).
- PARI provides ellheegner, ellheegnertwist, ellanalyticrank, ellL1, ellbsd, ellpadicbsd, ellpadicL, ellpadicheight, ellpadicheightmatrix, ellpadicregulator, ellpadiclambdamu, ellrank — [PARI doc](https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html). ellpadicbsd handles ordinary, multiplicative and supersingular examples and returns [r, Lp] with Lp conjecturally R_p·S.

**Stark-Heegner**
- [Cj] Darmon's conjecture: Stark-Heegner points are global points over ring class fields of real quadratic fields — [Darmon](https://www.math.columbia.edu/~goldfeld/JNT-HDarmon.pdf). Still open in general.
- [T] Bertolini-Darmon, Annals 170 (2009): genus-character combinations are defined over the predicted quadratic extensions — [Annals](https://annals.math.princeton.edu/2009/170-1/p09). Mok removed hypotheses, TAMS 2021 — [AMS](https://www.ams.org/tran/2021-374-02/S0002-9947-2020-08254-3/). Non-maximal orders — [arXiv:1801.05779](https://arxiv.org/abs/1801.05779v2).
- Plectic Stark-Heegner points: numerics, links to higher derivatives of p-adic L-functions, special-case algebraicity — [Fornea talk](https://www.math.princeton.edu/node/17791); [arXiv:2203.15998](https://ar5iv.labs.arxiv.org/html/2203.15998).
- Rigid meromorphic cocycles: Darmon-Vonk [real quadratic Borcherds products](https://www.math.mcgill.ca/darmon/pub/Articles/Research/72.DV2/borcherds.pdf); Caeiro-Darmon class number one application, Essential Number Theory 2025 — [MSP](https://msp.org/ent/2025/4-1/p02.xhtml); Hassan's higher weight cocycles with numerical evidence, arXiv:2509.09446 — [arXiv](https://arxiv.org/html/2509.09446v2).

**p-adic BSD**
- Balakrishnan-Muller-Stein (Math. Comp. 2015): p-adic BSD for abelian varieties and modular abelian surface data — [arXiv:1210.2739](https://ar5iv.labs.arxiv.org/html/1210.2739). Nonvanishing of the p-adic regulator is a serious hypothesis, easy to check once E(Q) is known — [Muller talk](https://www.math.uni-hamburg.de/home/js.mueller/oxford12.pdf).
- Banwait: Schneider's leading term theorem gives order of vanishing = corank exactly when Sha is finite and the pairing nondegenerate; nondegeneracy assumed, not proved — [arXiv:2609.08431](https://arxiv.org/html/2609.08431).
- LMFDB p-adic regulators exist only for good ordinary p from 5 to 97 — [curve page](https://www.lmfdb.org/EllipticCurve/Q/389/a/1).

**Iwasawa invariants**
- [Cj] Greenberg (Conj 1.11, 1999): E/Q, odd good ordinary p, E[p] irreducible implies mu = 0; and for good ordinary p != 2 some isogenous E' has mu = 0 — [Chakravarthy, arXiv:2408.07826](https://arxiv.org/html/2408.07826v2). Mazur's X_0(11) at p = 5 has mu != 0, a reducible case — [arXiv:2408.07826](https://arxiv.org/pdf/2408.07826). No irreducible counterexample is given there.
- [T] Greenberg-Vatsal: mu = 0 when E[p] has a submodule unramified at p and odd, or ramified at p and even. Trifkovic: infinitely many reducible cases at p = 3, 5. Drinen: isogeny version false over general number fields — [arXiv:2408.07826](https://arxiv.org/html/2408.07826v2).
- [T*] Chakravarthy: mu <= 1 for all but finitely many good ordinary p — [arXiv:2408.07826](https://arxiv.org/html/2408.07826v2). [T*] Ray: positive density of curves with mu_5 = lambda_5 = 0 — [arXiv:2404.09009](https://arxiv.org/abs/2404.09009). [T*] Chnaras, arXiv:2502.16910 (24 Feb 2025): numerical Gold-type criterion for rank one curves deciding minimality mu + lambda = 1 — [abs](https://arxiv.org/abs/2502.16910). See also [arXiv:2405.05871](https://arxiv.org/pdf/2405.05871) on mu in analytic rank zero.
- [Cj] Kundu-Ray: for 100% of good ordinary primes mu = 0 and lambda = r_E; for supersingular mu^+ = mu^- = 0 and lambda^+ = lambda^- = r_E. Proved for rank 0 — [arXiv:2102.02411](https://arxiv.org/pdf/2102.02411).
- For rank 0 and p > 5 the invariants vanish unless p divides L(E,1)/Omega, p is split multiplicative, or a_p = 1. The first two happen finitely often — [LMFDB knowl](https://LMFDB.org/knowledge/show/ec.iwasawa_invariants).
- Existing data: LMFDB shows p = 2 to 47 plus bad primes — [curve page](https://www.lmfdb.org/EllipticCurve/Q/389/a/1); Pollack's tables: conductors to about 5000, p in {2,...,13}, 37A at varying p, with warnings about bugs — [tables](https://archive.math.arizona.edu/rpollack/Data/data.html); recent 2-adic twist data — [arXiv:2607.05305](https://arxiv.org/pdf/2607.05305); Stein-Wuthrich for rank >= 2, p < 1000 — [AMS](https://www.ams.org/mcom/2013-82-283/S0025-5718-2012-02649-4/).

### Inferences
- New large-p Iwasawa data is novel in coverage. The content lies at anomalous primes (a_p = 1) in rank 0, and in rank >= 1 at primes dividing Sha, Tamagawa numbers, or p-adic regulators. Mass tables at generic primes only reconfirm the formula.
- p-parity should force lambda to be even in rank 0 (my reasoning, not sourced), so at anomalous p the test is lambda = 2 versus lambda >= 4, a rare event (roughly 1/p per candidate if residues are random). That is what is testable for Kundu-Ray.
- A mu >= 1 at irreducible E[p] would falsify Greenberg's conjecture. Prior probability is tiny. The candidate pairs are few and cheap, so it costs little to look.
- Stark-Heegner numerics give evidence only. Rational recognition of a point in a ring class field is not a proof of Darmon's conjecture.

### Gaps
- No primary statement read for Greenberg 1999; quoted through Chakravarthy.
- Full Stein-Wuthrich tables, and whether any larger Iwasawa datasets exist unpublished, unknown.
- Part IV of Banwait (non-CM discussion, Coates-Liang-Sujatha comparison, software and timing) was not readable through the fetch tool.
- From memory, unverified: PARI has overconvergent modular symbol routines (mspadicinit, mstooms, mspadicmoments); Sage has a darmonpoints package by Masdeu. Confirm before planning on them.
- No 2026 Stark-Heegner rationality theorem found in searches; arXiv listing not read directly.

## Q7. For each area: is there a specific open computational question, what does it cost, what counts as new

### Takeaway
Three projects look feasible and honestly new on a 16-core workstation: full BSD beyond conductor 5000 (theorem for listed curves), rank >= 2 Sha[p] vanishing with p-adic regulators beyond the Stein-Wuthrich and Banwait ranges (theorems for pairs plus a new dataset), and exceptional-pair Iwasawa scans. One high-risk, high-value target is the Furio-Lombardo quartic, which needs an idea more than compute. Everything Clay-level, uniform or effective remains out of reach, because no finite computation implies those statements.

### Cited Findings
- The facts behind this table are cited in Q1 to Q6. Key anchors: published full BSD range stops at N < 5000 — [Creutz-Miller](https://arxiv.org/pdf/1105.4018); LMFDB exact rank 1 Sha stops at N < 5000 — [Reliability](https://www.lmfdb.org/EllipticCurve/Q/Reliability); Sha[p] = 0 pairs stop at N <= 30,000, p < 1000 — [AMS](https://www.ams.org/mcom/2013-82-283/S0025-5718-2012-02649-4/); CM rank 2 regulators stop at p < 30,000 on five curves — [Banwait](https://arxiv.org/abs/2609.08431); remaining 7-adic object is one quartic — [Furio-Lombardo](https://arxiv.org/pdf/2507.17967).

### Inferences

All costs below are my estimates unless cited. Benchmark before committing. Ranked by value for one person.

| Rank | Target | Finite statement | Cost on 16 cores, no Magma | What counts as new | Risk |
|---|---|---|---|---|---|
| 1 | Full BSD past N = 5000 | For all rank <= 1 classes with 5000 <= N < N_0, prove ord_p Sha = ord_p Sha_an for every p, or list exceptions | Exact Sha_an: rank 0 by modular symbols; rank 1 from Gross-Zagier with bounded denominator. p >= 5 irreducible by theorems or Kolyvagin index. p = 2 by mwrank/ellrank descent. Weeks of compute for N_0 = 10^4 to 2 x 10^4. Bottleneck: 3-descent and isogeny descents exist in Magma, so need reimplementation or the Stein-Wuthrich route; Sha_an divisible by 4 needs second 2-descent or Cassels-Tate | Theorem for an explicit finite set plus exception table; first extension since 2012 as far as I found. Also exact rank 1 Sha_an past N = 5000 | Low to medium. Value is in exposing which (E,p) current theorems miss |
| 2 | Rank >= 2 Sha[p] = 0 and p-adic regulators | Extend to N up to 10^5 or 5 x 10^5, p < 1000; or single curves (389a, 433a, 5077a) to p < 3 x 10^4 or beyond | ellpadicbsd, ellpadicregulator. L-series mod T^3 needs level p^2, so about p^2 modular symbol sums per pair. Rough C estimate seconds at p ~ 1000, minutes at p ~ 10^4. Regulators alone are far cheaper. 1,534,422 pairs at N <= 30,000 suggests 10^7+ pairs at N = 5 x 10^5, so needs a filter | New pairs with Sha[p] = 0 (theorem per pair), list of p dividing non-CM regulators, test of the about (1/2) log log X failure heuristic, comparison with Banwait's CM data | Low. Modest prestige. Hypotheses must be read from the paper first |
| 3 | Exceptional-pair Iwasawa scan | For N < 5 x 10^5, all anomalous p < 10^5 or so: is lambda = 2 in rank 0? Is mu = 0 at irreducible E[p]? Rank 1: apply Chnaras criterion | Candidate pairs per curve grow like sqrt(X)/log X. Level p^2 test, so about p^2 modular symbol steps per pair; rank 1 criterion likely much cheaper. Days to weeks | First census past LMFDB p < 50 and Pollack p <= 13. Any lambda >= 4 cases. Statistics for Kundu-Ray. Counterexample to Greenberg would be major, but do not expect one | Low. Publishable as a data paper, unless mined for structure |
| 4 | Rank 2/3 Kolyvagin classes | Compute M_r and ord(kappa) for p dividing c_l in rank 2, test Thm B numerically; attempt a first rank 3 class for 5077a | Ring class degree (l+1)h, or (l1+1)(l2+1)h for rank 3. High precision Heegner sums. Rank 2 feasible; rank 3 hard | Numerics for a formula now a theorem under hypotheses, so new mainly where hypotheses fail (Eisenstein p, non-surjective) | Medium |
| 5 | Mayle-Rouse residual triage | 3,321 finite-point curves: local obstructions, rank 0 quotients; list what is left | Python plus PARI, LMFDB models. Days | Shrinks the list; short note | Low, but many cases may fall to Magma users first |
| 6 | Furio-Lombardo quartic C | Prove C(Q) has the four known points, or the restricted case c = -z^2 | Compute is small for a search or sieve; the method is missing. Sieve needs Mordell-Weil generators and saturation, which need Jacobian arithmetic in PARI (Makdisi style) or a port. QC over a degree 21 field looks infeasible | Completes the 7-adic classification [with Thm 1.7]. Real theorem | High. Needs an idea, e.g. the c = -z^2 cover or the 7-torsion cover. Short Mordell-Weil sieve bound is a realistic partial result |
| 7 | Stark-Heegner numerics | New real quadratic fields of class number > 1, non-split level, plectic cases | Overconvergent modular symbols; hours per point at moderate precision | New evidence, only if in an untested regime. Not a proof | Medium, requires Sage, and much of the regime is already covered |
| 8 | Records: Hall, Szpiro, Sha | Hall x < 2 x 10^29; Szpiro > 9.02; Sha > 1937832^2 | Hall about 5 months by extrapolation in Q4; Szpiro days; Sha weeks | Records only | Low value |
| 9 | X_ns^+(25) point search | Height > 1000 on X_ns^+(5) | Sieve scaling H^2 from 6 hours in Magma; C plus sieving could reach H of 10^4 to 10^5 | Evidence only | Low value |

**Out of reach, and why**
- Finiteness of Sha for any curve of rank >= 2: every known method gives one prime at a time, and no finite computation handles all p. Banwait's results stay vertical for this reason.
- Proving r_an = 4 for any curve: no tool shows L''(E,1) = 0, and LMFDB can only say r_an is in {2, 4}. For r_an <= 3, parity plus exact vanishing of L(1) or L'(1) suffices.
- Rationality of Sha_an for any curve with r_an >= 2.
- Serre uniformity and Zywina's conjectures: infinitely many p. Each X_ns^+(p) is a separate problem, genus grows, and even rank = genus is checked only for p < 100.
- X_ns^+(121): genus 511, no model. Sieve evidence is enormous, but gives no proof.
- X_ns^+(23), (25), (29) by QC on this hardware without Magma, in competition with groups who have code. Worth following, not racing.
- Ten Mayle-Rouse curves without Magma: memory wall reported at degree 280 even with Magma.
- Effective Mordell, abc: no computation can establish these. Alpoge-Lawrence's algorithm is conditional and, per the authors, impractical.
- Goldfeld for general E: Smith settles 2^inf-Selmer coranks. The analytic statement needs BSD or a 2-adic p-converse (Selmer corank r <= 1 implies analytic rank r), known only in cases such as the CM rank 0 case (Burungale-Tian).
- Rationality of Stark-Heegner points in general: needs theory; numerics cannot prove it.
- Modularity residual cases: not compute-limited in the sense of this workstation.
- H10 over Q: untouched by this body of work.

**What to do first (one week, as a go or no-go)**
1. Time ellpadicbsd and ellpadicregulator at p ~ 10^3 and 10^4 on 389a and at N ~ 10^5, and write the C modular symbol loop for comparison.
2. For N in [5000, 6000), generate the list of (E,p) with p dividing 2·3·Sha_an·prod c_q·#E(Q)_tors·(isogeny degrees), and check how many are covered by Miller's Kolyvagin route and by BSTW, Skinner-Urban and Castella-Grossi-Skinner. The size of the uncovered residue decides project 1.
3. For project 6, run a sieve on C and test the c = -z^2 restriction before investing in Jacobian code.

### Gaps
- All timings above are unmeasured here: PARI is not installed on this machine, so no benchmarks were run. Treat them as order of magnitude.
- The p^2 cost for L-series assumes level p^2 is needed for Teichmuller-trivial coefficient mod p; a refinement may lower this.
- Whether someone has an unpublished extension of Stein-Wuthrich or of BSD verification past N = 5000 could not be excluded.
- Whether mwrank or Sage is acceptable under the "no Magma" constraint should be decided; projects 1 and 2 are much easier with Sage's existing Stein-Wuthrich implementation (referenced in [Miller](https://arxiv.org/pdf/1010.2431)).
