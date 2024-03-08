H, W = map(int, input().split())
C = [
    input() for _ in range(H)
]

acc = [[0]*(W+1) for _ in range(H+1)]
acc[1][1] = 1

for i in range(H):
    for j in range(W):
        if i != 0 or j != 0:
            acc[i+1][j+1] = (C[i][j] == ".") * (acc[i][j+1] + acc[i+1][j])

print(acc[H][W])