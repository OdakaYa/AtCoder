INF = 1 << 50
class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class MaxFlow:
    def __init__(self, N):
        self.size = N
        self.g = [[] for _ in range(N)]
    
    def add_edge(self, a, b, c):
        g = self.g
        e = Edge(b, c, None)
        rev = Edge(a, 0, e)
        e.rev = rev
        g[a].append(e)
        g[b].append(rev)
    
    def dfs(self, u, goal, flow):
        if u == goal:
            return flow
        self.visited[u] = True
        for e in self.g[u]:
            v = e.to
            if self.visited[v] or e.cap == 0:
                continue
            f = self.dfs(v, goal, min(flow, e.cap))
            if f:
                e.cap -= f
                e.rev.cap += f
                return f
        return 0

    def max_flow(self, s, goal):
        res = 0
        while True:
            self.visited = [False]*self.size
            net_flow = self.dfs(s, goal, INF)
            if net_flow == 0:
                break
            res += net_flow
        return res

N, M = map(int, input().split())
g = MaxFlow(N+26)
for i in range(N):
    C = input()
    for j, c in enumerate(C):
        if c == "1":
            g.add_edge(i+1, j+N+1, 1)
    g.add_edge(0, i+1, 10)

for j in range(24):
    g.add_edge(j+N+1, N+25, M)

f = g.max_flow(0, N+25)
if f >= M*24:
    print("Yes")
else:
    print("No")