N = int(input())
A = list(map(int, input().split()))

stack = [None]*N
c = -1
ans = []

for i in range(N):
    while c >= 0 and A[stack[c]] <= A[i]:
        c -= 1
    ans.append(stack[c])
    c += 1
    stack[c] = i

for i in range(len(ans)):
    if ans[i] == None:
        ans[i] = -1
    else:
        ans[i] += 1
print(*ans)