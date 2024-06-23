N, K = map(int, input().split())
S = input()
T = [None]*N
for i in range(N):
    if S[i] == "A":
        T[i] = 2
    elif S[i] == "B":
        T[i] = 3
    else:
        T[i] = 0
print(T)

acc_l = [0]*(N+1)
acc_r = [0]*(N+1)
for i in range(N):
    acc_l[i+1] = acc_l[i] + T[i]
    acc_r[N-i-1] = acc_r[N-i] + T[N-1-i]
print(acc_l)
print(acc_r)