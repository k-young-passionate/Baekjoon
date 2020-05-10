from collections import deque


def getinput():
    size = list(map(int, input().split()))
    mymap = []
    for i in range(size[0]):
        tmpmap = list(map(int, input().split()))
        mymap.append(tmpmap.copy())
    virus = []
    space = []
    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] == 2:
                virus.append([i, j])
            elif mymap[i][j] == 0:
                space.append([i, j])
    return size, mymap, virus, space


def spread(size, mymap, virus):
    queue = deque()
    for i in virus:
        queue.append(i)
    result = len(virus)
    results = []
    while len(queue) > 0:
        q = queue.popleft()
        spr = [(q[0] - 1, q[1]), (q[0] + 1, q[1]), (q[0], q[1] - 1), (q[0], q[1] + 1)]

        for i in spr:
            if 0 <= i[0] < size[0] and 0 <= i[1] < size[1]:
                if mymap[i[0]][i[1]] == 0 and i not in results:
                    queue.append(i)
                    result += 1
                    results.append(i)
    return mymap, result


def show(mymap):
    for i in mymap:
        for j in i:
            print(j, end=' ')
        print()
    print('====================')
    return mymap



def test(size, mymap, virus, space):
    maxresult = 65
    for si in range(len(space)):
        mymap[space[si][0]][space[si][1]] = 1
        for sj in range(si + 1, len(space)):
            mymap[space[sj][0]][space[sj][1]] = 1
            for sk in range(sj + 1, len(space)):
                mymap[space[sk][0]][space[sk][1]] = 1
                tmpmymap, result = spread(size, mymap, virus)
                if maxresult > result:
                    maxresult = result
                    # show(mymap)
                mymap[space[sk][0]][space[sk][1]] = 0
            mymap[space[sj][0]][space[sj][1]] = 0
        mymap[space[si][0]][space[si][1]] = 0

    # print(maxresult, len(space))
    return len(space) - maxresult + len(virus) - 3


if __name__ == "__main__":
    size, mymap, virus, space = getinput()

    result = test(size, mymap, virus, space)
    print(result)
