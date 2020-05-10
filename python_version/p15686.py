from itertools import combinations

def getinput():
    n, m = map(int, input().split())

    mymap = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        mymap.append(tmp.copy())

    chicken = []
    home = []

    for i in range(n):
        for j in range(n):
            if mymap[i][j] == 1:
                home.append([i, j, -1])
            elif mymap[i][j] == 2:
                chicken.append([i, j])

    return n, m, mymap, home, chicken


def dist(src, chicken):
    distance = 0
    for i in chicken:
        tmp = abs(i[0]-src[0]) + abs(i[1]-src[1])
        if distance == 0:
            distance = tmp
        elif distance > tmp:
            distance = tmp
    return distance


def distall(home, chicken):
    total = 0
    for i in home:
        total += dist(i, chicken)
    return total


def simulation(n, m, home, chicken):
    c = combinations(chicken, m)
    score = 0
    for i in c:
        tmp = distall(home, i)
        if score == 0:
            score = tmp
        elif score > tmp:
            score = tmp
    return score


if __name__ == "__main__":
    n, m, mymap, home, chicken = getinput()
    print(simulation(n, m, home, chicken))