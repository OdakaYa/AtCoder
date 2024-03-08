Q = int(input())
for _ in range(Q):
    x = int(input())
    i = 2
    while i**2 < x+1:
        if not x % i:
            print("No")
            break
        i += 1
    else:
        print("Yes")