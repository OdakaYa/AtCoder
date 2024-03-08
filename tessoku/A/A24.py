N = int(input())
A = list(map(int, input().split()))
LIS = [None]*N

for a in A:
    l = -1
    r = N
    while r - l > 1:
        c = (l+r) // 2
        if LIS[c] == None or LIS[c] > a-1:
            r = c
        else:
            l = c
    
    LIS[r] = a

l = -1
r = N
while r - l > 1:
    c = (l+r) // 2
    if LIS[c] == None:
        r = c
    else:
        l = c
print(r)