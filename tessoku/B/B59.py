N = int(input())
A = list(map(int, input().split()))

AA = []
for i, a in enumerate(A):
    AA.append([a, i])
AA.sort()

ans = 0
X = []
n = 0
for a, i in AA:
    ans += i
    l = -1
    r = n
    while r - l > 1:
        c = (r+l)//2
        if X[c] > i:
            r = c
        else:
            l = c
    ans -= r
    X.insert(r, i)
    n += 1
print(ans)