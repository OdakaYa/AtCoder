N = int(input())

Num = [True]*N
for i in range(1, N):
    if Num[i]:
        n = 2*i+1
        while n < N:
            Num[n] = False
            n += i+1

for i in range(1, N):
    if Num[i]:
        print(i+1)