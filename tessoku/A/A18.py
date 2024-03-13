N, S = map(int, input().split())
A = list(map(int, input().split()))

M = 10000
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][0] = True

for i, a in enumerate(A):
    for j in range(M+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j+a <= M:
                dp[i+1][j+a] = True
if dp[N][S]:
    print("Yes")
else:
    print("No")