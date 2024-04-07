import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False]*N

def dfs(fr, g, path):
    path.append(fr+1)
    visited[fr] = True
    if fr == g:
        print(*path)
    else:
        for x in G[fr]:
            if not visited[x]:
                dfs(x, g, path)
    path.pop(-1)

dfs(0, N-1, [])