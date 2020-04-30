from itertools import product, combinations

def getinput():
    n, m, h = map(int, input().split())

    ladder = []  # 사다리 상태, 현 index와 오른쪽에 연결된 사다리 상황 저장
    for i in range(h):
        tmp = [False] * (n)
        ladder.append(tmp.copy())

    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        ladder[a][b] = True
    minus = 0
    for i in range(4, h):  # 5개 연속 빈 줄이면 2줄 없애기 - 중복 시험할 필요가 없음
        if h >= 5 and i - minus > 5:
            if ladder[i-2-minus] == ladder[i-1-minus] == ladder[i-minus] == ladder[i-minus-3] == ladder[i-4-minus]:
                del(ladder[i-minus])
                del(ladder[i-minus-1])
                minus += 2
                h -= 2

    ladderlist = []  # 발판 없는 사다리 후보, 좌우에 기존의 발판이 없어야 함
    for i in range(h):
        for j in range(n - 1):
            if not ladder[i][j]:
                if n - 1 != 1:
                    if j == 0:
                        if ladder[i][j + 1]:
                            continue
                    elif j == n - 2:
                        if ladder[i][j - 1]:
                            continue
                    else:
                        if ladder[i][j + 1] or ladder[i][j - 1]:
                            continue
                ladderlist.append((i, j))
    return n, m, h, ladder, ladderlist


def currentladder(ladder, candidate=[]):  # 사다리 현재 상태, 디버그용
    index = 1
    for i in ladder:
        iindex = 0
        print(index, end="\t")
        index += 1
        for j in i:
            print("|", end="")
            if j or (index - 2, iindex) in candidate:
                print("_", end="")
            else:
                print(" ", end="")
            iindex += 1
        print('|', end="")
        print()
    print()


def simulation(n, h, ladder, candidate):  # 결과 조건에 맞는지 체크
    if len(candidate) == 2:
        if candidate[0][0] == candidate[1][0] and candidate[0][1] + 1 == candidate[1][1]:
            return False
    elif len(candidate) == 3:
        if candidate[0][0] == candidate[1][0] and candidate[0][1] + 1 == candidate[1][1]:
            return False
        elif candidate[1][0] == candidate[2][0] and candidate[1][1] + 1 == candidate[2][1]:
            return False
    for i in range(n - 1):
        column = i
        for j in range(h):
            row = j
            if column == 0:
                if ladder[row][column] or (row, column) in candidate:
                    column += 1
            elif column == n - 1:
                if ladder[row][column - 1] or (row, column - 1) in candidate:
                    column -= 1
            else:
                if ladder[row][column] or (row, column) in candidate:
                    column += 1
                elif ladder[row][column - 1] or (row, column - 1) in candidate:
                    column -= 1
            row += 1
        if i != column:
            return False
    return True


def check(n, h, ladder, candidate):
    for i in candidate:
        if simulation(n, h, ladder, i):
            return True
    return False


if __name__ == "__main__":
    n, m, h, ladder, ladderlist = getinput()
    flag = True
    for i in range(4):
        if (m + i) % 2 != 0:
            continue
        candidate = combinations(ladderlist, i)
        result = check(n, h, ladder, candidate)
        if result:
            print(i)
            flag = False
            break

    if flag:
        print(-1)

'''
찾아봐야하는 반례
1 0 30

꼭 체크해줘야하는 것
가로선 겹치는 case
'''