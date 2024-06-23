N = int(input())
H = [10**9] + list(map(int, input().split()))

X = [None]*(N+1)
X[0] = 0
for i in range(N):
    if H[i+1] > H[i]:
        X[i+1] = X[i]
    else:
        X[i+1] = i

print(X)