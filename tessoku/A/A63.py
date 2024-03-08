import queue

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dis = [-1]*N
dis[0] = 0

q = queue.Queue()
q.put(0)
while not q.empty():
    u = q.get()
    for v in G[u]:
        if dis[v] == -1:
            dis[v] = dis[u] + 1
            q.put(v)

for d in dis:
    print(d)