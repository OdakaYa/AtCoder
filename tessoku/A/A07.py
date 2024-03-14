D = int(input())
N = int(input())
A = [0]*(D+1)
for _ in range(N):
    l, r = map(int, input().split())
    A[l-1] += 1
    A[r] -= 1

ans = 0
for i in range(D):
    ans += A[i]
    print(ans)