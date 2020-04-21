def getinput():  # get inputs
    size = list(map(int, input().split()))
    office = []
    for i in range(size[0]):
        tmp = list(map(int, input().split()))
        office.append(tmp.copy())

    cameras = []  # cameras info [(position), type, [directions]]
    walls = []  # wall position info
    for i in range(size[0]):
        for j in range(size[1]):
            if office[i][j] not in [0, 6]:
                camera = [(i, j), office[i][j], [0]]

                if office[i][j] == 1:
                    camera[2] = [0]
                elif office[i][j] == 2:
                    camera[2] = [0, 2]
                elif office[i][j] == 3:
                    camera[2] = [0, 1]
                elif office[i][j] == 4:
                    camera[2] = [0, 1, 2]
                elif office[i][j] == 5:
                    camera[2] = [0, 1, 2, 3]
                cameras.append(camera.copy())
            if office[i][j] == 6:
                walls.append([i,j])

    return size, office, cameras, walls


def simulation(size, office, cameras):  # camera sight count
    result = []

    for i in cameras:
        for j in i[2]:
            if j == 0:
                for k in range(i[0][0]-1, -1, -1):
                    pos = (k, i[0][1])
                    if office[k][i[0][1]] == 0 and pos not in result:
                        result.append(pos)
                    elif office[k][i[0][1]] == 6:
                        break
            elif j == 1:
                for k in range(i[0][1]-1, -1, -1):
                    pos = (i[0][0], k)
                    if office[i[0][0]][k] == 0 and pos not in result:
                        result.append(pos)
                    elif office[i[0][0]][k] == 6:
                        break
            elif j == 2:
                for k in range(i[0][0], size[0]):
                    pos = (k, i[0][1])
                    if office[k][i[0][1]] == 0 and pos not in result:
                        result.append(pos)
                    elif office[k][i[0][1]] == 6:
                        break
            elif j == 3:
                for k in range(i[0][1], size[1]):
                    pos = (i[0][0], k)
                    if office[i[0][0]][k] == 0 and pos not in result:
                        result.append(pos)
                    elif office[i[0][0]][k] == 6:
                        break
    return len(result)


def check(size, office, cameras, index):  # change all cameras' direction one by one by recursion, 4^n
    maxresult = 0
    for i in range(4):
        tmp = []
        for c in cameras[index][2]:
            tmp.append((c+i)%4)
        cameras[index][2] = tmp.copy()
        if index == len(cameras) - 1:
            result = simulation(size, office, cameras)
            if result > maxresult:
                maxresult = result
        else:
            result = check(size, office, cameras, index+1)
            if maxresult < result:
                maxresult = result
    return maxresult


if __name__ == "__main__":
    size, office, cameras, walls = getinput()
    if len(cameras) == 0:  # the case there is no camera
        print(size[0]*size[1] - len(walls))
    else:  # general cases
        result = check(size, office, cameras, 0)
        print(size[0] * size[1] - result - len(cameras) - len(walls))