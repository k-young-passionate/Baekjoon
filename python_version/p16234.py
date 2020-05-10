from collections import deque


def getinput():  # input 받기
    n, l, r = map(int, input().split())
    mymap = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        mymap.append(tmp.copy())

    return n, l, r, mymap


def bfs(n, l, r, mymap):  # 개방할 국가들 찾아서 반환
    mergelist = []  # 개방된 국가 연합체 정보
    for i in range(n):
        for j in range(n):  # 모든 위치의 국가 확인
            tmp = []  # 이번 루프에서 연결된 국가 리스트 및 정보, index 0은 연합체 인구 수의 합
            queue = deque()
            if mymap[i][j] < 0:  # 국가 값이 음수면 무시 == 국가가 이미 연합체이면 무시
                continue
            tmp.append(mymap[i][j])
            mymap[i][j] *= -1  # 방문 시 음수로 변경
            queue.append((i, j))
            while True:
                q = queue.popleft()
                tmp.append(q)
                checklist = [(q[0] - 1, q[1]), (q[0] + 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1)]  # 상하좌우체크

                for k in checklist:
                    if 0 <= k[0] < n and 0 <= k[1] < n and mymap[k[0]][k[1]] > -1:  # index out of range error 방지
                        if l <= abs(mymap[q[0]][q[1]] + mymap[k[0]][k[1]]) <= r and k not in tmp:  # l과 r 사이일 때만 체크, 이미 들린 곳은 방문하지 않음
                            queue.append((k[0], k[1]))
                            tmp[0] += mymap[k[0]][k[1]]  # tmp 첫번째 index에 인구 추가
                            mymap[k[0]][k[1]] *= -1  # 방문 시 음수로 변경

                if len(queue) == 0:  # 무한 루프 탈출
                    break

            if len(tmp) != 2:  # 연합체가 없는 경우 무시
                mergelist.append(tmp.copy())
            else:
                mymap[i][j] *= -1

    return mergelist


def mergenations(mergelist, mymap, cnt):  # 연합국가 인구 분배
    cnt += 1
    for i in mergelist:
        l = len(i) - 1
        for j in range(1, l+1):
            mymap[i[j][0]][i[j][1]] = i[0] // l
    return cnt


def show(mymap):  # debugging 용 코드
    for i in mymap:
        print(i)
    print()


if __name__ == "__main__":
    n, l, r, m = getinput()  # n, l, r, 지도
    cnt = 0
    while True:
        result = bfs(n, l, r, m)
        print(result)
        if len(result) == 0:  # 더이상 연합이 안될 경우 out
            break
        show(m)
        cnt = mergenations(result, m, cnt)
        show(m)

    print(cnt)

