N = int(input())

T = []
for _ in range(N):
    T.append(list(map(int, input().split())))
T = sorted(T, key=lambda x:(-x[0], -x[1]))

now = 86400
cnt = 0
for l, r in T:
    if r <= now:
        now = l
        cnt += 1
print(cnt)