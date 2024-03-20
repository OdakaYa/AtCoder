a, b = map(int, input().split())
MOD = 10**9 + 7

def pow(a, b):
    if b == 0:
        return 1
    else:
        return (a**(b%2) * pow(a**2%MOD, b//2)) % MOD
    
print(pow(a, b))