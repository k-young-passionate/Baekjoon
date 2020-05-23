import time
from copy import deepcopy

def getinput():  # 값 받음
    n, m = map(int, input().split())
    mymap = []
    for _ in range(n):
        tmp = input()
        tmp = [x for x in tmp]
        mymap.append(tmp.copy())

    pos = {}  # 각 구슬과 탈출점의 위치 저장
    for i in range(n):
        for j in range(m):
            if mymap[i][j] == 'R':
                pos['R'] = [i, j]
                mymap[i][j] = '.'
            elif mymap[i][j] == 'B':
                pos['B'] = [i, j]
                mymap[i][j] = '.'
            elif mymap[i][j] == 'O':
                pos['O'] = [i, j]
                mymap[i][j] = '.'

    return (n, m), mymap, pos


def debug(size, mymap, pos):  # 현재 map 출력 for debug
    print('====================')
    for i in range(size[0]):
        for j in range(size[1]):
            if [i, j] == pos['R']:
                toprint = 'R'
            elif [i, j] == pos['B']:
                toprint = 'B'
            elif [i, j] == pos['O']:
                toprint = 'O'
            else:
                toprint = mymap[i][j]
            print(toprint, end=" ")
        print()
    print('====================')


def move(size, mymap, pos, color, direction):  # 방향이 주어질 때, 실제 움직임 반영
    cur = pos[color]

    othercolor = 'B' if color == 'R' else 'R'

    for i in range(max(size)):  # 최대 n 혹은 m 만큼 움직임
        cur[1] += direction[1]  # 좌우로 이동
        cur[0] += direction[0]  # 상하로 이동
        if mymap[cur[0]][cur[1]] != '.' or pos[othercolor] == cur:  # 벽을 만나면
            pos[color] = [cur[0] - direction[0], cur[1] - direction[1]]
            return False, pos  # 탈출 여부와 정착 값 return
        elif cur == pos['O']:  # 탈출구를 만나면?
            pos[color] = [-1, -1]
            return True, pos


def stackprint(stack):  # stack 시각적 debugging 용
    print('---stack---')
    for i in range(len(stack)):
        print(stack[len(stack) - i - 1])
    print('-----------')


def dfs(size, mymap, pos):
    stack = []
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    for d in directions:  # 초기 stack 추가
        stack.append([d, deepcopy(pos), 1, deepcopy(pos)])

    for i in range(2000000):
        if len(stack) == 0:
            break

        s = stack.pop()
        beforepos = deepcopy(s[1])
        if (s[0][1] == -1 and s[1]['R'][1] > s[1]['B'][1]) or \
                (s[0][1] == 1 and s[1]['R'][1] < s[1]['B'][1]) or \
                (s[0][0] == -1 and s[1]['R'][0] > s[1]['B'][0]) or \
                (s[0][0] == 1 and s[1]['R'][0] < s[1]['B'][0]):  # B가 R보다 먼저 있을 경우 (좌, 우, 상, 하 순)
            flag, cur = move(size, mymap, s[1], 'B', s[0])  # B 움직여
            if flag:  # B먼저 탈출
                continue  # 무시
            flag, cur = move(size, mymap, cur, 'R', s[0]) # R 움직여
            if flag:  # R 탈출
                print(1)
                return True
        else:   # R이 B보다 먼저 있을 경우
            flag, cur = move(size, mymap, s[1], 'R', s[0])  # R 움직여
            afterflag, cur = move(size, mymap, cur, 'B', s[0])  # B 움직여
            if afterflag:  # B 먼저 탈출
                continue
            elif flag:  # R 탈출
                print(1)
                return True
        s[1] = deepcopy(cur)  # update
        s[2] += 1  # 횟수 ++

        if (beforepos['R'] == s[1]['R'] and beforepos['B'] == s[1]['B']) or \
                (s[3]['R'] == s[1]['R'] and s[3]['B'] == s[1]['B']):  # 안움직였거나 지난번과 같은 위치이면 탈출
            continue
        if s[2] > 10:  # 10 번 넘으면 탈출
            continue

        for d in directions:
            if d == s[0]:
                continue
            newone = [d, s[1], s[2], beforepos]
            if newone in stack:  # stack 에 중복 넣지 않음
                continue
            stack.append(deepcopy(newone))  # 스택에 추가

    return False


if __name__ == "__main__":
    size, mymap, pos = getinput()
    result = dfs(size, mymap, pos)
    if not result:
        print(0)


'''
5 3
###
#R#
#B#
#O#
###
'''

'''
10 10
##########
#R#...##B#
#...#.##.#
#####.##.#
#......#.#
#.######.#
#.#O...#.#
#.#.#.#..#
#...#..#.#
##########

'''