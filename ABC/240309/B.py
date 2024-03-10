a = -1
ans = []
while a != 0:
    a = int(input())
    ans.append(a)

N = len(ans)
for i in range(N):
    print(ans[N-1-i])