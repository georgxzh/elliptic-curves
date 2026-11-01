#!/usr/bin/env python3
"""Check prime coverage and optional agreement with an earlier binary run."""
import hashlib
import json
import sys
from pathlib import Path
import numpy as np
from analyze_law import REC


def main(path, limit, baseline=None):
    data = Path(path).read_bytes()
    assert len(data) % REC.itemsize == 0
    records = np.frombuffer(data, dtype=REC)
    sieve = np.ones(limit+1, dtype=bool)
    sieve[:2] = False
    for q in range(2, int(limit**.5)+1):
        if sieve[q]: sieve[q*q::q] = False
    primes = np.flatnonzero(sieve)
    expected = primes[(primes >= 7) & (primes % 3 == 1)]
    assert np.array_equal(expected, records['p'])
    result = dict(limit=limit,records=len(records),last_prime=int(records['p'][-1]),
                  bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                  full_prime_coverage=True)
    if baseline:
        old = Path(baseline).read_bytes()
        assert data[:len(old)] == old
        result['bitwise_equal_prefix_records'] = len(old)//REC.itemsize
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main(sys.argv[1],int(sys.argv[2]),sys.argv[3] if len(sys.argv)>3 else None)
