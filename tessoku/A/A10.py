N = int(input())
A = list(map(int, input().split()))
accL = [0]*(N+1)
accR = [0]*(N+1)
for i in range(N):
    accL[i+1] = max(accL[i], A[i])
    accR[N-i-1] = max(accR[N-i], A[N-i-1])

D = int(input())
for _ in range(D):
    l, r = map(int, input().split())
    print(max(accL[l-1], accR[r]))