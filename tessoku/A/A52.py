Q = int(input())

retsu = []
i = 0
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        retsu.append(q[1])
    elif q[0] == "2":
        print(retsu[i])
    elif q[0] == "3":
        i += 1