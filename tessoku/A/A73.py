import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    G[a-1].append([b-1, 100000*c-d])
    G[b-1].append([a-1, 100000*c-d])

dist = [10**10]*N
dist[0] = 0
visited = [False]*N
q = [[0, 0]]
while q:
    u = heapq.heappop(q)[1]
    if not visited[u]:
        for v, c in G[u]:
            if not visited[v]:
                tmp = dist[u] + c
                if tmp < dist[v]:
                    dist[v] = tmp
                    heapq.heappush(q, [tmp, v])
    visited[u] = True

ans1 = (dist[N-1]+99999)//100000
ans2 = ans1*100000 - dist[N-1]
print(ans1, ans2)