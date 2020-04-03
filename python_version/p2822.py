from operator import itemgetter

score = []
for i in range(8):
    score.append((int(input()), i))

score = sorted(score, key=itemgetter(0), reverse=True)
ii = []
sc = []
for i in score[:5]:
    ii.append(i[1])
ii.sort()
for i in score[:5]:
    sc.append(i[0])
print(sum(sc))
for i in ii:
    print(i+1, end=" ")