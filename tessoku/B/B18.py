N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False]*(S+1)
cards = [[] for _ in range(S+1)]
dp[0] = True

for i, a in enumerate(A):
    for j in range(S+1):
        if dp[S-j] and a-j < 1:
            dp[S-j+a] = True
            cards[S-j+a] = cards[S-j] + [i+1]

if dp[-1]:
    print(len(cards[-1]))
    print(*cards[-1])
else:
    print(-1)