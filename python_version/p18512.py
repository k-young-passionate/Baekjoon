x, y, p1, p2 = map(int, input().split())

cnt = 0

while p1 != p2:
    if cnt == 10000:
        break
    if p1 > p2:
        p2 += y
    elif p1 < p2:
        p1 += x
    cnt += 1

if cnt == 10000:
    print(-1)
else:
    print(p1)