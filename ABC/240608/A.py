N, M = map(int, input().split())
H = list(map(int, input().split()))

cnt = 0
for h in H:
    if M < h:
        break
    M -= h
    cnt += 1
print(cnt)