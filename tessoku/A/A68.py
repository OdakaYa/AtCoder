from collections import deque
class MaximumFlow:
    def __init__(self, n):
        self.table = [[0]*n for _ in range(n)]

    def add(self, x, y, z):
        self.table[x][y] += z

    def bfs(self):
        n = len(self.table)
        level = [-1]*n
        level[0] = 0
        q = deque()
        q.append(0)
        while q:
            pos = q.popleft()
            for i in range(n):
                if self.table[pos][i] > 0 and level[i] == -1:
                    level[i] = level[pos] + 1
                    q.append(i)
        return level

    def dfs(self, x, f, l):
        n = len(self.table)
        if x == n-1:
            return f
        else:
            for i in range(n):
                if self.table[x][i] > 0 and l[x] < l[i]:
                    res = self.dfs(i, min(f, self.table[x][i]), l)
                    if res > 0:
                        self.table[x][i] -= res
                        self.table[i][x] += res
                        return res
            return 0

    def net_flow(self, l):
        return self.dfs(0, 10**9, l)
    
    def update(self, f):
        pos = 0
        l = [0]

import heapq
N, M = map(int, input().split())
T = MaximumFlow(N)

for _ in range(M):
    a, b, c = map(int, input().split())
    T.add(a-1, b-1, c)

ans = 0
L = T.bfs()
nf = T.net_flow(L)
while nf > 0:
    ans += nf
    L = T.bfs()
    nf = T.net_flow(L)
print(ans)