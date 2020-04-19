def getinput():
    size = list(map(int, input().split()))
    paper = []
    for i in range(size[0]):
        tmppaper = list(map(int, input().split()))
        paper.append(tmppaper.copy())
    return size, paper.copy()


def getmax(size, paper, tetsize, tet):
    minsum = 0
    for i in range(0, size[0] - tetsize[0] + 1):
        for j in range(0, size[1] - tetsize[1] + 1):
            tmp = 0
            for ii in range(0, tetsize[0]):
                for jj in range(0, tetsize[1]):
                    if tet[ii][jj] == 1:
                        tmp += paper[i + ii][j + jj]
            if minsum < tmp:
                minsum = tmp
    return minsum


def rotate(tetsize, tet):
    newtet = []
    for i in range(tetsize[1]):
        tmp = []
        for j in range(tetsize[0]):
            tmp.append(tet[tetsize[0] - j - 1][i])
        newtet.append(tmp.copy())
    return newtet

def inverse(tetsize, tet):
    newtet = []
    for i in range(tetsize[0]):
        tmp = []
        for j in range(tetsize[1]):
            tmp.append(tet[i][tetsize[1] - j - 1])
        newtet.append(tmp.copy())
    return newtet

def show(tot):
    print("=================")
    for i in tot:
        for j in i:
            print(j, end=" ")
        print()
    print("================")


def basictet():
    a = [[1, 1, 1, 1]]
    b = [[1, 1], [1, 1]]
    c = [[1, 0], [1, 0], [1, 1]]
    d = [[1, 0], [1, 1], [0, 1]]
    e = [[1, 1, 1], [0, 1, 0]]

    return [b, a, d, c, e]


if __name__ == "__main__":
    size, paper = getinput()
    basic = basictet()

    result = []
    for i in range(5):
        tetsize = [len(basic[i]), len(basic[i][0])]
        if i == 0:
            # show(basic[i])
            result.append(getmax(size, paper, tetsize, basic[i]))
        else:
            for k in range(2):
                for j in range(4):
                    # show(basic[i])
                    result.append(getmax(size, paper, tetsize, basic[i]))
                    basic[i] = rotate(tetsize, basic[i])
                    tetsize = [tetsize[1], tetsize[0]]
                basic[i] = inverse(tetsize, basic[i])
    print(max(result))
