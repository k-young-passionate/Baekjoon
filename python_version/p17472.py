from collections import deque
from itertools import combinations

def getinput():  # input 받기
    N, M = map(int, input().split())
    mymap = []
    for _ in range(N):
        mymap.append(list(map(int, input().split())))

    island = getIsland(N, M, mymap)  # island 집합
    numisland = len(island)  # island 갯수

    return N, M, island, numisland, mymap


def getIsland(n, m, mymap):  # island 구하는 함수, 전체 탐색하며 섬에 대해 bfs 탐색
    island = []
    for i in range(n):
        for j in range(m):
            if mymap[i][j] == 1:
                tmp = []
                tmp.append((i, j))
                queue = deque()
                queue.append((i, j))
                mymap[i][j] = 2
                while True:
                    if len(queue) == 0:
                        tmp.sort(key=lambda x: x[0]*16+x[1])
                        island.append(tmp.copy())
                        break
                    q = queue.popleft()
                    candidate = [(q[0] - 1, q[1]), (q[0] + 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1)]
                    for c in candidate:
                        if 0 <= c[0] < n and 0 <= c[1] < m and mymap[c[0]][c[1]] == 1:
                            queue.append((c[0], c[1]))
                            mymap[c[0]][c[1]] = 2  # 원래 지도에서 섬을 2로 바꿈
                            tmp.append((c[0], c[1]))

    return island


def bp(island, numisland, mymap):  # brute force의 오타, 결과 값 찾기
    bridges = list(combinations(range(0, numisland), 2))  # 섬 간의 조합 찾기
    bd = []  # 가능한 다리의 연결 + 거리 보관
    for b in range(len(bridges)):
        tmpb = (bridges[b][0], bridges[b][1], possibility(island[bridges[b][0]], island[bridges[b][1]], mymap))
        if tmpb[2] != 30:
            bd.append(tmpb)

    bdcb = list(combinations(bd, numisland-1))  # 가능한 다리끼리의 연결 조합, 섬이 n개 있으면 다리는 n-1개로 모든 섬 연결 가능
    result = -1  # 실패 시 -1 리턴
    for b in bdcb:  # 모든 다리 조합 탐색
        candlist = []  # 모든 섬을 거치는지 찾기 위한 용도
        tmpsum = 0
        for bb in b:
            if bb[0] not in candlist:
                candlist.append(bb[0])
            if bb[1] not in candlist:
                candlist.append(bb[1])
            tmpsum += bb[2]  # 총 거리 구하기
        if len(candlist) != numisland or not isall(b, numisland):  # 빼먹은 섬 존재 여부 확인
            continue
        if result == -1 or result > tmpsum:  # 최소 길이 update
            result = tmpsum

    return result


def isall(bd, l):  # 빼먹은 섬 존재 여부 확인
    queue = deque()
    queue.append(bd[0][0])
    result = []
    result.append(bd[0][0])
    while True:  # bfs 로 update
        if len(queue) == 0:
            break
        q = queue.popleft()
        for i in bd:
            # print(i, q, result)
            if i[0] == q and i[1] not in result:
                result.append(i[1])
                queue.append(i[1])
            elif i[1] == q and i[0] not in result:
                result.append(i[0])
                queue.append(i[0])
    # print(result)
    if len(result) != l:
        return False
    return True


def possibility(island1, island2, mymap):  # 다리 길이 return, 불가능 시 30 return
    dist = 30
    for il in island1:
        for il2 in island2:  # 모든 다리 조합해보기
            flag = False
            if il[0] == il2[0]:  # 가로의 위치가 같으면
                if dist > abs(il[1] - il2[1]) > 2:  # 세로의 길이 확인, 2칸 이상 떨어져 있어야 함
                    for i in range(min([il[1], il2[1]]) + 1, max([il[1], il2[1]])):  # 방금 잰 거리 사이에 바다만 있는지 확인
                        if mymap[il[0]][i] == 2:  # 섬이 있다고???
                            flag = True
                            break
                    if flag:  # 섬 있는 경우 (유효하지 않음)
                        continue
                    dist = abs(il[1] - il2[1])
            elif il[1] == il2[1]:  # 세로의 위치가 같으면
                if dist > abs(il[0] - il2[0]) > 2:  # 가로의 길이 확인, 2칸 이상 떨어져 있어야 함
                    for i in range(min([il[0], il2[0]]) + 1, max([il[0], il2[0]])):  # 방금 잰 거리 사이에 바다만 있는지 확인
                        if mymap[i][il[1]] == 2:  # 섬이 있다고???
                            flag = True
                            break
                    if flag:  # 섬 있는 경우 (유효하지 않음)
                        continue
                    dist = abs(il[0] - il2[0])

    if 10 > dist - 1 > 1:  # 섬 길이 유효한 경우
        return dist - 1
    return 30  # 섬 길이 유효하지 않은 경우


if __name__ == "__main__":
    n,m,island,numisland,mymap = getinput()
    result = bp(island, numisland, mymap)
    print(result)