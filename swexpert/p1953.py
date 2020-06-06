from collections import deque


# 슬슬 주석달기 귀찮아짐
def getinput():  # input 받기
    n, m, r, c, l = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]
    # 각 관이 이동할 수 있는 후보들
    tunnel = [[(0, 0)], [(0, 1), (0, -1), (1, 0), (-1, 0)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)],
              [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]

    return (n, m), (r, c), l, underground, tunnel


def bfs(mapsize, manhole, l, underground, tunnel):  # bfs 탐색
    queue = deque()
    queue.append((manhole, 1))  # 시작 위치와 세대 저장
    visited = []
    while len(queue) > 0:
        ss = queue.popleft()
        s = ss[0]
        if ss[1] > l:
            continue
        if s not in visited:  # 방문 안한 점 방문으로 처리
            visited.append(s)
        for t in tunnel[underground[s[0]][s[1]]]:  # 현재 위치에서 갈 수 있는 점 체크
            newpos = (s[0] + t[0], s[1] + t[1])
            # 진짜 갈 수 있는지 체크 (범위 & 0 아닌 곳)
            if 0 <= newpos[0] < mapsize[0] and 0 <= newpos[1] < mapsize[1] and underground[newpos[0]][newpos[1]]:
                if newpos not in visited:  # 방문 안 한 곳
                    oppot = (-t[0], -t[1])  # 갈 곳에서 현재의 점 방문 가능한 지
                    if oppot not in tunnel[underground[newpos[0]][newpos[1]]]:
                        continue
                    queue.append([newpos, ss[1] + 1])

    return len(visited)


def debug(mapsize, ug, vs):
    print('----------')
    tunnel = [' ', '+', '|', '-', '└', '┌', '┐', '┘']
    cnt = 0
    print("X  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19")
    for i in range(mapsize[0]):
        print(i, end='  ')
        for j in range(mapsize[1]):
            print(tunnel[ug[i][j]], end='  ')
            # if (i, j) in vs:
            #     print('X', end=' ')
            #     cnt += 1
            # else:
            #     print(ug[i][j], end=' ')
        print()
    print()
    print(cnt)


def debug2(mapsize, ug, vs):
    print('----------')
    tunnel = [' ', '+', '|', '-', '└', '┌', '┐', '┘']
    cnt = 0
    # print("X  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19")
    for i in range(mapsize[0]):
        # print(i, end='  ')
        for j in range(mapsize[1]):
            # print(tunnel[ug[i][j]], end='  ')
            if (i, j) in vs:
                if (i, j) == vs[0]:
                    print('S', end=' ')
                else:
                    print('X', end=' ')
                cnt += 1
            else:
                print(ug[i][j], end=' ')
        print()
    print()
    print(cnt)


test_case = int(input())

for T in range(test_case):
    mapsize, manhole, l, underground, tunnel = getinput()
    result = bfs(mapsize, manhole, l, underground, tunnel)
    print("#" + str(T + 1), result)
