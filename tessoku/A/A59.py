class SegTree():
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.size = size
        self.tree = [0]*(2*size)
    
    def update(self, pos, x):
        pos += self.size
        self.tree[pos] = x
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos + 1]
            pos //= 2
    
    def get(self, l, r):
        s = self.size
        l += s
        r += s
        res = 0
        while r - l > 0:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                res += self.tree[r-1]
                r -= 1
            l //= 2
            r //= 2
        return res

N, Q = map(int, input().split())
A = SegTree(N)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A.update(q[1]-1, q[2])
    elif q[0] == 2:
        print(A.get(q[1]-1, q[2]-1))