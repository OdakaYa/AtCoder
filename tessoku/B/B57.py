N, K = map(int, input().split())

memo = [[None]*34000 for _ in range(31)]
for i in range(34000):
    n = 9*i
    memo[0][i] = n
    while n:
        memo[0][i] -= n%10
        n //= 10

for i in range(30):
    for j in range(34000):
        memo[i+1][j] = memo[i][memo[i][j]//9]

for i in range(N):
    tmp = i+1
    tmp2 = i+1
    while tmp2 > 0:
        tmp -= tmp2%10
        tmp2 //= 10
    cnt = K-1
    n = 0
    while cnt:
        if cnt % 2:
            tmp = memo[n][tmp//9]
        cnt //= 2
        n += 1
    print(tmp)