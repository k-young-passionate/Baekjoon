from collections import deque

def getinput():  # input 받기, shark의 위치만 따로 저장
    n = int(input())
    mymap = [list(map(int, input().split())) for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if mymap[i][j] == 9:
                mymap[i][j] = 0
                shark = (i, j)


    return n, mymap, shark


def bfs(n, mymap, shark, size):  # 가장 가까운 먹이 탐색
    visit = [[False for _ in range(n)] for _ in range(n)]

    queue = deque()
    time = 0
    queue.append([shark, time])
    visit[shark[0]][shark[1]] = True
    result = []
    resulttime = 0
    while len(queue) > 0 :
        front = queue.popleft()
        q = front[0]
        time = front[1]
        candidates = [(q[0] - 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1), (q[0] + 1, q[1])]
        for c in candidates:  # 4방향에 대해 탐색
            if 0 <= c[0] < n and 0 <= c[1] < n:  # 범위 안에 있는 좌표만 탐색
                if mymap[c[0]][c[1]] <= size and not visit[c[0]][c[1]]:  # 갈 수 있는 범위만 탐색
                    if mymap[c[0]][c[1]] in [0, size]:  # 먹지 못하는 곳 탐색 시, queue에 추가
                        queue.append([c, time + 1])
                        visit[c[0]][c[1]] = True
                    else:  # 먹이가 있으면 result 에 추가
                        if len(result) == 0:  # result 가 비어있으면 최소 time 정해줌
                            resulttime = time
                        if resulttime < time:  # 기준 시간 초과 시, 결과 리턴
                            result.sort(key=lambda x: x[0][0] * 100 + x[0][1])  # 위, 왼쪽 기준 우선순위
                            r = result[0]  # 가장 우선순위 높은 것 출력
                            c, time = r[0], r[1]
                            mymap[c[0]][c[1]] = 0
                            shark = c
                            return True, time + 1, shark
                        else:  # 기준 시간과 같을 경우 결과 값에 포함
                            result.append([c, time])

    if len(result) == 0:  # 결과 값이 없으면 False 반환
        return False, 0, shark
    else:  # 결과 값이 있으면 sorting 후, 우선순위 값 리턴
        result.sort(key=lambda x: x[0][0] * 100 + x[0][1])
        r = result[0]
        c, time = r[0], r[1]
        mymap[c[0]][c[1]] = 0
        shark = c
        return True, time + 1, shark


def debug(n, mymap, shark, size, time):  # 디버그용 상어 위치 및 먹이 현황 그래프
    print("=======",size,"======")
    for i in range(n):
        for j in range(n):
            if (i, j) == shark:
                print("9", end=" ")
            else:
                print(mymap[i][j], end=" ")
        print()
    print("========",time,"=======")


def gettime(n, mymap, shark):  # 최소 시간 계산
    size = 2  # 상어 크기
    cnt = 0  # 먹은 수
    totaltime = 0  # 총 걸린 시간
    for i in range(n*n):  # 최대 n*n 번의 시행
        result, time, shark = bfs(n, mymap, shark, size)  # 1회 bfs 순환
        # debug(n, mymap, shark, size, time)
        totaltime += time
        if not result:  # 먹이를 못찾았으면 return
            return totaltime
        else:  # 먹이를 찾았으면
            if cnt+1 == size:  # 몸집이 커지는 조건에서는 몸집 증가
                size += 1
                cnt = 0  # 초기화
            else:  # 먹은 수 증가
                cnt += 1
    return totaltime


if __name__ == "__main__":
    n, mymap, shark = getinput()
    print(gettime(n, mymap, shark))