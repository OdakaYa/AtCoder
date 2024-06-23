N = int(input())
A = [None]*N
B = [None]*N

for i in range(N):
    A[i], B[i] = map(int, input().split())

sum_pp, sum_pm, sum_mp, sum_mm = 0, 0, 0, 0
for i in range(N):
    if A[i] + B[i] > 0:
        sum_pp += A[i] + B[i]
    else:
        sum_mm -= A[i] + B[i]
    if A[i] - B[i] > 0:
        sum_pm += A[i] - B[i]
    else:
        sum_mp -= A[i] - B[i]
print(max(sum_pp, sum_pm, sum_mp, sum_mm))