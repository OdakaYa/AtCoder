import heapq
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a-1].append([b-1, c])
    G[b-1].append([a-1, c])

dist = [10**10]*N
visited = [False]*N
prev = [-1]*N

q = []
heapq.heappush(q, [0, 0])
dist[0] = 0
while q:
    u = heapq.heappop(q)[1]
    if not visited[u]:
        visited[u] = True
        for v, c in G[u]:
            if not visited[v]:
                tmp = dist[u] + c
                if tmp < dist[v]:
                    dist[v] = tmp
                    heapq.heappush(q, [tmp, v])
                    prev[v] = u

def dfs(x, path):
    path.append(x+1)
    if x == 0:
        path.reverse()
        print(*path)
    else:
        dfs(prev[x], path)

dfs(N-1, [])