S = input()
d = {}

for s in S:
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1

ans = 0
tmp = 0
ad = 0
for v in d.values():
    ans -= v**2
    tmp += v
    if v > 1:
        ad = 1
ans += tmp**2
ans //= 2
print(ans+ad)
