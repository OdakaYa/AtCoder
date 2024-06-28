import queue

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

M = []
for _ in range(R):
    M.append(list(input()))
dp = [[10**4]*C for _ in range(R)]

q = queue.Queue()
q.put([sy-1, sx-1])
dp[sy-1][sx-1] = 0
while not q.empty():
    x, y = q.get()
    tmp = dp[x][y]
    if M[x+1][y] == "." and dp[x+1][y] > tmp + 1:
        dp[x+1][y] = tmp+1
        q.put([x+1, y])
    if M[x-1][y] == "." and dp[x-1][y] > tmp + 1:
        dp[x-1][y] = tmp+1
        q.put([x-1, y])
    if M[x][y-1] == "." and dp[x][y-1] > tmp + 1:
        dp[x][y-1] = tmp+1
        q.put([x, y-1])
    if M[x][y+1] == "." and dp[x][y+1] > tmp + 1:
        dp[x][y+1] = tmp+1
        q.put([x, y+1])

print(dp[gy-1][gx-1])