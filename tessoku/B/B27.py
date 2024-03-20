A, B = map(int, input().split())

def gcd(n, m):
    if m == 0:
        return n
    elif n < m:
        return gcd(m, n)
    else:
        return gcd(m, n%m)
print(A*B//gcd(A, B))