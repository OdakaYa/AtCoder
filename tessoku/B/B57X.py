N, K = map(int, input().split())

dp = [[None]*33334 for _ in range(31)]
for i in range(33334):
    dp[0][i] = 9*i
    a = dp[0][i]
    while a:
        dp[0][i] -= a%10
        a //= 10
for i in range(30):
    for j in range(33334):
        dp[i+1][j] = dp[i][dp[i][j]//9]

for i in range(N):
    x = i+1
    temp = i+1
    while temp:
        x -= temp%10
        temp //= 10
    cnt = K-1
    n = 0
    while cnt:
        if cnt % 2 == 1:
            x = dp[n][x//9]
        n += 1
        cnt //= 2
    print(x)