N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

G = [0, 0, 1, 1, 2]

g = 0
for a in A:
    g ^= G[a%5]

if g:
    print("First")
else:
    print("Second")