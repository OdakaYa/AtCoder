class Edge():
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class MaxFlow():
    def __init__(self, N):
        self.size = N
        self.g = [[] for _ in range(N)]
    
    def add(self, a, b, c):
        e = Edge(b, c, None)
        rev = Edge(a, 0, e)
        e.rev = rev
        self.g[a].append(e)
        self.g[b].append(rev)
    
    def dfs(self, u, goal, flw):
        if u == goal:
            return flw
        self.visited[u] = True
        for e in self.g[u]:
            v = e.to
            if self.visited[v] or e.cap == 0:
                continue
            tmp = self.dfs(e.to, goal, min(flw, e.cap))
            if tmp > 0:
                e.cap -= tmp
                e.rev.cap += tmp
                return tmp
        return 0
    
    def maxflow(self, s, goal):
        res = 0
        while True:
            self.visited = [False]*self.size
            nf = self.dfs(s, goal, 10**50)
            if nf == 0:
                break
            res += nf
        return res

N, M = map(int, input().split())
g = MaxFlow(N+26)
for i in range(N):
    C = input()
    g.add(0, i+1, 10)
    for j in range(24):
        if C[j] == "1":
            g.add(i+1, j+N+1, 1)

for j in range(24):
    g.add(j+N+1, N+25, M)

res = g.maxflow(0, N+25)
if res >= 24*M:
    print("Yes")
else:
    print("No")