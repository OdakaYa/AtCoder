N, M = map(int, input().split())
E = []
for _ in range(M):
    E.append(list(map(int, input().split())))

Q = int(input())
Queries = []
for _ in range(Q):
    Queries.append(list(map(int, input().split())))

avail = [True]*M
for q in Queries:
    if q[0] == 1:
        avail[q[1]-1] = False

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
uf = union_find(N)
for i in range(M):
    if avail[i]:
        uf.union(E[i][0]-1, E[i][1]-1)
ans = []

for q in reversed(Queries):
    if q[0] == 1:
        x = q[1]-1
        uf.union(E[x][0]-1, E[x][1]-1)
    elif q[0] == 2:
        if uf.is_same(q[1]-1, q[2]-1):
            ans.append("Yes")
        else:
            ans.append("No")

for a in reversed(ans):
    print(a)