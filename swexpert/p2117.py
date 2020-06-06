def getinput():  # input 받기
    n, m = map(int, input().split())
    myhome = [list(map(int, input().split())) for _ in range(n)]
    house = []  # 좌표만 저장
    for i in range(n):
        for j in range(n):
            if myhome[i][j] == 1:
                house.append((i, j))
    return n, m, house


def getdistance(src, dst):  # euclidean distance 구하기 == 가능 범위 계산용
    return abs(src[0]-dst[0]) + abs(src[1]-dst[1])


def checkarea(n, m, pos, house, size, payment):  # 집 중, 방법 구역에 포함되는 수와, 이득여부
    cnt = 0
    for h in house:
        if getdistance(pos, h) < size:
            cnt += 1

    if cnt*m >= payment:
        return True, cnt

    return False, cnt


def check(n, m, house):  # 모든 영역 사이즈에 대해, 모든 중심에 대해 체크해 최댓값 리턴
    global getareatime, calctime
    cnt = 0
    for size in range(2*n):  # 모든 사이즈
        payment = size**2 + (size-1)**2
        for i in range(n):  # 모든 영역
            for j in range(n):
                isgood, tmpcnt = checkarea(n, m, (i, j), house, size, payment)
                if isgood:
                    if cnt < tmpcnt:
                        cnt = tmpcnt
    return cnt


test_case = int(input())
for T in range(test_case):
    n, m, house = getinput()
    print("#"+str(T+1), check(n, m, house))