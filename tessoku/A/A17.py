N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [10**10 for _ in range(N)]
root = [-1]*N
dp[0] = 0

for i in range(N-1):
    if i < N-2:
        if dp[i] + B[i] <= dp[i+2]:
            dp[i+2] = dp[i] + B[i]
            root[i+2] = i+1
    if dp[i] + A[i] <= dp[i+1]:
        dp[i+1] = dp[i] + A[i]
        root[i+1] = i+1

ans = []
pos = N
while pos != -1:
    ans.append(pos)
    pos = root[pos-1]
ans.reverse()

print(len(ans))
print(*ans)
