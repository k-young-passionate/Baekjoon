def getinput():  # get input
    _size = list(map(int, input().split()))
    _pos = list(map(int, input().split()))
    _mymap = []
    for i in range(_size[0]):
        tmp = list(map(int, input().split()))
        _mymap.append(tmp.copy())

    return _size, _pos, _mymap


def checkresult(_pos):  # get the number of the cleaned tile
    result = 0
    for i in _pos:
        for j in i:
            if j == 2:
                result += 1

    return result


def show(_mymap, _pos):  # debug code to show current map
    for i in range(len(_mymap)):
        for j in range(len(_mymap[0])):
            if i == _pos[0] and j == _pos[1]:
                print("X", end=" ")
            else:
                print(_mymap[i][j], end=" ")
        print()
    print('=========================')


def act(_pos, _mymap):  # clear move
    go = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    flag = 0
    while True:
        _mymap[_pos[0]][_pos[1]] = 2  #clean
        left = (_pos[2] + 3) % 4  # turn 90 degree
        if left == 0:
            togo = go[0]
        elif left == 1:
            togo = go[1]
        elif left == 2:
            togo = go[2]
        else:
            togo = go[3]
        index1 = _pos[0] + togo[0]
        index2 = _pos[1] + togo[1]
        _pos[2] = left
        if _mymap[index1][index2] == 0:  # if it has not been cleaned
            _pos[0] = index1
            _pos[1] = index2
            flag = 0
        else:  # if it has been cleaned
            flag += 1
            if flag == 4:  # if it checked all sides
                flag = 0
                index1 = _pos[0] + togo[0] * -1
                index2 = _pos[1] + togo[1] * -1
                if _mymap[index1][index2] == 1:  # if the back side is a wall
                    break
                else:  # if the back side is a cleaned tile
                    _pos[0] = index1
                    _pos[1] = index2
            else:  # if it finds an uncleaned tile
                None

    return _mymap


if __name__ == "__main__":
    size, pos, mymap = getinput()
    mymap = act(pos, mymap)
    result = checkresult(mymap)
    print(result)