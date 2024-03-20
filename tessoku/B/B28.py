N = int(input())

dp = [None]*N
dp[0] = 1
dp[1] = 1
MOD = 10**9+7
for i in range(N-2):
    dp[i+2] = (dp[i+1] + dp[i]) % MOD
print(dp[-1])