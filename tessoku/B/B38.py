N = int(input())
S = input()

Hl = [1]*N
Hr = [1]*N
for i in range(N-1):
    if S[i] == "A":
        Hl[i+1] = Hl[i] + 1
    if S[N-2-i] == "B":
        Hr[N-2-i] = Hr[N-1-i] + 1

ans = 0
for i in range(N):
    ans += max(Hl[i], Hr[i])
print(ans)