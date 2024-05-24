N = int(input())
H = list(map(int, input().split()))

h = H[0]
for i in range(N):
    if H[i] > h:
        print(i+1)
        break
else:
    print(-1)