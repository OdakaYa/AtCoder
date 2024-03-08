N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

l = -1
r = N
while r - l > 1:
    c = (l+r)//2
    if A[c] >= X:
        r = c
    else:
        l = c

if r < N and A[r] == X:
    print("Yes")
else:
    print("No")