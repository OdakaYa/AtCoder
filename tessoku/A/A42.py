N, K = map(int, input().split())
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))
X.sort()

ans = 0
for i in range(N):
    temp = []
    val = X[i][0] + K
    for j in range(i, N):
        if X[j][0] <= val:
            temp.append(X[j][1])
    temp.sort()
    n = len(temp)
    for j in range(n):
        l = j
        r = n
        val = temp[j] + K
        while r - l > 1:
            c = (l+r)//2
            if temp[c] <= val:
                l = c
            else:
                r = c
        ans = max(ans, r-j)
print(ans)