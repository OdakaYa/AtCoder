N, M = map(int, input().split())
A = list(map(int, input().split()))

X = [M]*N
for a in A:
  X[a-1] -= 1

for x in X:
  print(x)