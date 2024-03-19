class union_find:
    def __init__(self, n):
        self.par = [-1]*n

    def root(self, x):
        while self.par[x] > -1:
            x = self.par[x]
        return x

    def union(self, x, y):
        rootx = self.root(x)
        rooty = self.root(y)
        if rootx != rooty:
            if self.par[rootx] > self.par[rooty]:
                rootx, rooty = rooty, rootx
            self.par[rootx] += self.par[rooty]
            self.par[rooty] = rootx

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

N, M = map(int ,input().split())
G = []

for _ in range(M):
    a, b, c = map(int ,input().split())
    a -= 1
    b -= 1
    G.append([c, a, b])
G.sort()

T = union_find(N)
ans = 0
for c, a, b in G:
    if not T.is_same(a, b):
        T.union(a, b)
        ans += c
print(ans)