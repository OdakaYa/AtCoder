N = int(input())
A = list(map(int, input().split()))
A.reverse()

ans = [0]*N
for i, a in enumerate(A):
    ans[a-1] += ans[N-1-i] + 1
print(*ans)