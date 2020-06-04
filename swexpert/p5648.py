
def getinput():
    n = int(input())
    atoms = {}  # 원자 정보 저장
    candidates = []  # 같은 거리의 쌍과 거리 저장
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        tmp = [(x, y), d, k]
        for aindex in atoms:  # 각 원자에 대해 같은 거리 확인해 그 쌍을 저장
            a = atoms[aindex]
            if tmp[1] == 0:
                if a[1] == 1 and a[0][0] == tmp[0][0] and a[0][1] > tmp[0][1]:
                    candidates.append([a[0], tmp[0], a[0][1] - tmp[0][1]])
                elif a[1] == 2 and 0 < a[0][0] - tmp[0][0] == a[0][1] - tmp[0][1]:
                    candidates.append([a[0], tmp[0], (a[0][0]-tmp[0][0]) *2])
                elif a[1] == 3 and 0 < tmp[0][0] - a[0][0] == a[0][1] - tmp[0][1]:
                    candidates.append([a[0], tmp[0], 2*(a[0][1]-tmp[0][1])])
            elif tmp[1] == 1:
                if a[1] == 0 and a[0][0] == tmp[0][0] and a[0][1] < tmp[0][1]:
                    candidates.append([a[0], tmp[0], tmp[0][1] - a[0][1]])
                elif a[1] == 2 and 0 < a[0][0] - tmp[0][0] == tmp[0][1] - a[0][1]:
                    candidates.append([a[0], tmp[0], (tmp[0][1]-a[0][1])*2])
                elif a[1] == 3 and 0 < tmp[0][0] - a[0][0] == tmp[0][1] - a[0][1]:
                    candidates.append([a[0], tmp[0], 2*(tmp[0][1]-a[0][1])])
            elif tmp[1] == 2:
                if a[1] == 3 and a[0][1] == tmp[0][1] and a[0][0] < tmp[0][0]:
                    candidates.append([a[0], tmp[0], tmp[0][0] - a[0][0]])
                elif a[1] == 0 and 0 < tmp[0][0] - a[0][0] == tmp[0][1] - a[0][1]:
                    candidates.append([a[0], tmp[0], (tmp[0][1]-a[0][1])*2])
                elif a[1] == 1 and 0 < tmp[0][0] - a[0][0] == a[0][1] - tmp[0][1]:
                    candidates.append([a[0], tmp[0], 2*(a[0][1]-tmp[0][1])])
            elif tmp[1] == 3:
                if a[1] == 2 and a[0][1] == tmp[0][1] and a[0][0] > tmp[0][0]:
                    candidates.append([a[0], tmp[0], a[0][0] - tmp[0][0]])
                elif a[1] == 0 and 0 < a[0][0] - tmp[0][0] == tmp[0][1] - a[0][1]:
                    candidates.append([a[0], tmp[0], (tmp[0][1]-a[0][1]) * 2])
                elif a[1] == 1 and 0 < a[0][0] - tmp[0][0] == a[0][1] - tmp[0][1]:
                    candidates.append([a[0], tmp[0], (a[0][1]-tmp[0][1]) * 2])
        atoms[tmp[0]] = tmp.copy()

    return n, atoms, candidates


test_case = int(input())
for T in range(test_case):
    result = 0
    n, atoms, candidates = getinput()

    candidates.sort(key=lambda x : x[2])  # 원자 매칭 쌍 거리 순으로 정렬
    deletedlist = []  # 부딪힌 원자 중, 다른 것과 또 부딪힐 가능성이 있는지 확인하는 리스트
    deleted = []  # 실제로 부딪혀서 더 부딪히면 안되는 리스트
    for c in candidates:
        if c[0] in deleted or c[1] in deleted:  # 이미 부딪혀서 상대 원자가 없다면 무시
            continue
        deletedlist.append([c[0], c[2]])
        deletedlist.append([c[1], c[2]])
        deleted.append(c[0])
        deleted.append(c[1])
        result += atoms[c[0]][2]
        result += atoms[c[1]][2]
        while len(deletedlist) > 0:  # 부딪힌 원자에 대해 더 동시에 부딪힌 원자 있는지 확인
            d = deletedlist.pop()
            for cc in candidates:
                if d[1] < cc[2]:  # 시간이 초과되면 루프 탈출
                    break
                if d[1] == cc[2]:  # 시간이 같으면
                    if cc[0] == d[0] and cc[1] not in deleted:  # 둘 중 하나가 맞고, 나머지가 이미 체크된 것이 아니라면
                        deletedlist.append([cc[1], cc[2]])
                        deleted.append(cc[1])
                        result += atoms[cc[1]][2]
                    elif cc[1] == d[0] and cc[0] not in deleted:
                        deletedlist.append([cc[0], cc[2]])
                        deleted.append(cc[0])
                        result += atoms[cc[0]][2]
    print("#"+str(T+1), result)


