N = int(input())
H = list(map(int, input().split()))

dp = [10**10]*N
dp[0] = 0

for i in range(N-2):
    dp[i+1] = min(dp[i+1], dp[i] + abs(H[i] - H[i+1]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(H[i] - H[i+2]))
dp[N-1] = min(dp[N-1], dp[N-2] + abs(H[N-2] - H[N-1]))

print(dp[-1])