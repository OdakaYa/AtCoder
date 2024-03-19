N = int(input())
A = list(map(int, input().split()))
d = {}
for a in A:
    if a not in d.keys():
        d[a] = 1
    else:
        d[a] += 1

ans = 0
for v in d.values():
    ans += v*(v-1)*(v-2)//6
print(ans)