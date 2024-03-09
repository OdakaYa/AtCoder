N, Q = map(int, input().split())
A = list(map(int, input().split()))

LEVEL = 30
dp = [[None]*N for _ in range(LEVEL)]

for j in range(N):
    dp[0][j] = A[j]-1
for i in range(LEVEL-1):
    for j in range(N):
        dp[i+1][j] = dp[i][dp[i][j]]

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    i = 0
    while y > 0:
        if y%2 == 1:
            x = dp[i][x]
        i += 1
        y //= 2
    print(x+1)