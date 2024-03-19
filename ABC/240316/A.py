S = input()
N = len(S)

for i in range(N):
    if i == 0:
        cor = "<"
    elif i == N-1:
        cor = ">"
    else:
        cor = "="
    if S[i] != cor:
        print("No")
        break
else:
    print("Yes")