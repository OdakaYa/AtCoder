N, W, L, R = map(int, input().split())
X = [0] + list(map(int, input().split())) + [W]
dp_sum = [0]*(N+2)
dp_sum[0] = 1
MOD = 10**9 + 7
for i in range(1, N+2):
    x = X[i]
    ll = -1
    rl = i
    while rl - ll > 1:
        cl = (ll+rl)//2
        if X[cl] < x - R:
            ll = cl
        else:
            rl = cl
    lr = -1
    rr = i
    while rr - lr > 1:
        cr = (lr+rr)//2
        if X[cr] > x - L:
            rr = cr
        else:
            lr = cr
    dp_sum[i] += dp_sum[lr] + dp_sum[i-1]
    if ll > -1:
        dp_sum[i] -= dp_sum[ll]
    dp_sum[i] %= MOD
print((dp_sum[-1] - dp_sum[-2])%MOD)