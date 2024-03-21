H, W = map(int ,input().split())
MOD = 10**9 + 7

def pow(a, b):
    if b == 0:
        return 1
    else:
        return (a**(b%2) * pow(a**2%MOD, b//2)) % MOD

def inv(a):
    return pow(a, MOD-2)

ans = 1
for i in range(1, H):
    ans *= W-1+i
    ans *= inv(i)
    ans %= MOD
print(ans)