N, Q = map(int, input().split())
S = input()

MOD = 10**9+7
accl = [None]*(N+1)
accr = [None]*(N+1)
accl[0] = 0
accr[N] = 0
b = 1
p = 37
for i in range(N):
  accl[i+1] = (accl[i] + (ord(S[i]) - ord("a") + 1)*b) % MOD
  accr[N-1-i] = (accr[N-i] + (ord(S[N-1-i]) - ord("a") + 1)*b) % MOD
  b *= p
  b %= MOD

def pow(a, b):
  if b == 0:
    return 1
  else:
    return a**(b%2) * pow((a**2)%MOD, b//2) % MOD

def inv(a):
  return pow(a, MOD-2)

for _ in range(Q):
  l, r = map(int, input().split())
  hashl = (accl[r] - accl[l-1]) * inv(pow(p, l)) % MOD
  hashr = (accr[l-1] - accr[r]) * inv(pow(p, N-r+1)) % MOD
  if hashl == hashr:
    print("Yes")
  else:
    print("No")