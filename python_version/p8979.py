from operator import itemgetter

n, k = map(int, input().split())

nations = []
for i in range(n):
    t = list(map(int,input().split()))
    nations.append([t[0], t[1], t[2], t[3], 0])

for i in range(len(nations)):
    nations[i][4] = nations[i][1] * 1000000000000 + nations[i][2] * 1000000 + nations[i][3]

nations = sorted(nations, key=itemgetter(4), reverse=True)

cnt = 0
bcnt = 0
before = 0
for i in nations:
    if before != i[4]:
        before = i[4]
        cnt += (1 + bcnt)
        bcnt = 0
    else:
        bcnt += 1
    if i[0] == k:
        break
print(cnt)