
def getinput():  # input 받기
    n = int(input())
    mymap = [list(map(int, input().split())) for _ in range(n)]
    wormhole = {}  # 웜홀 위치들 번호로 짝짓기
    blackhole = []  # 블랙홀 위치들
    startlist = []  # 시작할 수 있는 곳들에 대한 후보들
    for i in range(n):
        for j in range(n):
            if mymap[i][j] == -1:
                blackhole.append((i, j))
            elif mymap[i][j] > 5:
                if mymap[i][j] not in wormhole:
                    wormhole[mymap[i][j]] = []
                wormhole[mymap[i][j]].append((i, j))
            elif mymap[i][j] == 0:
                startlist.append((i, j))
    return n, mymap, blackhole, wormhole, startlist


def changedirection(direction, block):  # 블록을 만났을 때, 방향을 바꿔줌
    if block == 1:
        if direction[0] == 1 or direction[1] == -1:
            return (direction[1], direction[0])
        else:
            return (-direction[0], -direction[1])
    elif block == 2:
        if direction[0] == -1 or direction[1] == -1:
            return (-direction[1], -direction[0])
        else:
            return (-direction[0], -direction[1])
    elif block == 3:
        if direction[0] == -1 or direction[1] == 1:
            return (direction[1], direction[0])
        else:
            return (-direction[0], -direction[1])
    elif block == 4:
        if direction[0] == 1 or direction[1] == 1:
            return (-direction[1], -direction[0])
        else:
            return (-direction[0], -direction[1])
    elif block in [-1, 5]:
        return (-direction[0], -direction[1])


def simulation(pos, direction, n, mymap, blackhole, wormhole):  # 실제 돌려보기
    score = 0  # 반환할 점수
    start = pos  # 시작 점 기억
    while True:
        if not (0 <= pos[0] < n) or not (0 <= pos[1] < n):  # 벽 밖으로 나갈 때
            direction = changedirection(direction, -1)
            score += 1
        elif pos in blackhole:  # 블랙홀 들어갔을 때
            return score
        elif mymap[pos[0]][pos[1]] > 5:  # 웜홀 만났을 때
            if wormhole[mymap[pos[0]][pos[1]]][0] == pos:
                pos = wormhole[mymap[pos[0]][pos[1]]][1]
            else:
                pos = wormhole[mymap[pos[0]][pos[1]]][0]
        elif mymap[pos[0]][pos[1]] in range(1, 6):  # 블록 만났을 때
            direction = changedirection(direction, mymap[pos[0]][pos[1]])
            score += 1

        pos = (pos[0] + direction[0], pos[1] + direction[1])  # 해당 방향으로 이동
        if pos == start:  # 시작점과 같을 때
            return score


def debug(n, mymap, pos):  # 디버그용 코드
    for i in range(n):
        for j in range(n):
            if mymap[i][j] != 0:
                print(mymap[i][j], end='\t')
            else:
                if pos == (i, j):
                    print('b', end='\t')
                else:
                    print(mymap[i][j], end='\t')
        print()
    print('==================')


test_case = int(input())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for T in range(test_case):
    n, mymap, blackhole, wormhole, startlist = getinput()
    result = 0
    for s in startlist:  # 모든 시작 위치에 대해
        for d in direction:  # 모든 시작 방향에 대해
            r = simulation(s, d, n, mymap, blackhole, wormhole)
            if result < r:  # 더 큰 점수로 update
                result = r
    print("#"+str(T+1), result)