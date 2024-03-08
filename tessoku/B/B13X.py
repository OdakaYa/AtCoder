N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    sum = 0
    j = i
    while j < N and sum + A[j] <= K:
        sum += A[j]
        cnt += 1
        j += 1
print(cnt)