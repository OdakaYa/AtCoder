N, Q = map(int, input().split())
S = list(input())
MOD1 = 10**9 + 7
MOD2 = 999999937
p = 31

h1 = [None]*(N+1)
h2 = [None]*(N+1)
h1[0] = 0
h2[0] = 0
base1 = 1
base2 = 1
for i in range(N):
    h1[i+1] = (h1[i] + (ord(S[i]) - ord("a") + 1) * base1) % MOD1
    h2[i+1] = (h2[i] + (ord(S[i]) - ord("a") + 1) * base2) % MOD2
    base1 = (base1 * p) % MOD1
    base2 = (base2 * p) % MOD2

h3 = [None]*(N+1)
h4 = [None]*(N+1)
h3[N] = 0
h4[N] = 0
base3 = 1
base4 = 1
for i in range(N):
    h3[N-1-i] = (h3[N-i] + (ord(S[N-1-i]) - ord("a") + 1) * base3) % MOD1
    h4[N-1-i] = (h4[N-i] + (ord(S[N-1-i]) - ord("a") + 1) * base4) % MOD2
    base3 = (base3 * p) % MOD1
    base4 = (base4 * p) % MOD2

def pow(a, b, m):
    if b == 0:
        return 1
    else:
        return a**(b%2) * pow((a**2)%m, b//2, m) % m

def inv(n, m):
    return pow(n, m-2, m)

for _ in range(Q):
    l, r = map(int, input().split())
    val1 = (h1[r] - h1[l-1]) * inv(pow(p, l, MOD1), MOD1) % MOD1
    val3 = (h3[l-1] - h3[r]) * inv(pow(p, N-r+1, MOD1), MOD1) % MOD1
    val2 = (h2[r] - h2[l-1]) * inv(pow(p, l, MOD2), MOD2) % MOD2
    val4 = (h4[l-1] - h4[r]) * inv(pow(p, N-r+1, MOD2), MOD2) % MOD2
    if val1 == val3 and val2 == val4:
        print("Yes")
    else:
        print("No")