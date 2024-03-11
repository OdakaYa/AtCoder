N, C = input().split()
N = int(N)
A = list(input())

dict = {"W": 0, "B": 1, "R": 2}

amari = 0
for a in A:
    amari = (amari + dict[a]) % 3

if amari == dict[C]:
    print("Yes")
else:
    print("No")