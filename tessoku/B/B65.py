import sys
sys.setrecursionlimit(1 << 30)  # 再帰上限をなくす

N, T = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
rank = [0]*N

def dfs(par, i):
    for j in G[i]:
        if j != par:
            r = dfs(i, j) + 1
            if r > rank[i]:
                rank[i] = r
    return rank[i]

dfs(-100, T-1)
print(*rank)