def getinput():
    ii = list(map(int,input().split()))
    m,n,k = ii
    stickers = []
    for i in range(k):
        tmp = []
        size = list(map(int, input().split()))
        for j in range(size[0]):
            ttmp = list(map(int, input().split()))
            tmp.append(ttmp.copy())
        stickers.append([size, tmp.copy()])
    return m, n, k, stickers

# def drawmap(mymap):
#     print("=======mymap=======")
#     for i in mymap:
#         print(i)


def generatemap(size):
    l = []
    row = [0] * size[1]
    for i in range(size[0]):
        l.append(row.copy())
    return l

def rotate(sticker, stickersize):
    newsticker = []
    tmp = [0] * stickersize[0]
    for i in range(stickersize[1]):
        newsticker.append(tmp.copy())
    for i in range(stickersize[0]):
        for j in range(stickersize[1]):
            newsticker[j][i] = sticker[stickersize[0]-i-1][j]
    return newsticker


def traverse(size, stickersize, mymap, sticker):
    for k in range(4):
        if size[0] < stickersize[0] or size[1] < stickersize[1]:
            # print(k, "continue")
            sticker = rotate(sticker, stickersize)
            stickersize = [stickersize[1], stickersize[0]]
            continue
        for i in range(size[0] - stickersize[0] + 1):
            for j in range(size[1] - stickersize[1] + 1):
                if match([i,j],mymap,sticker):
                    mymap = draw(mymap, sticker, [i, j])
                    # print(k)
                    return True, mymap
        sticker = rotate(sticker, stickersize)
        stickersize = [stickersize[1], stickersize[0]]

    return False, mymap

def draw(mymap, sticker, pos):
    # drawmap(sticker)
    # print(pos)
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                mymap[i+pos[0]][j+pos[1]] = sticker[i][j]

    # drawmap(mymap)

    return mymap

def match(pos, mymap, sticker):
    # drawmap(sticker)
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            # print(i+pos[0],j+pos[1],i,j)
            if mymap[i+pos[0]][j+pos[1]] == 1 and sticker[i][j] == 1:
                # drawmap(mymap)
                return False
    # print("match here", pos)
    return True

def countzero(mymap, size):
    cnt = 0
    for i in range(size[0]):
        for j in range(size[1]):
            if mymap[i][j] == 1:
                cnt += 1
    return cnt

def result():
    m, n, k, stickers = getinput()

    mymap = generatemap((m,n))

    for i in stickers:
        # print("################new sticker######################")
        # print([m,n], i[0])
        # drawmap(i[1])
        ischanged, mymap = traverse([m,n], i[0], mymap, i[1])
        # print(ischanged)

    # for i in mymap:
    #     print(i)

    print(countzero(mymap, (m,n)))