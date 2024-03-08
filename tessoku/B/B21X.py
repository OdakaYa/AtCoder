N = int(input())
S = input()

if N == 1:
    print(1)
else:
    dp = [[None]*N for _ in range(N)]
    for i in range(N):
        dp[0][i] = 1
        if i != N-1 and S[i] == S[i+1]:
            dp[1][i] = 2
        else:
            dp[1][i] = 1
    if N >= 3:
        for LEN in range(2, N):
            for i in range(N-LEN):
                if S[i] == S[i+LEN]:
                    dp[LEN][i] = dp[LEN-2][i+1] + 2
                else:
                    dp[LEN][i] = max(dp[LEN-1][i], dp[LEN-1][i+1])
    print(dp[N-1][0])