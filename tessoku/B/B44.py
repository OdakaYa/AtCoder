N = int(input())
A = [
  list(map(int, input().split())) for _ in range(N)
]
AA = list(range(N))

Q = int(input())
for _ in range(Q):
  q, x, y = map(int, input().split())
  if q == 1:
    AA[x-1], AA[y-1] = AA[y-1], AA[x-1]
  if q == 2:
    print(A[AA[x-1]][y-1])