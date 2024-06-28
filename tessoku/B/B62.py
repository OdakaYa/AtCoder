import sys
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

reach = [False]*N

def dfs(x, l: list):
    l.append(x+1)
    reach[x] = True
    if x == N-1:
        print(*l)
    else:
        for y in G[x]:
            if not reach[y]:
                dfs(y, l)
    l.pop()

dfs(0, [])