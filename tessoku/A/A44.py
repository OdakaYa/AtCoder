N, Q = map(int, input().split())
ch = 1
def pos(n, c):
    if c > 0:
        return n
    else:
        return N - 1 - n

A = list(range(1, N+1))
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        x, y = int(q[1])-1, int(q[2])
        A[pos(x, ch)] = y
    if q[0] == "2":
        ch *= -1
    if q[0] == "3":
        x = int(q[1]) - 1
        print(A[pos(x, ch)])