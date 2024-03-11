Q = int(input())

dict = {}
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        dict[q[1]] = q[2]
    elif q[0] == "2":
        print(dict[q[1]])