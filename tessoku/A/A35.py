N = int(input())
A = list(map(int, input().split()))

dp = [[None]*N for _ in range(N)]
for i in range(N):
    dp[0][i] = A[i]

for i in range(N-1):
    if (N-i) % 2:
        for j in range(N-1-i):
            dp[i+1][j] = min(dp[i][j], dp[i][j+1])
    else:
        for j in range(N-1-i):
            dp[i+1][j] = max(dp[i][j], dp[i][j+1])

print(dp[-1][0])