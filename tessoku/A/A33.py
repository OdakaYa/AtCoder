N = int(input())
A = list(map(int, input().split()))
L = max(A)

G = list(range(L+1))

tmp = 0
for a in A:
    tmp ^= a

if tmp:
    print("First")
else:
    print("Second")