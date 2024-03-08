import heapq
Q = int(input())
que = []

for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        x = int(q[1])
        heapq.heappush(que, x)
    if q[0] == "2":
        print(min(que))
    if q[0] == "3":
        heapq.heappop(que)