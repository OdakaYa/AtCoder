N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False]*(K+1)
dp[0] = True
for a in A:
    for j in reversed(range(K+1)):
        if dp[j] and j+a <= K:
            dp[j+a] = True

if dp[K]:
    print("Yes")
else:
    print("No")