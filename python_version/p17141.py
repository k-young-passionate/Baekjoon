from itertools import combinations
from collections import deque


def getinput():
    n, m = map(int, input().split())
    mymap = [list(map(int, input().split())) for _ in range(n)]

    viruses = []

    for i in range(n):  # 모든 바이러스 좌푯값 저장 + 해당 좌표 0으로 만들기
        for j in range(n):
            if mymap[i][j] == 2:
                viruses.append((i, j))
                mymap[i][j] = 0

    return n, m, mymap, viruses


def debug(mymap, time, pos):  # 디버깅용 프린트
    print('=====', time, pos, '=====')
    for i in mymap:
        print(i)
    print('============')


def bfs(n, mymap, virus):  # bfs로 퍼지는 시간 찾기
    time = 0

    queue = deque()
    for v in virus:  # 투하지점 추가
        queue.append([v, time])

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(queue) > 0:
        q = queue.popleft()
        if mymap[q[0][0]][q[0][1]] != 0:  # 이미 퍼진 곳일 경우 되돌아가기
            continue
        mymap[q[0][0]][q[0][1]] = 2  # 퍼진 곳 2로 만들기
        time = q[1]  # 시간 저장
        for d in direction:  # 모든 방향에 대해 퍼질 수 있으면 퍼뜨리기
            pos = (q[0][0] + d[0], q[0][1] + d[1])
            if 0 <= pos[0] < n and 0 <= pos[1] < n:
                if mymap_copy[pos[0]][pos[1]] == 0:
                    queue.append([(pos[0], pos[1]), q[1] + 1])

    for m in mymap:  # 안 퍼진 곳 있으면 -1 리턴
        for mm in m:
            if mm == 0:
                return -1

    return time


if __name__ == "__main__":
    n, m, mymap, viruses = getinput()

    candidates = combinations(viruses, m)  # 모든 투하지점의 조합 계산
    result = 1000000  # 임의의 큰 수
    for c in candidates:  # 모든 조합에 대해 탐색
        mymap_copy = []  # call by reference 에 의한 원본 값 수정 방지
        for i in range(n):
            mymap_copy.append(mymap[i].copy())
        tmpresult = bfs(n, mymap_copy, c)  # 결과값 저장
        if tmpresult < result and tmpresult != -1:  # 결과값이 더 작으면
            result = tmpresult  # 결과값 update

    if result == 1000000:  # update 되지 않은 경우
        result = -1
    print(result)
