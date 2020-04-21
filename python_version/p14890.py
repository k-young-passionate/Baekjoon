
def getinput():
    n, l = map(int, input().split())
    roads = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        roads.append(tmp.copy())
    return n, l, roads


def roadcheck(n, l, road):
    ramp = []
    flag = 0
    now = 0
    ramp.append(0)
    result = False
    for i in range(len(road)-1):
        r = 0
        if flag == 0:
            if road[i] == road[i+1] + 1:
                flag = 1
                now = road[i+1]
            elif road[i] > road[i+1] + 1:
                return result
        if 1 <= flag <= l:
            if road[i+1] == now:
                if flag == l:
                    flag = 0
                else:
                    flag += 1
                r = 1
            else:
                return False
        ramp.append(r)
    if flag > 0:
        return False
    flag = 0
    for i in range(len(road)-1, 0, -1):
        r = 0
        if flag == 0:
            if road[i] == road[i - 1] + 1:
                flag = 1
                now = road[i-1]
            elif road[i] > road[i - 1] + 1:
                return result
        if 1 <= flag <= l:
            if road[i - 1] == now:
                r = 1
                if flag == l:
                    flag = 0
                else:
                    flag += 1
            else:
                return False
        ramp[i-1] += r
    if flag > 0:
        return False
    for i in ramp:
        if i > 1:
            return result
    return True


def check(n, l, roads):
    result = 0
    for i in range(n):
        road = roads[i].copy()
        if roadcheck(n, l, road):
            result += 1
    for i in range(n):
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