from itertools import combinations
from collections import deque


def getinput():
    n, m = map(int, input().split())
    mymap = [list(map(int, input().split())) for _ in range(n)]

    viruses = []

    for i in range(n):
        for j in range(n):
            if mymap[i][j] == 2:
                viruses.append((i, j))
                mymap[i][j] = 0

    return n, m, mymap, viruses


def debug(mymap, time, pos):
    print('=====', time, pos, '=====')
    for i in mymap:
        print(i)
    print('============')


def bfs(n, mymap, virus):
    time = 0

    queue = deque()
    for v in virus:
        queue.append([v, time])

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(queue) > 0:
        q = queue.popleft()
        if mymap[q[0][0]][q[0][1]] != 0:
            continue
        mymap[q[0][0]][q[0][1]] = 2
        time = q[1]
        # debug(mymap, time, q[0])
        for d in direction:
            pos = (q[0][0] + d[0], q[0][1] + d[1])
            if 0 <= pos[0] < n and 0 <= pos[1] < n:
                if mymap_copy[pos[0]][pos[1]] == 0:
                    queue.append([(pos[0], pos[1]), q[1] + 1])

    for m in mymap:
        for mm in m:
            if mm == 0:
                return -1

    return time


if __name__ == "__main__":
    n, m, mymap, viruses = getinput()

    candidates = combinations(viruses, m)
    result = 1000000
    for c in candidates:
        mymap_copy = []
        for i in range(n):
            mymap_copy.append(mymap[i].copy())
        tmpresult = bfs(n, mymap_copy, c)
        # print(tmpresult)
        if tmpresult < result and tmpresult != -1:
            result = tmpresult

    if result == 1000000:
        result = -1
    print(result)
