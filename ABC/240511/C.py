N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = sum(A)*(N-1)
for i, a in enumerate(A):
    l = i
    r = N
    while r - l > 1:
        c = (l+r)//2
        if A[c] + a < 10**8:
            l = c
        else:
            r = c
    ans -= 10**8 * (N-r)
print(ans)