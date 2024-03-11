class SegTree():
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.size = size
        self.tree = [0]*(2*size)
    
    def update(self, pos, x):
        N = self.size
        self.tree[pos+N] = x
        a = (pos + N)//2
        while a > 0:
            self.tree[a] = max(self.tree[2*a], self.tree[2*a+1])
            a //= 2
    
    def get(self, l, r):
        N = self.size
        l += N
        r += N
        ans = 0
        while r - l > 0:
            if l % 2:
                ans = max(ans, self.tree[l])
                l += 1
            if r % 2:
                ans = max(ans, self.tree[r-1])
                r -= 1
            l //= 2
            r //= 2
        print(ans)

N, Q = map(int, input().split())
T = SegTree(N)
for _ in range(Q):
    q = list(input().split())
    if q[0] == "1":
        T.update(int(q[1])-1, int(q[2]))
    elif q[0] == "2":
        T.get(int(q[1])-1, int(q[2])-1)