N = int(input())

cnt = [0]*10

b = 1
l, c, r = N//10, N%10, 0
while b < N:
    for i in range(10):
        cnt[i] += b*l
        if i < c:
            cnt[i] += b
    cnt[c] += r+1
    l, c, r = l//10, l%10, r+c*b
    b *= 10

ans = 0
for i, n in enumerate(cnt):
    ans += i*n
print(ans)