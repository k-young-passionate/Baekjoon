
def getinput():
    ii = list(map(int, input().split()))
    m,n,k = ii
    rect = []
    for i in range(k):
        tmp = list(map(int, input().split()))
        rect.append([(tmp[0], tmp[1]), (tmp[2], tmp[3])])

    return m,n,k,rect

def drawmap(rect, mm):
    for i in range(rect[0][1], rect[1][1]):
        for j in range(rect[0][0], rect[1][0]):
            mm[i][j] = '1'

    return mm

def bfs(mm, point):
    queue = []
    queue.append(point)
    cnt = 1
    mm[point[0]][point[1]] = 1
    while True:
        if len(queue) == 0:
            break
        # print(queue)
        q = queue[0]
        queue.pop(0)

        if 0 < q[0] and mm[q[0]-1][q[1]] == 0:
            mm[q[0]-1][q[1]] = 1
            queue.append((q[0]-1, q[1]))
            cnt += 1
        if q[0] < len(mm) - 1 and mm[q[0]+1][q[1]] == 0:
            mm[q[0]+1][q[1]] = 1
            cnt += 1
            queue.append((q[0]+1, q[1]))
        if 0 < q[1] and mm[q[0]][q[1]-1] == 0:
            mm[q[0]][q[1]-1] = 1
            cnt += 1
            queue.append((q[0], q[1]-1))
        if q[1] < len(mm[0]) - 1 and mm[q[0]][q[1]+1] == 0:
            mm[q[0]][q[1]+1] = 1
            cnt += 1
            queue.append((q[0], q[1]+1))

    return mm, cnt




def detect(mm):
    cnt = 0
    ccntlist = []
    for i in range(len(mm)):
        for j in range(len(mm[0])):
            if mm[i][j] == 0:
                cnt += 1
                mm, ccnt = bfs(mm, (i,j))
                ccntlist.append(ccnt)

    return cnt, ccntlist

def show(mm):
    for i in mm:
        for j in i:
            print(j, end="\t")
        print()

def result():
    m,n,k,rect = getinput()
    mymap = []
    tmp = [0] * (n)
    for i in range(m):
        mymap.append(tmp.copy())
    for r in rect:
        mymap = drawmap(r, mymap)
    cnt, ccnt = detect(mymap)
    ccnt.sort()
    print(cnt)
    for c in ccnt:
        print(c, end=" ")
