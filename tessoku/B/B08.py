N = int(input())
X = [[0]*2000 for _ in range(2000)]
for _ in range(N):
    x, y = map(int, input().split())
    X[x][y] += 1

acc = [[0]*2001 for _ in range(2001)]
for i in range(2000):
    for j in range(2000):
        acc[i+1][j+1] = acc[i+1][j] + acc[i][j+1] - acc[i][j] + X[i][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(acc[c+1][d+1] - acc[a][d+1] - acc[c+1][b] + acc[a][b])