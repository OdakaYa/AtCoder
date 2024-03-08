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

N, M = map(int, input().split())
tree = union_find(N)

for _ in range(M):
    a, b = map(int, input().split())
    tree.union(a-1, b-1)

if tree.par[tree.root(0)] == -N:
    print("The graph is connected.")
else:
    print("The graph is not connected.")