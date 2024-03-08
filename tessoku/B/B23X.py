import math
N = int(input())
pos = []
for _ in range(N):
    pos.append(list(map(int, input().split())))

dp = [[10**15]*(N-1) for _ in range(2**(N-1))]

for i in range(N-1):
    dp[2**i][i] = math.sqrt((pos[N-1][0] - pos[i][0])**2 + (pos[N-1][1] - pos[i][1])**2)
for i in range(2**(N-1)):
    for j in range(N-1):
        if (i >> j) % 2:
            for k in range(N-1):
                if not ((i >> k) % 2):
                    dis = math.sqrt((pos[j][0] - pos[k][0])**2 + (pos[j][1] - pos[k][1])**2)
                    dp[i+2**k][k] = min(dp[i+2**k][k], dp[i][j] + dis)

ans = 10**15
for i in range(N-1):
    temp = dp[-1][i] + math.sqrt((pos[N-1][0] - pos[i][0])**2 + (pos[N-1][1] - pos[i][1])**2)
    if ans > temp:
        ans = temp
print(ans)