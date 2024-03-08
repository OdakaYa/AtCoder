H, W = map(int, input().split())

m = 10**9 + 7

def pow(n, m, MOD):
    if m == 0:
        return 1
    else:
        n %= MOD
        m %= MOD
        return (n**(m%2) * pow(n**2, m//2, MOD)) % MOD

def Comb(a, b, MOD):
    res = 1
    for i in range(b):
        res *= (a-i) * pow(i+1, MOD-2, MOD)
        res %= MOD
    return res

print(Comb(H+W-2, H-1, m))