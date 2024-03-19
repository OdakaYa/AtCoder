D, N = map(int, input().split())

A = [24]*D
for _ in range(N):
    l, r, h = map(int, input().split())
    for i in range(l-1, r):
        A[i] = min(A[i], h)

print(sum(A))