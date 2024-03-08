N = int(input())
ans = (N%10) * (N%10 + 1) // 2

sum9 = 45
i = 1
while N > 10**i:
    n = (N//10**i) % 10
    if n > 0:
        ans += sum9*n + 10**i * n*(n-1)//2 + n * (N%(10**i) + 1)
    sum9 = sum9*10 + 45*(10**i)
    i += 1
print(ans)