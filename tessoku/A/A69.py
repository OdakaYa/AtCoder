class Edge():
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

class FF():
    def __init__(self, n):
        self.size = n
        self.g = [[] for _ in range(n)]
    
    def add(self, u, v, c):
        g = self.g
        e = Edge(v, c, None)
        r = Edge(u, 0, e)
        e.rev = r
        g[u].append(e)
        g[v].append(r)
    
    def dfs(self, u, goal, f):
        if u == goal:
            return f
        self.visited[u] = True
        for e in self.g[u]:
            v = e.to
            if self.visited[v] or e.cap == 0:
                continue
            new_f = self.dfs(v, goal, min(e.cap, f))
            if new_f > 0:
                e.cap -= new_f
                e.rev.cap += new_f
                return new_f
        return 0
    
    def max_flow(self, u, goal):
        res = 0
        while True:
            self.visited = [False]*self.size
            net_flow = self.dfs(u, goal, 10**10)
            if net_flow == 0:
                break
            res += net_flow
        return res

N = int(input())
G = FF(2*N+2)

for i in range(N):
    C = list(input())
    G.add(0, i+1, 1)
    for j, c in enumerate(C):
        if c == "#":
            G.add(i+1, j+N+1, 1)
    G.add(i+N+1, 2*N+1, 1)

print(G.max_flow(0, 2*N+1))