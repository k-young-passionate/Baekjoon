import math


def getinput():
    m, M = map(int, input().split())
    return m, M



def result(m, M):
    m, M = getinput()
    total = M - m + 1
    done = [False] * (M-m+2)
    mm = int(math.sqrt(m))
    MM = int(math.sqrt(M))
    cnt = 0
    for ii in range(2, MM+1):
        i = ii ** 2
        minindex = m // i
        dup = 0
        status = True
        for jj in range(minindex, M // i + 1):
            j = i * jj
            if m <= j <= M:
                if not done[j-m]:
                    done[j - m] = True
                    cnt += 1
                    dup = 0
                    status = False
                elif status:
                    dup += 1
                    if dup == 10:
                        break

    print(total - cnt)

