N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

LEN = max(A)+1

G = [None]*LEN
G[0] = 0
for i in range(LEN):
    temp = []
    if i >= X:
        temp.append(G[i-X])
    if i >= Y:
        temp.append(G[i-Y])
    j = 0
    while True:
        if j not in temp:
            G[i] = j
            break
        j += 1

g = 0
for a in A:
    g ^= G[a]

if g:
    print("First")
else:
    print("Second")