C = [[["#"]]]
N = int(input())

def matrix_add(A, B):
    res = []
    for (a, b) in zip(A, B):
        res.append(a+b)
    return res

for i in range(1, N+1):
    tmp = []
    tmpc = C[-1]
    tmp += matrix_add(tmpc, matrix_add(tmpc, tmpc))
    tmpc2 = [["."]*3**(i-1) for _ in range(3**(i-1))]
    tmp += matrix_add(tmpc, matrix_add(tmpc2, tmpc))
    tmp += matrix_add(tmpc, matrix_add(tmpc, tmpc))
    C.append(tmp)

for c in C[N]:
    print("".join(c))