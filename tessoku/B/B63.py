import queue

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sx, sy = sy-1, sx-1
gx, gy = gy-1, gx-1

M = []
for _ in range(R):
    M.append(input())

Steps = [[-1]*C for _ in range(R)]

q = queue.Queue()
Steps[sx][sy] = 0
q.put([sx, sy, Steps[sx][sy]])
while not q.empty():
    x, y, s = q.get()
    if M[x-1][y] == "." and Steps[x-1][y] < 0:
        Steps[x-1][y] = s+1
        q.put([x-1, y, s+1])
    if M[x+1][y] == "." and Steps[x+1][y] < 0:
        Steps[x+1][y] = s+1
        q.put([x+1, y, s+1])
    if M[x][y-1] == "." and Steps[x][y-1] < 0:
        Steps[x][y-1] = s+1
        q.put([x, y-1, s+1])
    if M[x][y+1] == "." and Steps[x][y+1] < 0:
        Steps[x][y+1] = s+1
        q.put([x, y+1, s+1])

print(Steps[gx][gy])