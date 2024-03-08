N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b)
    G[b-1].append(a)

for i in range(N):
    print(str(i+1) + ": {" + ", ".join(map(str, G[i])) + "}")