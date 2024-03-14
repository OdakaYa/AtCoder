N = int(input())

bit = [None]*10
i = 10
while i:
    i -= 1
    bit[i] = N%2
    N //= 2

ans = ""
for b in bit:
    ans += str(b)
print(ans)