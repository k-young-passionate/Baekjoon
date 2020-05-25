def getinput():
    L = int(input())
    n = int(input())
    dirlist = [list(input().split()) for _ in range(n)]
    dirlist.append([3 * L, "L"])  # 마지막에 무한히 가도록 추가
    for i in range(n):
        dirlist[i][0] = int(dirlist[i][0])

    return L, dirlist


def changedirection(curdir, to):  # 방향 전환하는 함수
    if to == 'L':
        lr = ((curdir[0] + 1) % 2) * curdir[1] * -1
        ud = ((curdir[1] + 1) % 2) * curdir[0]
    else:
        lr = ((curdir[0] + 1) % 2) * curdir[1]
        ud = ((curdir[1] + 1) % 2) * curdir[0] * -1

    curdir = [lr, ud]

    return curdir


if __name__ == "__main__":
    L, D = getinput()
    curdir = [0, 1]  # 현재 방향, 오른쪽으로 초기화
    snake = [(0, 0)]  # 꺾어지는 점 저장 리스트, 시작점인 (0, 0) 저장
    cur = (0, 0)  # 현재의 위치
    past = (0, 0)  # 직전 꺾어지는 점의 위치
    cnt = 0  # 생존 시간
    index = -1  # 현재 방향 간략화
    startflag = True  # 처음에는 중복 검사 안 하기 위한 것
    for d in D:  # 모든 방향 지시 따라감
        if curdir == [0, 1]:  # 각 방향 간략화 값 index에 넣기
            index = 3
        elif curdir == [0, -1]:
            index = 1
        elif curdir == [1, 0]:
            index = 2
        else:
            index = 0
        endflag = False  # 종료 상황 체크 (죽은 상황)
        past = cur  # 지난 번 꺾인 점 update
        cur = (cur[0] + curdir[0] * d[0], cur[1] + curdir[1] * d[0])  # 현재 점 update
        cnt += d[0]  # 간 거리 추가
        maxcnt = 0  # 죽고 난 이후 더 간 거리 값 저장

        if startflag:  # 처음일 경우 자신에게 부딪혀 죽는 것 체크하지 않음
            startflag = False
        else:  # 처음이 아닐 경우 자신에게 부딪혀 죽는 것 체크
            spast = (0, 0)  # snake 돌 때, 지난 번 꺾이는 점
            for s in snake[1:-1]:  # 현재 점을 제외하고 모든 꺾어지는 점 체크
                if index % 2 == 0:  # 위아래로 갈 때
                    if s[0] == spast[0]:  # 꺾어지는 점(=barrier) 끼리의 row 가 같음
                        if min(past[0], cur[0]) <= s[0] <= max(past[0], cur[0]):  # 내가 지나가는 곳이 barrier 의 row 같은 곳 지나나
                            if min(spast[1], s[1]) <= cur[1] <= max(spast[1],
                                                                    s[1]):  # 내가 지나가는 곳이 barrier 의 col 같은 곳 지나나
                                endflag = True  # 나가야 해!
                                tmpcnt = abs(spast[0] - cur[0])  # 빼줘야하는 값
                                if maxcnt < tmpcnt:  # 최댓값으로 update
                                    maxcnt = tmpcnt
                    else:  # row 가 같은 점이 아닐 경우
                        if min(past[0], cur[0]) <= spast[0] <= max(past[0], cur[0]):  # 지나가는 선에 몸통 꺾인 부분이 있으면 (사실 0,0 용)
                            if spast[1] == past[1]:
                                endflag = True
                                tmpcnt = abs(spast[0] - cur[0])
                                if maxcnt < tmpcnt:
                                    maxcnt = tmpcnt
                else:  # 좌우로 갈 때
                    if s[1] == spast[1]:  # col 이 같음
                        if min(past[1], cur[1]) <= s[1] <= max(past[1], cur[1]):  # 내가 지나가는 곳이 barrier 의 col 같은 곳 지나나
                            if min(spast[0], s[0]) <= cur[0] <= max(spast[0],
                                                                    s[0]):  # 내가 지나가는 곳이 barrier 의 row 같은 곳 지나나
                                endflag = True
                                tmpcnt = abs(spast[1] - cur[1])
                                if maxcnt < tmpcnt:
                                    maxcnt = tmpcnt
                    else:  # col 이 같은 점이 아닐 경우
                        if min(past[1], cur[1]) <= spast[1] <= max(past[1], cur[1]):  # 지나가는 선에 몸통 꺾인 부분이 있으면 (사실 0,0 용)
                            if spast[0] == past[0]:
                                endflag = True
                                tmpcnt = abs(spast[1] - cur[1])
                                if maxcnt < tmpcnt:
                                    maxcnt = tmpcnt
                spast = s  # 과거의 점 update

        if not (-L <= cur[0] <= L and -L <= cur[1] <= L) and not endflag:  # 바깥으로 나가버리면? (이미 몸통에 부딪힌 경우 체크 X)
            if index % 2 == 0:  # 위아래로 이동할 때
                if index == 0:  # 위로 이동할 때
                    maxcnt = abs(cur[0] + L)
                else:  # 아래로 이동할 때
                    maxcnt = abs(cur[0] - L)
            else:  # 좌우로 이동할 때
                if index == 1:  # 좌로 이동할 때
                    maxcnt = abs(cur[1] + L)
                else:  # 우로 이동할 때
                    maxcnt = abs(cur[1] - L)
            cnt += 1  # 경계선에서 한 번 더 사니깐 1 추가
            endflag = True

        if endflag:  # 죽었따 ㅜㅜ
            cnt -= maxcnt  # 잘린 값 빼주기
            break

        curdir = changedirection(curdir, d[1])  # 방향 전환
        snake.append(cur)  # 꺾인 점 추가

    print(cnt)  # 결과 출력
