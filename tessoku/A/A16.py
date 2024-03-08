N = int(input())
A = list(map(int, input().split()))
B = [10**8] + list(map(int, input().split()))

dp = [10**8]*N
dp[0] = 0
for i in range(N-1):
    a = A[i]
    b = B[i]
    dp[i+1] = min(dp[i+1], a + dp[i], b + (dp[i-1] if i > 0 else 0))
print(dp[N-1])