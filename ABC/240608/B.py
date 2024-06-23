S = input()

cntA = 0
cnta = 0
for s in S:
    if ord(s) > ord("Z"):
        cnta += 1
    else:
        cntA += 1

if cnta > cntA:
    print(S.lower())
else:
    print(S.upper())