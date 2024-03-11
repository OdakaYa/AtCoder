T = int(input())
N = int(input())
X = [0]*(T+1)

for _ in range(N):
    l, r = map(int, input().split())
    X[l] += 1
    X[r] -= 1

ans = 0
for i in range(T):
    ans += X[i]
    print(ans)