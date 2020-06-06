from collections import deque
import time

def getinput():  # input 받기
    n, k = map(int, input().split())
    mymap = [list(map(int, input().split())) for _ in range(n)]
    hps = []
    hp = 0
    for i in range(n):
        for j in range(n):
            if hp < mymap[i][j]:
                hp = mymap[i][j]
                hps = [(i, j)]
            elif hp == mymap[i][j]:
                hps.append((i, j))

    return n, k, mymap, hp, hps


def findpath(n, k, mymap, hp):  # 경로 찾기 (dfs)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = []
    stack.append([[hp], True, (-1, -1), -1])
    longest = []
    while len(stack) > 0:
        q = stack.pop()
        if len(q[0]) > len(longest):  # 가장 긴 경로 저장
            longest = q[0]
        for m in moves:  # 각 이동 후보 탐색 (상하좌우)
            origin = q[0][-1]
            if origin == q[2]:
                originsize = q[3]
            else:
                originsize = mymap[origin[0]][origin[1]]
            newpos = (q[0][-1][0] + m[0], q[0][-1][1] + m[1])  # 새 좌표
            if 0 <= newpos[0] < n and 0 <= newpos[1] < n and newpos not in q[0]:  # 새 좌표가 범위 안 & 이전에 가지 않은 경로
                ismore = q[1]  # 산 깎을 수 있는지 여부 가져오기
                if mymap[newpos[0]][newpos[1]] >= originsize:  # 갈 곳이 현재 위치 이상이면
                    if ismore:  # 산을 깎을 수 있으면
                        amount = originsize - 1
                        if amount + k >= mymap[newpos[0]][newpos[1]]:  # k 만큼 안에 깎을 수 있는지 확인
                            ismore = False
                            moved = newpos
                            qcopy = q[0].copy()
                            qcopy.append(newpos)
                            stack.append([qcopy, ismore, moved, amount])
                else:  # 내려가는 경우면
                    qcopy = q[0].copy()
                    qcopy.append(newpos)
                    stack.append([qcopy, q[1], q[2], q[3]])

    return len(longest)


test_case = int(input())
for T in range(test_case):
    n, k, mymap, hp, hps = getinput()
    result = 0
    for h in hps:  # 모든 봉우리에 대해 test
        tmp = findpath(n, k, mymap, h)
        if result < tmp:
            result = tmp
    print("#"+str(T+1), result)

