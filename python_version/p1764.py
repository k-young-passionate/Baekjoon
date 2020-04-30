
dj = []
bj = []
dbj = []

n, m = map(int, input().split())
for i in range(n):
    d = input()
    dj.append(d)


for i in range(m):
    b = input()
    bj.append(b)

dj.sort()
bj.sort()
idxd, idxb = 0, 0
while True:
    if idxd == n or idxb == m:
        break
    if dj[idxd] > bj[idxb]:
        idxb += 1
    elif dj[idxd] < bj[idxb]:
        idxd += 1
    else:
        dbj.append(dj[idxd])
        idxd += 1
        idxb += 1


# for i in dj:
#     if i in bj:
#         dbj.append(i)

print(len(dbj))
for i in dbj:
    print(i)