N, D = map(int, input().split())
X = [None]*N
Y = [None]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 0
Done = [False]*N
for i in range(D):
    maxV = 0
    maxID = -1
    for j in range(N):
        if not Done[j] and Y[j] > maxV and X[j] <= i+1:
            maxV = Y[j]
            maxID = j
    if maxID > -1:
        Done[maxID] = True
        ans += maxV
print(ans)