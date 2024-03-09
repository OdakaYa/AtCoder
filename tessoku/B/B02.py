A, B = map(int, input().split())
X = [1, 2, 4, 5, 10, 20, 25, 50, 100]

for x in X:
    if A <= x and x <= B:
        print("Yes")
        break
else:
    print("No")