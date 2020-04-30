
def getinput():
    n = int(input())
    mymap = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        mymap.append(tmp.copy())
    return n, mymap


def result():
    n, mymap = getinput()
    print(mymap)