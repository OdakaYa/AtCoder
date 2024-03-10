H, W = map(int, input().split())
X = []
for _ in range(H):
    X.append(list(map(int, input().split())))

acc = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        acc[i+1][j+1] = acc[i][j+1] + acc[i+1][j] - acc[i][j] + X[i][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(acc[c][d] - acc[c][b-1] - acc[a-1][d] + acc[a-1][b-1])