from operator import itemgetter

n = int(input())
l = list(map(int, input().split()))

for i in range(len(l)):
    l[i] = [l[i], True]

ll = sorted(l, key=itemgetter(0))
print(l)
print(ll)
idx = 0
for i in l:
    for j in range(len(ll)):
        if ll[j] == i:
            ll[j][1] = False
            print(j, end=" ")
            break
