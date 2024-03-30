import sys
sys.setrecursionlimit(1000000)

X, Y = map(int, input().split())

def func(x, y, n):
    if x == 1 and y == 1:
        print(n)
        return True
    else:
        if x > y:
            func(x-y, y, n+1)
        else:
            func(x, y-x, n+1)
        print(x, y)

func(X, Y, 0)