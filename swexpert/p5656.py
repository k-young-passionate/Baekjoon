from copy import deepcopy
from itertools import product


def getinput():
    n, w, h = map(int, input().split())
    bricks = [list(map(int, input().split())) for x in range(h)]
    bombed = []
    tmp = []
    for _ in range(w):
        tmp.append(False)

    for _ in range(w):
        bombed.append(tmp.copy())

    originsize = 0
    for i in range(h):
        for j in range(w):
            if bricks[i][j] > 0:
                originsize += 1

    droppos = product(range(w), repeat=n)
    return n, w, h, bricks, bombed, droppos, originsize


def simulation(w, h, pos, bricks, bombed):
    sizes = 0
    height = -1
    for j in range(h):
        size = bricks[j][pos]
        if size > 0:
            height = j
            break
    if height == -1:
        return False
    stack, size = bombing(w, h, (height, pos), size, bricks)
    sizes += size
    while len(stack) > 0:
        s = stack.pop()
        tmpl, size = bombing(w, h, s[0], s[1], bricks)
        sizes += size
        for t in tmpl:
            stack.append(t)
        # print(stack)
        # debug(bricks)
    dropdown(w, h, bricks)
    return sizes


def debug(bricks):
    print("=================")
    for i in bricks:
        print(i)


def dropdown(w, h, bricks):
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


def bombing(w, h, position, size, bricks):
    candidates = []
    result = 0
    for i in range(position[0] - size + 1, position[0] + size):
        if 0 <= i < h:
            if bricks[i][position[1]] > 1:
                candidates.append([(i, position[1]), bricks[i][position[1]]])
            if bricks[i][position[1]] >= 1:
                result += 1
            bricks[i][position[1]] = 0
    for i in range(position[1] - size + 1, position[1] + size):
        if 0 <= i < w:
            # print(position[0], i, bricks[position[0]][i])
            if bricks[position[0]][i] > 1:
                candidates.append([(position[0], i), bricks[position[0]][i]])
            if bricks[position[0]][i] >= 1:
                result += 1
            bricks[position[0]][i] = 0

    # for i in range(lower, -1, -1):
    #     if i - (lower - upper + 1) < 0:
    #         bricks[i][position[1]] = 0
    #     else:
    #         bricks[i][position[1]] = bricks[i - (lower - upper + 1)][position[1]]
    #
    # for j in range(left , right+1):
    #     for i in range(position[0], -1, -1):
    #         if i == 0:
    #             bricks[i][j] = 0
    #         else:
    #             bricks[i][j] = bricks[i-1][j]
    return candidates, result


def count(bricks):
    cnt = 0
    for bb in bricks:
        for b in bb:
            if b > 0:
                cnt += 1

    return cnt


test_case = int(input())
for T in range(test_case):
    n, w, h, bricks, bombed, droppos, originsize = getinput()
    # print('new era')
    # debug(bricks)
    maxsize = 0
    for dp in droppos:
        size = 0
        new_bricks = deepcopy(bricks)

        for i in range(n):
            size += simulation(w, h, dp[i], new_bricks, bombed)
            # debug(new_bricks)
        # print(dp, size, maxsize)
        # size = count(new_bricks)
        if size > maxsize:
            maxsize = size
        if maxsize == originsize:
            break
    # print(originsize)
    print("#"+str(T+1), originsize - maxsize)