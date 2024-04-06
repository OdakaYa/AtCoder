import queue

H, W = map(int, input().split())

A = []
for _ in range(H):
    A.append(input())

for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            Si, Sj = i, j
        if A[i][j] == "T":
            Ti, Tj = i, j

N = int(input())
P = [[0]*W for _ in range(H)]
for _ in range(N):
    r, c, e = map(int, input().split())
    P[r-1][c-1] = e

arrival = [[False]*W for _ in range(H)]

q = queue.Queue()
q.put([Si, Sj, 0])

i = 0
while not q.empty():
    px, py, e = q.get()
    arrival[px][py] = True
    if e > 1:
        if px > 0 and A[px-1][py] != "#":
            q.put([px-1, py, e-1])
            arrival[px-1][py] = True
        if py > 0 and A[px][py-1] != "#":
            q.put([px, py-1, e-1])
            arrival[px][py-1] = True
        if px < H-1 and A[px+1][py] != "#":
            q.put([px+1, py, e-1])
            arrival[px+1][py] = True
        if py < W-1 and A[px][py+1] != "#":
            q.put([px, py+1, e-1])
            arrival[px][py+1] = True
    else:
        if P[px][py] > 0:
            q.put([px, py, P[px][py]])
            P[px][py] = 0
    print(i, q.queue)
    i += 1

if arrival[Ti][Tj]:
    print("Yes")
else:
    print("No")