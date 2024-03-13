T = input()
N = int(input())
Boxes = []
for _ in range(N):
    temp = list(input().split())
    Boxes.append(temp)

S = ""
d = {S: 0}
for t in T:
    S += t
    d[S] = 1000

dp = [{} for _ in range(N+1)]
dp[0] = d

for i in range(N):
    for k, v in dp[i].items():
        dp[i+1][k] = v
    for j, s in enumerate(Boxes[i]):
        if j == 0:
            continue
        for k, v in dp[i].items():
            if k+s in d.keys():
                dp[i+1][k+s] = min(dp[i+1][k+s], dp[i][k] + 1)

if dp[N][T] > 100:
    print(-1)
else:
    print(dp[N][T])