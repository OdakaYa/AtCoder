Q = int(input())
stack = [None]*Q
now = -1

for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        now += 1
        stack[now] = q[1]
    elif q[0] == "2":
        print(stack[now])
    elif q[0] == "3":
        now -= 1