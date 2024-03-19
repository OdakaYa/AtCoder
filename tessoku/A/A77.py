N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]
AA = [None]*(N+1)
for i in range(1, N+2):
    AA[i-1] = A[i] - A[i-1]

def cnt_part(x, yokan):
    cnt = 0
    LEN = 0
    for y in yokan:
        LEN += y
        if LEN >= x:
            LEN = 0
            cnt += 1
    return cnt

l = 0
r = L+1
while r - l > 1:
    c = (l+r)//2
    if cnt_part(c, AA) > K:
        l = c
    else:
        r = c
print(l)