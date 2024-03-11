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
            self.tree[a] = self.tree[2*a] + self.tree[2*a+1]
            a //= 2
    
    def get(self, l, r):
        d = r-l
        N = self.size
        l += N
        r += N
        ans = 0
        while r - l > 0:
            if l % 2:
                ans += self.tree[l]
                l += 1
            if r % 2:
                ans += self.tree[r-1]
                r -= 1
            l //= 2
            r //= 2
        if ans*2 > d:
            print("win")
        elif ans*2 < d:
            print("lose")
        else:
            print("draw")

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
T = SegTree(N)
for i, a in enumerate(A):
    T.update(i, a)
for _ in range(Q):
    l, r = map(int, input().split())
    T.get(l-1, r)