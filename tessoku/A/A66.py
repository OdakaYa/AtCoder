class UF:
    def __init__(self, n):
        self.par = [-1]*n
    
    def root(self, x):
        while self.par[x] > -1:
            x = self.par[x]
        return x
    
    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx != ry:
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
    
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

N, Q = map(int, input().split())
tree = UF(N)
for _ in range(Q):
    q, u, v = map(int, input().split())
    if q == 1:
        tree.union(u-1, v-1)
    if q == 2:
        if tree.is_same(u-1, v-1):
            print("Yes")
        else:
            print("No")