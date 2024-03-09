N = int(input())
A = list(map(int, input().split()))
A.sort()

possible = False
for i in range(N-2):
    ai = A[i]
    for j in range(i+1, N-1):
        aj = A[j]
        val = 1000-ai-aj
        l = j
        r = N
        while r - l > 1:
            c = (l+r)//2
            if A[c] <= val:
                l = c
            else:
                r = c
        if A[l] == val:
            possible = True
if possible:
    print("Yes")
else:
    print("No")