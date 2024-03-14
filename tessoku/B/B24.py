N = int(input())
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
B = sorted(B, key=lambda x:(x[0], -x[1]))

INF = 10**10
LIS = [INF]*N
for x, y in B:
    l = -1
    r = N
    while r - l > 1:
        c = (l + r) // 2
        if LIS[c] >= y:
            r = c
        else:
            l = c
    LIS[r] = min(y, LIS[r])

l = -1
r = N
while r - l > 1:
    c = (l + r) // 2
    if LIS[c] == INF:
        r = c
    else:
        l = c
print(r)