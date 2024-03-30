N = int(input())

A = [None]*N
B = [None]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

sumpp = 0
sumpm = 0
summp = 0
summm = 0
for i in range(N):
    a, b = A[i], B[i]
    if a + b > 0:
        sumpp += a+b
    else:
        summm += -a-b
    if a - b > 0:
        sumpm += a-b
    else:
        summp += -a+b
ans = max(sumpp, sumpm, summp, summm)
print(ans)