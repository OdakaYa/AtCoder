N, K = map(int, input().split())
A = list(map(int, input().split()))

Al = [0]*(N+1)
for i in range(N):
    Al[i+1] = Al[i] + A[i]

ans = 0
val = K
for i in range(N):
    l = -1
    r = N+1
    while r - l > 1:
        c = (r+l)//2
        if Al[c] > val:
            r = c
        else:
            l = c
    ans += l-i
    val += A[i]
print(ans)