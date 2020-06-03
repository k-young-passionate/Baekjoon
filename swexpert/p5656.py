from copy import deepcopy
from itertools import product


def getinput():
    n, w, h = map(int, input().split())
    bricks = [list(map(int, input().split())) for x in range(h)]
    bombed = []  # 필요 없음

    originsize = 0  # 원래 사이즈
    for i in range(h):
        for j in range(w):
            if bricks[i][j] > 0:
                originsize += 1

    droppos = product(range(w), repeat=n)  # 모든 경우의 수, 중복순열
    return n, w, h, bricks, bombed, droppos, originsize


def simulation(w, h, pos, bricks, bombed):
    sizes = 0  # 총 사라진 벽돌
    height = -1
    for j in range(h):  # 해당하는 column 벽돌 찾기
        size = bricks[j][pos]
        if size > 0:
            height = j
            break
    if height == -1:  # 없으면 return
        return 0
    stack, size = bombing(w, h, (height, pos), size, bricks)  # 해당 벽독 파괴하고, splash damage 값 저장
    sizes += size  # 터진 벽돌 수 저장
    while len(stack) > 0:  # 연쇄작용으로 터질 벽돌들 계속 터뜨림
        s = stack.pop()
        tmpl, size = bombing(w, h, s[0], s[1], bricks)
        sizes += size
        for t in tmpl:
            stack.append(t)
    dropdown(w, h, bricks)  # 벽돌 내리기
    return sizes


def debug(bricks):
    print("=================")
    for i in bricks:
        print(i)


def dropdown(w, h, bricks):  # 중간에 0 이면 내리기
    for j in range(w):
        for i in range(h-1, 0, -1):
            flag = True
            if bricks[i][j] == 0:
                for ii in range(i, -1, -1):
                    if bricks[ii][j] != 0:
                        bricks[i][j] = bricks[ii][j]
                        bricks[ii][j] = 0
                        flag = False
                        break
                if flag:
                    break


def bombing(w, h, position, size, bricks):  # 폭탄 터뜨리기
    candidates = []  # 더 터질 후보들
    result = 0  # 터진 벽돌들
    for i in range(position[0] - size + 1, position[0] + size):  # 세로로 터뜨리기
        if 0 <= i < h:  # 범위 체크
            if bricks[i][position[1]] > 1:  # 더 터질 벽돌 세기
                candidates.append([(i, position[1]), bricks[i][position[1]]])
            if bricks[i][position[1]] >= 1:  # 파괴된 벽돌 세기
                result += 1
            bricks[i][position[1]] = 0
    for i in range(position[1] - size + 1, position[1] + size):  # 가로로 터뜨리기
        if 0 <= i < w:
            if bricks[position[0]][i] > 1:
                candidates.append([(position[0], i), bricks[position[0]][i]])
            if bricks[position[0]][i] >= 1:
                result += 1
            bricks[position[0]][i] = 0

    return candidates, result



test_case = int(input())
for T in range(test_case):
    n, w, h, bricks, bombed, droppos, originsize = getinput()
    maxsize = 0
    for dp in droppos:
        size = 0
        new_bricks = deepcopy(bricks)

        for i in range(n):
            size += simulation(w, h, dp[i], new_bricks, bombed)
        if size > maxsize:
            maxsize = size
        if maxsize == originsize:
            break
    print("#"+str(T+1), originsize - maxsize)