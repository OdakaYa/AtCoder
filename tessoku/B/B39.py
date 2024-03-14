import heapq
N, D = map(int, input().split())
task = []
for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(task, [-y, x])

ans = 0
for i in range(D):
    maxV = 0
    maxI = 10**9
    task2 = []
    while maxI > i+1 and task:
        maxV, maxI = heapq.heappop(task)
        if maxI > i+1:
            heapq.heappush(task2, [maxV, maxI])
    task = task2 + task
    ans += maxV

print(-ans)