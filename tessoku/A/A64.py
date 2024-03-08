import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a-1].append([b-1, c])
    G[b-1].append([a-1, c])

dis = [-1]*N
dis[0] = 0
arr = [False]*N
q = []
heapq.heappush(q, [0, 0])

while q:
    u = heapq.heappop(q)[1]
    if not arr[u]:
        arr[u] = True
        for v, c in G[u]:
            if not arr[v]:
                dis0 = dis[u] + c
                if dis0 < dis[v] or dis[v] < 0:
                    dis[v] = dis0
                    heapq.heappush(q, [dis0, v])

for d in dis:
    print(d)