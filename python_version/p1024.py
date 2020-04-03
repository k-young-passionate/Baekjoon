n, l = map(int, input().split())
endflag = True
for i in range(l, 101):
    m = n // i
    s = 0
    mm = i // 2
    l = []
    if i % 2 == 0:
        if m - mm + 1 < 0:
            break
        for j in range(m - mm + 1, m + mm + 1):
            l.append(j)
            s += j
    else:
        if m - mm < 0:
            break
        for j in range(m - mm, m + mm + 1):
            l.append(j)
            s += j
    if s == n:
        endflag = False
        for j in l:
            print(j, end=" ")
        break
if endflag:
    print(-1)