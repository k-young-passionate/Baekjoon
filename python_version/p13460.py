from collections import deque


# input 받아서 return
def getinput():
    n, m = map(int, input().split())

    _mymap = []

    for i in range(n):
        tmpmap = input()
        tmpmap = list(j for j in tmpmap)
        _mymap.append(tmpmap.copy())

    for i in range(n):
        for j in range(m):
            if _mymap[i][j] == "B":
                _b = [i, j]
            elif _mymap[i][j] == "R":
                _r = [i, j]
    _mymap = clear(_mymap, (n, m))
    return (n, m), _mymap, _b, _r


# debugging 용 현황 시각화
def show(mymap, size, b, r):
    for i in range(size[0]):
        for j in range(size[1]):
            if [i, j] == b:
                print("B", end="")
            elif [i, j] == r:
                print("R", end="")
            else:
                print(mymap[i][j], end="")
        print()


# map clear (R, B 없애줌)
def clear(_mymap, _size):
    for i in range(_size[0]):
        for j in range(_size[1]):
            if _mymap[i][j] == "B" or _mymap[i][j] == "R":
                _mymap[i][j] = "."
    return _mymap


# 원하는 방향으로 이동시킴
def go(_mymap, p, other, d):  # p(움직일거), other(다른 구슬 위치), d(방향)
    while True:
        p[0] += d[0]  # 상하 움직임 반영
        p[1] += d[1]  # 좌우 움직임 반영

        if _mymap[p[0]][p[1]] == "O":  # 만나면 떨어짐
            return [-1, -1]
        if _mymap[p[0]][p[1]] == "#" or p == other:  # 막다른 길 간거면 되돌아감
            p[0] -= d[0]
            p[1] -= d[1]
            break

    return p  # 바뀐 위치 return


# bfs
def bfs(_mymap, _size, _b, _r):  # _b(B 위치), _r(R 위치)
    _time = 0  # 결과
    q = [_b.copy(), _r.copy(), _time, (0, 0)]  # 최초 queue의 element
    queue = deque()  # queue 선언
    queue.append(q)

    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    paststat = []  # 이전 위치 기록

    while True:
        if len(queue) == 0:  # queue 비면 종료, 갈 수 없음
            break

        q = queue.popleft()
        _b, _r, _time, past = q[0], q[1], q[2], q[3]
        _time += 1

        if _time > 10:    # 너무 많이 가면 종료
            _time = -1
            break

        for i in direction:
            if (past[0] * -1, past[1] * -1) == i:  # 왔던 길은 다시가지 않아
                continue

            if (i[0] == -1 and _r[0] > _b[0]) \
                    or (i[0] == 1 and _r[0] < _b[0]) \
                    or (i[1] == -1 and _r[1] > _b[1]) \
                    or (i[1] == 1 and _r[1] < _b[1]):  # B가 R 보다 앞서있을 경우
                tmpb = go(_mymap, _b.copy(), _r.copy, i)
                if tmpb == [-1, -1]:    # B가 빠짐
                    continue
                tmpr = go(_mymap, _r.copy(), tmpb.copy(), i)
                if tmpr == [-1, -1]:    # R이 빠짐
                    return _time
            else:   # R이 B 보다 앞서있을 경우
                tmpr = go(_mymap, _r.copy(), _b.copy(), i)
                tmpb = go(_mymap, _b.copy(), tmpr.copy(), i)
                if tmpb == [-1, -1]:    # B가 빠짐
                    continue
                if tmpr == [-1, -1]:    # R이 빠짐
                    return _time

            tmpq = [tmpb.copy(), tmpr.copy(), _time, i]

            if [tmpq[0], tmpq[1]] in paststat \
                    or [tmpq[0], tmpq[1], tmpq[2] - 1, past] == q:
                continue
            queue.append(tmpq.copy())
            paststat.append([tmpq[0], tmpq[1]])
            # print(_time)
            # show(_mymap, _size, _b, _r)
            # print()
            # show(_mymap, _size, tmpb, tmpr)
            # print('============================')
    return -1


if __name__ == "__main__":
    size, mymap, b, r = getinput()  # input 받기
    time = bfs(mymap, size, b, r)  # bfs 돌려서 결과 받기
    print(time)  # 결과출력
