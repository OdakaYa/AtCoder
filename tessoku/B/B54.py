N = int(input())

dic = {}
for _ in range(N):
  x = int(input())
  if x in dic.keys():
    dic[x] += 1
  else:
    dic[x] = 1

ans = 0
for v in dic.values():
  ans += v*(v-1)//2
print(ans)