N = int(input())
A = list(map(int, input().split()))
B = [None]*N

new_A = []
for i in range(N):
    new_A.append([A[i], i])
new_A.sort()

ord = 1
val = new_A[0][0]
B[new_A[0][1]] = 1
for i in range(1, N):
    if new_A[i][0] > val:
        ord += 1
        val = new_A[i][0]
    B[new_A[i][1]] = ord
print(*B)