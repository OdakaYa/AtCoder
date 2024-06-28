N, K = map(int, input().split())

def get(n):
    return (n - sum(list(map(int, list(str(n))))))//9

LEVEL = 30
T = [[None]*33334 for _ in range(LEVEL)]
for i in range(33334):
    T[0][i] = get(9*i)
for i in range(1, LEVEL):
    for j in range(33334):
        T[i][j] = T[i-1][T[i-1][j]]

for i in range(N):
    ans = get(i+1)
    M = K-1
    m = 0
    while M > 0:
        if M % 2:
            ans = T[m][ans]
        M //= 2
        m += 1
    print(9*ans)