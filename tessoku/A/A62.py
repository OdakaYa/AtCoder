from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

arr = [False]*N
arr[0] = True

q = deque()
q.append(0)
while q:
    u = q.popleft()
    for v in G[u]:
        if not arr[v]:
            arr[v] = True
            q.append(v)

ans = "The graph is connected."
for a in arr:
    if not a:
        ans = "The graph is not connected."
print(ans)