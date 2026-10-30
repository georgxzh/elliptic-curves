# Quantitative comparison and scope of the arithmetic advance

Checked 2026-10-29. Astra located the quantitative comparisons below;
the root agent inspected the primary statements and the relevant
Chi--Lai--Tan proof. This is a targeted comparison, not a priority certificate.

## Existing rank-only bounds

| Source | Rank dependence relevant here | Uniformity and scope |
|---|---|---|
| Gross--Silverman (1995), Theorem 0.1 | (32*10^9)^r for j=0 over Q | Quasiminimal models of sufficiently large height; finitely many bounded-height sixth-free Mordell exceptions can be absorbed into an absolute constant |
| Chi--Lai--Tan (2005), Theorem 1.3 | displayed base 7^1.64=24.319844...; proof retains base 24 | Absolute prefactor for sixth-free Mordell coefficients, with no large-coefficient exception |
| Choi, arXiv:2509.03274v3, Theorem 1.1 | 4^r | Fixed quadratic-twist family, positive squarefree twist D above a base-curve-dependent threshold; prefactor absolute in that range |
| Present draft, all sixth-free Mordell coefficients | 12^r | Absolute explicit prefactor; still a research proof draft |
| Present draft, fixed d and B=dn^2 | 6^r | Prefactor depends on d, n positive cube-free |
| Present draft, squarefree B or injective-class criterion | 2^r | Absolute explicit prefactor under the stated hypotheses |

### Gross--Silverman

[Primary paper](https://msp.org/pjm/1995/167-2/pjm-v167-n2-p05-p.pdf),
Pacific J. Math. 167 (1995), 263--288, Theorem 0.1, pp. 263--264.
The Q specialization is 32*10^11*(32*10^9)^(r*delta(j)+s), for
sufficiently large height. Here delta(j) is one plus the number of
denominator primes, so j=0 gives delta=1. For ordinary integral points
s=1. Sixth-power-free Mordell equations are quasiminimal short models;
bounded coefficient height leaves finitely many exceptions. This proves
the classical qualitative rank-only assertion, but not base 12 or 2.

### Chi--Lai--Tan: retain the unrounded base

[Primary paper](https://msp.org/pjm/2005/222-2/pjm-v222-n2-p02-p.pdf),
*Integer points on elliptic curves*, Pacific J. Math. 222 (2005), 237--252.
Theorem 1.3 on p. 239 gives

    11 * 7^(1.64r + 2.27(s' + s1) + 3.7sm + 10.3md).

The proof on p. 251 first retains 24^r, then rounds it up to 7^(1.64r).
Thus base 24, rather than approximately 25, is the correct comparison
with their proof. The parameters are defined on pp. 238--239.

For our sixth-free short Mordell models, field degree d=1, splitting
degree m<=6, s'=1, and s1<=2: the model is minimal away from 2 and 3.
Potentially good reduction at every odd prime gives sm<=1. These safe
upper bounds give the absolute estimate

    #E_B(Z) <= 11 * 7^72.31 * 24^r.

Its prefactor has decimal logarithm about 62.15. The draft's
C=53,516,832*7^192 has decimal logarithm about 169.99. Therefore our
smaller exponential base does **not** imply a better numerical bound at
every rank. No finite-r superiority or best-known claim follows from this
comparison. The small-prime and Thue constants are deliberately inefficient.

### Choi and other smaller bases

[Primary preprint](https://arxiv.org/html/2509.03274v3), Theorem 1.1 and
Remark 1.2, were inspected beyond the abstract. They give an absolute,
effective prefactor for D>=D(A,B) in y^2=x^3+D^2 A x+D^3 B, with
A,B fixed and D positive squarefree. Extending to all positive D can
introduce a base-curve-dependent prefactor. This subsumes the qualitative
4^r conclusion on each fixed Mordell quadratic-twist family B=bD^3;
our local factors and uniform treatment across varying base curves remain
additional structure. It does not directly subsume the 6^r cubic-twist
family B=dn^2, the varying squarefree-B base-two claim, or the entire
sixth-free coefficient range with an absolute prefactor.

The preprint introduction also cites Chan's base 3.8 for congruent-number
curves and Helfgott--Venkatesh's base about 1.34 with discriminant-dependent
factors. These have different families or remaining coefficient dependence;
they do not give the same uniform Mordell statement by direct substitution.
Those original proofs were not audited here. Choi's work is listed as a
preprint, not assumed to have completed journal publication or review.

[Alpoge, *Note on a theorem of Professor X*](https://arxiv.org/html/2109.14328),
Theorem 1.1, was also checked directly. Its base-two estimate is stated
for degree at least five and assumes that the polynomial discriminant
is an S-unit. The remaining constant grows exponentially with |S|.
The introduction refers the elliptic case back to Alpoge--Ho. Thus this
is not an absolute base-two theorem for arbitrary Mordell coefficients;
enlarging S to contain the varying bad primes retains coefficient dependence.

## Class groups are established descent machinery

The identity Norm(y+sqrt(B))=x^3, factorization of its principal ideal,
and resulting class-group conditions are classical. We do not claim
the class-group restriction as a new descent principle.

[Jha--Majumdar--Shingavekar, *3-Selmer groups, ideal class groups and the
cube sum problem*](https://arxiv.org/html/2207.12487), Introduction and
Section 3, explicitly develops Mordell 3-isogeny Selmer/class-group
relations, including S-class groups. Its main field is Q(zeta_3) and
associated extensions; its statements are not identical to our component
map over Q(sqrt(B)). This is directly relevant prior machinery, not
evidence that no component-map formulation existed earlier.

[*Formalized Class Group Computations and Integral Points on Mordell
Elliptic Curves*](https://arxiv.org/abs/2209.15492) and its
[code repository](https://github.com/lean-forward/class-group-and-mordell-equation)
likewise document ideal descent for Mordell equations. The abstract and
repository description were inspected; no formal verification of the
present notes is claimed.

The standard quadratic-form/ideal-class correspondence is used in our
certificates only for negative fundamental discriminants -139 and -4027.
Reduced primitive positive definite forms classify the ordinary ideal
classes in these imaginary quadratic fields. Enumerating the reduced
forms, and checking prime-ideal products by compatible discriminant roots,
therefore proves the required class groups without analytic assumptions.

## What remains potentially new, and what has been ruled out

The general rank-only phenomenon is subsumed by published results. The
norm-descent restriction is also standard machinery. The remaining
candidate contribution is the explicit combination of those restrictions
with the actual quartic row-lattice count: a class-group-certified support
bound, the injective-class criterion for an absolute C*2^r estimate, and
the direct exclusion of locally admissible nonstandard lattices.

The inspected general published estimate has base 24, while the draft
has base 12. This documents a quantitative distinction from that theorem,
not a proof of priority over the whole literature. The earlier comparisons
with Sadek's marked minimal models, Cremona--Fisher--Stoll minimisation,
and Chan's cubic-twist work remain necessary before any novelty assertion.

The explicit mixed-image example B=197225 proves that simultaneous
extremality of A(H_2) and S(H_3) is possible arithmetically. It refutes
a universal strict-deficit statement without additional hypotheses; it
does not refute an asymptotic saving with an absolute prefactor or prove
that arbitrary large codes are realized. Neither unbounded Mordell ranks
nor s+h<=r is assumed anywhere in this continuation.

## Review record

Astra completed and saved the separate [bridge/averaging audit](AUDIT.md).
Its literature and arithmetic runs ended before final files were saved,
after communicating primary-source findings and the norm-descent idea.
The root agent checked and wrote this comparison, completed the ternary
proof, and supplied the independent exact arithmetic certificates. No
independent human review or complete literature-exhaustiveness claim exists.
