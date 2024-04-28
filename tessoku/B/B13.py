N, K = map(int, input().split())
A = list(map(int, input().split()))
acc = [0]*(N+1)
for i in range(N):
    acc[i+1] = acc[i] + A[i]

cnt = 0
for i in range(N+1):
    tmp = K+acc[i]
    l = i
    r = N+1
    while r - l > 1:
        c = (r+l)//2
        if acc[c] > tmp:
            r = c
        else:
            l = c
    cnt += l-i
print(cnt)