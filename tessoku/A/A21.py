N = int(input())
P = []
A = []
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p-1)
    A.append(a)

dp = [[None]*N for _ in range(N)]
for i in range(N):
    dp[0][i] = 0
for i in range(1, N):
    for j in range(N-i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
        if j < P[j] and P[j] <= i+j:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1] + A[j])
        if j <= P[i+j] and P[i+j] < i+j:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i+j])
print(dp[-1][0])