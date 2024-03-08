N, L = list(map(int, input().split()))
max_E = 0
max_W = 0
for _ in range(N):
    a, b = input().split()
    if b == "E" and L - int(a) > max_E:
        max_E = L - int(a)
    elif b == "W" and int(a) > max_W:
        max_W = int(a)
print(max(max_E, max_W))