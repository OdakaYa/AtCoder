import math
N = int(input())
n = int(math.sqrt(N)) + 1

P = []
for i in range(2, n+1):
    a = True
    for p in P:
        if i % p == 0:
            a = False
    if a:
        P.append(i)

num = []
for p in P:
    x = p
    while x <= N:
        num.append(x)
        x += p

m = len(num)
num.sort()

for i in range(2, N+1):
    l = 0
    r = m-1
    while r - l > 1:
        c = (r + l) // 2
        if num[c] >= i:
            r = c
        else:
            l = c
    if i in P or not (num[l] == i or num[r] == i):
        print(i)