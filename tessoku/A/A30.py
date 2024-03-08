def pow(x, y, m):
    if y == 0:
        return 1
    else:
        return x**(y%2) * pow((x**2) % m, y//2, m) % m

def inv(x, m):
    return pow(x, m-2, m)

n, r = map(int, input().split())
MOD = 10**9 + 7

ans = 1
for i in range(r):
    ans *= (n-i) * inv(i+1, MOD) % MOD
    ans %= MOD
print(ans)