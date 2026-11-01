# Computational and cryptographic elliptic curve problems: state of the art as of November 2026

Scope note for the report writer: compiled 1 November 2026 from published literature only. Many of the most important items are 2026 preprints, some only days old and none independently replicated in anything I read. Where a claim rests on a preprint, a press report, a forum post or a search snippet, the bullet says so. ePrint PDFs returned HTTP 403 to my fetch tool, so for ePrint items I usually read the abstract page and not the full paper. I did not route around that block. Exceptions, where I read the full text, are marked "(full text read)".

## ECDLP records and classical algorithms: what is the largest public solve, and does any sub-exponential algorithm exist for prime fields?

### Takeaway
Nothing has changed the classical picture for prime-field curves. The largest completed full-group solve is still around 112 to 114 bits (2009 and 2017), generic square-root methods remain the best known, no sub-exponential algorithm exists, and the 131-bit Certicom challenges were still unsolved as of the latest source. The only 2024-2026 movement is engineering: GPU throughput, an in-progress public attempt on ECC2K-130, and interval (bounded-key) solves reported outside academic venues.

### Cited Findings

**Full-group records**
- ECC2K-108 (2000), ECCp-109 (2002, about 10,308 participants led by Chris Monico, 549 days), ECC2-109 (2004, about 2,600 participants, 17 months) were solved with parallelised Pollard rho — [Wikipedia, used as a lead](https://en.wikipedia.org/wiki/Discrete_logarithm_records); solve dates for the two 109-bit challenges match [Certicom](https://www.certicom.com/content/certicom/en/the-certicom-ecc-challenge.html).
- 112-bit prime field: a standardised 112-bit curve was solved with 62.6 PS3-years on a cluster of more than 200 PS3s, January to July 2009; run continuously with the latest code it would have taken 3.5 months. Pollard rho is described there as the fastest known ECDLP algorithm — [Bos, Kaihara, Montgomery, "Pollard Rho on the PlayStation 3"](https://www.joppebos.com/files/rho_ps3.pdf) (full text read for this passage). Wikipedia additionally lists Kleinjung and Lenstra as team members for the record — [Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records).
- 113-bit binary field: Wenger and Wolfger on FPGA clusters, 113-bit Koblitz curve in 2014 (47 days, 18-core Virtex-6 cluster) and 113-bit binary curve in 2015 (about 82 days, 10-core Kintex-7 cluster) — [Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records).
- 114-bit prime field: a Barreto-Naehrig curve solved in August 2017 using the BN sextic twist, 2,000 CPU cores, about 6 months (Kusaka, Joichi, Ikuta, Khandaker, Nogami, Uehara, Yamai, Duquesne) — [Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records).
- 117-bit binary: Wikipedia lists a 2 December 2016 result over F_2^127 with an "interval search 2^117.35", by Bernstein, Engels, Lange, Niederhagen, Paar, Schwabe, Zimmermann, 64 to 576 FPGAs, about 6 months — [Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records). The abstract of the corresponding paper says only that it set a size record on sect113r2 and covered a much larger curve over a 127-bit field to demonstrate scalability — [ePrint 2016/382](https://eprint.iacr.org/2016/382). The 117.35 figure is therefore not confirmed by the primary abstract.

**Certicom status**
- ECCp-109 solved November 2002, ECC2-109 solved April 2004; 131, 163, 191, 239 and 359-bit challenges remain open and all Level II challenges are described as believed computationally infeasible — [Certicom](https://www.certicom.com/content/certicom/en/the-certicom-ecc-challenge.html). The page gives no prize amounts. Wikipedia states no 131-bit or larger challenge has been met as of 2026 — [Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records).

**Interval records (bounded keys, not full-group ECDLP)**
- 114-bit interval on secp256k1 (June or August 2020, Zieniewicz and Pons, 256 Tesla V100s, 13 days). Wikipedia's table and body text disagree on date and on rho versus kangaroo — [Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm_records).
- Non-academic claims since then: solver RetiredCoder claims 120, 125, 130 and 135-bit public puzzle intervals — [BitcoinTalk post](https://bitcointalk.org/index.php?topic=5517607). A Habr article dates the 135-bit solve to 28 July 2026: interval width 2^134, about 1.7·10^20 expected operations, about 5·10^19 actually used (about 30 percent of expectation), about 200 GPUs, about 5 months, based on the solver's own forum post — [Habr](https://habr.com/ru/articles/1064866/). These are self-reported and not peer-reviewed. A GitHub project still lists 135 as unsolved — [hevnsnt/collider](https://github.com/hevnsnt/collider) — so sources conflict, possibly only by date.

**Pollard rho state of the art (2026)**
- ePrint 2026/2469 (Buran, Nguyen, 14 October 2026) gives GPU field-arithmetic engineering with no algorithmic claim: the authors state it does not improve on the generic-group bound. Using ECC2K-130 over F_2^131 as benchmark: expected about 2^60.9 iterations; 14.64 billion iterations/s on one RTX PRO 6000 Blackwell in the audited build (15.88 billion/s later), versus 0.85 billion/s for the bitsliced baseline; under 5 GPU-years to solve; about 230 times the best 2010 GPU kernel per card; 8.25 billion/s on one AWS F2 FPGA; P-256 at 1.632 billion/s and P-384 at 0.548 billion/s on the same card; P-256 stated to be about 6·10^21 card-years away. Campaign progress is reported as 2^56.68 iterations walked, 5.4 percent of expected work — [ePrint 2026/2469](https://eprint.iacr.org/2026/2469). This is an unreviewed preprint and an ongoing campaign, not a record.
- The negation map gives roughly a √2 speedup — [ePrint 2011/008](https://eprint.iacr.org/2011/008.pdf) (seen via search only).

**Index calculus and summation polynomials on prime fields**
- A 2024 preprint concludes no sub-exponential method is known for ECDLP over prime fields, hedged to the present state of research — [Hu, ePrint 2024/1923](https://eprint.iacr.org/2024/1923).
- Why Semaev polynomials do not help directly: over extension fields, the factor base is restricted to a subfield or vector space and the relation equation is solved by Weil descent, yielding better-than-generic or sub-exponential results only for extension degree and field size growing appropriately (Gaudry, Diem). Semaev's paper proposes a factor base for the prime case but no algorithm to compute relations; and almost no attacks had been proposed against prime-field curves — [Petit, Kosters, Messeng, PKC 2016](https://christophe.petit.web.ulb.be/files/16PKC_primeECDLP.pdf) (full text read).
- That paper generalises the factor base to F = {(x,y) : L(x) = 0} with L a large-degree rational map that composes low-degree maps, so that relation search becomes a low-degree Gröbner-basis system. Its two instances need either a smooth divisor of p−1 or an auxiliary curve with a smooth subgroup. One standardised NIST curve meets the first structural precondition, but the authors state the attacks are not practical and their asymptotic complexity is unknown. They also report preliminary results that a Gröbner version of Semaev's original factor base is easier to solve than theirs, which may suggest their approach is asymptotically unpromising — [same paper](https://christophe.petit.web.ulb.be/files/16PKC_primeECDLP.pdf).
- Open problem named there: a dedicated algorithm for the generalised root-finding problem (find X_i with f(X_1..X_m) = 0 and L(X_i) = 0 for all i) that avoids Gröbner bases — [same paper](https://christophe.petit.web.ulb.be/files/16PKC_primeECDLP.pdf).
- Binary curves: complexity estimates depend on the first fall degree assumption, which is known to be false in general; generic algorithms outperform index calculus at practical parameters — [same paper](https://christophe.petit.web.ulb.be/files/16PKC_primeECDLP.pdf).
- A survey of this area exists but only its abstract was retrievable — [Galbraith, Gaudry, ePrint 2015/1022](https://eprint.iacr.org/2015/1022).

**Anything new in 2024-2026?**
- Mahalanobis, "A Guess and Determine Attack on the ECDLP" (July 2026) reduces ECDLP to finding a zero minor in a matrix, using a Las Vegas algorithm — [arXiv 2607.09814](https://arxiv.org/abs/2607.09814). One GitHub contributor's benchmark reports it as roughly 260 to 6715 times slower than rho with negation — [PR #1713, unreviewed](https://github.com/aburan28/crypto/pull/1713).
- A 2026 paper claims a 16-bit prime-field ECDLP solve on a D-Wave annealer — [ICN 2026.0017](https://www.sciopen.com/article/10.23919/ICN.2026.0017). I saw this only in search results. The instance size is trivial.

### Inferences
- A fresh full-group prime-field record needs more than 2^57 group operations. Expected rho cost with negation for a 112-bit group is sqrt(π·2^112/4) ≈ 2^55.8 (my arithmetic). At the 1.632 billion/s quoted for one top-end card on P-256, one card does about 2^55.5 iterations a year, so a single high-end card could repeat a 112-bit-size instance in roughly a year or less. A smaller field would run faster than the P-256 rate. A record, say 118 bits, costs 8 times more, so it needs a small cluster, not one card.
- If ECC2K-130 completes it would be the first Certicom challenge solved since 2004, but at 2^60.9 it adds no mathematics.
- Interval records are not comparable to group-size records: a width-2^134 interval costs about 2^67 operations regardless of the 256-bit group.
- The honest answer on prime-field index calculus: absence of an algorithm, not a lower bound. Nothing rules out a sub-exponential method; the generic-group lower bound does not apply to curves with explicit structure.

### Gaps
- I could not confirm 117.35 bits from a primary source, nor confirm whether Wikipedia's 2016 entry is a full-group or restricted-range result.
- The lifting story (xedni, Silverman-Suzuki) and the fall-degree refutations (Huang-Kosters-Yeo, Kosters-Yeo) were not read in primary form. A [GitHub survey PR](https://github.com/aburan28/crypto/pull/19) lists them as a lead only. Its username suggests it may share an author with ePrint 2026/2469, so I do not treat it as independent.
- I found no peer-reviewed prime-field full-group record after 2017, but absence from search and from Wikipedia (whose page carries a maintenance tag) is not proof.
- ePrint 2026/2469's ECC2K-130 campaign status is self-reported.

## Quantum resource estimates: how much does Shor cost for 256-bit curves as of 2026?

### Takeaway
2026 saw a dramatic compression: logical-qubit claims fell from about 2,330 (2017) to 835 (July to September 2026), Toffoli counts fell to tens of millions at around 1,200 to 1,450 logical qubits, and physical-qubit claims now run from under 500,000 superconducting qubits down to tens of thousands of atoms or ions under aggressive assumptions. All of these are estimates, not demonstrations, and the lowest qubit counts come with higher gate counts, so no single number is "the" cost.

### Cited Findings

| Source | Logical qubits | Toffoli | Physical / runtime |
|---|---|---|---|
| Roetteler et al. 2017 ([arXiv 1706.06752](https://arxiv.org/pdf/1706.06752)), figures as cited in [arXiv 2607.14082](https://arxiv.org/pdf/2607.14082) | 2,330 | 1.26·10^11 | n/a |
| Häner et al., as cited in [ePrint 2026/280](https://eprint.iacr.org/2026/280) | 2,124 | about 2^30 | n/a |
| Litinski 2023 ([arXiv 2306.08585](https://arxiv.org/abs/2306.08585)) | n/a | (44+65/k) million per key, k parallel instances | active-volume photonic architecture; strict 2D-local gives one key per 38 hours |
| Chevignard, Fouque, Schrottenloher, EUROCRYPT 2026 ([ePrint 2026/280](https://eprint.iacr.org/2026/280)) | 1,193 (3.12n+o(n)) | 2^38.98 per run, 22 runs; gates Õ(n^4) | n/a |
| Babbush et al., 30 March 2026, v2 15 April ([arXiv 2603.28846](https://arxiv.org/abs/2603.28846)) | under 1,200 / under 1,450 | under 90M / under 70M | under 500k physical at 10^-3 error, planar superconducting, minutes |
| Cain et al., 30 March 2026 ([arXiv 2603.28627](https://arxiv.org/abs/2603.28627)) | n/a | n/a | 26,000 reconfigurable atoms, a few days for P-256; headline floor 10,000 atoms |
| Schrottenloher, 1 June 2026 ([arXiv 2606.02235](https://arxiv.org/abs/2606.02235)) | about 1.5% above Babbush | 6.5 to 10% below Babbush | secp256k1, with a generic prime-field variant |
| Luo et al., v1 15 July, v3 5 September 2026 ([arXiv 2607.13816](https://arxiv.org/abs/2607.13816)) | 835 | leading term 1056n³/log₂n | n/a |
| IonQ, 8 September 2026 ([press release](https://ionq.com/news/ionq-publishes-worlds-first-fully-compiled-end-to-end-blueprint-for-breaking-256-bit-elliptic-curve-signatures); [report](https://thequantuminsider.com/2026/09/08/ionq-estimates-20000-qubit-machine-could-break-bitcoin-secp256k1-26-days/)) | 1,457 | 39M | 19,397 physical, qLDPC, 25.7 days per attempt, 63.3% heuristic or 40.7% rigorous success |

- Babbush et al. withheld the circuits and published a zero-knowledge proof that they compiled them; v2's comment says it patches a software bug that enabled an exploit against the proof's soundness — [arXiv 2603.28846](https://arxiv.org/abs/2603.28846).
- IonQ also withheld circuits, and one report says the paper was not on arXiv at publication and that no journal or review record exists despite IonQ calling it peer-reviewed — [PostQuantum](https://postquantum.com/quantum-research/ionq-secp256k1-resource-estimate/).
- RSA comparison: Gidney (May 2025) estimates RSA-2048 factoring in under a week with under a million noisy qubits, under the same assumptions as the 2019 Gidney-Ekerå estimate of 20 million qubits and 8 hours (0.1% gate error, 1 µs surface code cycle, 10 µs reaction time) — [arXiv 2505.15917](https://arxiv.org/abs/2505.15917). Gidney also records that Chevignard et al. 2024 use 2 trillion Toffoli gates and a bit more than 0.5n logical qubits — [same](https://arxiv.org/abs/2505.15917).
- Binary-curve estimates, with exact handling of exceptional cases in point addition: [Garn, Kan, arXiv 2503.02984](https://arxiv.org/abs/2503.02984).
- Benchmark ladder: Dallaire-Demers, Doyle, Foo propose nothing-up-my-sleeve instances on y² = x³ + 7 shrinking from 256 to 6 bits and estimate a 2027-2033 window for the 256-bit instance under stated assumptions — [arXiv 2508.14011](https://arxiv.org/abs/2508.14011) (v3 dated 29 October 2026).
- A July 2026 paper formalises Shor attacks in Lean — [arXiv 2607.14082](https://arxiv.org/pdf/2607.14082).

### Inferences
- Comparing RSA-2048 with ECC-256: Cain et al. put RSA-2048 at one to two orders of magnitude longer than P-256 on the same machine — [arXiv 2603.28627](https://arxiv.org/abs/2603.28627). Gidney's under-a-week RSA figure against Babbush et al.'s minutes for ECC points the same way, although those are separate estimates on different assumptions.
- Evaluating the Luo et al. leading term at n=256 gives about 2.2·10^9 Toffoli (my arithmetic, ignoring O(n²)), so 835 qubits costs roughly 25 to 30 times the Toffolis of Babbush et al. Their abstract does not compare Toffoli counts. Treat 835 as a space-optimised point, not a dominating one.
- These estimates all assume fault-tolerance that does not exist yet, so the numbers measure theory progress, not machine progress. A 2027-2033 window is one group's assumption-laden projection.

### Gaps
- Conflict: Luo et al. cite 1,098 (Chevignard et al.) and 1,175 (Babbush et al.) as prior bests, whereas ePrint 2026/280 shows 1,193 and arXiv 2603.28846 says under 1,200. I could not reconcile these; 1,098 may refer to a different conference version or variant.
- A search snippet said the Toffoli count of Luo et al. changed across versions; only v3 was read.
- [ePrint 2026/106](https://eprint.iacr.org/2026/106.pdf) ("New Quantum Circuits for ECDLP") returned 403, so its numbers are unverified.
- Absolute counts for arXiv 2606.02235 were not on the abstract page.
- A secondary source reports a February 2026 "Pinnacle" qLDPC architecture claiming RSA-2048 under 100,000 physical qubits. I did not verify it.

## Isogeny-based cryptography: what survived SIDH, and how did the 2026 attacks change SQIsign?

### Takeaway
The biggest 2026 result in this whole survey is here: in July 2026 Wesolowski gave a heuristic p^{1/3+o(1)} time-and-memory algorithm for the supersingular isogeny problem, beating the long-standing p^{1/2} barrier. SQIsign advanced to NIST Round 3 and its 3.0 spec (1 September 2026) grew sizes by roughly a third, reportedly in response. Concrete impact is contested: one analysis says it likely beats prior attacks only at NIST Level I, and another preprint from two days ago claims the heuristic can be removed.

### Cited Findings

**SIDH break**
- Castryck-Decru: key recovery via Kani's glue-and-split theorem, using a small non-scalar endomorphism on the starting curve. The final version breaks SIKEp434 in about ten minutes on one core; the preliminary version took about an hour — [ePrint 2022/975](https://eprint.iacr.org/2022/975.pdf); [pqc-forum](https://groups.google.com/a/list.nist.gov/g/pqc-forum/c/ygqtBcCdfF4).
- Maino-Martindale: arbitrary starting curve, subexponential; applies to schemes that publish images of points under the secret isogeny, but not CSIDH, CSI-FiSh or SQIsign — [ePrint 2022/1026](https://eprint.iacr.org/2022/1026).
- Robert: classical polynomial time even with a random starting curve, published at Eurocrypt 2023 — [ePrint 2022/1038](https://eprint.iacr.org/2022/1038).

**The 2026 complexity shift**
- Wesolowski: supersingular isogeny problem in time and memory p^{1/3+o(1)}, heuristic on smoothness of certain random integers, improving on about p^{1/2}·polylog(p). The abstract flags a superpolynomial overhead hidden in the o(1) and high memory, so concrete impact is unclear. Received 20 July 2026, preprint — [ePrint 2026/1486](https://eprint.iacr.org/2026/1486).
- Udovenko: unconditional p^{2/5+o(1)} time and memory, using multivariate multipoint evaluation; extends Eisenträger et al. 2020 and Fuselier et al. 2025. All these methods look for a separable isogeny from a curve to its Galois conjugate to produce a non-scalar endomorphism. The author states it is theoretical and does not threaten schemes in practice. Received 31 July 2026 — [ePrint 2026/1575](https://eprint.iacr.org/2026/1575).
- Mamah analyses Wesolowski's algorithm and concludes it likely beats the state of the art only at NIST Level I; at higher levels memory offsets the gain over accelerated Delfs-Galbraith methods, although a highly parallel van Oorschot-Wiener variant can recover it. It also covers Grover and Tani claw-finding and includes an optimised SageMath implementation. Six revisions through 30 October 2026 — [ePrint 2026/1821](https://eprint.iacr.org/2026/1821).
- Search-snippet level only: that paper gives Wesolowski-style estimates near 2^106 time and 2^92 memory for a 256-bit case, and says the algorithm does not significantly affect group-action protocols such as CSIDH and CSI-FiSh, so impact is focused on SQIsign and the CGL hash — [PDF, not readable by my fetch tool](https://eprint.iacr.org/2026/1821.pdf).
- Ouyang, Wei, Xu claim smoothness bounds on the minimum degree δ_E of isogenies to the Frobenius conjugate make Wesolowski's attack unconditional. Received 29 October 2026, proof not read, no independent check yet — [ePrint 2026/2677](https://eprint.iacr.org/2026/2677).

**SQIsign and NIST**
- NIST IR 8610 (May 2026) advanced SQIsign with no classical or quantum polynomial-time attack on its core assumptions reported in Round 2; notes smallest combined public key and signature size, resilience to SIDH attacks because it avoids auxiliary torsion information, a move from KLPT to higher-dimensional isogenies, roughly 20 times faster signing and 6 times faster verification, 148-byte signatures at category 1, and full constant-time signing as a priority — [NIST IR 8610](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8610.pdf), §3.3 (full text read). NIST names understanding of the novel assumptions as a primary challenge — [same](https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8610.pdf), §2.2.
- Round 3 candidates announced 14 May 2026: FAEST, HAWK, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign, UOV; the phase is expected to last about two years, with a 7th conference planned for late spring or early summer 2027. NIST's page, updated 29 July 2026, says the HAWK team withdrew HAWK after Anthropic announced its AI model found a mathematical vulnerability — [NIST](https://www.nist.gov/news-events/news/2026/05/nine-candidates-advance-third-round-additional-digital-signatures-pqc). HAWK is lattice-based, so this is outside the isogeny question.
- SQIsign 3.0 (1 September 2026) sizes in bytes, public key / signature: 83/200, 129/306, 169/406 at NIST I/III/V. Raptor Lake x86-64 megacycles at Level I: keygen 32.2, sign 93.9, verify 12.1 — [sqisign.org](https://sqisign.org/).
- Old values were 65/148, 97/224, 129/292; a third-party data repository attributes the growth to Wesolowski's attack and says signing and verification got faster despite it — [PQShield nist-sigs-zoo PR #46](https://github.com/PQShield/nist-sigs-zoo/pull/46).
- Ray ports the dimension-4 SQIsignHD response to Round-3 primes: 142-byte signature, 84-byte key, 226 total versus 283, verify 120.3 versus 12.2 megacycles (9.9 times slower) — [ePrint 2026/2221](https://eprint.iacr.org/2026/2221).

**Endomorphism ring problems**
- Supersingular isogeny, EndRing and maximal order problems are claimed equivalent under probabilistic polynomial-time reductions with no unproven assumption; hard-instance existence implies average-case hardness — [ePrint 2025/271](https://eprint.iacr.org/2025/271).
- Isogeny problem is equivalent to EndRing, which reduces to OneEnd, per Page-Wesolowski and Herlédan Le Merdy-Wesolowski as cited in [ePrint 2026/1575 full text snippet](https://orbilu.uni.lu/bitstream/10993/68953/1/2026-1575.pdf).
- Given one non-scalar endomorphism α, the full ring is computable in classical time about disc(Z[α])^{1/4}, and quantum subexponential time under GRH — [Herlédan Le Merdy, Wesolowski, CiC 2025](https://cic.iacr.org/p/2/1/6).
- Chen-Petit: polynomial-time quantum algorithm for EndRing given a full-rank suborder — [EUROCRYPT 2025](https://dl.acm.org/doi/10.1007/978-3-031-91095-1_16).
- GRH-conditional embedding algorithm and reduction of oriented EndRing to vectorisation — [ePrint 2025/186](https://eprint.iacr.org/2025/186).

**PRISM and POKÉ**
- PRISM: hash-and-sign from computing large-prime-degree isogenies — [ePrint 2025/135](https://eprint.iacr.org/2025/135). Weakened-version analysis: with a weak primality test the standard-model assumption fails; Miller-Rabin is argued sufficient, with iteration counts estimated — [Cottaar, Galbraith, Maino, Trimoska, ePrint 2026/906](https://eprint.iacr.org/2026/906).
- POKÉ: PKE from isogenies of unknown degree, higher-dimensional representations, about 100 ms encryption and decryption at Level I, EUROCRYPT 2025 — [ePrint 2024/624](https://eprint.iacr.org/2024/624). The paper itself says an earlier version included insecure constructions.
- Moriya: POKÉ has weak keys. They are negligible for POKÉ-2D but a real threat to POKÉ-4D, whose repaired parameters lose its advantages — [ePrint 2026/1002](https://eprint.iacr.org/2026/1002).
- Other 2026 items: fault attacks on PRISM, POKÉ and FESTA ([ePrint 2026/1944](https://eprint.iacr.org/2026/1944)), threshold POKÉ ([ePrint 2026/2243](https://eprint.iacr.org/2026/2243.pdf)), POKÉ KEM ([ePrint 2025/1616](https://eprint.iacr.org/2025/1616.pdf)).

**CRS, CSIDH and class group actions**
- CSIDH adapts the Couveignes-Rostovtsev-Stolbunov layout to supersingular curves over a large prime field, with 64-byte keys at a conjectured AES-128 level — [ePrint 2018/383](https://eprint.iacr.org/2018/383).
- Peikert estimates CSIDH-512 key recovery at about 2^16 quantum evaluations with 2^40 bits of quantumly accessible classical memory, concluding relatively little quantum security beyond the cost of evaluating the action — [ePrint 2019/725](https://eprint.iacr.org/2019/725); earlier baseline in [Bonnetain, Schrottenloher, ePrint 2018/537](https://eprint.iacr.org/2018/537.pdf). A classical simulator of the sieve is public — [cpeikert/CollimationSieve](https://github.com/cpeikert/CollimationSieve).
- 2025 follow-up on the vectorisation problem with shifted inputs reanalyses CSIDH-512-based schemes — [ePrint 2025/376](https://eprint.iacr.org/2025/376.pdf). One 2026 preprint says estimates for CSIDH-512 range from 2^29 to 2^139 depending on cost model and that quantum security is unsettled — [arXiv 2608.22360](https://arxiv.org/pdf/2608.22360) (the search tool flagged its identifier as unverified).
- CSI-FiSh computed a record class group for a 154-digit discriminant — [ePrint 2019/498](https://eprint.iacr.org/2019/498).
- SCALLOP uses orders of large prime conductor so the class group structure is known; 35 s at CSIDH-512-equivalent and 12.5 min at CSIDH-1024-equivalent — [ePrint 2023/058](https://eprint.iacr.org/2023/058).
- PEGASIS evaluates the action for any class group element without needing class group structure, via 4-dimensional isogenies: 1.5 s at CSIDH-512, 21 s at CSIDH-2048, about 2 minutes at CSIDH-4096, in SageMath; first EGA at the two larger levels — [ePrint 2025/401](https://eprint.iacr.org/2025/401).

### Inferences
- Size growth from 65 to 83 bytes and 148 to 200 is about 28 to 35 percent, consistent with primes growing by about a third, which is what p^{1/3} instead of p^{1/2} would require if the attack were taken at face value. Whether the SQIsign team set this margin for that reason, I infer from PR #46 and did not confirm from the spec.
- The p^{1/3} result implies a shift in what counts as open: the question is no longer whether p^{1/2} is optimal but where the true exponent sits. Lower exponents would hit SQIsign and the CGL hash hardest. The snippet-level evidence above suggests the group-action setting is not touched.
- With a 2/5 unconditional bound, a 1/3 heuristic bound and a possible unconditional 1/3 two days old, expect this to move further within months. Any notes on this topic age quickly.

### Gaps
- Full text of ePrint 2026/1486, 2026/1821, 2026/2221 and the SQIsign 3.0 specification were not read, so the exact round-3 primes, the spec's security argument, and any official SQIsign team or NIST response to Wesolowski are unverified. No pqc-forum thread surfaced.
- A blog-reported tweak deadline of 14 August 2026 was not confirmed from NIST — [Project Eleven](https://www.projecteleven.com/blog/nine-schemes-advance-to-round-3-of-nists-additional-digital-signatures-process). The date also precedes the 1 September spec date.
- PEARL-SCALLOP and any class group record beyond CSI-FiSh's 154 digits were not found.
- Whether Fuselier et al. and Eisenträger et al. give the same smoothness setup as Wesolowski was not checked.

## Curve generation: CM, pairing families, embedded curves, cycles, and point counting records

### Takeaway
Point counting and CM are mature, with records dating to 2010 to 2012 and recent progress that is theoretical (unconditional quasi-linear modular polynomials). The live open problem is pairing-friendly cycles: MNT4/MNT6 remains the only known ordinary pairing-friendly 2-cycle, negative results keep accumulating, and an August 2026 paper reframes the necessary condition as a prime-pair problem with an explicit computational database and open questions.

### Cited Findings

**Point counting**
- Current listed SEA record: 7 July 2010, y² = x³ + 2718281828x + 3141592653 mod p = 16219299585·2^16612 − 1, over 5,000 digits, 8 quad-core 3.0 GHz Phenom II, about 6 weeks, 1,378 CPU days — [Sutherland, Genus 1 point-counting records](https://math.mit.edu/~drew/SEArecords.html).
- The earlier 2,500-digit record needed nearly a terabyte of precomputed modular polynomials; the 2010 work needs quadratic space and modular polynomials took under 2 percent of total time — [Sutherland, JMM abstract](https://jointmathematicsmeetings.org/meetings/national/jmm/1067-11-436.pdf).
- Kunzweiler-Robert give an unconditional CRT algorithm for Φ_ℓ in quasi-linear time via higher-dimensional embeddings and deformations of isogenies, previously heuristic (Enge), with Kieffer making the floating-point approach rigorous — [arXiv 2408.06990](https://arxiv.org/abs/2408.06990); extension to higher-level invariants in [Onuki, Uchida, Yoshizumi, arXiv 2601.17338](https://arxiv.org/abs/2601.17338).
- Elkies-prime distribution is studied in [Shparlinski, Sutherland, arXiv 1112.3390](https://arxiv.org/pdf/1112.3390) (not read in detail).

**CM and class polynomials**
- CM method demonstrated with |D| > 10^16 at q ~ 2^256 and |D| > 10^15 at q ~ 2^33220 — [Sutherland, Accelerating the CM method, arXiv 1009.1082](https://arxiv.org/abs/1009.1082).
- Enge-Sutherland: class invariants via CRT reach |D| above 10^15 — [arXiv 1001.3394](https://arxiv.org/abs/1001.3394); talk example with class number 10,034,174 at about 1.0·10^15 — [slides](https://klein.mit.edu/~drew/ants9talk.pdf).
- Leroux gives heuristic supersingular-curve algorithms for class and modular polynomials, best known complexity when p is small relative to the discriminant — [ePrint 2023/064](https://eprint.iacr.org/2023/064).
- ECPP record: repunit R(109297), 109,297 digits, with Enge's CM software, jointly with Paul Underwood; second phase 133 CPU-years and 21 months real time on 96 cores — [Enge blog](https://enge.math.u-bordeaux.fr/blog/ecpp-109297.html). Wikipedia dates submission to May 2025 — [Wikipedia](https://en.wikipedia.org/wiki/Elliptic_curve_primality). The previous 86,453-digit record involved a class polynomial for discriminant −2083578323, class number 11,920 — [FastECPP over MPI, arXiv 2404.05506](https://arxiv.org/pdf/2404.05506).

**Pairing-friendly families and NFS**
- Barbulescu-Duquesne analysed exTNFS precisely and concluded key sizes must rise for KSS16, KSS18, BN, BLS12 and BLS24 — [ePrint 2017/334](https://eprint.iacr.org/2017/334). Secondary accounts give BLS12 over 461 bits and BN over 462 bits at the 128-bit level; check against the paper. Later refinements came from Menezes-Sarkar-Singh and Guillevic-Singh — [Springer 2020](https://link.springer.com/10.1007/978-3-030-45388-6_19).

**Embedded curves and chains**
- Bandersnatch: curve over the BLS12-381 scalar field with an efficient endomorphism, 42 percent faster scalar multiplication than Jubjub, no R1CS or multi-scalar-multiplication gain — [ePrint 2021/1152](https://eprint.iacr.org/2021/1152); found by a CM search at discriminant −8 — [authors' post](https://ethresear.ch/t/introducing-bandersnatch-a-fast-elliptic-curve-built-over-the-bls12-381-scalar-field/9957). Guillevic-Masson generate more such curves, including with larger discriminant — [ePrint 2024/1737](https://eprint.iacr.org/2024/1737.pdf).
- Survey of SNARK and recursive-SNARK curves — [Aranha, El Housni, Guillevic, ePrint 2022/586](https://eprint.iacr.org/2022/586). BW6-761 forms a 2-chain with BLS12-377 — [gnark team](https://hackmd.io/@gnark).

**Cycles**
- Only known ordinary pairing-friendly 2-cycles are MNT, parameterised p = x²−x+1, q = x²+1, (k,k') = (4,6). Chiesa-Chua-Weidner rule out (5,10), (8,8), (12,12) for ordinary curves — [Costello, Korpal, arXiv 2608.03268](https://arxiv.org/pdf/2608.03268) (full text read); original [arXiv 1803.02067](https://arxiv.org/pdf/1803.02067).
- Bellés-Muñoz, Jiménez Urroz, Silva (CRYPTO 2023) compute the density of pairing-friendly cycles among all cycles — [ePrint 2022/1662](https://eprint.iacr.org/2022/1662) — and state that known families contain no pairing-friendly 2-cycles apart from MNT4-MNT6 — [slides](https://iacr.org/submit/files/slides/2023/crypto/crypto2023/167/slides.pdf). A talk lists extending their bounds to all k < 56 as a goal — [slides](https://members.loria.fr/AGuillevic/files/siam-ag23/20230713-1030-BELLES-2.pdf).
- Novotný-Sedláček: a 2-cycle containing an MNT3, Freeman or BN curve cannot be pairing-friendly; no SNARK-friendly 2-chains of reasonable size from those families except MNT4/MNT6 — [ePrint 2024/1697](https://eprint.iacr.org/2024/1697).
- Corte-Real Santos, Costello, Naehrig show dimension above 1 unlocks more cycle options (CRYPTO 2024) — [ePrint 2024/869](https://eprint.iacr.org/2024/869.pdf).
- Costello-Korpal define (k,k')-order reciprocity: ord_q(p)=k, ord_p(q)=k', a necessary condition for such cycles. They give a sieve, a database for pairs among the first 200 million primes, 2 ≤ k ≤ k' ≤ 51, in PARI/GP on a Threadripper PRO 3995WX with 128 GB. They give a toy genus-2/elliptic 2-cycle with (k,k')=(12,12) on (620461,15493), the only (12,12) pair found. Counts: (4,6) has 738 pairs in the first 100 million primes and 258 in the next; among 1,275 (k,k') pairs, 1,108 have no examples in the second block — [arXiv 2608.03268](https://arxiv.org/pdf/2608.03268). Code and data — [gkorpal/order-reciprocity](https://github.com/gkorpal/order-reciprocity).
- Their open questions: is (620461,15493) the only (12,12) pair; is any fixed (k,k') with min(k,k') > 4 infinite; is any fixed (k,k') with min > 2 empty; are there any large (at least 2^160) pairs with small (k,k') — [same](https://arxiv.org/pdf/2608.03268).

### Inferences
- Costello-Korpal's Algorithm 1 loops s from 1 to k'−1 over elements of order k' mod p, which is constant for fixed k'. On my reading that makes per-prime cost polylogarithmic after a primitive root is known, not Õ(p) as their complexity section states. Either the extracted text misleads me or the search can be pushed far beyond the 200-millionth prime (about 4.2·10^9, my estimate) on a workstation for restricted (k,k'). This needs checking before relying on it.
- Heuristically, a given p has O(1) candidates q and each passes the second order condition with probability on the order of 1/q, so the expected count over p ≤ X grows only about like log log X. Failure to find new pairs would be expected and would be weak evidence. A sieve extension is therefore cheap but low-yield in any single run, and the interesting output is data on the open questions, not a usable cycle at 2^160.
- Beating the 2010 SEA record looks feasible on modern 16-core hardware within a couple of months of runtime, assuming roughly quartic scaling and good modular polynomial code (rough estimate, not sourced). It would be a record of low mathematical value, and the memory demand is unknown.

### Gaps
- I could not confirm the widely repeated statement that no curve from any known family can be in a 2-cycle with partner embedding degree k ≤ 22. It surfaced in a search summary from one of these ePrints but the PDFs returned 403.
- No authoritative current bit-security estimate for BLS12-381 was found. Sources call it a non-conservative 128-bit choice.
- I could not determine whether Sutherland's SEA page is current; nothing newer surfaced. No newer CM record than |D| > 10^16 surfaced either, and that absence was not exhaustively checked.
- Whether higher-dimensional isogeny methods give practical point-counting improvements was not established; Robert's overview papers were not read.

## Supersingular primes, isogeny graphs, and hashing: what is proved and what is open?

### Takeaway
Infinitude of supersingular primes is settled but counting them is not, with bounds of x^{3/4} above and log log x below still standing. Unlevelled supersingular isogeny graphs are Ramanujan; with level structure the picture is still being worked out. Hashing into the supersingular graph without revealing an endomorphism remains open, and the one 2026 paper claiming a quantum solution has been withdrawn.

### Cited Findings
- Elkies: every non-CM curve over Q has infinitely many supersingular primes and π_{E,0}(x) ≪ x^{3/4} unconditionally; Serre earlier had x^{3/4} under GRH — [as summarised in Wan, Xi, arXiv 2109.14256](https://arxiv.org/pdf/2109.14256).
- Fouvry-Murty: effective unconditional lower bound, π_{E,0}(x) ≫ log log x for infinitely many x — [Canad. J. Math. 1996](https://cambridge.org/core/services/aop-cambridge-core/content/view/361802E6BB331285996AA35BA4FFE1D0/S0008414X00034076a.pdf/on-the-distribution-of-supersingular-primes.pdf). Lang-Trotter predicts order √x/log x for r = 0 — [Wan, Xi](https://arxiv.org/pdf/2109.14256).
- Recent adjacent work: abelian surfaces [Wang, arXiv 2402.12218](https://arxiv.org/pdf/2402.12218); family averages [arXiv 2604.00822](https://arxiv.org/pdf/2604.00822). Neither improves the fixed-curve bounds.
- Uniform Ramanujan bound for any prime ℓ < p/4 via Deligne — [El Baraka, Ezzouak, Bol. Soc. Paran. Mat.](https://periodicos.uem.br/ojs/index.php/BSocParanMat/article/download/76382/751375160499).
- Level structure: Codogni-Lido cover expansion and mixing as a corollary — [arXiv 2308.13913](https://arxiv.org/abs/2308.13913); Zobernig notes they treat non-backtracking walks only in a special case and builds abstract isogeny graphs with an Ihara-type determinant formula — [arXiv 2509.15214](https://arxiv.org/pdf/2509.15214). Explicit algorithms for graphs with level structure — [Colò, Kohel, arXiv 2604.00184](https://arxiv.org/pdf/2604.00184). Computational expansion study of superspecial digraphs — [Decru, Reijnders, ePrint 2026/500](https://eprint.iacr.org/2026/500).
- Spine (F_p subgraph) and diameters: [Adventures in Supersingularland, arXiv 1909.07779](https://arxiv.org/pdf/1909.07779) gives diameter data for ℓ=2; [Hedayat, Arpin, Scheidler, arXiv 2502.03613](https://arxiv.org/abs/2502.03613v1) finds graph centres behave like random (ℓ+1)-regular graphs; [Hedayat, arXiv 2607.14572](https://arxiv.org/abs/2607.14572) treats ℓ=2, p ≡ 71, 119 mod 120; [Boscardin, Spindler, ePrint 2025/1361](https://eprint.iacr.org/2025/1361) prove a diameter bound for the directed case.
- Hashing: producing hard supersingular curves without a trusted authority, and hashing to graph vertices without revealing the endomorphism ring or a path to a known one, are stated as open. Genus-2 random walks give no real advantage and may leak endomorphism information — [Booher et al., Failing to hash into supersingular isogeny graphs, ePrint 2022/518](https://eprint.iacr.org/2022/518.pdf). CGL collision resistance reduces to EndRing and breaks if started from a curve of known endomorphism ring — [AWS 2026 notes](https://swc-math.github.io/aws/2026/2026EisentraegerNotes.pdf).
- Mamah, Doliskani, Jao claimed provable quantum polynomial-time sampling and a proof of Quantum Unique Ergodicity for these graphs; v3 (21 September 2026) is a withdrawal citing errors in analysis — [arXiv 2602.02263](https://arxiv.org/abs/2602.02263). Those claims must not be relied on.

### Inferences
- The gap between log log x and x^{3/4} against the predicted √x/log x is one of the widest in the area and is a theory problem. Computation can only add evidence, not close it.
- Wesolowski and Udovenko's reliance on isogenies to Frobenius conjugates turns spine-distance questions into a cryptanalytically relevant topic. Statistics of δ_E are now directly useful, which raises the value of the graph experiments that are cheap at small p.

### Gaps
- I did not find a clean statement of a diameter conjecture attributed to Sardari, and did not read it.
- "Hash-to-curve" in the deployed sense (RFC 9380) was not investigated; only the supersingular-graph sense was.
- No confirmed 2026 positive result on hashing was found.

## Number-theoretic problems with small computational verification potential

### Takeaway
Lang-Trotter, Koblitz, Silverman-Stange aliquot cycles, elliptic Carmichael numbers and elliptic divisibility sequences are all open conjecturally and have small published numerics, so this is where a workstation is most useful. Recent activity is mostly theoretical, and I found no large published numerical tables for general curves, which is a real opening but needs a literature check before claiming novelty.

### Cited Findings

**Lang-Trotter**
- Conjecture: asymptotic count of primes with fixed Frobenius trace r (1976); r is a missing trace if the predicted constant vanishes. Jones-Vissuet classify curves over Q(t) with a missing trace — [arXiv 2108.08727](https://arxiv.org/pdf/2108.08727).
- Wan-Xi prove a conditional asymptotic for CM curves, frame a constant-comparison conjecture, say their analytic constant gives an explicit way to compute the algebraic one, and include numerics — [arXiv 2109.14256](https://arxiv.org/abs/2109.14256).
- Qin treats y² = x³ + Dx with explicit δ, Science China Math 2025 — [arXiv 2108.06292](https://arxiv.org/abs/2108.06292).
- Two-curve version and refined variants — [Akbary, Parks, arXiv 1711.00176](https://arxiv.org/pdf/1711.00176); [Baier, Zhao, arXiv 0801.3946](https://arxiv.org/abs/0801.3946).

**Koblitz**
- Zywina corrected the constant to account for dependence between orders modulo distinct primes, generalised to |E(F_p)|/t, with worked numerical examples — [arXiv 0909.5280](https://arxiv.org/abs/0909.5280).
- Open for any individual curve, known on average by Banks-Shparlinski. Lee, Mayle, Wang give an arithmetic-progression version with opposing biases — [arXiv 2408.16641](https://arxiv.org/html/2408.16641v1) (Canad. J. Math. 2025). Conditional constant determination is by Dey, Saha, Sivaraman, Vatwani — [On the refined Koblitz conjecture](https://digitalcommons.isical.ac.in/journal-articles/5504); see also [arXiv 2608.29938](https://arxiv.org/pdf/2608.29938).

**Aliquot cycles**
- Silverman-Stange conjecture about √x/(log x)^L aliquot cycles of length L for non-CM curves; CM curves with j ≠ 0 have no cycles of length above 2; amicable pairs are far more common in the CM case, with over 800 for one curve below 10^6 — [arXiv 0912.1831](https://arxiv.org/pdf/0912.1831). Jones refines the constant with tables to 10^13 — [arXiv 1212.1010](https://ar5iv.labs.arxiv.org/html/1212.1010).

**Elliptic Carmichael and pseudoprimes**
- Silverman defines Type I and Type II Korselt numbers; Type II is equivalent to elliptic Carmichael for odd n > 2; he guesses universal elliptic Carmichael numbers probably do not exist and asks for bounds on the number of reductions E mod n with n Carmichael. Examples only reach about 2·10^5 and he says he does not know why one curve has no Type I Korselt numbers below 25,000 — [arXiv 1108.3830](https://ar5iv.labs.arxiv.org/html/1108.3830).
- Infinitude: conditional in [Ekstrom, Pomerance, Thakur](https://math.dartmouth.edu/~carlp/elliptic31011.pdf); unconditional in [Wright, arXiv 1609.00231](https://arxiv.org/pdf/1609.00231).
- Products of distinct anomalous primes are Type I Korselt — [MaRDI: Anomalous primes and the elliptic Korselt criterion](https://portal.mardi4nfdi.de/wiki/Publication:2631689).

**EDS**
- Einsiedler, Everest, Ward argued from heuristics and computation that an EDS contains finitely many primes, against the Chudnovsky suggestion — [LMS JCM 2001](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E2CE61AFB56AFDBC17263F9905DED3E9/S1461157000000772a.pdf/primes-in-elliptic-divisibility-sequences.pdf). Open in general; a special case for isogeny-derived sequences was proved by Everest, Miller, Stephens — [Wikipedia](https://en.wikipedia.org/wiki/Elliptic_divisibility_sequence); [thesis](https://ueaeprints.uea.ac.uk/id/eprint/10608/1/Thesis_phuksuwan_o_2009.pdf).
- All but finitely many terms have a primitive divisor (Silverman 1988), used by Poonen towards Hilbert's tenth problem — [Wikipedia](https://en.wikipedia.org/wiki/Elliptic_divisibility_sequence).

**Anomalous primes and murmurations**
- Mazur's conjecture of infinitely many anomalous primes for y² = x³ + D is unproved; Qin derives it from Hardy-Littlewood with exceptions; count predicted around √N/log N — [UNSW seminar](https://www.unsw.edu.au/science/our-schools/maths/engage-with-us/seminars/2016/anomalous-primes-elliptic-curve-ed-y2-x3-d); [arXiv 2108.06292](https://arxiv.org/pdf/2108.06292).
- Murmurations: discovered in [He, Lee, Oliver, Pozdnyakov, arXiv 2204.10140](https://arxiv.org/html/2204.10140v2). Sawin-Sutherland give the first explicit density formula for a family of elliptic curves, ordered by height, with data to height 2^28 and a predicted prime-conductor density that lacks a supporting theorem — [arXiv 2504.12295](https://arxiv.org/abs/2504.12295). Nelson, Ross, Wassercug, Xue identify gaps in Zubrilina's proof including omitted Chebyshev factors and give repairs — [arXiv 2609.29631](https://arxiv.org/abs/2609.29631). Function-field trace statistics — [Wachs, arXiv 2603.13802](https://arxiv.org/abs/2603.13802).

### Inferences
- Rough throughput guide (my estimates, unsourced): computing a_p for one non-CM curve for all p up to about 10^12 is a modest job on 16 cores, and 10^13 is days to weeks. Each decade above that costs more than ten times, so Jones's 10^13 aliquot tables for non-CM curves can be extended by at most about one decade. CM curves are much cheaper since a_p comes from a norm equation, so they extend further.
- EDS terms grow doubly fast (log W_n quadratic in n), so primality testing runs out of reach at small index. Only very small extensions of the Einsiedler-Everest-Ward data are possible.
- I saw no large elliptic Carmichael tables, but I did not search for them specifically, and a MaRDI listing suggests counting-function papers exist. The Korselt criterion makes these numbers easy to sieve. Silverman's unexplained 25,000 gap is a concrete small question.

### Gaps
- Could not confirm whether anyone has published large-scale tables of Lang-Trotter or Koblitz constants against counts across LMFDB curves. The adelic-image work needed to compute entanglement-corrected constants, and tools like smalljac and average-polynomial-time methods, were not checked in this session. A novelty check is essential before claiming anything.
- Elliptic Wieferich and Gross's elliptic Mersenne test: only catalogue pages found ([MaRDI](https://portal.mardi4nfdi.de/wiki/Item:Q1976803)), so I cannot state what is open.
- Exact EEW numerics were not extracted.

## Ratings: (a) out of reach, (b) reproducible but nothing new, (c) plausibly new with modest computing

### Takeaway
For a single researcher with 16 cores and an NVIDIA GPU, full-size ECDLP, quantum hardware and new pairing cycles at cryptographic size are out of reach. The best targets are the suddenly reopened isogeny-exponent experiments at small p, the order-reciprocity sieve, and numerics on Koblitz, aliquot and elliptic Carmichael questions.

### Cited Findings
All facts are cited in the sections above. Ratings below are my judgments, so they sit under Inferences.

### Inferences

| Topic | Rating | Why, and the concrete first step |
|---|---|---|
| Prime-field ECDLP record above 114 bits | (a) | Needs at least about 2^57 group operations, so a cluster; one top-end card gives about 2^55.5 a year |
| Prime-field ECDLP around 100 to 110 bits | (b) | Reproducible as a benchmark, teaches implementation, no new knowledge |
| Certicom ECC2K-130 / ECCp-131 | (a) | About 5 GPU-years for ECC2K-130 at best card rates, and already being attempted in public |
| Sub-exponential prime-field ECDLP | (a) | No route known; a real result would be a major mathematical breakthrough, not a compute job |
| Experiments on Gröbner degree of regularity for prime-field factor bases | (b), edging to (c) | Small Magma/Sage runs; Petit et al.'s open questions on theory and on Semaev's original basis are concrete, but the outcome is likely more evidence, not an algorithm |
| Quantum hardware results | (a) | No machine exists |
| Quantum circuit accounting and formal verification | (c), but scope-sensitive | Public, reproducible counts and Lean verification fit modest compute. Google and IonQ withheld circuits, so stay on the verification and defensive side |
| Reconciling 2026 quantum estimates into one table (qubits versus Toffoli versus runtime) | (b) | Useful synthesis, little original content |
| Isogeny: measuring Wesolowski's algorithm at small p against Delfs-Galbraith and vOW | (c) | Best target. At p around 2^60 to 2^80, p^{1/3} is 2^20 to 2^27 memory. The crossover and o(1) overhead are the open concrete question. Start from the SageMath code in ePrint 2026/1821. Competition is intense and the area moves weekly |
| Statistics of δ_E (shortest isogeny to Frobenius conjugate) for all supersingular curves at p up to about 10^7 | (c) | Tests the smoothness heuristic and the formula in ePrint 2026/2677 directly; cheap |
| Breaking SQIsign parameters | (a) | Even optimistic estimates are near 2^106 |
| Isogeny exponent theory below 1/3 | (c) for ideas, not compute | Mathematical, and open as of this month |
| Reproducing SIDH attack on SIKEp434 | (b) | Public code runs in minutes |
| PRISM and POKÉ parameter analysis | (c) | Young schemes with weak-key and primality-test results appearing in 2026; cryptanalytic thinking matters more than compute. Implement on toy parameters only |
| SQIsign constant-time signing | (c), engineering | NIST explicitly names it as a priority; not a compute problem |
| CSIDH collimation-sieve simulations | (b) | Peikert's simulator is public; rerunning adds little |
| CSIDH quantum security, cost-model question | (c) for theory | Estimates span 2^29 to 2^139; the question is modelling |
| Class group computation beyond 154 digits | (a) | Well beyond one workstation; PEGASIS also removes the practical need |
| SEA point-counting record above 5,000 digits | (c), low value | Probably feasible in weeks to months; memory unknown; a record, not mathematics |
| CM record beyond |D| > 10^16 | (b) to (c), low value | Largely an implementation exercise |
| Finding Bandersnatch-like embedded curves | (b) | Done systematically by Guillevic-Masson |
| Order-reciprocity sieve extension | (c) | Second-best target. Public code and data; run first to check whether the Õ(p) complexity claim is an overestimate, then extend past 4.2·10^9 for chosen (k,k') |
| Proving nonexistence for specific (k,k') | (c) for theory | Questions (2) and (3) of Costello-Korpal are open and elementary-looking |
| Extending Bellés-Muñoz et al. bounds toward k < 56 | (c), status unverified | Check the [pairingfriendlycycles GitHub](https://members.loria.fr/AGuillevic/files/siam-ag23/20230713-1030-BELLES-2.pdf) reference first; may already be done |
| A non-MNT pairing-friendly cycle at 2^160 or above | (a) | Negative results keep accumulating and the search has no known construction |
| Fixed-curve supersingular prime bounds | (a) | Pure theory, untouched since the 1990s |
| Spine and diameter statistics | (b) to (c) | Cheap, but several 2025 to 2026 papers already cover it |
| Hash into supersingular graph | (a) | Open and central; the one 2026 claim was withdrawn |
| Lang-Trotter constants versus counts at scale | (c), pending novelty check | a_p up to 10^12 or 10^13 is cheap; constants need adelic images |
| Koblitz numerics, including congruence-class versions of Lee-Mayle-Wang | (c), pending novelty check | Same data pipeline, so one a_p computation serves both |
| Non-CM aliquot cycles beyond 10^13 | (b) | One decade at most |
| CM aliquot cycles and amicable pairs | (c) | Cheap a_p, and Silverman-Stange's CM behaviour differs and has small data |
| Elliptic Carmichael counts | (c), pending novelty check | Silverman's examples stop near 2·10^5; later papers not checked; easy sieve; a good first project |
| EDS primes | (b) | Term growth blocks real extension |
| Anomalous prime counts versus Mazur/Qin | (b) to (c) | Same a_p pipeline, r = 1 |
| Murmuration densities | (b) to (c) | Sawin-Sutherland has data to height 2^28; the prime-conductor case lacks a theorem |

- Suggested order: (1) elliptic Carmichael sieve, because it is fast and a clean first result; (2) shared a_p pipeline for Koblitz, Lang-Trotter and CM aliquot data; (3) order-reciprocity extension; (4) small-p isogeny experiments, the highest impact and highest competition.
- A warning on (c) ratings: I did not confirm that any of these is actually unpublished. Each needs a literature check first.

### Gaps
- The user's GPU model and memory are unknown, so throughput estimates use one top-end card from ePrint 2026/2469, which likely overstates a consumer card.
- Runtime estimates in this section are mine and rough, and none were benchmarked.
- Recent preprints in this survey are unreviewed. Ratings that depend on ePrint 2026/1486, 2026/1821 and 2026/2677 should be revisited as those papers are checked.
