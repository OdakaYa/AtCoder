import queue

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = []
for _ in range(M):
    x, y, z = map(int, input().split())
    X.append((2**x + 2**y + 2**z)//2)
a = 0
for i in range(N):
    a += A[i] * 2**i

dp = [-1]*(2**N)
dp[a] = 0
q = queue.Queue()
q.put(a)
while not q.empty():
    pos = q.get()
    for x in X:
        if dp[x^pos] == -1:
            dp[x^pos] = dp[pos] + 1
            q.put(x^pos)
print(dp[-1])