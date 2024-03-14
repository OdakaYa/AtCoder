N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False, []] for _ in range(S+1)]
dp[0][0] = True
for i, a in enumerate(A):
    for j in reversed(range(S+1)):
        if dp[j][0] and j+a <= S and not dp[j+a][0]:
            dp[j+a][0] = True
            dp[j+a][1] = dp[j][1] + [i+1]

if dp[S][0]:
    ans = dp[S][1]
    print(len(ans))
    print(*ans)
else:
    print(-1)