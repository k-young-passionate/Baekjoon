

def spring(mymap, trees):




def getinput():
    tmpnmk = input().split()
    tmpnmk = [int(e) for e in tmpnmk]
    N, M, K = tmpnmk[0], tmpnmk[1], tmpnmk[2]

    mymap = []
    trees = []

    for i in range(N):
        tmpmap = input().split()
        tmpmap = [ int(t) for t in tmpmap ]
        mymap.append(tmpmap.copy())

    for i in range(M):
        tmp = input().split()
        tmp = [ int(e) for e in tmp ]
        trees.append([(tmp[0], tmp[1]), tmp[2], True])

    for i in range(N):
        for j in range(N):
            tmp = []
            for j in trees:
                if j[1] == i:
                    tmp.append(j.copy())


    return N, M, K, mymap, trees


def result():
    n, m, k, mymap, trees = getinput()
    print(n, m, k)
    print(mymap)
    print(trees)
    return 0