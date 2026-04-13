import sys
from math import gcd
input = sys.stdin.readline

def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y

def solve_linear_congruence(a, b, m):
    # ax ≡ b (mod m), returns (x0, mod) or None
    g = gcd(a, m)
    if b % g != 0:
        return None
    a, b, m = a // g, b // g, m // g
    _, inv, _ = ext_gcd(a, m)
    x0 = (b * inv) % m
    return x0, m

def crt(r1, m1, r2, m2):
    # x ≡ r1 (mod m1), x ≡ r2 (mod m2)
    g = gcd(m1, m2)
    if (r2 - r1) % g != 0:
        return None
    lcm = m1 // g * m2
    _, inv, _ = ext_gcd(m1 // g, m2 // g)
    diff = (r2 - r1) // g
    x0 = (r1 + m1 * (diff * inv % (m2 // g))) % lcm
    return x0, lcm

T = int(input())
for _ in range(T):
    K, N, M, P, Q = map(int, input().split())
    asteroids = []
    for _ in range(K):
        x, y = map(int, input().split())
        asteroids.append((x, y))
    
    x0, y0 = asteroids[0]
    best_t = None
    best_idx = None
    
    for i in range(1, K):
        ax, ay = asteroids[i]
        dx = (ax - x0) % N
        dy = (ay - y0) % M
        
        # t*Q ≡ dx (mod N)
        res_x = solve_linear_congruence(Q, dx, N)
        # t*P ≡ dy (mod M)
        res_y = solve_linear_congruence(P, dy, M)
        
        if res_x is None or res_y is None:
            continue
        
        tx, mx = res_x
        ty, my = res_y
        
        combined = crt(tx, mx, ty, my)
        if combined is None:
            continue
        
        t, mod = combined
        if t == 0:
            t = mod  # must be t > 0
        
        if best_t is None or t < best_t:
            best_t = t
            best_idx = i
    
    # Also check asteroid 0: laser returns to start after full cycle
    # The cycle length is lcm(N/gcd(Q,N), M/gcd(P,M))
    from math import lcm
    cycle = lcm(N // gcd(Q, N), M // gcd(P, M))
    
    if best_t is None or cycle <= best_t:
        print(0)
    else:
        print(best_idx)