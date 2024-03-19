import math
N = int(input())
pos = []
for _ in range(N):
    pos.append(list(map(int, input().split())))

def get_dist(n, m):
    return math.sqrt((pos[n][0]-pos[m][0])**2 + (pos[n][1]-pos[m][1])**2)

dp = [[10**20]*(N-1) for _ in range(2**(N-1))]
for i in range(N-1):
    dp[2**i][i] = get_dist(i, N-1)

for i in range(2**(N-1)):
    for j in range(N-1):
        if (i>>j) % 2:
            for k in range(N-1):
                if not (i>>k) % 2:
                    dp[i + 2**k][k] = min(dp[i + 2**k][k], dp[i][j] + get_dist(j, k))

ans = 10**20
for i in range(N-1):
    ans = min(ans, dp[-1][i] + get_dist(i, N-1)) 
print(ans)