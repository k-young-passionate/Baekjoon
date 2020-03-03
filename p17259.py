

def getSet(n):
    emps = []
    for i in range(n):
        _e = input().split()
        emp = [(int(_e[0]), int(_e[1])), int(_e[2]), 0]
        emps.append(emp)
    return emps

def realmove(f, b, m, i, j):
    if i == 0 and j == 0 and m > 0:
        f[i][j] = 1
    else:
        f[i][j] = 0
    if i == 0 and j != 0:
        f[i][j] = f[i][j - 1]
    if i == b - 1 and j != b - 1:
        f[i][j] = f[i][j + 1]
    if j == b - 1 and i != 0:
        f[i][j] = f[i - 1][j]
    return f

def move(f, b, m):
    # print("curM: ", m)
    trash = 0
    if f[b-1][0] == 1:
        trash = 1
    for i in range(b):
        f = realmove(f, b, m, b-1, i)
    for i in range(b-1, -1, -1):
        f = realmove(f, b, m, i, b-1)
    for i in range(b-1, -1, -1):
        f = realmove(f, b, m, 0, i)

            # print("i, j: ", i, j)
            # print(f)
    return f, trash

def check(f, e):
    if f[e[0][0]+1][e[0][1]] == 1:
        return e[0][0] + 1, e[0][1]
    elif f[e[0][0]][e[0][1]+1] == 1:
        return e[0][0], e[0][1] + 1
    elif f[e[0][0]-1][e[0][1]] == 1:
        return e[0][0] - 1, e[0][1]
    return [-1, -1]

def checkandwork(f, e):
    e = work(e)
    for i in range(len(e)):
        c = check(f, e[i])
        if e[i][2] <= 0 and c[0] != -1:
            e[i][2] = e[i][1]
            f[c[0]][c[1]] = 0
    return f, e



def work(e):
    for i in range(len(e)):
        if e[i][2] >= 0:
            e[i][2] -= 1
    return e

def result():
    b, n, m = input().split()
    b, n, m = int(b), int(n), int(m)
    emps = getSet(n)

    f = [0].copy() * b
    factory = []
    for i in range(b):
        factory.append(f.copy())
    # factory[0][0] = 1
    t = 0
    for i in range(b*3 + m - 1):
        # print("TIEM:", i)
        # for j in factory:
        #     print(j)
        # print()
        factory, trash = move(factory, b, m - i)
        factory, emps = checkandwork(factory, emps)
        t += trash
    # print(emps)
    # print(factory)
    print(m - t)