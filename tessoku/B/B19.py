N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

V_max = 1000*100+1
dp = [[W+1]*(V_max) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    wi = w[i]
    vi = v[i]
    for j in range(V_max):
        dp[i+1][j] = dp[i][j]
        if j >= vi and dp[i+1][j] > dp[i][j-vi] + wi:
            dp[i+1][j] = dp[i][j-vi] + wi

ans = 0
for i in range(V_max):
    if dp[N][i] <= W:
        ans = i
print(ans)