from collections import deque
from itertools import combinations


def getInput():
    N = int(input())  # 도시 수 입력
    city = list(map(int, input().split()))  # 인구 수 입력
    conn = {}  # 연결 관계 입력
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp2 = list(x-1 for x in tmp[1:] )
        conn[i] = tmp2.copy()
        conn[i].sort()
    return N, city, conn


def check(connset, conn):  # 도시의 연결성 확인
    queue = deque()
    queue.append(connset[0])
    connset.remove(connset[0])
    while True:  # bfs 로 연결 관계 확인
        if len(queue) == 0:  # loop 종료
            if len(connset) == 0:  # 연결 다 되어 있으면 False
                return True
            else:  # 연결 안 된 것 있으면 False
                return False

        q = queue.popleft()  # deque
        for c in conn[q]:  # 연결 가능한지 검색
            if c in connset:  # 연결 가능 대상 찾으면 후보 지우고 enqueue
                queue.append(c)
                connset.remove(c)


def bfs(N, city, conn):  #
    result = -1
    cities = [x for x in range(N)]
    for i in range(1, len(cities) // 2 + 1):
        cb = list(map(list, combinations(cities, i)))
        for c in cb:
            c2 = []
            for j in cities:
                if j not in c:
                    c2.append(j)

            if check(c.copy(), conn) and check(c2.copy(),conn):
                s1 = sum([city[x] for x in c])
                s2 = sum([city[x] for x in c2])
                tmpresult = abs(s1 - s2)
                if result == -1 or tmpresult < result:
                    result = tmpresult
    return result


if __name__ == "__main__":
    N, city, conn = getInput()

    print(bfs(N, city, conn))