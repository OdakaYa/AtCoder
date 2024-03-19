N = int(input())
S = input()

dp = [[None]*N for _ in range(N+1)]

for i in range(N):
    dp[0][i] = 0
    dp[1][i] = 1
for i in range(2, N+1):
    for j in range(N-i+1):
        if S[j] == S[i+j-1]:
            dp[i][j] = dp[i-2][j+1] + 2
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j+1])
print(dp[-1][0])