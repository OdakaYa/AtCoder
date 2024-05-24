def pow(a, b, m):
    if b == 0:
        return 1
    else:
        return (a**(b%2) * pow(a**2 % m, b//2, m)) % m

MOD = 10**9 + 7
H, W = map(int, input().split())
H, W = H-1, W-1
if H < W:
    H, W = W, H

ans = 1
for i in range(W):
    ans *= H+1+i
    ans *= pow(i+1, MOD-2, MOD)
    ans %= MOD
print(ans)