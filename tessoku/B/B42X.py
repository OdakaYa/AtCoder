N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

def get_score(ca, cb):
    sum = 0
    for i in range(N):
        val = A[i] * ca + B[i] * cb
        if val > 0:
            sum += val
    return sum

ans = max(get_score(1, 1), get_score(1, -1), get_score(-1, 1), get_score(-1, -1))
print(ans)