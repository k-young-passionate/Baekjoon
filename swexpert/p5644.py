from copy import deepcopy


def getinput():  # input 받기
    M, A = map(int, input().split())
    a = list(map(int, input().split()))  # a 위치
    a.insert(0, 0)  # 처음 위치 저장
    b = list(map(int, input().split()))  # b 위치
    b.insert(0, 0)  # 처음 위치 저장
    ap = [list(map(int, input().split())) for _ in range(A)]  # ap 정보 저장
    aps = []  # ap 구성 좌표들 저장
    apsize = []  # 각 ap에 대한 크기 저장
    for aa in ap:
        apsize.append(aa[3])
        tmp = []
        for i in range(1, 11):
            for j in range(1, 11):
                if distance((i, j), (aa[1], aa[0])) <= aa[2]:
                    tmp.append((i, j))
        aps.append(deepcopy(tmp))
    return M, A, a, b, aps, apsize


def distance(a, b):  # 거리 구하기
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def simulation(M, A, a, b, ap, apsize):  # brute force
    direction = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]  # 각 위치 변환 정보를 리스트로 저장
    apos = (1, 1)  # a 위치
    bpos = (10, 10)  # b 위치
    charged = 0  # 총 충전량
    for m in range(M+1):  # 모든 이동에 대해
        apos = (apos[0] + direction[a[m]][0], apos[1] + direction[a[m]][1])  # 이동
        bpos = (bpos[0] + direction[b[m]][0], bpos[1] + direction[b[m]][1])  # 이동
        acharger, bcharger = [], []  # 각각의 충전 후보 리스트
        for aa in range(A):  # 각 소속 ap 찾기
            if apos in ap[aa]:
                acharger.append(aa)
            if bpos in ap[aa]:
                bcharger.append(aa)

        acharger.sort(key=lambda x: apsize[x], reverse=True)  # ap 크기 순 정렬
        bcharger.sort(key=lambda x: apsize[x], reverse=True)

        # 아래는 어떤 ap를 고를지 결정해 ac, bc에 각각 저장
        if len(acharger) == 0:
            if len(bcharger) == 0:
                continue
            else:
                ac = 0
                bc = apsize[bcharger[0]]
            charged += (ac + bc)
            continue

        if len(bcharger) == 0:
            bc = 0
            ac = apsize[acharger[0]]
            charged += (ac + bc)
            continue

        if acharger[0] != bcharger[0]:
            ac = apsize[acharger[0]]
            bc = apsize[bcharger[0]]
        else:
            if len(acharger) == 1:
                if len(bcharger) == 1:
                    ac = apsize[acharger[0]] // 2
                    bc = apsize[bcharger[0]] // 2
                else:
                    ac = apsize[acharger[0]]
                    bc = apsize[bcharger[1]]
            elif len(bcharger) == 1:
                ac = apsize[acharger[1]]
                bc = apsize[bcharger[0]]
            else:
                if apsize[acharger[1]] > apsize[bcharger[1]]:
                    ac = apsize[acharger[1]]
                    bc = apsize[bcharger[0]]
                else:
                    ac = apsize[acharger[0]]
                    bc = apsize[bcharger[1]]
        charged += (ac + bc)  # 정해진 charging 크기 더해줌

    return charged


test_case = int(input())
for T in range(test_case):
    M, A, a, b, ap, apsize = getinput()
    result = simulation(M, A, a, b, ap, apsize)
    print("#"+str(T+1), result)