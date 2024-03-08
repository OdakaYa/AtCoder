N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

dp = [False]*(K+1)

dp[0] = True
for i in range(N):
    for j in range(K+1):
        if dp[K-j] and (K-j)+A[i] <= K:
            dp[(K-j)+A[i]] = True

if dp[K]:
    print("Yes")
else:
    print("No")