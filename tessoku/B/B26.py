N = int(input())
P = []
for i in range(2, N+1):
    for p in P:
        if i % p == 0:
            break
        elif p**2 > i:
            P.append(i)
            print(i)
            break
    else:
        P.append(i)
        print(i)