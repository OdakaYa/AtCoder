N = int(input())
A = list(map(int, input().split()))

B = [None]*N
B[N-1] = 0
for i in range(1, N):
    B[N-1-i] = B[N-i] + 10**len(str(A[N-i]))

ans = 0
for i, a in enumerate(A):
    ans += B[i]*a
    ans += a*i
    ans %= 998244353
print(ans)