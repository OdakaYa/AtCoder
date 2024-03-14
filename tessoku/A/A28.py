N = int(input())

ans = 0
for _ in range(N):
    t, a = input().split()
    a = int(a)
    if t == "+":
        ans += a
    elif t == "-":
        ans -= a
    elif t == "*":
        ans *= a
    ans %= 10000
    print(ans)