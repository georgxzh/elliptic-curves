# Record-setting and explicit-construction work on elliptic curves over Q and number fields (state as of 1 November 2026)

Scope note for the report writer. The field changed violently between May and November 2026. The ICARM Elliptic Curve Rank Leaderboard (launched 2026, 6,369 curves when scraped on 2026-11-01) is now the primary live record source, and it moves hourly. Anything older than about August 2026 should be treated as stale, including the brief's own starting point ("rank >= 29, anything since"): the record is now **rank >= 32**. Numbers marked "my computation" were derived by me from downloaded data and are not published statements. Items recalled from memory without a retrieved source are confined to the Gaps sections.

## Rank records over Q: current value, holder, and anything since Elkies-Klagsbrun rank >= 29

### Takeaway
The record is **rank >= 32** (Elkies, Klagsbrun, Li; ICARM #4239, submitted 2026-10-15), after a run of 29 (Aug 2024) -> 30 (Aug 2026) -> 31 (Aug 2026) -> 32 (Oct 2026). The largest rank known exactly and unconditionally is 22 (Samuel Li, Sept 2026). Rank exactly 32 is conditional on GRH and BSD.

### Cited Findings
- Record history as now listed: 28 Elkies 2006; 29 Elkies-Klagsbrun 2024; 30 Alpoge-Howell 2026; 31 Alpoge-Howell 2026; 32 Elkies-Klagsbrun-Li 2026 — [Dujella rank history](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html).
- Rank-32 curve: [1, 0, 0, -28623928991398919165500467001947502452240040593445344054331428726899413, 1636638097022027963025086119463360482368875730889253334875693440181143871885452358966522018914326964558817], 32 independent points listed — [Dujella rk32 page](https://web.math.pmf.unizg.hr/~duje/tors/rk32.html).
- #4239: submitted by zevklagsbrun 2026-10-15 17:27:56 UTC, trivial torsion, 180-digit conductor, naive height 498.3114, regulator about 7.17e42, "discovered by Noam Elkies, Zev Klagsbrun, and Samuel Li"; specialization of a rank-17 elliptic fibration on the K3 surface of discriminant 1152 at T = -2868768/362209 — [ICARM curve 4239](https://elliptic-rank.icarm.cloud/curve/4239).
- Upper bound for #4239: S. Hackfort (16 Oct 2026), explicit-formula bound with L = 12.41, using all 2,529,822,599 primes below 6.02e10, certified 33.99820448 +/- 1.83e-9; with root number +1 this gives r_an = 32 under GRH; rank exactly 32 under GRH + BSD — [ICARM curve 4239](https://elliptic-rank.icarm.cloud/curve/4239).
- Rank 31: ICARM #302, posted 2026-08-23 by Ava Howell, credited to Claude, Levent Alpoge and Ava Howell; a = [1, 1, 1, -1284727764113567728281797636015784768866707681415849262157224232063, 560368321454261339256859338901915312332769858684945406858043869199456710681989058863306170127006181]; T = 164518/924945 — [ICARM curve 302](https://elliptic-rank.icarm.cloud/curve/302).
- Rank 30: ICARM #273, 2026-08-20, specialization at T = 12473/32946 of an explicit family y^2+(Lx+B)y = x(x+D)(x+E); the Bober method with Delta = 4.25 gives analytic rank at most 31, root number 1 gives even rank — [ICARM news](https://icarm.io/news/new-record-breaking-elliptic-curve-reported/); [Wolfram Cloud note](https://www.wolframcloud.com/obj/fbc67625-2e2f-4913-83b2-6355ce5c5e51). Family formula confirmed from the #273 page commentary scraped 2026-11-01.
- Independent rank 30 by Elkies-Klagsbrun dated September 2025 (posted Aug 2026 as #398); Elkies reports exact rank 30 under GRH for number fields, without BSD — [MathWorld](https://mathworld.wolfram.com/EllipticCurveRank.html); [ICARM curve 398](https://elliptic-rank.icarm.cloud/curve/398).
- The Claude-credited curves came from an internal non-public model and a "relatively simple prompt"; no compute figures were published — [Scientific American, 16 Sep 2026](https://www.scientificamerican.com/article/anthropics-ai-steals-mathematicians-record-for-most-complicated-curve/). Epoch's "rank >= 30" problem is marked solved (human + AI) — [Epoch](https://epoch.ai/frontiermath/open-problems/elliptic-curve-rank).
- Exact-rank chain: Kretschmer 10, Schneiders-Zimmer 11, Fermigier 14, Dujella 15, Elkies 17, 18, 19, Elkies-Klagsbrun 20, Li 21, Li 22 — [Dujella rank history](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html); same 22 figure in [Layr-Labs challenge README](https://github.com/Layr-Labs/elliptic-rank-challenge-public).
- Smaller curves at the top ranks (log conductor, scrape of 2026-11-01): rank 32 only #4239 (414.09); rank >= 31 best #3900 (325.25, 142 digits, Ritik Jain, 2026-10-04, T = 35013/50879 on a rank-17 fibration of X1152); rank >= 30 best #3897 (279.89, T = 208/29933); rank >= 29 best #3835 (265.37, Matej Jurasic, T = 4157/637 on a rank-16 fibration of X1092); rank >= 28 best #3762 (242.93) — [ICARM leaderboard](https://elliptic-rank.icarm.cloud/); [curve 3900](https://elliptic-rank.icarm.cloud/curve/3900); [curve 3835](https://elliptic-rank.icarm.cloud/curve/3835).

**Conflicts and stale sources:**
- MathWorld says the largest unconditional exact rank is 20 and the record is 31 ("as of Aug. 29, 2026"), which is superseded by Dujella's 22 and 32 — [MathWorld](https://mathworld.wolfram.com/EllipticCurveRank.html).
- A cached search snapshot of Dujella's torsion page showed 31 and Z/2 = 20, while the live page and its [GitHub mirror](https://dujella.github.io/tors/tors.html) show 32 and 22. His pages carry no update date, so the table was edited within weeks.
- The Layr-Labs baseline is frozen at 2026-10-15 04:07 UTC, before #4239, so it stops at 31 — [records.json](https://raw.githubusercontent.com/Layr-Labs/elliptic-rank-challenge-public/main/ec_verify/records.json).
- metaforismo/elliptic-rank-32 makes no rank-32 claim and is not a record source — [repo](https://github.com/metaforismo/elliptic-rank-32).

### Inferences
- The barrier moved from compute to geometry. The rank-30 and rank-31 specializations above have parameter height only about 2^15 (T = 208/29933, 35013/50879); the rank-32 one has height about 2^21.5 (my computation from the listed T values). Choosing the fibration matters far more than sweeping harder.
- Attribution of leaderboard handle "wgxli" to Samuel Li is my inference: the Dujella credit "Li (2026)" matches wgxli's submissions and commentary style, but no page I read states the identity.

### Gaps
- No preprint located for the rank-32 method or for the Alpoge-Howell construction. Lozano-Robledo publicly asked for details; I found no answer.
- I found no primary document for Li's exact rank 22 (paper, certificate, or which curve). Presumably #4118, a Z/2 curve, but that link is unconfirmed.
- NMBRTHRY posts were not retrievable; the Aug 2024 "Z29 in E(Q)" post is known only through citations.

## Dujella's table: rank record per Mazur torsion group, when last improved, and which are weakest

### Takeaway
Only T = 0 and Z/2 have actually increased since 2020; 2026 activity elsewhere consists of ties. The weakest by age are Z/2xZ/8 (2000), Z/10 (2005), Z/8 and Z/2xZ/6 (2006), Z/12 (2008), Z/9 (2009). Z/9, Z/10 and Z/12 also have remarkably small record parameters, which makes them the most exposed.

### Cited Findings
Table (bounds and credits from [Dujella tors.html](https://web.math.pmf.unizg.hr/~duje/tors/tors.html), also identical on [his GitHub mirror](https://dujella.github.io/tors/tors.html); "first reached" separates a real increase from later ties; curves from [Layr-Labs records.json](https://raw.githubusercontent.com/Layr-Labs/elliptic-rank-challenge-public/main/ec_verify/records.json) and ICARM curve pages):

| T | Rank >= | First reached | Later ties | Conj. asymptotic bound (EK 2020) | Smallest-N record curve (ICARM) | log N |
|---|---|---|---|---|---|---|
| 0 | 32 | Elkies-Klagsbrun-Li, Oct 2026 | none | 21 | #4239 | 414.09 |
| Z/2 | 22 | Li 2026 (#4118, Oct 9 on board) | none | 13 | #4118 | 228.67 |
| Z/3 | 15 | Elkies-Klagsbrun 2020 | Li 2026 (#4645) | 9 | #318 | 145.16 |
| Z/4 | 13 | Elkies-Klagsbrun 2020 | Li May 2026 (#325, #803) | 7 | #1919 | 145.51 |
| Z/5 | 9 | Klagsbrun 2020 | none | 5 | #1215 | 76.48 |
| Z/6 | 9 | Klagsbrun 2020 | Voznyy 2020, Dujella-Peral 2026 | 5 | #1216 | 69.84 |
| Z/7 | 6 | Klagsbrun 2020 | Park 2026 (#6078) | 3 | #6078 | 74.92 |
| Z/8 | 6 | Elkies 2006 | DMP 2013, Voznyy 2021 | 3 | #1904 | 60.46 |
| Z/9 | 4 | Fisher 2009 | van Beek 2015, D-P 2021, D-P-R 2022, Voznyy 2026 | n/a | #1117 | 37.33 |
| Z/10 | 4 | Dujella 2005 | Elkies 2006, Dujella 2008, Fisher 2016 | n/a | #1090 | 50.24 |
| Z/12 | 4 | Fisher 2008 | none | n/a | #1105 | 61.14 |
| Z/2xZ/2 | 15 | Elkies 2009 | Li 2026 (#4549) | n/a | #4549 | 179.16 |
| Z/2xZ/4 | 9 | Dujella-Peral 2012 | D-P 2019, Klagsbrun 2020 | n/a | #1827 | 73.16 |
| Z/2xZ/6 | 6 | Elkies 2006 | DPT 2015, D-P 2020 | n/a | #1833 | 59.95 |
| Z/2xZ/8 | 3 | Connell 2000, Dujella 2000 | many, to 2022 | n/a | #1087 | 27.56 |

Conjectured bounds are "for n = 2,...,8 the bound 21 is replaced by 13, 9, 7, 5, 5, 3, 3" — [Elkies-Klagsbrun 2020](https://arxiv.org/pdf/2003.00077). The January 2023 table differed from today's only at T = 0 (28) and Z/2 (20) — [Elkies JMM 2023 slides](https://abel.math.harvard.edu/~elkies/Elkies_JMM23.pdf).

Record curves as a-invariants (the rank-32 curve is in the previous section). These are the frozen 2026-10-15 baselines, chosen by smallest naive height, so a curve here can differ from the smallest-N curve in the table above:
```
Z/2  r22 #4118 [1,0,1,-173719528525019397613189688778644156848077689219115646293,655283790102850006567977331426970882151340170628667781827093572298216118282111782608]
Z/3  r15 #318  [1,0,1,-107404730164187455100283304999195859754632145403,48976939778870435455584633601954124477725966045276826839333933204370006]
Z/4  r13 #803  [0,-1,0,-893211001377324088868409658436161336697176597505301441,322318489353257476127105984661383880720198001931577617014493148996108419252695905]
Z/5  r9  #1215 [1,0,0,-1271376476514788123979112128312980,248131717764014678423337299444388036083025142487952]
Z/6  r9  #1216 [1,0,0,-801598222309406030167646512525,1340218010187071010144873439749301626926500625]
Z/7  r6  #1214 [1,0,0,-326034514850898538462143577535732108974101688866,126139807177463916084745782524191445068029238338478785879968870214064452]
Z/8  r6  #1904 [1,1,1,690560257169377937125059126423812540,-33492188518937203020097127431557287129957999127407035]
Z/9  r4  #1117 [1,0,0,-210121912561076041141788727170,37072777483029442821111037453964917510678212]
Z/10 r4  #1090 [1,0,0,-3913976067656937637459249967383835,80614222594310898664080091661625700445673557913297]
Z/12 r4  #1105 [1,0,0,-4422329901784763147754792226039053294186858800,98943710602886706347390586357680210847183616798063680624530387016000]
2x2  r15 #319  [1,-1,0,-1478818379630960182018543975144238479079598870400357903794,21612333371564362906227820064846376685227380006732368388851217276076518563786908263808]
2x4  r9  #1827 [1,0,0,-160457317436491036800639760108090,-369449120458315595021673906507946532059648303900]
2x6  r6  #1833 [1,0,0,-37680956700999226080263982005713090640,-36992898397926078743894505902555362159162611772488902400]
2x8  r3  #1087 [1,0,0,-15745932530829089880,24028219957095969426339278400]
```
- Details of new ties: #4118 is T = -97053/246469 on the rank-9 fibration of X1008 — [curve 4118](https://elliptic-rank.icarm.cloud/curve/4118). #325 was "found May 2026 without AI assistance" at T = 11367979/38917800 of EK's E1 — [curve 325](https://elliptic-rank.icarm.cloud/curve/325). #4549 is T = 4206111/3370112 on a rank-5 fibration of X400 — [curve 4549](https://elliptic-rank.icarm.cloud/curve/4549). #4645 is T = -5652311/1171368 on a rank-5 fibration of X163 — [curve 4645](https://elliptic-rank.icarm.cloud/curve/4645).
- Dujella lists no rank-5 for Z/9, Z/10, Z/12 and no rank-4 for Z/2xZ/8 — [Dujella](https://web.math.pmf.unizg.hr/~duje/tors/tors.html). Published counts: 1 Z/12 rank-4 entry ([z12](https://web.math.pmf.unizg.hr/~duje/tors/z12.html)); 7 Z/9 ([z9](https://web.math.pmf.unizg.hr/~duje/tors/z9.html)); 25 Z/10 ([z10](https://web.math.pmf.unizg.hr/~duje/tors/z10.html)); 34 Z/2xZ/8 rank 3 ([z2z8](https://web.math.pmf.unizg.hr/~duje/tors/z2z8.html)).
- EK searched Z/5 to height 2^28 with no rank 9, finding 151 rank-8 curves; Z/6 over 0<a<2^25, |b|<2^26 finding one rank 9; Z/7 to height 2^20 finding one rank 6; Z/3 on 13 fibrations of X163 with a region of 2^43 each; Z/4 to height 2^22; Z/2 about a<2^21, |b|<2^23. They tried Z/8 and Z/2xZ/6 "without any luck" — [Elkies-Klagsbrun 2020](https://arxiv.org/pdf/2003.00077).
- Rubinstein's public curve lists cover Z/2, Z/3, Z/4, Z/5, Z/6, Z/7, Z/8, Z/2xZ/2, Z/4xZ/2, Z/6xZ/2, with "the search for the remaining groups ongoing" — [Rubinstein repo](https://github.com/mrubinst/elliptic-curves-by-rank). So Z/9, Z/10, Z/12, Z/2xZ/8 are the groups not yet covered.

### Inferences
- **Record parameters (my computation).** I recovered the universal-curve parameter from Dujella's listed torsion points via Tate normal form. Checks passed: for Z/7 I get 820369/1568697, equivalent under t -> (t-1)/t to EK's published t = -748328/820369, and -1076219/12925, equivalent under t -> 1/(1-t) to znan2's t = 12925/1089144 on #6078. This also shows "Park (2026)" and ICARM #6078 are the same curve.

| T | Universal surface type | Max record height (bits) | Note |
|---|---|---|---|
| Z/12 | 10 cusps | t = 859/266, 2^9.7 | single curve |
| Z/9 | 8 cusps | 8.6 to 12.0 (Voznyy t = -4199/2920) | 7 curves |
| Z/10 | 8 cusps | 10.1 to 14.7 | 25 curves |
| Z/8 | 6 cusps | 16.3 to 18.0 | param d |
| Z/2xZ/8 | param d = b/c | 8.4 to 20.9 | 34 curves; d is not the uniformizer, so height is inflated |
| Z/7 | K3, 6 cusps | 20.0, 20.6 | Park's is just past EK's 2^20 boundary |
| Z/5 | rational, 4 cusps | t = -266165145/442317512, 2^28.7 | just past EK's 2^28 boundary |

- Conductor scaling check: N is about H^(number of cusps); Z/12 with H = 859 gives 2.2e29 against the true N of 3.6e26.
- Both Z/5 and Z/7 records sit immediately outside EK's exhaustive box, which suggests those families were exhausted at the box edge rather than being sparse.
- Tip ratios on the frozen board (known_count differences, biased toward high rank, not population data): rank r-1 to rank r about 20:1 for Z/7, 11:1 Z/5, 22:1 Z/6, 10:1 Z/2xZ/4, 15:1 Z/2xZ/6, 10:1 Z/8, 6:1 Z/9, 2.6:1 Z/10, 55:1 Z/12. Z/10's unusually dense rank-4 tip is the single best hint that a rank 5 may be nearby.

### Gaps
- PPVW-type conjectural bounds for Z/9, Z/10, Z/12 and the non-cyclic groups were not retrieved.
- How far Fisher, Dujella, Voznyy, Rathbun actually swept Z/9, Z/10, Z/12, Z/2xZ/8 is undocumented; heights listed are heights of hits, not sweep limits.
- "Last improved" for Li's rank 21 Z/2 is not dated in any source I found.

## Families of high generic rank: Mestre, Nagao, Fermigier, Martin-McMillen, Elkies, and Q(t) records per torsion group

### Takeaway
Over Q(t) the torsion-free record remains 18 (Elkies 2006), but 2026 saw several torsion increases. In practice the new engine is K3 surfaces with rank 16-17 fibrations, reached by neighbour steps between fibrations.

### Cited Findings
Generic rank table — [Dujella generic.html](https://web.math.pmf.unizg.hr/~duje/tors/generic.html):

| T | G(T) >= | Authors |
|---|---|---|
| 0 | 18 | Elkies 2006 |
| Z/2 | 11 | Elkies 2009, Dujella-Peral 2023 |
| Z/3 | 7 | Elkies 2007, Eroshkin 2023 |
| Z/4 | 6 | Dujella-Peral 2022, 2026 |
| Z/5 | 4 | Eroshkin 2020, Dujella-Peral 2026 |
| Z/6 | 4 | Jaswal 2026 |
| Z/7 | 1 | Kulesz 1998, Lecacheux 2003, Rabarison 2008, Harrache 2009, MacLeod 2014 |
| Z/8 | 2 | Dujella-Peral 2012, MacLeod 2013, D-K-P 2021, D-P-Youmbai 2026 |
| Z/9, Z/10, Z/12, Z/2xZ/8 | 0 | Kubert 1976 |
| Z/2xZ/2 | 7 | Elkies 2007 |
| Z/2xZ/4 | 4 | Dujella-Peral 2012, Jang 2026 |
| Z/2xZ/6 | 2 | D-P 2012, 2015, 2017, MacLeod 2013, D-K-P 2021 |

- Historical Q(t) line: Mestre 1991 rank >= 11 and >= 12; Nagao 1994 >= 13; Kihara 2001 >= 14; Elkies 2006-07 rank 17, 18. Martin-McMillen's 23 (1998) and 24 (2000) are records over Q, not Q(t) — [Dujella history](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html); search results citing [Elkies lecture notes and Kihara](https://arxiv.org/pdf/1410.6919).
- Over-Q history: Mestre 12 (1982), 14 (1986), 15 (1992); Nagao 17 (1992), 20 (1993); Fermigier 19 (1992), 22 (1997); Nagao-Kouya 21 (1994); Martin-McMillen 23, 24; Elkies 28 — [Dujella history](https://web.math.pmf.unizg.hr/~duje/tors/rankhist.html).
- Live fibrations with explicit formulas, publicly posted: rank-17 fibrations of X1152 (#3897, #3900, #4239), rank-16 fibrations of X1092 (#752, #3835), of X1008 (#4541, #5490), rank-9 of X1008 with Z/2 (#4118), rank-5 of X163 with Z/3 (#4645), rank-5 of X400 with Z/2xZ/2 (#4549) — [ICARM curves](https://elliptic-rank.icarm.cloud/curve/3897).
- Jurasic's commentary describes reaching new fibrations by "neighbour steps" from known ones, e.g. #4541 "two neighbour steps from the one in curve #751" — [ICARM curve 4541](https://elliptic-rank.icarm.cloud/curve/4541).
- A new family: a Mordell curve over Q(T) with generic rank 4 from points on the Burkhardt quartic 1 + a^3 + b^3 + c^3 + d^3 + 3abcd = 0, claimed universal for rank >= 4 Mordell curves up to isogeny — [ICARM curve 5569](https://elliptic-rank.icarm.cloud/curve/5569).
- Mestre's ten-root construction is back in use: p = q^2 - r on ten integer roots gives y^2 = r(x) with ten points; Rubinstein has 304,957 curves of ranks 13-19 as of 2026-10-31, counts falling from 122,726 at rank 13 to 2 at rank 19 — [Rubinstein repo](https://github.com/mrubinst/elliptic-curves-by-rank); [ICARM curve 6180](https://elliptic-rank.icarm.cloud/curve/6180).

### Inferences
- Rubinstein's counts imply a factor of roughly 6-9 lost per rank step for ten-root curves (my arithmetic from the two endpoints).
- Z/7's generic rank of 1, stuck since 1998, and Z/9, Z/10, Z/12, Z/2xZ/8 at 0 are the natural structural targets, but generic rank 1 over X1(9) etc. is a problem about rational points on higher-genus curves rather than a compute problem.

### Gaps
- Fermigier's and Martin-McMillen's Q(t) contributions were not pinned down from primary sources. A memory-based claim that Martin-McMillen had rank 17 over Q(t) was not supported by what I retrieved.
- Papers behind the 2026 entries (Jaswal, Jang, Dujella-Peral-Youmbai) were not retrieved.

## Methods: Mestre-Nagao sieving, filtering, certification, GRH issues, and which steps need Magma

### Takeaway
The search stage needs no Magma at all. Upper-bound screening can be done from a_p alone under GRH. PARI's `ellrank` has certified curves up to about N = 10^55 in Rubinstein's pipeline. The real Magma dependency is at the point-finding end, higher descents and Selmer computations for curves with no 2-isogeny.

### Cited Findings
**Sieve (Elkies-Klagsbrun 2020):**
- Score S(t,B) = sum over good p<B of log(N_p/p). Tricks: a_p(t) depends on t mod p; staged bounds B_0 <= ... <= B with cutoffs C_i; an actual sieve over a for fixed b using integer-scaled logs (D = 1024, 16-bit counters) and vector instructions — [EK 2020](https://arxiv.org/pdf/2003.00077).
- Speed: S(a/b, 2^16) for 2^20 values of a in 3.2 s on one thread of a 2.3 GHz Skylake; S(a/b, 2^13) in 0.19 s. C_0 targets a cut-down of order 10^3, with B_0 between 2^13 and 2^16, then doubling to B = 2^18. Previous searches used B < 10^3 — [EK 2020](https://arxiv.org/pdf/2003.00077).
- EK warn the score degrades as the search region grows, and ask how to include Tamagawa factors. High-rank curves favour split multiplicative reduction at small primes — [EK 2020](https://arxiv.org/pdf/2003.00077).
- Skewed search regions (|a| max = s|b| max) reduce coefficient size — [EK 2020](https://arxiv.org/pdf/2003.00077).

**Elkies 2023 small-curve method.** Searches M_{1,k+1}: instead of all curves of height H (about H^10), enumerate marked curves with integral collinear points, using weighted-projective models for k <= 4 and a Grassmannian for k = 5, reducing H^10 to H^5. For |T| > 1, slices such as P^2 x P^2 for (|T|,k) = (2,3). Then Mestre-Nagao ranking, `ellratpoints`, and parity +1 — [Elkies JMM 2023](https://abel.math.harvard.edu/~elkies/Elkies_JMM23.pdf). Produced rank 12 and 13 records, improved in June 2026 — [ICARM curve 157](https://elliptic-rank.icarm.cloud/curve/157).

**Rubinstein pipeline (no Magma).** Enumerate ten-root sets, score S = sum of -a_p log(p)/p over 5 <= p <= 199 with early abort; thresholds S >= 31 (or 30 with one bad prime, 29 with two); screen by exact conductor and a GRH explicit-formula bound; certify with `ellrank`. Rank 16 "proved: 16 independent points, matching the 2-descent upper bound" — [ICARM curve 6180](https://elliptic-rank.icarm.cloud/curve/6180).

**Certification options:**
| Step | Tool | Magma needed? | Source |
|---|---|---|---|
| Rank lower bound | Exact points plus independence; ICARM uses exact 2-descent quadratic characters at good primes (Cremona/Brumer), no floats | No (PARI WASM 2.17.2) | [ICARM API](https://elliptic-rank.icarm.cloud/api); [icarm/elliptic-rank](https://github.com/icarm/elliptic-rank) |
| Lower bound alt | Height pairing at two precisions plus Weyl margin | No (PARI 2.17.4) | [Layr-Labs](https://github.com/Layr-Labs/elliptic-rank-challenge-public) |
| 2-descent upper bound | `ellrank` returns [r,R,V]; `ellsaturation`; uses the bnfinit of the 2-division algebra Q[X]/(P) | No | [Allombert](https://pari.math.u-bordeaux.fr/archives/pari-dev-2102/msg00003.html); [Belabas](https://pari.math.u-bordeaux.fr/archives/pari-dev-2102/msg00011.html) |
| 2-power isogeny bound | `TwoPowerIsogenyDescentRankBound` (Fisher) | Yes, as used by EK | [EK 2020](https://arxiv.org/pdf/2003.00077) |
| 3-isogeny bound | `ThreeIsogenySelmerGroups` plus own Cassels-Tate code | Yes, as used by EK | [EK 2020](https://arxiv.org/pdf/2003.00077) |
| Covering point search | Magma 2-covering search; Elkies cubic lattice method (memory leak in Magma's) | Yes, as used by EK | [EK 2020](https://arxiv.org/pdf/2003.00077) |
| GRH analytic bound | Bober 2013; Klagsbrun-Sherman-Weigandt 2019; radix-rank | No: Rust/Python/PARI/Arb, needs only a_p | [Bober](https://arxiv.org/abs/1112.1503); [radix-rank](https://github.com/sectio-aurea-q/radix-rank) |

- EK found that for torsion with 2-torsion, the isogeny upper bound always equalled the rank when the bound was large. Z/5 and Z/7 needed 2-Selmer plus Cassels-Tate; the Z/7 family's 2-division field discriminant has degree only 6, which made it tractable — [EK 2020](https://arxiv.org/pdf/2003.00077).
- GRH split: with torsion, isogeny Selmer groups are "entirely feasible"; unconstrained curves need 2-torsion in the class group of a large-discriminant cubic field and GRH for all unramified abelian extensions — [Elkies ANTS XVI](https://antsmath.org/ANTSXVI/slides/Elkies.pdf). Mordell curves sit between: 3-isogeny descent reduces to 3-torsion in class groups of Q(sqrt k) and Q(sqrt(-3k)), and Elkies proved the rank-16 curve unconditional via Burgess bounds — [Elkies ANTS XVI](https://antsmath.org/ANTSXVI/slides/Elkies.pdf).
- Bober's abstract: bounds under BSD + GRH for curves of rank >= 20-24, and 30 for the rank >= 28 curve — [Bober](https://arxiv.org/abs/1112.1503).
- radix-rank: per-curve optimized test function, 2.4-2.8x faster a_p than PARI per core; #3762 needed 19,235 primes vs 122,776 for Bober's kernel. These are self-reported and from a preprint — [radix-rank](https://github.com/sectio-aurea-q/radix-rank).
- `ellrank` does not use analytic methods, per Allombert; effort controls Selmer classes, quartic models, and `hyperellratpoints` height — [Allombert](https://pari.math.u-bordeaux.fr/archives/pari-dev-2102/msg00004.html).
- PARI-only evidence: Z/7 rank 6 #6078 records "PARI/GP rank bounds [6,6]" at N = 3.45e32 — [ICARM curve 6078](https://elliptic-rank.icarm.cloud/curve/6078). #3957 Z/6 rank 9 has a "matching unconditional upper bound computed using PARI/GP 2.17.2 ellrank" — [ICARM curve 3957](https://elliptic-rank.icarm.cloud/curve/3957). Rubinstein's ten-root curves were certified by `ellrank` up to rank 19, N = 1.4e54 — [ICARM curve 6120](https://elliptic-rank.icarm.cloud/curve/6120).
- Layr-Labs's feasibility ladder (their estimate, one laptop core): rank 5 ~10 s; rank 6 ~3 min; ranks 8-12 hours; rank 18 by specializing a published family; 19-24 weeks; 25-31 research — [Layr-Labs](https://github.com/Layr-Labs/elliptic-rank-challenge-public).

### Inferences
- Sieve capacity on a 16-core box (my computation from EK timings, scaling linearly with 16 full threads and ignoring second-stage work):
  - B_0 = 2^13: 8.8e7 t/s, 7.6e12 t/day, about 2^42.8 per day.
  - B_0 = 2^16: 5.2e6 t/s, 4.5e11 t/day, about 2^38.7 per day.
  - With about 1.2 H^2 parameters of height at most H: H = 2^18 in 16 min, H = 2^20 in 4.2 h, H = 2^22 in 2.8 days at B_0 = 2^13 (multiply by 16.8 at B_0 = 2^16).
- Scale of EK runs in those units at B_0 = 2^13: Z/7 (height 2^20) 4 h; Z/4 (height 2^22) 3 days; Z/3 (13 x 2^43) 15 days; Z/2 region about 5 days per fibration; Z/6 2^52 about 590 days; Z/5 height 2^28 about 11,600 days, or 500 core-years. So EK's K3 sweeps are workstation-scale; their rational-surface sweeps are not.
- Table building is negligible: all a_p(t) for p < 2^13 needs about 3.7e6 curves mod p; for p < 2^16 about 2e8 curves and memory of a few hundred MB.
- Screening candidates: a GRH bound is cheap at the sizes that matter here. Anchors from radix-rank's report: 19,235 primes for #3762 (log N 243), against 2.5e9 primes for #4239 (log N 414). Use it before `ellrank`. Root number parity halves the candidates.
- Curves with full 2-torsion (Z/2xZ/8 and the like) require no class group at all in 2-descent; one 2-torsion point needs only a quadratic field; only 2-torsion-free families hit cubic fields. So Z/10, Z/12, Z/8 and Z/2xZ/8 are PARI-friendly; Z/9, Z/5, Z/7 less so, though Z/5 and Z/7 are documented to work.

### Gaps
- Whether PARI's `ellrank` bound is unconditional: `bnfinit` assumes GRH unless certified. Rubinstein's README says "proven"; I could not confirm whether `bnfcertify` is used. Treat his and similar "proved" statements as possibly GRH-conditional.
- PARI has no 4-descent or 3-isogeny Selmer command that I could confirm. From memory, not sourced here: Magma's `MordellWeilShaInformation` combines 2-descent, 4-descent and analytic data; mwrank performs 2-descent only; `ellrank` is limited to curves over Q.
- From memory, not sourced: Fisher's rank-4 Z/12 result used 6- and 12-descent, and KSW 2019 established Elkies's 28 curve as rank 28 subject to GRH. Dujella's page confirms only that the Z/12 record's generators have coordinates with up to about 100 digits — [z12](https://web.math.pmf.unizg.hr/~duje/tors/z12.html).
- How many candidates are needed per record: no published funnel statistics beyond EK's "cut-down on the order of 10^3".

## Elliptic curves over number fields: torsion classifications and large-torsion records

### Takeaway
Phi(d) is now determined for d = 1,...,5. The quintic case (Najman, Sept 2026) gives three sporadic groups, including the first non-cyclic one. All such proofs and searches in the literature use Magma, and PARI's `ellrank` does not cover number fields, so this area is a poor fit for the workstation brief except for tables of rank lower bounds.

### Cited Findings
- d = 1 Mazur; d = 2 Kamienny, Kenku-Momose; d = 3 Derickx-Etropolski-van Hoeij-Morrow-Zureick-Brown; d = 4 Derickx-Najman (published Crelle 2025); d = 5 Najman 2026 — [Najman arXiv 2609.12846](https://arxiv.org/pdf/2609.12846); [Derickx-Najman](https://doi.org/10.1515/crelle-2025-0069).
- Degree 3: exactly one sporadic group Z/21Z, realized only by the base change of 162.c3 to Q(zeta_9)^+. Degree 4: no sporadic groups — [Najman](https://arxiv.org/pdf/2609.12846); [Derickx-Najman](https://arxiv.org/pdf/2412.16016).
- Degree 5: 35 groups, Z/nZ for n = 1..22, 24, 25, 28, 30 and Z/2Z x Z/2nZ for n = 1..9. Phi(5) = Phi_inf(5) union {Z/28, Z/30, Z/2xZ/18}. Pair counts 1, 2, 1 — [Najman](https://arxiv.org/pdf/2609.12846).
- Z/28 over 5.3.17348.1 (conductor norm 16); Z/30 over 5.3.10407.1 (norm 33, two curves); Z/2xZ/18 over 5.3.34779.1 (norm 6). The Z/2xZ/18 example is new; van Hoeij found the others; each field has signature (3,1), class number 1 and S_5 closure — [Najman](https://arxiv.org/pdf/2609.12846).
- Najman's computations used Magma V2.29-4 on an EPYC 9175F with 384 GB, and the paper discloses use of AI models in proofs and code — [Najman](https://arxiv.org/pdf/2609.12846).
- Phi_inf(5) and Phi_inf(6) are from Derickx-Sutherland 2017 — [Najman](https://arxiv.org/pdf/2609.12846).
- Rank records over quadratic fields — [Dujella torsquad](https://web.math.pmf.unizg.hr/~duje/tors/torsquad.html):

| T | Rank >= | d | | T | Rank >= | d |
|---|---|---|---|---|---|---|
| 0 | 34 (35 under parity) | -3 | | Z/15 | 2 | 190 |
| Z/2 | 28 | -1 | | Z/16 | 4 | -183443183 |
| Z/3 | 22 | -3 | | Z/18 | 2 | 9049 |
| Z/4 | 16 | 605113 | | Z/2xZ/2 | 22 | d173 |
| Z/5 | 13 | 367327 | | Z/2xZ/4 | 14 | 1410049 |
| Z/6 | 15 | 330374 | | Z/2xZ/6 | 10 | 624341 |
| Z/7 | 10 | 30781 | | Z/2xZ/8 | 8 | 31230597 |
| Z/8 | 10 | 1680281 | | Z/2xZ/10 | 4 (5) | 4063 (2740223761) |
| Z/9 | 8 | 408729 | | Z/2xZ/12 | 5 | -295935 |
| Z/10 | 8 | 234649 | | Z/3xZ/3 | 9 | -3 |
| Z/11 | 3 | 12601 | | Z/3xZ/6 | 6 | -3 |
| Z/12 | 7 | 2014 | | Z/4xZ/4 | 8 | -1 |
| Z/13 | 2 | 193 | | | | |
| Z/14 | 3 | 430 | | | | |

- Kazancioglu-Sadek (JNT 2025) study smallest-discriminant fields for torsion — [Sabanci record](https://research.sabanciuniv.edu/id/eprint/49866/) (not read in full).

### Inferences
- Z/15, Z/13, Z/18 at rank 2 and Z/11, Z/14 at rank 3 are the thin entries. Lower bounds only need explicit independent points over K, which PARI can search for with custom code, but no descent tool is available.
- A base-change trick covers Z/2,...,Z/12 entries, since rank E(K) = rank E(Q) + rank E^d(Q), which is why those are high; Voznyy's many credits show this is actively worked.
- Classifying Phi(6) is out of scope: it needs modular Jacobian machinery and Magma.

### Gaps
- Status of d = 6 and van Hoeij's low-degree-point lists were not retrieved; I found no claim that Phi(6) is known.
- No source located for smallest-conductor curves by torsion over cubic or quartic fields, beyond the quintic Table 7 values, and LMFDB's number-field pages were not checked.
- Isolated-point literature (Bourdon et al.) was not read for 2026 status.
- "Records" for torsion over cubic fields with rank were not found.

## Other explicit-object problems: conductors, integer points, congruent numbers, Mordell tables, Sha, good reduction, progressions, Diophantine tuples

### Takeaway
Yes, 234446 and 19047851 stand as the best known for ranks 4 and 5, with ranks 5-11 unchanged since 2004. Ranks 12-20 have all been lowered in 2026, most since late September, and these are falling daily. The clearest cheap record elsewhere is the analytic Sha record, untouched in any source I found since 2021.

### Cited Findings
**Smallest conductors by rank.** Current best known, scraped 2026-11-01; entries for ranks 5-13 give exact N from ICARM pages — [ICARM](https://elliptic-rank.icarm.cloud/):

| r | Best N | Curve / ICARM | Holder, date |
|---|---|---|---|
| 4 | 234446 | [1,-1,0,-79,289] #54 | classical |
| 5 | 19047851 | [0,0,1,-79,342] #41 | known before Elkies-Watkins 2004, confirmed there |
| 6 | 5187563742 | [1,1,0,-2582,48720] #43 | Elkies-Watkins 2004 |
| 7 | 382623908456 | [0,0,0,-10012,346900] #44 | Elkies-Watkins 2004 |
| 8 | 249649566346838 | [1,-1,0,-106384,13075804] #47 | Elkies-Watkins 2004 |
| 9 | 32107342006814614 | [1,-1,0,-135004,97151644] #48 | Elkies-Watkins 2004 |
| 10 | 10189285026863130793 | [0,0,1,-16312387,25970162646] #49 | Elkies-Watkins 2004 |
| 11 | 18031737725935636520843 (prime) | [0,0,1,-16359067,26274178986] #50 | Elkies-Watkins 2004 |
| 12 | 12212741842431104280769438 | #157 | Elkies, June 2026 |
| 13 | 13048475524065056885495472921 | #158 | Elkies, June 2026 |
| 14 | 25168869705838997533742636949448 | #759 | Rubinstein list, 2026-09-18 |
| 15 | 265121998882424427980422961463765954 | #811 | Rubinstein list, 2026-09-21 |
| 16 | 1306046612716079154116875733335056508018 | #6180 | Rubinstein ten-root, 2026-10-30 |
| 17 | 837877902601733961103246999529573248471046104 | #6095 | Rubinstein ten-root, 2026-10-29 |
| 18 | 1.28e49 | #6121 | Rubinstein ten-root, 2026-10-29 |
| 19 | 1.40e54 | #6120 | Rubinstein ten-root, 2026-10-29 |
| 20 | 8.06e57 | #6361 | "e-man" GPU ten-root via Layr-Labs, posted by The Wren, 2026-11-01 |
| 21 | 9.79e62 | #4541 | Jurasic, 2026-10-17 |
| 22-24 | log N 157.62, 170.40, 187.90 | #5492, #5491, #5490 | Jurasic, 2026-10-22 |
| 25-29 | log N 193.10, 214.49, 231.22, 242.93, 265.37 | #4540, #4539, #4043, #3762, #3835 | various |

The table is from these pages: [#157](https://elliptic-rank.icarm.cloud/curve/157), [#6180](https://elliptic-rank.icarm.cloud/curve/6180), [#6361](https://elliptic-rank.icarm.cloud/curve/6361). Elkies's 2023 values for 12 and 13 (2.61e25, 3.83e28) were superseded by his own June 2026 curves — [Elkies JMM 2023](https://abel.math.harvard.edu/~elkies/Elkies_JMM23.pdf).

- Provenness: OEIS keeps only a(0)-a(4) = 11, 37, 389, 5077, 234446; values for ranks 5-7 and 11 were removed as unproved, "just upper bounds" — [OEIS A052432](https://oeis.org/A052432). Elkies: "for r = 5 there may be smaller composite N" — [Elkies JMM 2023](https://abel.math.harvard.edu/~elkies/Elkies_JMM23.pdf).
- Databases: LMFDB 3,824,372 curves, conductors up to 299,996,953, max rank 5 (19 curves), max analytic Sha 75^2 — [LMFDB stats](https://www.lmfdb.org/EllipticCurve/Q/stats). Coverage is N <= 500000 by Cremona plus 7-smooth and prime conductor lists — [LMFDB sources](https://www.lmfdb.org/EllipticCurve/Q/Source). Rubinstein: 18,895,316 proven-rank curves, ranks 4-15 — [repo](https://github.com/mrubinst/elliptic-curves-by-rank). Height-ordered rank and 2-Selmer databases by Balakrishnan et al. — [arXiv 1602.01894](https://arxiv.org/abs/1602.01894).
- Hall's conjecture: best ratio r = sqrt(x)/|y^2 - x^3| = 46.60 at x = 5853886516781223 (Elkies); next 16.53, 10.65, 10.18, 6.50. List complete for x <= 10^29 (44 entries) — [Wikipedia](https://en.wikipedia.org/wiki/Hall%27s_conjecture); [Aanderaa-Kristiansen-Ruud 2018](https://www.ams.org/journals/mcom/2018-87-314/S0025-5718-2018-03298-7). Wikipedia mentions an Epoch challenge for r > 100, but it is not in the visible portion of [Epoch's list](https://epoch.ai/frontiermath/open-problems).
- Integral points: Bennett-Ghadermarzi solved y^2 = x^3 + k for all 0 < |k| <= 10^7 — [Bennett-Ghadermarzi](https://personal.math.ubc.ca/~bennett/BeGh-LMSJCM-2015.pdf). Rank-4 curve y^2 = x^3 - 9494304273243x + 11224300076670688758 has |E(Z)| = 208 — [Dujella survey](https://web.math.pmf.unizg.hr/~duje/coell.html). Bennett-Gherga-Rechnitzer's Thue-Mahler method handled particular large conductors and prime conductors heuristically to 2e13 — [BGR](https://personal.math.ubc.ca/~bennett/BeGhRe-MathComp-2019.pdf).
- Family rank records on ICARM (scrape 2026-11-01): Mordell y^2 = x^3 + k rank 18 (#5641, #5643, wgxli, 2026-10-24, up from Elkies's 16 in 2016, which he proved unconditionally); cube-sums x^3 + y^3 = A rank 11, A = 13293998056584952174157235 (Elkies-Rogers 2004); y^2 = x^3 + ax rank 14 (Watkins 2002); congruent family rank 7 (d = 797507543735, Watkins et al. 2014) — [ICARM curve 5641](https://elliptic-rank.icarm.cloud/curve/5641); [curve 4748](https://elliptic-rank.icarm.cloud/curve/4748); [curve 4695](https://elliptic-rank.icarm.cloud/curve/4695); [curve 2901](https://elliptic-rank.icarm.cloud/curve/2901); [Elkies ANTS XVI](https://antsmath.org/ANTSXVI/slides/Elkies.pdf).
- Congruent numbers: Hart-Tornaria-Watkins list to 10^12, accurate subject to BSD, found 3,148,379,694 new congruent numbers — [WRAP](https://wrap.warwick.ac.uk/id/eprint/41654); [press](https://www.eurekalert.org/news-releases/722991).
- Largest Sha: analytic |Sha| = 1937832^2 > 3.755e12, first row of Table 1 of the paper (q = 285, k = 3, L = 21.1540), Goldfeld-Szpiro ratio G = 153.084; best G = 163.119 at |Sha| = 804572^2. Method is quadratic twists of Frey curves from abc triples with lambda > 1.4; 241 such triples exist; 20 isogeny classes above 250000^2; computed with PARI's `ellap` on one laptop thread at about 600x less cost than the previous record — [Broadhurst 2021](https://arxiv.org/pdf/2111.07794). The triple's a and c are given in factored form in the PDF; PDF text extraction garbled the exponents, so copy them from the PDF itself.
- Largest proven Sha: 410536^2 for E_4(21,-233), using Kolyvagin, Kato, Skinner-Urban, Skinner — [Dabrowski-Szymaszkiewicz 2021](https://arxiv.org/pdf/2103.11001).
- Everywhere good reduction: Elkies's table of unit-discriminant curves over real quadratic fields with D < 10^6 lists 621 curves with non-rational j and 91 with rational j and m = 6 — [Elkies rqfu](https://people.math.harvard.edu/~elkies/rqfu/). Non-existence for many small m and full determinations for m = 6, 7, 14, 22, 29, 33, 37, 38, 41, 65, 77 — [Yokoyama-Shimasaki](https://ar5iv.labs.arxiv.org/html/1107.4648).
- Arithmetic progressions: x-coordinate records are length 8 on Weierstrass cubics (Bremner) and 14 on quartics (MacLeod, with Alvarado's 11 further examples); 9 on Edwards curves (Moody, not extendable) — [Bremner JIS](https://cs.uwaterloo.ca/journals/JIS/VOL16/Bremner/bremner2.html); [Moody JIS](https://cs.uwaterloo.ca/journals/JIS/VOL14/Moody/moody2.pdf).
- Diophantine m-tuples: no rational septuple known; Gibbs found 45 rational sextuples; infinite families of sextuples exist with mixed signs — [Dujella ratio](https://web.math.pmf.unizg.hr/~duje/ratio.html). Triples induce y^2 = (ax+1)(bx+1)(cx+1), and the Z/2xZ/4 rank-9 record comes from such a triple — [Dujella survey](https://web.math.pmf.unizg.hr/~duje/coell.html).

### Inferences
- The ICARM family filters only show curves someone has submitted. An untouched family (cube-sum rank 11 since 2004, y^2 = x^3 + ax rank 14 since 2002) is likely under-searched by modern methods, but also likely to be attacked soon, given that the Mordell record moved from 16 to 18 within weeks of the Burkhardt parametrization.
- Conductors 5e5 < N < 1.9e7, composite: a smaller rank-5 conductor is not excluded. Extending completeness there is a verification project, not a record search.
- The 2026 table above implies a half-life of days for conductor records at ranks 16-24.

### Gaps
- Largest Tamagawa product: no source or record located. LMFDB stats do not list it.
- No post-2021 analytic Sha record found. A search was run, but absence of results is not proof; check before claiming.
- Bober's and Balakrishnan's databases of small conductor were not separately characterized; database size and height bound for arXiv 1602.01894 were not confirmed from the abstract.
- Largest number of integral points on any curve, and the Stein-Watkins database figures, were not confirmed.
- Hall search cost in practice (AKR timings) not retrieved; y-coordinate progression record is inconsistently reported (7 vs 6) across sources.

## Which records look most attackable, with search-cost estimates

### Takeaway
Ranked by expected value for a 16-core PARI/C workstation over a few days, the best targets are an analytic Sha record, Z/10 (then Z/9 and Z/12) rank 5 by universal-curve sweep, and new K3 fibrations for Z/2, Z/3, Z/4, Z/2xZ/2. Overall rank 33 and small-conductor cells are feasible computationally but heavily contested. All probabilities below are my subjective judgment, not data.

### Cited Findings
- Live competition: on 2026-11-01 alone "The Wren" posted a burst of Z/6 curves within minutes — [ICARM recent](https://elliptic-rank.icarm.cloud/recent). Layr-Labs is running an open challenge over (torsion, rank) cells, with 52 curves on its board by 2026-11-01, a "breakthrough" bonus for new cells, and originality rules that bar copying known curves — [Layr-Labs](https://github.com/Layr-Labs/elliptic-rank-challenge-public); [board listing](https://api.github.com/repos/Layr-Labs/elliptic-rank-challenge-public/contents/submission/board).
- Layr-Labs itself says the most practical progress is smaller curves in thin cells and non-trivial torsion — [Layr-Labs](https://github.com/Layr-Labs/elliptic-rank-challenge-public).
- Submission to ICARM needs a GitHub login and API token; verification is automatic — [ICARM API](https://elliptic-rank.icarm.cloud/api).
- Broadhurst's burden formula: m is about |Sha|/(2 pi G) log(K sqrt|Sha|/(2^t L)), with total cost about (m/10^8)^(5/4) GHz-hours, and T/B = 0.8 +/- 0.2 — [Broadhurst](https://arxiv.org/pdf/2111.07794).

### Inferences
Costs use the sieve throughput derived above. Assumes modern 16 cores are at least as fast as EK's reference thread.

**1. Analytic Sha above 1937832^2, or G above 163.119 (best bet).**
- Why: PARI-only precedent, laptop-scale record, only 241 lambda > 1.4 triples but free choice of squarefree twist q, and no competition visible.
- Cost: record scale m is about 4e10, B is about 1,800, so about 1,500 GHz-hours, or 30 hours on 16 cores at 3 GHz using plain `ellap` (my arithmetic); a C a_p routine would cut that materially.
- Filter: reverse Mestre-Nagao. Want L(1) large, so rank Euler partial products over q for each triple, cost seconds per thousand q. Then do the full sum only for the best few dozen.
- Caveats: conditional on BSD, relies on the unproven K = 4 truncation, and the result is "analytic order". Check for a post-2021 record first.
- P(new record in a week): about 50-70%.

**2. Z/10 rank 5 (record 4, 2005), then Z/9 rank 5 and Z/12 rank 5.**
- Why: genus-0 universal curves, record parameters only 2^10 to 2^15, not yet in Rubinstein's lists, and not reported in EK's searches.
- Cost: H <= 2^20 in 4.2 h (B_0 = 2^13), H <= 2^22 in 2.8 days; use B_0 = 2^14-2^15 for the top band. Stage 2 lookups roughly double this. Then GRH bound and `ellrank`.
- Certification: Z/10 and Z/12 have rational 2-torsion, so the descent uses only a quadratic field. Z/9 has none, and needs cubic-field or 3-isogeny work.
- Main risk: points. Z/12's record generators have coordinates up to about 100 digits, and Z/9 and Z/10 are smaller but still non-trivial. PARI lacks higher descent, so a hand-rolled second 2-descent (Cremona-Rusin style) in PARI/Python is likely needed, one to several days of coding. A candidate without points is only a Selmer/GRH-conditional rank 5, not a record.
- P(certified rank 5 in any of the three in about 2 weeks): Z/10 about 15-25%, Z/9 about 8-15%, Z/12 about 3-8%. P(strong candidates with a Selmer rank of 5): roughly double.

**3. Z/2 rank 23, Z/3 rank 16, Z/4 rank 14, Z/2xZ/2 rank 16 by new K3 fibrations.**
- Why: Li gained +2 on Z/2 at T of height only 2^17.9 on a new fibration of X1008. Z/3, Z/4, Z/2xZ/2 have only tied so far.
- Cost per fibration at region 2^43: about 1 day (B_0 = 2^13). Sweep to height 2^20 takes 4 h. Sieve is the cheap part.
- Bottleneck: producing new fibrations (Kneser-Nishiyama neighbours, explicit Weierstrass models, section lifts). Mostly algebra in PARI/Python, several days of expertise. Direct route: re-sweep the published fibrations in #4118, #4549, #4645 past their hit heights.
- Certification: Z/2, Z/4 and Z/2xZ/2 fine via 2-isogeny descent (`ellrank` should be OK if the quadratic field is manageable, N about 10^80-100 is untested). Z/3 needs 3-Selmer/Cassels-Tate, a Magma gap.
- P(new record in 2 weeks): 5-15% per group, mainly because Elkies, Klagsbrun, Li, Jurasic and others are on exactly this.

**4. Overall rank 33 on published rank-17 fibrations of X1152 (#3897, #3900, #4239).**
- Cost: H <= 2^22 sweep, 2.8 days per fibration (2^13); rank 32 was at height 2^21.5.
- Blockers: trivial torsion so no 2-descent at this size, and extra points need Elkies-style lattice search, which must be implemented. GRH bound needs p up to about 6e10, or 2.5e9 primes: about hours to a day in fast code (radix-rank's numbers), not PARI's `ellap`.
- P(success in 2 weeks): 1-3%. Highly contested, and rank 33 may not occur on these fibrations.

**5. Conductor or height cells (T, r): the easiest to win, hardest to keep.**
- Trivial-torsion ranks 14-21 via ten-root search: rank 20 record fell today, with roots up to 140. Rubinstein's rates imply rank 21 needs about 50x the rank-19 effort.
- Non-trivial T via Elkies's M_{1,k+1} slices: Z/9, Z/10, Z/12, Z/2xZ/8 cells not covered by Rubinstein yet. Hours of compute; expect dozens of new small-curve cells at ranks 2-4 with these four groups.
- P(some record in 2 days): over 80%. Half-life: days to weeks. Scientific value: low, unless paired with statistics.

**6. Z/7 rank 7 or Mordell rank 19, cube-sum rank 12 (secondary).**
- Z/7: a week reaches H about 2^22.7 at B_0 = 2^13, and H = 2^23 takes 11 days. With a 20:1 tip ratio and falling density, rank 7 plausibly sits at H of 2^23-2^24 or beyond, which is 11-45 days and past the stated budget. Rank 6 examples beyond EK's box are feasible and new (P about 50% for another rank 6 in a week, under 5% for rank 7).
- Cube-sum rank 12: untouched on the board since 2004. Cost unknown; Elkies-Rogers method needs review. Mordell rank 19: active, Burkhardt family is public.

**Not realistically attackable with this hardware:**
- Z/5 rank 10, Z/6 rank 10: EK's rational-surface sweeps were hundreds of core-years. A 16-core week reaches only 2^45-2^46 of a region around 2^56.
- Hall r > 46.6: with about 1.5 good examples per decade of x and P(r > R) of order 1/R, about 3% per decade; extending exhaustive coverage beyond 10^29 likely takes months (rough heuristic from sqrt(X)-type algorithms).
- Congruent or twist rank 8; number-field classification; Phi(6).
- Z/2xZ/8 rank 4: compute is cheap (full 2-torsion, H = 2^22 in 3 days, no class groups), but 26 years of repeated attempts by Rathbun, Fisher, Dujella and Voznyy produced only rank 3 examples, and d-height already reaches 2^20.9. P about 3-8%. Worth a sweep as a side run because it shares code with target 2.

**Suggested order.** Build one C sieve for Tate-form families plus a GRH-bound screener. Run target 1 as a parallel background job. Run target 2 for 3-4 days, and target 5's T cells as by-products. Target 3 only if the fibration tooling is ready. Check [ICARM recent](https://elliptic-rank.icarm.cloud/recent) and [Dujella](https://web.math.pmf.unizg.hr/~duje/tors/tors.html) on the day of any claim.

### Gaps
- All probabilities and several cost multipliers are judgment calls; no source quantifies yield for rank 5 in Z/9, Z/10, Z/12.
- EK timing is for 2020 hardware and their fibrations; second-stage and `ellrank` costs at N of 10^60-10^100 were not benchmarked here. I did not run PARI, which was not found on this machine's shell path.
- Whether Voznyy or Dujella have privately swept Z/9, Z/10, Z/12 beyond published hits is unknown. Dujella's "Personal communication" credits suggest active private searches, and the ICARM Zulip was not read.
- A local PARI benchmark on a real Z/10 candidate is the most valuable next validation step before committing compute.
