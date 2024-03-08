import sys
sys.setrecursionlimit(1 << 20)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

vis = [False]*N
vis[0] = True
path = []

def dfs(pos):
    path.append(pos+1)
    vis[pos] = True
    if pos == N-1:
        print(*path)
    else:
        for x in G[pos]:
            if not vis[x]:
                dfs(x)
        path.pop()

dfs(0)