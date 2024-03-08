H, W, K = map(int, input().split())

C = [
    input() for _ in range(H)
]

bH = 2**H
ans = 0
for i in range(bH):
    bit = i
    bit_list = []
    for j in range(H):
        if bit % 2:
            bit_list.append(j)
        bit //= 2
    lenbl = len(bit_list)
    if lenbl <= K:
        cnt_list = [None]*W
        for j1 in range(W):
            temp = 0
            for j2 in range(H):
                if j2 not in bit_list and C[j2][j1] == "#":
                    temp += 1
            cnt_list[j1] = temp
        cnt_list.sort()
        temp = 0
        for j in range(W):
            if j < K - lenbl:
                temp += H
            else:
                temp += cnt_list[j] + lenbl
        ans = max(ans, temp)
print(ans)