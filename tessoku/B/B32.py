N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

G = [None]*(N+1)
G[0] = 0

for i in range(N):
    tmp = []
    for a in A:
        if i + 1 - a >= 0:
            tmp.append(G[i+1-a])
    j = 0
    while j in tmp:
        j += 1
    G[i+1] = j

if G[N]:
    print("First")
else:
    print("Second")