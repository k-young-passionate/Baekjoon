
def getinput():
    n, l = map(int, input().split())
    roads = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        roads.append(tmp.copy())
    return n, l, roads


def roadcheck(n, l, road): # checks a road valid or not, N
    ramp = []
    flag = 0
    now = 0
    ramp.append(0)

    for i in range(len(road)-1):  # left to right traverse
        r = 0
        if flag == 0:  # normal cases
            if road[i] == road[i+1] + 1:  # starts to add ramps
                flag = 1
                now = road[i+1]
            elif road[i] > road[i+1] + 1:  # gap more than 2
                return False

        if 1 <= flag <= l:  # cases adding ramps
            if road[i+1] == now:  # checks whether it is valid spaces
                if flag == l:  # end of the ramp
                    flag = 0
                else:  # middle of the ramp
                    flag += 1
                r = 1
            else:  # invalid space
                return False
        ramp.append(r)

    if flag > 0:  # handle uncompleted finish
        return False

    flag = 0
    for i in range(len(road)-1, 0, -1):  # right to left traverse
        r = 0
        if flag == 0:  # normal cases
            if road[i] == road[i - 1] + 1:  # starts to add ramps
                flag = 1
                now = road[i-1]
            elif road[i] > road[i - 1] + 1:  # gap more than 2
                return False
        if 1 <= flag <= l:  # cases adding ramps
            if road[i - 1] == now:  # checks whether it is valid spaces
                r = 1
                if flag == l:  # end of the ramp
                    flag = 0
                else:  # middle of the ramp
                    flag += 1
            else:  # invalid space
                return False
        ramp[i-1] += r

    if flag > 0:  # handle uncompleted finish
        return False

    for i in ramp:  # checks whether there is any duplicated ramps on a same place
        if i > 1:
            return False

    return True


def check(n, l, roads):  # checks road one by one and counts the number of valid roads, N
    result = 0
    for i in range(n):  # horizontal check
        road = roads[i].copy()
        if roadcheck(n, l, road):
            result += 1

    for i in range(n):  # vertical check
        road = []
        for j in range(n):
            road.append(roads[j][i])
        if roadcheck(n, l, road):
            result += 1
    return result


if __name__ == "__main__":
    n, l, roads = getinput()
    result = check(n, l, roads)
    print(result)