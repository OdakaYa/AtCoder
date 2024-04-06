N = int(input())

d = {}
for _ in range(N):
    a, c = map(int, input().split())
    if c not in d.keys():
        d[c] = a
    else:
        d[c] = min(d[c], a)

ans = 0
for v in d.values():
    if ans < v:
        ans = v
print(ans)