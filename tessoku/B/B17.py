N = int(input())
H = list(map(int, input().split()))

dp = [10**10]*N
root = [-1]*N
dp[0] = 0

for i in range(N-2):
    if dp[i+1] > dp[i] + abs(H[i] - H[i+1]):
        dp[i+1] = dp[i] + abs(H[i] - H[i+1])
        root[i+1] = i
    if dp[i+2] > dp[i] + abs(H[i] - H[i+2]):
        dp[i+2] = dp[i] + abs(H[i] - H[i+2])
        root[i+2] = i
if dp[N-1] > dp[N-2] + abs(H[N-2] - H[N-1]):
    dp[N-1] = dp[N-2] + abs(H[N-2] - H[N-1])
    root[N-1] = N-2

ans = []
pos = N-1
while pos != -1:
    ans.append(pos+1)
    pos = root[pos]
ans.reverse()
print(len(ans))
print(*ans)