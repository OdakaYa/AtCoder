S = input()
T = input()

N = len(S)
M = len(T)

INF = 10**7
dp = [[INF]*(M+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        if i == 0 or j == 0:
            dp[i][j] = max(i, j)
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)

print(dp[N][M])