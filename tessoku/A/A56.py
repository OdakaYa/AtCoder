N, Q = map(int, input().split())
S = input()
T = len(S)

H1 = [None]*(T+1)
H1[0] = 0

MOD = 10**9+7
p1 = 31
b1 = 1
for i in range(T):
    H1[i+1] = (H1[i] + (ord(S[i]) - ord("a") + 1)*b1) % MOD
    b1 *= p1
    b1 %= MOD

"""def pow(a, b):
    if b == 0:
        return 1
    else:
        return a**(b%2) * pow((a**2) % MOD, b//2) % MOD"""

def inv(a):
    return pow(a, MOD-2, MOD)

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    if ((H1[b] - H1[a-1]) * inv(pow(p1, a-1, MOD))) % MOD == ((H1[d] - H1[c-1]) * inv(pow(p1, c-1, MOD))) % MOD:
        print("Yes")
    else:
        print("No")