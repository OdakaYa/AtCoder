N = int(input())
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

B = sorted(B, key = lambda x:(x[0], -x[1]))

INF = 10**6
LIS = [INF]*N
for i in range(N):
    y = B[i][1]
    l = -1
    r = N
    while r - l > 1:
        c = (l+r)//2
        if LIS[c] < y:
            l = c
        else:
            r = c
    LIS[r] = y

l = -1
r = N
while r - l > 1:
    c = (l+r)//2
    if LIS[c] < 10**6:
        l = c
    else:
        r = c
print(r)