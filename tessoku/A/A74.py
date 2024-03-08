N = int(input())
P = [
    list(map(int, input().split())) for _ in range(N)
]

list = [None]*N
for i in range(N):
    for j in range(N):
        val = P[i][j]
        if val > 0:
            list[val-1] = [i, j]

cnt = 0
for i in range(N):
    xi, yi = list[i]
    c = abs(xi + yi)
    for j in range(i):
        xj, yj = list[j]
        if xj < xi:
            c -= 1
        if yj < yi:
            c -= 1
    cnt += c

print(cnt)