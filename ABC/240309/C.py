N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

L = int(input())
C = list(map(int, input().split()))

Q = int(input())
X = list(map(int, input().split()))

AB = []
for a in A:
    for b in B:
        AB.append(a+b)
AB = list(set(AB))
AB.sort()

ABC = []
for a in AB:
    for b in C:
        ABC.append(a+b)
ABC = list(set(ABC))
ABC.sort()
LEN = len(ABC)

for x in X:
    val = x
    l = -1
    r = LEN
    while r - l > 1:
        c = (r+l)//2
        if ABC[c] <= val:
            l = c
        else:
            r = c
    if ABC[l] == val:
        print("Yes")
    else:
        print("No")