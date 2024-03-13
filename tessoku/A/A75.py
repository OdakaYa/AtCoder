N = int(input())

T = []
for _ in range(N):
    T.append(list(map(int, input().split())))
T = sorted(T, key=lambda x: x[1])
dp = [[0]*1441 for _ in range(N+1)]
for i in range(N):
    for j in range(1441):
        t, d = T[i]
        dp[i+1][j] = dp[i][j]
        if t <= j and j <= d:
            dp[i+1][j] = max(dp[i][j], dp[i][j-t] + 1)
print(max(dp[N]))