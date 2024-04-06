class seg():
    def __init__(self, n):
        LEN = 1
        while LEN < n:
            LEN *= 2
        self.L = LEN
        self.Tree = [10**9]*(2*LEN)

    def update(self, pos, x):
        pos += self.L
        self.Tree[pos] = x
        pos //= 2
        while pos > 0:
            self.Tree[pos] = min(self.Tree[2*pos], self.Tree[2*pos + 1])
            pos //= 2
    
    def get(self, l, r):
        res = 10**9
        l += self.L
        r += self.L
        while r - l > 0:
            if l % 2:
                res = min(self.Tree[l], res)
                l += 1
            if r % 2:
                res = min(self.Tree[r-1], res)
                r -= 1
            l //= 2
            r //= 2
        return res

N, L, R = map(int, input().split())
X = list(map(int, input().split()))

T = seg(N)
T.update(0, 0)
for i in range(1, N):
    l1 = -1
    r1 = N
    val = X[i] - R
    while r1 - l1 > 1:
        c = (r1+l1)//2
        if X[c] < val:
            l1 = c
        else:
            r1 = c
    l2 = -1
    r2 = N
    val = X[i] - L
    while r2 - l2 > 1:
        c = (r2+l2)//2
        if X[c] > val:
            r2 = c
        else:
            l2 = c
    tmp = T.get(r1, r2)
    T.update(i, tmp+1)
print(T.Tree[T.L + N-1])