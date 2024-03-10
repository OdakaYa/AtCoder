S = list(input())
ans = ""
bef = -1
aft = -1
for s in S:
    if s == "|":
        if bef < 0:
            bef = 1
        else:
            aft = 1
    else:
        if bef * aft > 0:
            ans += s
print(ans)