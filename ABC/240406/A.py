S = ""
N = int(input())

for _ in range(N//3):
    S += "oox"

if N % 3 == 1:
    S += "o"
elif N % 3 == 2:
    S += "oo"

print(S)