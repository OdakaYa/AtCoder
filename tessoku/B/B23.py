import math

N = int(input())
X = [None]*N
Y = [None]*N

for i in range(N):
    X[i], Y[i] = map(int, input().split())

def get(n, m):
    return math.sqrt((X[n]-X[m])**2 + (Y[n]-Y[m])**2)

INF = 10**20
dp = [[INF]*(N-1) for _ in range(2**(N-1))]
for i in range(N-1):
    dp[2**i][i] = get(i, N-1)

for i in range(2**(N-1)):
    for j in range(N-1):
        if (i>>j) % 2:
            bit = i - 2**j
            if bit > 0:
                ind = []
                k = 0
                while bit>>k:
                    if (bit>>k) % 2:
                        ind.append(k)
                    k += 1
                for l in ind:
                    tmp = dp[bit][l] + get(l, j)
                    if dp[i][j] > tmp:
                        dp[i][j] = tmp

ans = INF
for i in range(N-1):
    tmp = dp[-1][i] + get(i, N-1)
    if ans > tmp:
        ans = tmp
print(ans)