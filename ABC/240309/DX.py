T = input()
N = int(input())
Boxes = []

G = [{"": 0} for _ in range(N+1)]
for _ in range(N):
    temp = list(input().split())
    Boxes.append(temp)

for i in range(N):
    for k, v in G[i].items():
        G[i+1][k] = v
        for j, s in enumerate(Boxes[i]):
            if j > 0:
                if k+s in G[i].keys():
                    G[i+1][k+s] = min(v+1, G[i][k+s])
                else:
                    G[i+1][k+s] = v + 1
    print(G[i+1])

if T in G[N].keys():
    print(G[N][T])
else:
    print(-1)