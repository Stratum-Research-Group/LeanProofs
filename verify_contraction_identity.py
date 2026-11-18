import itertools
import math

def s(p: bool, q: bool) -> int:
    """s(p,q) = (-1)^p [p != q]"""
    if p == q:
        return 0
    return -1 if p else 1

def X1(x: bool, y: bool, u: bool, v: bool) -> int:
    """One bit of diagonal crossing: [x = v][y = u]"""
    return 1 if (x == v and y == u) else 0

def I1(x: bool, y: bool, u: bool, v: bool) -> int:
    """One bit of uncrossed term: [x = u][y = v]"""
    return 1 if (x == u and y == v) else 0

def test_uncross_identity_single_bit():
    """Verify X1(x,y,u,v) = I1(x,y,u,v) - s(x,y)*s(u,v) for all 16 configurations."""
    for x in [False, True]:
        for y in [False, True]:
            for u in [False, True]:
                for v in [False, True]:
                    lhs = X1(x, y, u, v)
                    rhs = I1(x, y, u, v) - s(x, y) * s(u, v)
                    assert lhs == rhs, f"Mismatch at ({x},{y},{u},{v}): {lhs} != {rhs}"
    return 16

def cross_lambda(x, y, u, v):
    """Multi-bit crossing: [x = v][y = u]"""
    return 1 if (x == v and y == u) else 0

def A_i(n: int, i: int, x, y, u, v) -> int:
    """A_i component in multi-bit expansion."""
    total = 0
    indices = range(n)
    for S in itertools.combinations(indices, i):
        S_set = set(S)
        term1 = 1
        for k in S:
            term1 *= -(s(x[k], y[k]) * s(u[k], v[k]))
        term0 = 1
        for k in range(n):
            if k not in S_set:
                term0 *= I1(x[k], y[k], u[k], v[k])
        total += term1 * term0
    return total

def test_uncross_identity_lambda(n: int):
    """Verify sum_{i=0}^n A_i = cross for all inputs of length n."""
    count = 0
    domain = list(itertools.product([False, True], repeat=n))
    for x in domain:
        for y in domain:
            for u in domain:
                for v in domain:
                    lhs = sum(A_i(n, i, x, y, u, v) for i in range(n + 1))
                    rhs = cross_lambda(x, y, u, v)
                    assert lhs == rhs, f"Mismatch at lambda={n}, ({x},{y},{u},{v}): {lhs} != {rhs}"
                    count += 1
    return count

if __name__ == "__main__":
    n_bit1 = test_uncross_identity_single_bit()
    print(f"PASS: Single-bit uncrossing verified on all {n_bit1} input combinations.")
    for lam in [1, 2, 3]:
        n_eval = test_uncross_identity_lambda(lam)
        print(f"PASS: Multi-bit uncrossing identity verified for lambda={lam} on all {n_eval} combinations.")
