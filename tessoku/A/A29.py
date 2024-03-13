a, b = map(int, input().split())

def pow(n, m, MOD):
    if m == 0:
        return 1
    else:
        return n ** (m%2) * pow(n**2 % MOD, m//2, MOD) % MOD

print(pow(a, b, 10**9 + 7))