A, B = map(int, input().split())

def gcd(n, m):
    if n < m:
        return gcd(m, n)
    elif m == 0:
        return n
    else:
        return gcd(m, n%m)

print(gcd(A, B))