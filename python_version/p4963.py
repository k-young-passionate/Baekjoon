from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    mymap = []
    for i in range(h):
        mymap.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if mymap[i][j] == 1:
                queue = deque()
                queue.append((i, j))
                mymap[i][j] = 0

                while len(queue) != 0:
                    q = queue.popleft()
                    for d in direction:
                        newpos = (q[0] + d[0], q[1] + d[1])
                        if not (0 <= newpos[0] < h) or not (0 <= newpos[1] < w):
                            continue
                        if mymap[newpos[0]][newpos[1]] == 1:
                            queue.append(newpos)
                            mymap[newpos[0]][newpos[1]] = 0
                cnt += 1
    print(cnt)