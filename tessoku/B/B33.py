N, H, W = map(int, input().split())

g = 0
for _ in range(N):
    a, b = map(int, input().split())
    g ^= a-1
    g ^= b-1

if g:
    print("First")
else:
    print("Second")