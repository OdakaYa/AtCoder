N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

V_max = 100001
INF = 10**12
dp = [[INF]*V_max for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(V_max):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]] + w[i])

for i in range(V_max)[::-1]:
    if dp[N][i] <= W:
        print(i)
        break