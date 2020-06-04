def getinput():
    n, m, k = map(int, input().split())
    mymap = {}
    tmpmymap = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            mymap[(i, j)] = tmpmymap[i][j]

    status = {}  # 0 없음, 1 비활선, 2 활성, -1 사망
    timer = {}  # 시간 저장
    for i in range(n):
        for j in range(m):
            if mymap[(i, j)] != 0:
                status[(i, j)] = 1
            else:
                status[(i, j)] = 0

    for i in range(n):
        for j in range(m):
            if mymap[(i, j)] != 0:
                timer[(i, j)] = mymap[(i, j)]
            else:
                timer[(i, j)] = -1
    return (n, m), k, mymap, status, timer


def getresult(mymap):  # 남은 줄기세포 수 구하기
    result = 0
    for m in mymap:
        if status[m] > 0:
            result += 1
    return result


def debug(mymap, status, timer):
    keys = list(mymap.keys())
    keys.sort(key=lambda x: (x[0], x[1]))
    r, c, R, C = min([x[0] for x in keys]), min([x[1] for x in keys]), max([x[0] for x in keys]), max([x[1] for x in keys])
    for i in range(r, R+1):
        for j in range(c, C+1):
            if (i, j) in keys and status[(i, j)] > 0:
                print(mymap[(i, j)], end=" ")
            else:
                print("0", end=" ")
        print()

    print("==============")


def spread(size, mymap, status, timer):
    newmymap = {}
    for pos in mymap:  # 확산
        i, j = pos
        if status[(i, j)] == 2:
            candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for c in candidates:
                if c not in mymap:  # 기존의 map 에서 줄기세포를 찾을 수 없을 때
                    if c not in newmymap:  # 새로운 줄기세포가 생겼을 때
                        if c in status:
                            if status[c] == -1:  # 죽은 아이이면 무시  (시간초과 해결용)
                                continue
                        status[c] = 0
                        newmymap[c] = 0
                        timer[c] = -1

                    if status[c] == 0:
                        if mymap[(i, j)] > newmymap[c]:
                            newmymap[c] = mymap[(i, j)]
                else:
                    if status[c] == 0:
                        if mymap[(i, j)] > mymap[c]:
                            mymap[c] = mymap[(i, j)]
            timer[(i, j)] -= 1
        elif status[(i, j)] == 1:
            timer[(i, j)] -= 1
    for n in newmymap:
        mymap[n] = newmymap[n]

    newmymap = []
    for pos in mymap:  # 정리
        i, j = pos
        if mymap[(i, j)] > 0 and status[(i, j)] == 0:  # 새로 확산된 지역이면
            status[(i, j)] = 1
            timer[(i, j)] = mymap[(i, j)]
        if status[(i, j)] > 0 and timer[(i, j)] == 0:  # 시간초 다 되었으면
            status[(i, j)] += 1
            timer[(i, j)] = mymap[(i, j)]
            if status[(i, j)] == 3:
                status[pos] = -1
                newmymap.append(pos)
    for n in newmymap:  # 죽은 아이 삭제 (시간초과 해결용)
        del(mymap[n])


test_cases = int(input())

result = 0
for T in range(test_cases):
    size, k, mymap, status, timer = getinput()
    for i in range(k):
        spread(size, mymap, status, timer)
    print("#"+str(T+1), getresult(mymap))

