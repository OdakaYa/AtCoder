N = int(input())
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
B = sorted(B, key=lambda x:(x[0], -x[1]))

Y = [None]*N
for i in range(N):
    Y[i] = B[i][1]

LIS = [10**6]*N
for y in Y:
    l = -1
    r = N
    while r-l > 1:
        c = (l+r)//2
        if LIS[c] >= y:
            r = c
        else:
            l = c
    LIS[r] = min(y, LIS[r])
l = -1
r = N
while r - l > 1:
    c = (l+r)//2
    if LIS[c] < 10**6:
        l = c
    else:
        r = c
print(r)