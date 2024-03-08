N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 10**9
while r - l > 1:
    c = (l+r)//2
    temp = 0
    for a in A:
        temp += c//a
    if temp >= K:
        r = c
    else:
        l = c
print(r)