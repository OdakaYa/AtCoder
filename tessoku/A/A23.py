N, M = map(int, input().split())
A = [None]*M
for i in range(M):
    a = list(map(int, input().split()))
    tmp = 0
    for j in range(N):
        tmp += a[j] * 2**j
    A[i] = tmp
dp = [[M+1]*(1<<N) for _ in range(M+1)]
dp[0][0] = 0
for i, ai in enumerate(A):
    for j in range(2**N):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        dp[i+1][j|ai] = min(dp[i+1][j|ai], dp[i][j] + 1)
if dp[M][-1] <= M:
    print(dp[M][-1])
else:
    print(-1)