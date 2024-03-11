N = int(input())
A = list(map(int, input().split()))
A.sort()

Q = int(input())
for _ in range(Q):
    x = int(input())
    l = -1
    r = N
    while r - l > 1:
        c = (r+l)//2
        if A[c] < x:
            l = c
        else:
            r = c
    print(r)