N, K = map(int, input().split())

B = []
for i in range(N):
    c, v = map(int, input().split())
    B.append([v, i, c])
B.sort(reverse=True)

kaku = [[0, -1], [N+1, -1]]
ans = 0
for v, i, col in B:
    lk = len(kaku)
    l = -1
    r = lk
    while r - l > 1:
        c = (l+r)//2
        if kaku[c][0] < i:
            l = c
        else:
            r = c
    if col != kaku[l][1] and col != kaku[r][1]:
        kaku.insert(r, [i, col])
        ans += v
    if len(kaku) == N-K+2:
        break

if len(kaku) == N-K+2:
    print(ans)
else:
    print(-1)