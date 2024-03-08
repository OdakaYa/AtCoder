N, W = map(int, input().split())
item = []
for _ in range(N):
    item.append(list(map(int, input().split())))

dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
    w, v = item[i]
    for j in range(W):
        dp[i+1][j+1] = dp[i][j+1]
        if j+1-w >= 0:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1-w] + v)
print(dp[N][W])