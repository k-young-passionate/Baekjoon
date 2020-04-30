# cur
# 0, 1: i, j  /  2: size  /  3: the number of eat  /  4: move  /  5: isBlocked



def clear(n, space):
    for i in range(n):
        for j in range(n):
            if space[i][j] >= 9:
                space[i][j] -= 9
    return space

def eat(n, space, cur, addu, addl):
    clear(n, space)
    cur[0] = cur[0] + addu
    cur[1] = cur[1] + addl
    cur[3] += 1
    if cur[3] == cur[2]:
        cur[2] += 1
    space[cur[0]][cur[1]] = 9
    return space, cur

def go(n, space, cur, addu, addl):
    cur[0] = cur[0] + addu
    cur[1] = cur[1] + addl
    space[cur[0]][cur[1]] += 9
    return space, cur

def bfs(n, space, cur, queue):
    cur[4] += 1
    spacecmp = [space, space, space, space]
    curcmp = [cur, cur, cur, cur]

    try:
        up = space[cur[0]-1][cur[1]]
        if up <= cur[2]:
            if up == cur[2] or up == 0:
                spacecmp[0], curcmp[0] = go(n, space, cur, -1, 0)
            else:
                spacecmp[0], curcmp[0] = eat(n, space, cur, -1, 0)

    except:
        up = cur[2] + 1


    try:
        left = space[cur[0]][cur[1]-1]
        if left <= cur[2]:
            if left == cur[2] or left == 0:
                spacecmp[1], curcmp[1] = go(n, space, cur, 0, -1)
            else:
                spacecmp[1], curcmp[1] = eat(n, space, cur, 0, -1)
    except:
        left = cur[2] + 1

    try:
        right = space[cur[0]][cur[1]+1]
        if right <= cur[2]:
            if right == cur[2] or right == 0:
                spacecmp[2], curcmp[2] = go(n, space, cur, 0, 1)
            else:
                spacecmp[2], curcmp[2] = eat(n, space, cur, 0, 1)
    except:
        right = cur[2] + 1

    try:
        down = space[cur[0]+1][cur[1]]
        if down <= cur[2]:
            if down == cur[2] or down == 0:
                spacecmp[3], curcmp[3] = go(n, space, cur, 1, 0)
            else:
                spacecmp[3], curcmp[3] = eat(n, space, cur, 1, 0)
    except:
        down = cur[2] + 1

    if up > cur[2] and left > cur[2] and right > cur[2] and down > cur[2]:
        cur[5] = False
        return space, cur

    maxmove, maxi = curcmp[0][4], 0
    for i in range(4):
        if curcmp[i][5] and maxmove > curcmp[i][4]:
            maxmove = curcmp[i][4]
            maxi = i

    cur = curcmp[maxi]
    space = spacecmp[maxi]
    return space, cur




def getindex(n, space):
    ci, cj = 0, 0
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                ci, cj = i, j
                break

    return ci, cj


def getinput():
    n = int(input())
    space = []
    for i in range(n):
        tmp = input().split()
        tmp = [ int(t) for t in tmp ]
        space.append(tmp.copy())
    return n, space

def result():
    n, space = getinput()

    ci, cj = getindex(n, space)
    cur = [ci, cj, 2, 0, 0, True]
    results = bfs(n, space, cur, [])
    print(results)
    print(results[1][3])
    return 0