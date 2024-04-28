N, M = map(int, input().split())

G = []
for _ in range(M):
    a, b, c = map(int, input().split())
    G.append([c, a-1, b-1])

class UF():
    def __init__(self, n):
        self.par = [-1]*n
    
    def root(self, x):
        res = x
        while self.par[res] > -1:
            res = self.par[res]
        return res
    
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx > ry:
            ry, rx = rx, ry
        self.par[rx] += self.par[ry]
        self.par[ry] = rx
    
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

G.sort(reverse=True)
T = UF(N)
ans = 0
for c, u, v in G:
    if not T.is_same(u, v):
        ans += c
        T.union(u, v)
print(ans)