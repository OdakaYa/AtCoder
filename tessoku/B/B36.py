N, K = map(int, input().split())

S = input()
cnt1 = 0
for s in S:
    if int(s) == 1:
        cnt1 += 1

if (cnt1 - K) % 2:
    print("No")
else:
    print("Yes")