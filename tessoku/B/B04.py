N = int(input())
N = list(reversed(str(N)))

ans = 0
for i, n in enumerate(N):
    ans += int(n) * (2**i)
print(ans)