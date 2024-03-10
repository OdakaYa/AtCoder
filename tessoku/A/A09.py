H, W, N = map(int, input().split())
X = [[0]*(W+1) for _ in range(H+1)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    X[c][d] += 1
    X[a-1][d] -= 1
    X[c][b-1] -=1
    X[a-1][b-1] += 1

acc = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        acc[i][j] = X[i][j]
        if i > 0:
            acc[i][j] += acc[i-1][j]
        if j > 0:
            acc[i][j] += acc[i][j-1]
        if i > 0 and j > 0:
            acc[i][j] -= acc[i-1][j-1]
for ele in acc:
    print(*ele)