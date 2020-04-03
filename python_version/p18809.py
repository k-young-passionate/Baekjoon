def getinput():
    ii = list(map(int, input().split()))
    n, m, g, r = ii
    mymap = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        mymap.append(tmp.copy())

    return (n, m), g, r, mymap

def spread2(mymap, size, pos, color):
    status = False
    up = [pos[0]-1, pos[1]]
    down = [pos[0]+1, pos[1]]
    left = [pos[0], pos[1]-1]
    right = [pos[0], pos[1]+1]

    upcheck = pos[0] - 1 >= 0
    downcheck = pos[0] + 1 < size[0]
    leftcheck = pos[1] - 1 >= 0
    rightcheck = pos[1] + 1 < size[1]

    if color == 4:
        if upcheck:
            if mymap[up[0]][up[1]] == 3:
                mymap[up[0]][up[1]] = 5
                status = True
        if downcheck:
            if mymap[down[0]][down[1]] == 3:
                mymap[down[0]][down[1]] = 5
                status = True

        if leftcheck:
            if mymap[left[0]][left[1]] == 3:
                mymap[left[0]][left[1]] = 5
                status = True

        if rightcheck:
            if mymap[right[0]][right[1]] == 3:
                mymap[right[0]][right[1]] = 5
                status = True

    if upcheck:
        if 0 < mymap[up[0]][up[1]] < 3:   # upcheck
            mymap[up[0]][up[1]] = color
            status = True

    if downcheck:
        if 0 < mymap[down[0]][down[1]] < 3:  # upcheck
            mymap[down[0]][down[1]] = color
            status = True

    if leftcheck:
        if 0 < mymap[left[0]][left[1]] < 3:   # upcheck
            mymap[left[0]][left[1]] = color
            status = True

    if rightcheck:
        if 0 < mymap[right[0]][right[1]] < 3:   # upcheck
            mymap[right[0]][right[1]] = color
            status = True

    return status, mymap

def spread(mymap, size):
    # print("============spread===============")
    realstatus = False
    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] in [3, 4]:
                mymap[i][j] *= 10

    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] == 30:
                status, mymap = spread2(mymap, size, (i,j), 3)
                if status:
                    realstatus = True


    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] == 40:
                status, mymap = spread2(mymap, size, (i,j), 4)
                if status:
                    realstatus = True
    return realstatus, mymap

def findpos(mymap, size):
    candidate = []
    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] == 2:
                candidate.append((i,j))

    order = [0] * len(candidate)
    return candidate, order

def findflower(mymap, size):
    cnt = 0
    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] == 5:
                cnt += 1
    return cnt

def start(mymap, c, o):
    for i in range(len(c)):
        if o[i] == 3 or o[i] == 4:
            mymap[c[i][0]][c[i][1]] = o[i]

    return mymap

def drawmap(mymap):
    print("mymap")
    for i in mymap:
        print(i)

def test(origin, size, g, r, c, o, index):
    testmymap = arraycopy(origin,size)
    mymax = 0
    cnt = 0
    if len(o) == index and g + r != 0:
        return 0
    if g == 0 and r == 0:
        testmymap = start(testmymap, c, o)
        while True:
            status, testmymap = spread(testmymap, size)
            if not status:
                break
        cnt = findflower(testmymap, size)
        if mymax < cnt:
            mymax = cnt
        return mymax

    testset = [3, 4, 0]
    for i in testset:
        o[index] = i
        if i == 3 and g > 0:
            cnt = test(origin, size, g-1, r, c, o, index+1)
        elif i == 4 and r > 0:
            cnt = test(origin, size, g, r-1, c, o, index+1)
        elif i == 0 and len(o) - index >= r + g:
            cnt = test(origin, size, g, r, c, o, index+1)
        else:
            return 0
        if cnt > mymax:
            mymax = cnt
    return mymax

def arraycopy(origin, size):
    c = []
    for i in range(size[0]):
        tmp = []
        for j in range(size[1]):
            tmp.append(origin[i][j])
        c.append(tmp.copy())

    return c


def result():
    size, g, r, mymap = getinput()
    c, o = findpos(mymap, size)
    mymax = test(mymap, size, g,r,c,o, 0)
    print(mymax)
    # for i in mymap:
    #     print(i)

