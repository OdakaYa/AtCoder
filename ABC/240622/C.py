sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

ans = 0
if sx > tx:
    sx, sy, tx, ty = tx, ty, sx, sy
if sy > ty:
    ty = 2*sy-ty
if (sx+sy) % 2:
    sx, sy, tx, ty = 1, 0, tx-sx+1, ty-sy
else:
    sx, sy, tx, ty = 0, 0, tx-sx, ty-sy

x, y = sx, sy
tmp = min(tx-x, ty-y)
ans += tmp
x, y = sx + tmp, sy + tmp

if x < tx:
    if (x+y) % 2 == 0:
        x += 1
    ans += (tx-x+1)//2
else:
    ans += ty-y
print(ans)