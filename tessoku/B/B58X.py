N, L, R = map(int, input().split())
X = list(map(int, input().split()))

dp = [None]*N
dp[0] = 0
for i in range(1, N):
    l = -1
    r = i
    val = X[i] - R
    while r - l > 1:
        c = (l+r) // 2
        if val <= X[c]:
            r = c
        else:
            l = c
    m = N
    j = r
    while X[j] <= X[i] - L:
        if m > dp[j]:
            m = dp[j]
        j += 1
    dp[i] = m + 1

print(dp[N-1])