"""Numerical checks of consequences suggested by ABS and Koymans--Smith.

This evaluates a limiting Selmer-rank proxy distribution, not measured ranks.
It does not establish novelty or prove convergence of any arithmetic moment.
"""
from decimal import Decimal, getcontext
import json

getcontext().prec = 65
D = Decimal
J = 100
R = 24
p0 = D(1)
for j in range(J):
    p0 /= 1 + D(3) ** (-j)
probabilities = [p0]
for r in range(1, R):
    probabilities.append(probabilities[-1] * D(3) ** (1-r) / (1-D(3) ** (-r)))

mean_series = sum(1 / (D(3)**j + 1) for j in range(J))
variance = sum(D(3)**j / (D(3)**j + 1)**2 for j in range(J))
mean_distribution = sum(D(r)*p for r, p in enumerate(probabilities))
second_distribution = sum(D(r*r)*p for r, p in enumerate(probabilities))
assert abs(sum(probabilities) - 1) < D('1e-45')
assert abs(mean_series - mean_distribution) < D('1e-45')
assert abs(mean_series**2 + variance - second_distribution) < D('1e-44')

def generating_function(z):
    value = D(1)
    for j in range(J):
        value *= (1+z*D(3)**(-j))/(1+D(3)**(-j))
    return value

result = {
    'interpretation': 'Candidate upper bounds, not equalities for Mordell-Weil ranks.',
    'mean_rank_bound': str(mean_series),
    'mean_series_omitted_tail_upper_bound': str(D(3)**(-J) * D('1.5')),
    'second_rank_moment_bound': str(second_distribution),
    'conditional_root_number_plus_mean_bound': str(2*sum(D(r)*p for r,p in enumerate(probabilities) if r%2 == 0)),
    'conditional_root_number_minus_mean_bound': str(2*sum(D(r)*p for r,p in enumerate(probabilities) if r%2 == 1)),
    'exponential_moment_bounds_q_strictly_less_than_2': {
        str(q): str(generating_function(q)) for q in [D('1.25'),D('1.5'),D('1.75'),D('1.9')]
    },
    'proxy_generating_function_at_2_NOT_an_established_rank_bound': str(generating_function(D(2))),
    'proxy_probabilities_r_0_to_7': [str(p) for p in probabilities[:8]],
}
if __name__ == '__main__':
    print(json.dumps(result, indent=2))
