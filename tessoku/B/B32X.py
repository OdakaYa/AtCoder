N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [None]*(N+1)

for i in range(N+1):
    g = []
    for a in A:
        if a <= i:
            g.append(dp[i-a])
    j = 0
    while j in g:
        j += 1
    dp[i] = j

if dp[N]:
    print("First")
else:
    print("Second")