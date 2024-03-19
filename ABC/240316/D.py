N, H, W = map(int, input().split())

T = []
for _ in range(N):
    T.append(list(map(int, input().split())))

def dfs(T0, t0):
    if len(t0) == 0:
        if all(T0):
            return True
        else:
            return False
    else:
        for yoko, tate in t0:
            if 

B = 2**N
for bit in range(B):
    size = 0
    tmp = bit
    i = 0
    tiles = []
    while tmp:
        if tmp % 2:
            tiles.append(i)
        tmp //= 2
        i += 1
    size = 0
    for t in tiles:
        size += T[t][0] * T[t][1]
    if size == H*W:
        dp = [[True]*2 for _ in range(2)]
        print(tiles, all(dp))