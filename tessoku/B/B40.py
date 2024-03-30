N = int(input())
A = list(map(int, input().split()))
A = list(map(lambda x: x%100, A))

amari100 = [0]*100
for a in A:
    amari100[a] += 1

ans = (amari100[0]*(amari100[0]-1) + amari100[50]*(amari100[50]-1))//2
for i in range(1, 50):
    ans += amari100[i]*amari100[(100-i)%100]
print(ans)