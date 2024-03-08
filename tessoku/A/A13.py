N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    l = i
    r = N
    x = A[i] + K
    while r - l > 1:
        c = (l+r)//2
        if A[c] > x:
            r = c
        else:
            l = c
    cnt += l-i
print(cnt)