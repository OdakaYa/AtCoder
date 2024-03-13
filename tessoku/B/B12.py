N = int(input())

l = 0
r = N
while r - l > 0.001:
    x = (l+r)/2
    if N - x**3 - x > 0:
        l = x
    else:
        r = x
print(x)