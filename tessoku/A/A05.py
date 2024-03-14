N, K = map(int, input().split())

ans = 0
for i in range(N):
    for j in range(N):
        if K -(i+j+2) <= N and K -(i+j+2) > 0:
            ans += 1
print(ans)