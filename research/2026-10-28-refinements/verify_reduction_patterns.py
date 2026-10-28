"""Finite checks of the reduction-status switching lemma; standard library.

Uses previously generated p-adic point samples, but reconstructs the target
x residue from the actual transformation coefficient. No rank computation
or complete global integral-point search is performed.
"""

from collections import Counter
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "sixth_free", HERE.parent / "2026-10-25-inert/astra/verify_sixth_free.py")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def check():
    counts = Counter()
    examples = {}
    for p in (5, 7, 11, 13, 19):
        for m in (2, 4):
            e = m // 2
            for B, x, y in prior.points(p, m):
                counts["local_point_samples"] += 1
                center = y*pow(x, -1, p) % p if x % p else 0
                for z in range(center, p**3, p):
                    counts["residues_examined"] += 1
                    F = z**4-6*x*z*z+8*y*z-3*x*x
                    derivative = 4*(z**3-3*x*z+2*y)
                    if prior.old.vp(F, p) != 2*e:
                        continue
                    unit = F // p**(2*e) % p
                    if pow(unit, (p-1)//2, p) != 1:
                        continue
                    if derivative % p**e:
                        continue
                    root = next(a for a in range(1, p) if a*a % p == unit)
                    for q_unit in (root, -root % p):
                        d = derivative // p**e * pow(4*q_unit, -1, p) % p
                        xx = (x-z*z+d*d) % p
                        assert bool(x % p) != bool(xx)
                        direction = "unit_to_singular" if x % p else "singular_to_unit"
                        counts[f"m={m},{direction}"] += 1
                        examples.setdefault(f"m={m},{direction}", {
                            "p": p, "B": B, "source_x": x, "source_y_mod_p7": y,
                            "first_row_z": z, "det_unit_mod_p": q_unit,
                            "target_x_mod_p": xx})
    for m in (2, 4):
        for direction in ("unit_to_singular", "singular_to_unit"):
            assert counts[f"m={m},{direction}"]
    return {"counts": dict(counts), "examples": examples, "counterexamples": 0,
            "scope": "Selected p-adic points, all repeated-disk residues mod p^3, both square-root signs. Tests status switching only."}


if __name__ == "__main__":
    result = json.dumps(check(), indent=2) + "\n"
    (HERE / "reduction_pattern_results.json").write_text(result)
    print(result, end="")
