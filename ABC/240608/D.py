N = int(input())

MOD = 998244353
def get_d(n):
    res = 0
    while n > 0:
        n //= 10
        res += 1
    return res

def pow(a, b):
    if b == 0:
        return 1
    else:
        return a**(b%2) * pow(a**2%MOD, b//2) % MOD

M = get_d(N)
m = pow(10, M)
ans = 0
b = 1
for i in range(N%MOD):
    ans += b
    ans %= MOD
    b = b*m%MOD
ans = ans*N%MOD
print(ans)