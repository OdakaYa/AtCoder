N = int(input())
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))

for i in range(N):
    max_d = 0
    max_j = -1
    x, y = P[i]
    for j in range(N):
        if i != j:
            xj, yj = P[j]
            if (x-xj)**2 + (y-yj)**2 > max_d:
                max_j = j
                max_d = (x-xj)**2 + (y-yj)**2
    print(max_j + 1)