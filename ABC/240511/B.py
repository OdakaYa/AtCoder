N, K = map(int, input().split())
A = list(map(int, input().split()))

cap = K
cnt = 1
for a in A:
    if cap - a >= 0:
        cap -= a
    else:
        cnt += 1
        cap = K-a
print(cnt)