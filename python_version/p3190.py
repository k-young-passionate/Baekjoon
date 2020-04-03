from operator import add
def getinputs():
    n = int(input())    # size of the board
    k = int(input())    # # of apples
    pos = []            # apple position
    for ii in range(k):
        t = list(map(int, input().split()))
        pos.append(t.copy())

    l = int(input())    # # of direction change
    dr = []             # direction changes
    for i in range(l):
        t = input().split()
        dr.append([int(t[0]), t[1]])

    return n, k, pos, l, dr

def check(board, apple, worm, cur):
    if board[cur[0]][cur[1]] == 1:
        return -1
    if cur in worm:
        return -1
    for ii in range(len(apple)):
        if apple[ii] == cur:
            del(apple[ii])
            return 1

    return 0

def turn(dr, cur):
    if dr == 'L':
        cur = [cur[1] * -1, cur[0]]
    else:
        cur = [cur[1], cur[0] * -1]
    return cur

def go(dr, board, apple, worm, cur):
    cur = list(map(add, cur, dr))

    r = check(board, apple, worm, cur)
    if r == 0:
        worm.append(cur.copy())
        del(worm[0])
        return True, dr, apple, worm, cur
    elif r == 1:
        worm.append(cur.copy())
        return True, dr, apple, worm, cur
    else:
        return False, dr, apple, worm, cur


n, k, apple, l, dr = getinputs()

board = []
for i in range(n+2):
    if i == 0 or i == n+1:
        cell = [1] * (n+2)
    else:
        cell = []
        cell.append(1)
        for j in range(n):
            cell.append(0)
        cell.append(1)
    board.append(cell.copy())

togo = [0, 1]
worm = [[1,1]]
cur = [1,1]
time = 0
while True:
    # print(time,":", togo, "worm", worm, "cur", cur, "/////", apple)
    for i in dr:
        if time == i[0]:
            togo = turn(i[1], togo)
            break
    time += 1
    flag, togo, apple, worm, cur = go(togo, board, apple, worm, cur)
    if not flag:
        print(time)
        break
