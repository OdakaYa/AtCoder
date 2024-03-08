N, A, B = map(int, input().split())

G = [None]*(N+1)
for i in range(N+1):
    if i < A:
        G[i] = 0
    elif i < B:
        if G[i-A] == 0:
            G[i] = 1
        else:
            G[i] = 0
    else:
        a, b = G[i-A], G[i-B]
        val = 0
        while val in [a, b]:
            val += 1
        G[i] = val

if G[N]:
    print("First")
else:
    print("Second")