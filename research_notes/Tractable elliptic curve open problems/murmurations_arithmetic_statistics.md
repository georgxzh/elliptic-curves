# Murmurations and the arithmetic statistics of elliptic curves: state of the art, November 2026

Conventions. Each claim is tagged [THM] (unconditional theorem), [COND] (conditional theorem, hypotheses named), [CONJ] (stated conjecture or heuristic), [NUM] (numerical observation), [ANN] (announcement, not a refereed paper). Almost every 2025-2026 item below is an arXiv preprint and has not been refereed; a journal is named only where the arXiv record or publisher gives one. Height means H(E) = max(4|A|^3, 27B^2) for y^2 = x^3 + Ax + B unless stated otherwise.

Corrections to the assignment's framing, so they do not propagate:
- Bober-Booker-Lee-Lowry-Duda is the holomorphic weight aspect, level 1 ([arXiv:2310.07746](https://arxiv.org/abs/2310.07746)). It is not the Maass form paper.
- The Maass form paper is Booker-Lee-Lowry-Duda-Seymour-Howell-Zubrilina ([arXiv:2409.00765](https://arxiv.org/abs/2409.00765)).
- The rank landscape changed sharply in August-October 2026: the rank record is now at least 32, not 29 (details under the ranks question).

## Murmurations: what is proved, conditional, conjectured, and open, especially for elliptic curves

### Takeaway
I found no theorem, in any ordering and under GRH alone or unconditionally, that gives murmurations of elliptic curves as an average over primes. The strongest unconditional elliptic curve theorem is Sawin-Sutherland's height-ordered Theorem 2, which averages over integers n with no small prime factor (an iterated limit, smooth weight). Prime-average statements are conjectural (Sawin-Sutherland Conjecture 1) or conditional on ratios conjectures (Cowan). Conductor ordering has only a heuristic prediction for prime conductor and no supporting theorem.

### Cited Findings

Discovery
- [NUM] He, Lee, Oliver, Pozdnyakov (arXiv April 2022; Experimental Mathematics 2024) found oscillation in average a_p over curves in a fixed conductor range with fixed rank, via data-science classification by rank — [arXiv:2204.10140](https://arxiv.org/abs/2204.10140).
- [NUM] Without root-number weighting, elliptic curve averages reportedly show no murmurations (Sutherland's calculations, as cited by Martin) — [Martin, arXiv:2505.01093](https://arxiv.org/html/2505.01093).

Modular forms, level aspect
- [THM] Zubrilina (arXiv October 2023; Invent. math. 2025): squarefree N in [X, X+Y], Y = (1+o(1))X^(1-d2), prime P << X^(1+d1), 2d1 < d2 < 1, even weight k, a single prime with no prime averaging. Error O(X^(-d'+eps) + 1/P), d' = min{d2/2 - d1, 1/9 + d2/9 - d1}. The density M_k(y) with y = P/X is an explicit class-number-type expression, with a Chebyshev U_(k-2) factor inside the r-sum. Weight 2: M_2(y) grows like y^(1/4), and its normalized version is asymptotically almost periodic in sqrt(y). The method is the trace formula for T_p composed with W_N — [arXiv:2310.07681](https://ar5iv.labs.arxiv.org/html/2310.07681).
- [THM, correction] Nelson, Ross, Wassercug, Xue (arXiv 2609.29631, stamped 28 Aug 2026) report gaps in Zubrilina's proof, including a misplaced Chebyshev factor in the cited Skoruppa-Zagier trace formula and an inadequately justified bound in Lemma 7.3, and give a corrected Theorem 1.1. Its range is narrower: 0 < d1 < 1/11, 2d1 < d2 < (4-18d1)/13. Their smoothed-density theorem (continuity, power-saving limit 1/2 as y tends to infinity) is stated for k >= 6 only, so weight 2 is not covered, and they say it removes a Riemann hypothesis assumption that Zubrilina's version needed — [arXiv:2609.29631](https://arxiv.org/html/2609.29631). Conflict: the portion of Zubrilina's paper I read does not visibly invoke RH ([same source as above](https://ar5iv.labs.arxiv.org/html/2310.07681)); the remaining ~24k characters were not read, so this is unresolved.
- [THM] Hua-Mok (1 Sep 2026): for weight 2 squarefree level, for each fixed k >= 2, sqrt(X) E[eps(f) lambda_{sym^k f}(P)] = G(P^k/X) + o_k(1), with the same profile G as Zubrilina's. Conditions: Y = (1+o(1))X^(1-d1), P^k << X^(1+d2), 0 < 2d2 < d1 < 1/8, (k-1)d2 < 1. Their Conjecture 1.1 is the same universality for general self-dual GL2 families ordered by analytic conductor [CONJ], and their theorem is not stated for elliptic curves as such. They also state that the Kundu-Mueller profile omits a factor of 2 in the cutoff (r <= sqrt(y) versus 2 sqrt(y)) — [arXiv:2609.00777](https://arxiv.org/html/2609.00777); original [Kundu-Mueller, arXiv:2507.00738](https://arxiv.org/abs/2507.00738).
- [THM] Depth aspect: prime power level l^a, a tending to infinity, [Burrin-Kuperberg-Lee-Mujdei-Yang, arXiv:2603.25564](https://arxiv.org/abs/2603.25564) and [Tomczak, arXiv:2606.08353](https://arxiv.org/abs/2606.08353).
- [THM] Joint level-weight aspect, [Cardi, arXiv:2607.08982](https://arxiv.org/abs/2607.08982).

Other families
- [THM, COND] Lee-Oliver-Pozdnyakov (IMRN 2025): complex Dirichlet characters normalized by Gauss sums, unconditional limit for N prime in [X, cX]; the short-interval version assumes RH; the real family chi_{8d} with smooth weight assumes GRH; density interpolates the symplectic 1-level density transition — [arXiv:2307.00256](https://arxiv.org/html/2307.00256v4).
- [COND] Bober-Booker-Lee-Lowry-Duda (Algebra Number Theory 20 (2026) 299-332): level 1, weight tending to infinity, under GRH — [arXiv:2310.07746](https://arxiv.org/abs/2310.07746); GRH status per [Lowry-Duda, arXiv:2506.01640](https://arxiv.org/html/2506.01640v1) and [Cowan's slides](https://www.math.uwaterloo.ca/~a2cowan/uoftslides.pdf).
- [COND] Booker-Lee-Lowry-Duda-Seymour-Howell-Zubrilina: level 1 weight 0 Maass forms, eigenvalue tending to infinity, under GRH per [Cowan's slides](https://www.math.uwaterloo.ca/~a2cowan/uoftslides.pdf); the abstract does not state the hypothesis — [arXiv:2409.00765](https://arxiv.org/abs/2409.00765).
- [THM] Kuan-Lesesvre: weight aspect via the Petersson formula, improved range, first relative trace formula approach — [arXiv:2507.11418](https://arxiv.org/abs/2507.11418).
- Hecke L-functions: imaginary quadratic fields, density with an almost periodic feature ([Wang, arXiv:2503.17967](https://arxiv.org/abs/2503.17967)); quadratic Hecke L-functions of the Gaussian field under GRH ([Gao-Zhao, arXiv:2607.20853](https://arxiv.org/abs/2607.20853)).
- Function fields: quadratic characters, with the density matched to a correction term in traces of high Frobenius powers, tied to stable homology of hyperelliptic moduli; also thin cubic families — [Lalin-Lee-Oliver-Pozdnyakov, arXiv:2608.01337](https://arxiv.org/abs/2608.01337).
- [THM] Quadratic twist families of GL1 unconditionally, by averaging approximate functional equations; mean value estimates are given for GL2 twist families, but the abstract claims murmurations only for GL1 — [Cowan, arXiv:2504.09944](https://arxiv.org/abs/2504.09944).
- Limit of methods: Lowry-Duda says trace formula methods will not apply to sparse families such as elliptic curves or genus 2 curves, and lists unexplained similarities between arithmetic and unnormalized densities — [arXiv:2506.01640](https://arxiv.org/html/2506.01640v1).

Elliptic curves: the exact state
- As of August 2024 Cowan recorded no theorems, conjectures, or heuristic predictions for the HLOP experiment — [arXiv:2408.12723](https://arxiv.org/abs/2408.12723).
- [COND] Cowan Theorem 1.1 (v1 Aug 2024, v3 Apr 2025): for a height-ordered family F(H) with congruence restrictions and fixed sign, assuming the David-Huynh-Parks ratios conjecture (Conj. 3.7 there) plus two auxiliary hypotheses (his (16), (17)), a log-weighted prime power sum up to Hy has a main term independent of H, built from a Hecke trace Euler product A (his Definition 4.2) and the conductor distribution. Error terms carry a (log H) saving — [arXiv:2408.12723](https://arxiv.org/abs/2408.12723).
- [THM] Conductor input: the explicit density of N/H in height-ordered families, an effective Brumer-McGuinness-Watkins heuristic, and the strongest bounds for curves with conductor much smaller than height for H << N^1.2165 — [Cowan, arXiv:2408.09745](https://arxiv.org/abs/2408.09745).
- [COND] Quadratic twists of a fixed curve: for N_E odd prime with even sign, family d fundamental with chi_d(-N_E) eps_E = 1, Cowan Theorem 5.3 is a 1-level-density-type statement from Huynh-Miller-Morrison. The theorem's header says GRH, its proof uses the ratios conjecture, and the abstract lists it under ratios conjectures. Cowan notes its error term prevents use in the range p/N around 1, so a murmuration formula there comes only by rewriting the main term, subject to the associated ratios conjecture — [arXiv:2408.12723](https://arxiv.org/abs/2408.12723).
- [THM] Sawin-Sutherland Theorem 2 (v1 16 Apr 2025, v2 20 Oct 2025, 48 pp): with W smooth, compactly supported on (0, infinity), the iterated limit P then X to infinity exists for the height-ordered average of eps(E) a_n(E) weighted by W(n/N(E)), over n with no prime factor <= P, normalized by the product of (1-1/p)^(-1) for p <= P. The limit is the integral of W against an explicit density. Inputs are modularity and Voronoi summation, with no GRH in the portion read. All curves are included, with no restriction on rank, root number, or twist — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [THM] Same paper: Proposition 7 removes the coprimality condition (average over all n, Bessel-type integral with local factors). Proposition 9 restricts to curves with p not dividing N(E) for all p <= P; this is a variant, not a prime conductor theorem. No explicit convergence rate is given, though the authors think one can be extracted — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [CONJ] Sawin-Sutherland Conjecture 1: the prime-averaged limit over p in (C1 N, C2 N] equals the integral over u of a density of the form 2 pi sqrt(u) times a double sum over squarefree q and m of Moebius-weighted J_1(4 pi sqrt(u) m/q) terms times local factors. Local factors are p-adic averages of a_{p^nu}, with closed forms via traces on level 1 cusp forms of weight nu+2 for p > 3 and separate formulas at 2 and 3. The sum converges absolutely and uniformly away from u = 0, so the density is continuous. The authors say a primes-only proof seems very difficult — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [CONJ, NUM] Section 1.5: heuristic prediction (eq. 7-8) for prime conductor curves ordered by conductor, based on an informal claim that reduction type E_p occurs with probability 1/(p |Aut E_p|). The authors state that conductor ordering does not seem provable at present levels of understanding — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [NUM] Data in that paper: height X = 2^28 with intervals (j/2000, (j+1)/2000] and truncation q, m <= 10^5 (Fig. 1); unrestricted average at 2^28 (Fig. 2); prime conductor, height 2^40 (Fig. 3); prime conductor ordered by conductor up to 2^30 (Fig. 4). A persistent downward bias between data and density is seen for primes, not in the proved variant, and shrinks with X. The rank 2 explanation is doubted because the rank 2 proportion rises over the tested range — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [CONJ] Sawin-Sutherland expect a locally averaged form of Cowan's formula to agree with their density, but this has not been carried out — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [CONJ] Kimball Martin: elliptic curve murmurations tend to a function of p/X only after smoothing, and the correct smoothing is unresolved; root-number-free murmurations for modular forms under sqrt(N) weighting are conjectured — [arXiv:2505.01093](https://arxiv.org/html/2505.01093). Local-sign variants are conjectured in [arXiv:2409.02338](https://arxiv.org/abs/2409.02338).

Rank strata
- [NUM] HLOP's averages are by fixed rank — [arXiv:2204.10140](https://arxiv.org/abs/2204.10140).
- [NUM] Sawin-Sutherland find parity-split averages behave better than rank-by-rank ones, and they consider explaining the slower convergence challenging — [arXiv:2504.12295](https://arxiv.org/html/2504.12295v2).
- [NUM] Wachs (conductor < 10^5, one curve per isogeny class, p up to 10^5): the rank 0 profile depends on L(E,1); earlier claims about Sha were withdrawn by the author — [arXiv:2603.04604](https://arxiv.org/abs/2603.04604).
- [NUM] Congruent number twists up to 3 million: Deshpande et al. report trace averages tending to zero with no murmuration-like pattern — [arXiv:2509.03129](https://arxiv.org/abs/2509.03129).

### Inferences
- Zubrilina and Hua-Mok concern all weight 2 newforms of squarefree level, while rational newforms are a sparse subset, so neither implies anything for elliptic curves. This agrees with Lowry-Duda's sparsity remark.
- The cleanest summary of the gap: the proved Sawin-Sutherland object differs from the conjectured one by a sieve-to-primes step, plus a sharp cutoff. A proof with primes would need input on sums of a_p over primes in height families, which looks about as hard as parity-type problems. This is my reading, not a statement in the paper.
- The downward bias is measured only up to X = 2^28, about 2.7 x 10^8, while the average rank turnaround in Balakrishnan et al. is near 6 x 10^8 ([arXiv:1602.01894](https://ar5iv.labs.arxiv.org/html/1602.01894)). The same height is used in both papers. So the Sawin-Sutherland rejection of the rank 2 explanation rests on data entirely before the turnaround. Whether the bias tracks the rank 2 proportion after the turnaround is untested as far as I can find.
- Noise floor for any prime-average experiment: the signal in E[eps a_p/sqrt(p)] is about 1/sqrt(N), and a_p/sqrt(p) has variance about 1, so SNR per bin is about sqrt(M/N) for M (curve, prime) pairs. SNR 10 needs M about 100 N per bin. At N about 2^28 with 2000 bins that is about 5 x 10^13 pairs. Height X has about 0.485 X^(5/6) curves, which reproduces the 2.4 x 10^8 of Balakrishnan et al. at 2.7 x 10^10, and gives about 5 x 10^6 at 2^28 and 5 x 10^9 at 2^40.

### Gaps
- I could not read Sutherland's talk PDFs (all exceed the 10 MB fetch limit) or the Sarnak letter to Sutherland and Zubrilina (2023, cited in [Wang](https://www.arxiv.org/pdf/2503.17967) and others). Exact wording of those is unverified.
- How Sawin-Sutherland computed Figures 1-4 (software, sampling of primes) is not in the text I read, neither the first 100k characters nor the proof-heavy remainder.
- No paper found on murmurations for torsion-restricted families, or for a fixed Sato-Tate group of elliptic curves specifically. The closest are Wang's Hecke families ([arXiv:2503.17967](https://arxiv.org/abs/2503.17967)). Shi-Weng's titles concern a different object (high rank zetas), which I did not read ([arXiv:2410.04952](https://arxiv.org/abs/2410.04952)).
- No conjecture for all conductors (non-prime) ordered by conductor was found. Hua-Mok's Conjecture 1.1 assumes a prime profile exists and does not supply one.
- My arXiv sweep used the keyword murmuration(s) through Oct 2026, so papers not using the word could be missed.
- arXiv:2609.29631 has an ID that looks late for an August stamp. The arXiv API returned it with published date 2026-08-28; I report that as is.

## Arithmetic statistics of ranks: PPVW, Bhargava-Shankar, Selmer, Goldfeld, Poonen-Rains, and 2023-2026 developments

### Takeaway
For all curves ordered by height, the best unconditional results remain the Bhargava-Shankar series (average rank <= 0.885, at least 80% rank 0 or 1) and >66% satisfying BSD rank, while the minimalist conjecture is open. For quadratic twists, Smith (March 2025) proved the 50/50 distribution of 2^infinity-Selmer corank for every E/Q, so BSD implies Goldfeld, and Burungale-Tian gave the first even-parity Goldfeld case. In 2026 records jumped to rank >= 32, with exact unconditional rank 22 claimed; none of this refutes PPVW, which allows finitely many exceptions.

### Cited Findings

Height-ordered averages
- [THM] Average 2-Selmer size is 3, limsup average rank <= 1.5 — [Bhargava-Shankar, arXiv:1006.1002](https://arxiv.org/abs/1006.1002).
- [THM] Average 3-Selmer size is 4, average rank < 1.17, positive proportion rank 0 — [arXiv:1007.0052](https://arxiv.org/abs/1007.0052).
- [THM] Average 4-Selmer size is 7 — [arXiv:1312.7333](https://arxiv.org/abs/1312.7333).
- [THM] Average 5-Selmer size is 6, average rank < 0.885, at least four fifths rank 0 or 1, at least one fifth rank 0 — [arXiv:1312.7859](https://arxiv.org/abs/1312.7859).
- [THM] More than 66% satisfy the BSD rank conjecture — [Bhargava-Skinner-Zhang, arXiv:1407.1826](https://arxiv.org/abs/1407.1826).
- [THM] Second moment of the size of the 2-Selmer group is at most 15, confirming a Poonen-Rains prediction — [Bhargava-Shankar-Swaminathan, arXiv:2110.09063](https://arxiv.org/abs/2110.09063).
- [THM] Ordering by max(|A|,|B|) gives average rank <= 1.5 — [Janbazi, arXiv:2506.07089](https://arxiv.org/abs/2506.07089).
- [THM] Global fields of characteristic not 2, 3, 5 — [Bhargava-Shankar-Wang, arXiv:2604.16978](https://arxiv.org/abs/2604.16978).
- [THM] Function fields, q >= 5: average rank <= 25/14, adapting Young's GRH bound over Q — [Balcik, arXiv:2510.25630](https://arxiv.org/abs/2510.25630).
- [THM] Families with marked points: bounded average rank and Selmer averages — [Bhargava-Ho, arXiv:2207.03309](https://arxiv.org/abs/2207.03309).
- [THM] Conductor ordering, special subfamily (good at 2 and 3, small j, Delta/C squarefree): average 2-Selmer 3, average rank <= 1.5 — [Shankar-Shankar-Wang, arXiv:1904.13063](https://arxiv.org/abs/1904.13063).

Models
- [CONJ] Poonen-Rains maximal isotropic model — [arXiv:1009.0287](https://arxiv.org/abs/1009.0287).
- [CONJ] Bhargava-Kane-Lenstra-Poonen-Rains joint model of rank, Selmer, Sha — [arXiv:1304.3971](https://arxiv.org/abs/1304.3971).
- [CONJ] PPVW (JEMS 2019) random alternating matrix model: for 1 <= r <= 20 the count with height <= H and rank >= r is H^((21-r)/24+o(1)); rank >= 21 count at most H^(o(1)); all but finitely many have rank <= 21. Theorem 1.1.1 proves this for the random model only. Remark 1.1.3 records Elkies's objection that the heuristic is unconvincing until it predicts ranks in parametric families. Section 12 says rank 21 could go either way on the sign of an o(1) — [arXiv:1602.01431](https://ar5iv.labs.arxiv.org/html/1602.01431).
- [CONJ] PPVW family rule: a family with H^(1/d) members has rank bound 1 + floor(24/d). Quadratic twists give 5 (Granville-type heuristic 7); quartic twists of y^2 = x^3 - x give 9 (11); sextic twists of y^2 = x^3 - 1 give 13 (13); torsion: Z/2 13, Z/3 9, Z/4 7, Z/5 5, Z/6 5, Z/7 3, Z/8 3, Z/9 2, Z/10 2, Z/12 2, Z/2xZ/2 9, Z/2xZ/4 5, Z/2xZ/6 3, Z/2xZ/8 2 — [arXiv:1602.01431](https://ar5iv.labs.arxiv.org/html/1602.01431).
- [CONJ] Watkins: about c X^(19/24)(log X)^(3/8) even-parity positive-rank curves with |Delta| < X, against about X^(5/6) total — [arXiv:math/0608766](https://arxiv.org/abs/math/0608766).

Data
- [NUM] Balakrishnan-Ho-Kaplan-Spicer-Stein-Weigandt: 238,764,310 curves with H <= 2.7 x 10^10. Rank proportions 0.32685, 0.47381, 0.17151, 0.02615, 0.00159, ... Average rank about 0.901976 after peaking near height 6 x 10^8. Average 2-Selmer 2.6656 in the database. 100,000-curve samples at k = 11..16: 2.73566 rising to 2.90311, with average rank falling from 0.887 to 0.813. Ranks unconditional for about 80.77% of the database. Data at wstein.org/papers/2016-height/ — [arXiv:1602.01894](https://ar5iv.labs.arxiv.org/html/1602.01894).
- [NUM] PPVW section 10: random samples from H = 10^10 (279,090 curves) to 10^15 (5,028); rank >= 2 proportion falls from about 17.3% to 15.1%; Magma used, GRH-conditional 2-Selmer — [arXiv:1602.01431](https://ar5iv.labs.arxiv.org/html/1602.01431).
- [NUM] LMFDB: 3,824,372 curves in 2,917,287 isogeny classes, ranks 0-5 present, average rank 0.78 — [LMFDB stats](https://www.lmfdb.org/EllipticCurve/Q/stats). Coverage: all conductors < 500,000, all 7-smooth conductors, all prime conductors <= 3 x 10^8 — [LMFDB completeness](https://www.lmfdb.org/EllipticCurve/Q/Completeness).
- [NUM] Bennett-Gherga-Rechnitzer prime conductor enumeration (Math. Comp. 2019): complete to 2 x 10^9 (10^10 for positive discriminant) per the paper, with sources differing on the bound, heuristic extension further — [search summary of sources](https://personal.math.ubc.ca/~bennett/BeGhRe-MathComp-2019.pdf). I did not read the PDF directly.

Quadratic twists and Goldfeld
- [THM] Smith 2017: full 2-torsion, no rational cyclic subgroup of order 4: Delaunay distribution for 2^infinity-Selmer, rank >= 2 count o(N) — [arXiv:1702.02325](https://arxiv.org/abs/1702.02325).
- [THM] Smith 2022: general l^infinity technique; 100% of twists have rank <= 1 under technical conditions; average rank in quadratic twist families of any abelian variety over a number field is bounded — [I](https://arxiv.org/abs/2207.05674), [II](https://arxiv.org/abs/2207.05143).
- [THM] Smith, 22 Mar 2025: for every E/Q, 50% of twists have 2^infinity-Selmer corank 0, 50% corank 1, 0% >= 2. Twists ordered by |d| over all nonzero integers. Root number +1 twists (asymptotically all) have corank 0, root number -1 have corank <= 1 — [arXiv:2503.17619](https://arxiv.org/abs/2503.17619), [text](https://arxiv.org/html/2503.17619).
- [COND] Corollary 1.2: BSD across the twist family implies Goldfeld. Smith says converse theorems at p = 2 are known so far only for CM curves, so he does not prove Goldfeld unconditionally — [text](https://arxiv.org/html/2503.17619).
- [THM] New non-Poonen-Rains 2-Selmer distributions in balanced isogeny cases: tail of P(2-Selmer rank > r) is 2^(-r^2/2+O(r)) in Case I, 2^(-3r^2/8+O(r)) in Case IV, 2^(-r^2/4+O(r)) in Case V; motivated by X_0(15), Case V — [text](https://arxiv.org/html/2503.17619).
- [THM] Burungale-Tian: for CM E/Q, Selmer corank 0 implies ord_{s=1} L = 0; with Smith this gives 50% of positive squarefree n with ord L(E^(n)) = 0 for y^2 = x^3 - x, the first even-parity Goldfeld instance — [arXiv:2506.03465](https://arxiv.org/abs/2506.03465).
- [THM] Pan-Tian: full 2-torsion, random alternating matrices with 0, 1, or 2 holes; different equivalence classes in one twist family can have different distributions; average of essential 2-Selmer is 3 + sum of 2^(t_i) — [arXiv:2503.21462](https://arxiv.org/abs/2503.21462).
- [THM] Function fields: Ellenberg-Landesman, BKLPR-type result in quadratic twist families up to error tending to 0 as q grows — [arXiv:2310.16286](https://arxiv.org/abs/2310.16286). Landesman-Levy compute Selmer moments for suitably large q — [arXiv:2510.02068](https://arxiv.org/abs/2510.02068).
- [THM] Sparse twist family 2-Selmer distributions — [Bartel-Morgan, arXiv:2508.14026](https://arxiv.org/abs/2508.14026).
- Survey: [Ellenberg, arXiv:2606.06024](https://arxiv.org/abs/2606.06024).

Rank records (2024-2026)
- [ANN] History per Dujella: >= 28 Elkies 2006; >= 29 Elkies-Klagsbrun Aug 2024; >= 30 and >= 31 Alpoge-Howell 2026; >= 32 Elkies-Klagsbrun-Li 2026 — [Dujella](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html).
- [ANN] ICARM #273 (20 Aug 2026) rank >= 30; #302 (23 Aug 2026) rank >= 31; credited to Claude (an internal Anthropic model) with Levent Alpoge and Ava Howell; method not public; exact rank under BSD + GRH — [Epoch AI](https://epoch.ai/frontiermath/open-problems/elliptic-curve-rank), [Scientific American](https://www.scientificamerican.com/article/anthropics-ai-steals-mathematicians-record-for-most-complicated-curve/).
- [ANN] ICARM #4239 (submitted 15 Oct 2026): rank >= 32, specialization of a rank 17 elliptic fibration on a K3 surface of discriminant 1152 at T = -2868768/362209. Upper bound attributed to S. Hackfort: explicit formula over p < 6.02 x 10^10 certified with Arb gives about 33.998, so with root number +1, r_an = 32 under GRH, and rank exactly 32 under GRH + BSD — [ICARM #4239](https://elliptic-rank.icarm.cloud/curve/4239). Coefficients and 32 points are on [Dujella's page](https://web.math.pmf.unizg.hr/~duje/tors/rk32.html).
- [ANN] Elkies curve ICARM #398, reported found Sept 2025: rank exactly 30 under GRH for number fields alone, without BSD — [MathWorld](https://mathworld.wolfram.com/EllipticCurveRank.html).
- [ANN] Conflict on exact unconditional rank: Dujella says 22 (Samuel Li, Sept 2026) — [Dujella](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html); the Layr-Labs page says the same — [repo](https://github.com/Layr-Labs/elliptic-rank-challenge-public); MathWorld, updated 1 Nov 2026, still says 20 — [MathWorld](https://mathworld.wolfram.com/EllipticCurveRank.html). A search found no paper by Li.
- [ANN] Torsion records now: trivial 32, Z/2 22, Z/3 15, Z/4 13, Z/5 9, Z/6 9, Z/7 6, Z/8 6, Z/9 4, Z/10 4, Z/12 4, Z/2xZ/2 15, Z/2xZ/4 9, Z/2xZ/6 6, Z/2xZ/8 3 — [Dujella](https://web.math.pmf.unizg.hr/~duje/tors/tors.html).
- [THM/ANN] Infinite families: Elkies now gives the K3 with Mordell-Weil rank 17 over Q(t) and base changes of rank 18 and 19, the latter yielding infinitely many curves of rank >= 19 — [arXiv:2608.25406](https://arxiv.org/abs/2608.25406).
- Layr-Labs Elliptic Rank Challenge: a PARI/GP 2.17.4 harness certifying independence via canonical height matrices; cells by torsion and rank; a sieve on partial sums plus 2-descent reaches rank 5-6 in seconds to minutes on a laptop core, `ellrank` for ranks 8-12 — [repo](https://github.com/Layr-Labs/elliptic-rank-challenge-public). ICARM's own axis is small conductor for given rank — [leaderboard](https://elliptic-rank.icarm.cloud/).

### Inferences
- The new records are consistent with PPVW as literally stated, which allows finitely many exceptions. But every torsion record now exceeds the corresponding model bound (Z/2: 22 vs 13; Z/3: 15 vs 9; Z/4: 13 vs 7; Z/7: 6 vs 3). The correct comparison is infinite families over Q(t), where Elkies's 19 is still below 21. The pressure test on the heuristic is whether exceptions look finite and whether high-rank curves concentrate in parametric families, which is Elkies's old objection.
- Smith's result is about Selmer coranks, so calling Goldfeld proved would be wrong: the odd-parity side needs a p = 2 converse theorem that Smith says is CM-only so far, and the rank statement needs BSD or Sha finiteness. Ellenberg's survey phrase about resolving the minimalist conjecture refers to this Selmer statement in twist families as far as the abstract shows.
- Over all curves, 2-Selmer convergence is slow: 2.90 at H about 10^16 against the limit 3. Rank >= 2 proportion was still 15% at 10^15. Data at any accessible height is pre-asymptotic, so exponent fits like -1/24 are weak without modelling H^(o(1)).

### Gaps
- Alpoge-Howell method unpublished. I found no paper on rank 30-32 beyond leaderboard, Dujella, and press. The rank >= 32 claim is confirmed by the leaderboard page and Dujella but has no paper. The Layr-Labs page and MathWorld (statements dated Aug 2026) still list 31.
- How many leaderboard curves have rank >= 22 was not counted. The page is 311k characters and only partly read.
- PPVW's height definition section (5.1) was not read directly.
- I found no theoretical secondary term or rate of convergence for Selmer averages, and no explanation of the turnaround near 6 x 10^8, which Balakrishnan et al. list as open.
- Rank records in quadratic twist families were not verified from a source.

## Bias, Mestre-Nagao sums, and the Riemann hypothesis for L(E,s)

### Takeaway
The analytic picture is clean: if the Mestre-Nagao limit exists it must equal 1/2 - r (Kim-Murty); the original BSD product asymptotic implies RH for L(E,s) (Goldfeld); and under RH that asymptotic holds off a set of finite logarithmic measure (Sheth). Existence of the actual limit is open and no finite computation can decide it. Fiorilli links extreme bias to unbounded rank under strong hypotheses. Murmurations explain why the Mestre-Nagao rank classifier is non-monotone in B at fixed conductor.

### Cited Findings
- [COND] Goldfeld 1982: the original BSD product asymptotic implies RH for L(E,s) and ord = rank — as stated in [Sheth, arXiv:2312.05236](https://arxiv.org/abs/2312.05236).
- [COND] Sheth (IMRN 2025): under RH for L(E,s), the product over p <= x of N_p/p is asymptotic to C (log x)^r for x outside a set of finite logarithmic measure — [arXiv:2312.05236](https://arxiv.org/abs/2312.05236).
- [THM] Kim-Murty: if the limit of (1/log x) sum_{p <= x} a_p log p / p exists, it equals -r + 1/2; relates this to Nagao's conjecture — [arXiv:2105.10805](https://arxiv.org/abs/2105.10805). Sutherland's slides are reported in search to pair this with RH for L(E,s); not read directly.
- [COND] Sheth 2024: GRH for GL_n, Ramanujan when needed: central Euler product asymptotic off finite log measure, confirming a Kurokawa conjecture; Chebyshev bias in the Aoki-Koyama framework — [arXiv:2405.01512](https://arxiv.org/abs/2405.01512).
- [COND] Rosen-Silverman proved a conjecture of Nagao relating the first moment of a one-parameter family to the rank of the surface over Q(T), for families satisfying Tate's conjecture — as described in [Batterman et al., arXiv:2311.17215](https://arxiv.org/abs/2311.17215).
- [CONJ, NUM] Miller's Bias Conjecture: in second moments of one-parameter families, the first lower-order term that does not average to zero is on average negative. Batterman et al. find a family positive on half the primes, and their numerics could not decide it — [arXiv:2311.17215](https://arxiv.org/abs/2311.17215).
- [COND] Fiorilli (IMRN 2014). Race S(t) = -sum_{p <= t} a_p/sqrt(p), logarithmic densities of S >= 0. Under ECRH and LI(E), Sarnak showed delta(E) exists and differs from 1/2. Under RH, the limiting variable has mean 2 r_an - 1 and variance comparable to log N_E, giving delta >= 1 - 2 Var/(2 r_an - 1)^2. Theorem 1.2: ECRH + bounded multiplicity + limsup r_an/sqrt(log N_E) = infinity implies races with delta arbitrarily near 1. Theorem 1.5: LI + delta tending to 1 implies that limsup statement. Theorem 1.7: LI + a nontrivial bias implies RH for L(E,s) — [arXiv:1304.8011](https://ar5iv.labs.arxiv.org/html/1304.8011).
- [NUM] Bujanovic-Kazalicki-Novak: Mestre-Nagao sums oscillate in step with murmurations. For N in [40,000, 45,000], B = 3,200 classifies rank 0/1 better than B = 50,000, partly explained by Zubrilina — [arXiv:2403.17626](https://arxiv.org/abs/2403.17626).
- [NUM] Bujanovic-Kazalicki-Vlah: multi-value S_0, S_5 improves classification significantly; learned conductor-dependent weights give only a slight edge — [arXiv:2506.07967](https://arxiv.org/abs/2506.07967).
- [THM] Klagsbrun-Sherman-Weigandt: Elkies's 2006 curve has rank 28 subject only to GRH, via 2-ranks of class groups of cubic fields — [arXiv:1606.07178](https://arxiv.org/abs/1606.07178).
- [CONJ] Martin notes BSD predicts a subtle correlation between a_p sizes and ranks, unresolved in relation to murmurations — [arXiv:2505.01093](https://arxiv.org/html/2505.01093).

### Inferences
- Existence of the limit needs more than RH. Sheth's exceptional set is exactly the obstruction, and it cannot be settled by finite computation, so a project here should target quantitative behaviour: size of error, tail of the logarithmic distribution, or comparison with the limiting variable X_E.
- Applying Fiorilli's bound to record curves: with mean 2r - 1 = 63 at r = 32, and log N around 330 ([leaderboard](https://elliptic-rank.icarm.cloud/) log conductor for rank 31 curves is 329-387), Var is about log N and the lower bound is around 1 - 2(330)/63^2, about 0.83. This is rough because Var excludes the central zero and has an unspecified constant. These curves have r/sqrt(log N) about 1.7, likely the most extreme bias instances known, assuming BSD or RH as needed.

### Gaps
- Not verified: whether anyone has computed delta(E) for rank >= 28 curves. No such paper turned up, but the search was shallow.
- Sarnak's 2007 letter to Mazur was not retrieved. Attribution here is via Fiorilli.
- No precise literature statement found on the size of S(B) minus its limit for fixed E beyond RH-type bounds.

## Machine learning: rank, Sha, and what produced new mathematics

### Takeaway
Only one ML-originated finding has become new mathematics: murmurations themselves. Nearly everything since has shown networks recovering Mestre-Nagao sums, BSD-formula invariants, or murmuration curves, and at least one high-accuracy result has been shown to be a dataset artefact. AI-assisted search for rank records is a separate development with an undisclosed method.

### Cited Findings
- New mathematics: HLOP's murmurations, later reviewed by the authors as an AI-assisted case study, detected via PCA weightings, saliency curves, convolutional filters — [arXiv:2603.09680](https://arxiv.org/abs/2603.09680).
- Kazalicki-Vlah: CNN rank classification from conductor and normalized a_p, trained on LMFDB and on a custom trivial-torsion set with conductor to 10^30, rank to 10 — [arXiv:2207.06699](https://arxiv.org/abs/2207.06699).
- Pozdnyakov: interpretable models learn a mixture of Mestre-Nagao and murmurations; evidence against any low-complexity root number statistic learnable by standard ML — [arXiv:2403.14631](https://arxiv.org/abs/2403.14631).
- Bieri et al. 2025: vanishing order from Dirichlet coefficients, PCA clusters, murmuration-like averages — [arXiv:2502.10360](https://arxiv.org/abs/2502.10360).
- Bieri et al. 2026, XECQ dataset of 1,536,784 curves, conductor <= 400,000: 1D CNN accuracy 99.81% to 98.34% with fixed b = 10^4; saliency early resembles the difference of class means (murmuration curve), later Mestre-Nagao-like; no formal conjecture stated; synthetic Sato-Tate sequences also get classified, so networks read bias patterns — [arXiv:2603.17681](https://arxiv.org/html/2603.17681).
- Konda 2026: transformer >99% on rank 0/1 for conductor <= 10,000, top neuron weights match log p/(p log B) with Spearman 0.997, the CLS embedding encodes log L(E,1) — [arXiv:2606.15036](https://arxiv.org/abs/2606.15036).
- Babei et al.: Sha order prediction from BSD-formula invariants, >0.9 accuracy; applied a regression model to the rank 29 curve — [arXiv:2412.18576](https://arxiv.org/abs/2412.18576). Since the inputs are BSD ingredients, this is largely formula recovery (my reading).
- Babei et al.: predicting a_p from other a_q — [arXiv:2502.10357](https://arxiv.org/abs/2502.10357).
- Babei-Shah-Kebe show quadratic twist redundancy alone suffices for high accuracy in a_p prediction; they propose a twist-class-representative benchmark — [arXiv:2605.14288](https://arxiv.org/abs/2605.14288).
- Hua-Mok: prime-power features raise root number balanced accuracy by 0.7425 points (2.56% of baseline errors), rank 0 vs 1 relative error down 7.77%, three-class model accuracy down; transport across conductor ranges unstable — [arXiv:2609.00777](https://arxiv.org/html/2609.00777).
- He-Lee-Oliver-Qi: 2D CNN on twist data separates arithmetic from random matrix data better than 1D on traces, inspired by converse theorems — [arXiv:2604.15155](https://arxiv.org/abs/2604.15155).
- Retraction caution: Wachs withdrew three theorems of arXiv:2603.22807v1 and said a sign flip and a "100% Tamagawa channel" were artefacts ([arXiv:2603.22807](https://arxiv.org/abs/2603.22807)), and withdrew a Sha claim in [arXiv:2603.04604](https://arxiv.org/abs/2603.04604) because analytic Sha is defined by the BSD formula.

### Inferences
- Do not spend time on rank-from-a_p classification, Sha-from-BSD-invariants prediction, or a_p-from-a_q prediction unless twist classes are controlled and a new statistic is the point. All have been done, some repeatedly.
- The remaining ML value is interpretive. A linear classifier under gradient descent starts at the class-mean difference, which is why saliency looks like murmurations; that is a fact about training dynamics as much as arithmetic.

### Gaps
- No published case found of ML yielding a new theorem in this area other than via the murmuration discovery. Claims of guiding new conjectures remain aspirational in the sources I read.
- Whether the rank 30-31 work used ML on L-function data is unknown because the method is unpublished.

## Open problems with a computational component, and cost estimates for a 16-core PARI/Python/C workstation

### Takeaway
Best targets are places where a stated open point meets cheap computation: quadratic twist murmurations (reducible to one a_p table plus character sums, reaching conductors around 10^12), comparing the Cowan and Sawin-Sutherland densities, extending the prime-conductor prediction to all conductors, testing Hua-Mok universality on elliptic curves, extending Selmer sampling past height 10^16, and record-curve bias. Height-ordered prime averages at or beyond 2^28 with fine bins are out of reach on one workstation.

### Cited Findings
Problems stated in the literature, by source:
1. Prove Conjecture 1 (primes), or a sharp-cutoff form of Theorem 2, and extract a convergence rate — [Sawin-Sutherland](https://arxiv.org/html/2504.12295v2). Theory.
2. Show locally averaged Cowan agrees with the Sawin-Sutherland density, not yet done — [Sawin-Sutherland](https://arxiv.org/html/2504.12295v2).
3. Explain the persistent downward bias for primes, and why parity-split averages converge more slowly — [Sawin-Sutherland](https://arxiv.org/html/2504.12295v2).
4. Conductor ordering: prediction eq. 7 has no theorem. Faltings height and whether p = 2, 3 stop being special; hypergeometric motives; orthogonal monodromy with discontinuous density — [Sawin-Sutherland](https://arxiv.org/html/2504.12295v2).
5. Whether elliptic curve murmurations have a limit after smoothing, and which smoothing; class number sums showing murmurations; no-root-number murmurations and non-squarefree levels — [Martin](https://arxiv.org/html/2505.01093).
6. Hua-Mok Conjecture 1.1 beyond weight 2 squarefree; Conjecture 2.2 (von Mangoldt average needs their bound (2.6)); larger k; predictive transport — [Hua-Mok](https://arxiv.org/html/2609.00777).
7. Extend Kundu-Mueller to general weight using corrected weighted results; Lemma 7.3 of Zubrilina unrepaired; weight 2 smoothed density theorem not covered for k < 6 — [Nelson et al.](https://arxiv.org/html/2609.29631).
8. PPVW Questions 11.2.1 (growth of rank 0 curves with Sha isomorphic to G, conjectured H^(19/24+o(1)), with Elkies-Hindry and Watkins in conflict), 11.3.1 (limit law of #Sha/H^(1/12) for rank 0), 11.4 (Sha distribution for rank >= 2), 11.5 — [PPVW](https://ar5iv.labs.arxiv.org/html/1602.01431).
9. Theoretical explanation of the rank turnaround, positive vs negative discriminant rank gap, and databases for Bhargava-Ho marked point families — [Balakrishnan et al.](https://ar5iv.labs.arxiv.org/html/1602.01894).
10. Bias Conjecture numerics inconclusive — [Batterman et al.](https://arxiv.org/abs/2311.17215).
11. Rank growth: limsup r/sqrt(log N), log N/log log N vs sqrt(log N log log N); data cannot yet separate models — [Fiorilli](https://ar5iv.labs.arxiv.org/html/1304.8011).
12. Whether high-accuracy prediction reflects arithmetic structure — [Bieri et al.](https://arxiv.org/html/2603.17681).
13. Smith's method failing over some number fields (Remark 1.19) — [Smith](https://arxiv.org/html/2503.17619). Theory.

### Inferences
All costs below are my estimates, not benchmarks. Assumption: 10^4 to 10^5 a_p per second per core at p around 2^32, so 10^10 to 10^11 a_p per 16-core day, higher for small p. Measure this first; PARI was not available on the machine where these notes were written.

Tier 1 (hours to days, plausible new content)

| # | Project | Why open | Cost estimate | Risk |
|---|---|---|---|---|
| A | Quadratic twist murmurations at conductor 10^10 to 10^13. For fixed E, a_p(E_d) = chi_d(p) a_p(E) and eps(E_d) = eps(E) chi_d(-N_E), so the family sum is a single a_p table times character sums over d. Test the main term of Cowan's Theorem 5.3 at p/N around 1, where his error term gives no proof | Only conditional formula exists; Deshpande et al. saw nothing for congruent curves, perhaps because p never reached N_E d^2 | D = 10^5 to 10^6, 10^7 primes near 10^10 to 10^13: a few hours total. Sieve-multiply (d/p) from quadratic characters of p mod q, about 2 ms per p at D = 10^6 | Formula extraction from HMM11 is real work. Window in d must be narrow so N_d is nearly constant |
| B | Numerically compare Cowan's main term with the Sawin-Sutherland density, ideally prove equality via a term match | Explicitly not done | CPU minutes to hours; effort is mathematical | Conductor-distribution bookkeeping; families differ by congruence conditions |
| C | Extend eq. 7 from prime conductor to squarefree or all conductors by adding local factors at p dividing N; test on all N < 500,000 | No such conjecture found | About 3 x 10^6 curves times 8 x 10^4 primes = 2 x 10^11 small a_p, about half a day. SNR about 70 per bin with 100 bins | Non-squarefree local factors need thought |
| D | Hua-Mok universality on elliptic curves at k = 2, 3: check G(p^k/X) against k = 1 for conductor-ordered and height-ordered families | Conjecture states general families; elliptic curves not proved | Minutes to an hour from LMFDB-range data. About 3.6 x 10^7 pairs per bin at k = 2, SNR about 8 at N about 5 x 10^5 | Appendices of their paper were unread, so check they did not already plot this |
| E | Extend 100k-curve Selmer samples to k = 17..24 with `ellrank` or 2-Selmer via `bnfinit`, fit rate of approach to 3 and Poonen-Rains rank distribution | Published samples stop at k = 16 | Assuming 1 s per curve at k = 24: about 14 hours for 8 x 10^5 curves. Benchmark first | GRH-conditional; no theory for rate found; sample noise at 10^5 curves |
| F | Fiorilli race for rank >= 28 curves: S(t) to 10^10 to 6 x 10^10, empirical logarithmic density, compare with mean 2r - 1 | No computation found | About 4.5 x 10^8 primes per curve at 10^10: under an hour to a few hours per curve | A short note, not a major result. Var needs zeros that are inaccessible at log N about 330 |
| G | Elliptic curves over F_q(t), q = 5, 7: root-number-weighted averages of Frobenius traces at degree about conductor degree. Analogue of Sawin-Sutherland's geometric family remark, adjacent to Lalin et al. and Wachs | No paper found on elliptic curve murmurations in this setting | Exhaustive for conductor degree up to about 16, under a day | Definitions need care; large-q equidistribution may wash out the phenomenon, so fixed q is essential |
| H | Mestre-Nagao optimal B(N): integrate the Zubrilina or Sawin-Sutherland density with weight log p/p to predict class means vs B/N, compare with empirical optimum | "Partial explanation" only | Hours on LMFDB-range data | Partly anticipated by Bujanovic et al. |

Tier 2 (weeks, or uncertain payoff)

| # | Project | Cost estimate | Note |
|---|---|---|---|
| I | Downward bias vs X for X from 2^16 to 2^26, 20-40 bins: fit decay rate, split by parity. Combine with ranks from the Balakrishnan et al. database | M about 100 N per bin. At 2^26, 20 bins: about 10^11 a_p, about 1-10 days | Reaching X about 2^32, past the turnaround near 2^29, needs about 4 x 10^12 pairs (10 bins at SNR 10, or 100 bins at SNR 3), 40-400 days, so marginal |
| J | Murmurations in torsion families, Z/2 first (H^(1/2) curves), with a Sawin-Sutherland style local factor conjecture | Same M law, about days at H around 2^26 | The authors say the method should apply broadly. New conjecture plus numerics would be a paper. Balakrishnan et al. also want such databases |
| K | PPVW Question 11.3.1, law of #Sha/H^(1/12) at rank 0 | 10^5 curves at H about 10^16, about 10^8 terms each: about a day | Dependence on root number and Tamagawa needs handling. Note that the model cannot predict it, so data alone is the contribution |
| L | Rank >= 2 proportion on larger samples at H = 10^15 to 10^20 | 10^4-10^5 curves per height; analytic rank costs about sqrt(N) terms | Weak exponent resolution |
| M | Bias Conjecture, second moments for families where it is undecided, p <= 10^6 | About 4 x 10^10 small a_p, about an hour per family | Inconclusive is a likely outcome |
| N | Quadratic twist rank bound: PPVW 5 vs Granville 7, search high-rank twists by character-sum sieve | d up to 10^10 sieve, days | Only ever gives lower bounds; finite exceptions allowed |
| O | Smaller curves for fixed rank and torsion on ICARM or Layr-Labs, PARI sieve | Rank 5-6 trivial; 8-12 weeks | Mostly benchmark; competitive field right now |

Out of reach here: proving anything for conductor ordering; X = 2^28 at 2000 bins (about 5 x 10^13 pairs, roughly 1-10 years at the assumed rate) or anything near 2^40; finding rank >= 33 by naive means; settling existence of the Mestre-Nagao limit.

Do not rediscover: HLOP plots; Zubrilina density plots; root number or rank classification from a_p; Mestre-Nagao weights recovered by networks; smaller-B classification effect; 2^infinity-Selmer 50/50 in twists; rank turnaround near 6 x 10^8; average rank declining in samples; non-Poonen-Rains distributions for balanced isogeny or full 2-torsion hole models; prime-power murmurations in weight 2 squarefree level.

### Gaps
- All throughput figures are unbenchmarked assumptions, and BSGS speed for a_p in PARI vs custom C can differ by an order of magnitude.
- Project A's signal estimate assumes the 1/sqrt(conductor) law carries over to twist families, where family size is only about conductor^(1/2). Cowan's formula involves L(sym^2 E) factors, so the amplitude may depend on E. Run a small pilot at D = 10^4 before scaling.
- Whether the Hua-Mok 99-page appendices already contain item D, or later preprints already do items B or C, should be rechecked at project start. Items were screened only by titles and abstracts through the arXiv API as of 1 Nov 2026, plus partial reads.
- Item K would need L(E,1) and Tamagawa data at heights beyond LMFDB, and the cost estimate there is for a single-precision central value.
