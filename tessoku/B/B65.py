import sys
sys.setrecursionlimit(1000000)

N, T = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False]*N

ans = [-1]*N
def dfs(x):
    visited[x] = True
    ans[x] = -1
    for y in G[x]:
        if not visited[y]:
            dfs(y)
            tmp = ans[y]
            if tmp > ans[x]:
                ans[x] = tmp
    ans[x] += 1

dfs(T-1)
print(*ans)