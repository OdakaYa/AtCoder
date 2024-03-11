X = [[0]*1502 for _ in range(1502)]

N = int(input())
for _ in range(N):
    a, b, c, d = map(int, input().split())
    X[a][b] += 1
    X[a][d] -= 1
    X[c][b] -= 1
    X[c][d] += 1

acc = [[0]*1501 for _ in range(1501)]
ans = 0
for i in range(1501):
    for j in range(1501):
        tmp = X[i][j]
        if i > 0:
            tmp += acc[i-1][j]
        if j > 0:
            tmp += acc[i][j-1]
        if i > 0 and j > 0:
            tmp -= acc[i-1][j-1]
        if tmp > 0:
            ans += 1
        acc[i][j] = tmp
print(ans)