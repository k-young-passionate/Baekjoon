def getinput():  # input 받기
    r, c, t = map(int, input().split())
    mymap = [list(map(int, input().split())) for _ in range(r)]
    upper = []  # 위쪽 청정기 cycle 해당되는 좌표
    lower = []  # 아랫쪽 청정기 cycle 해당되는 좌표
    for i in range(r):
        for j in range(c):
            if mymap[i][j] == -1:
                for jj in range(j+1, c-1):
                    upper.append((i, jj))
                for ii in range(i, 0, -1):
                    upper.append((ii, c-1))
                for jj in range(c-1, 0, -1):
                    upper.append((0, jj))
                for ii in range(i):
                    upper.append((ii, 0))

                i+=1
                for jj in range(j+1, c-1):
                    lower.append((i, jj))
                for ii in range(i, r-1):
                    lower.append((ii, c-1))
                for jj in range(c-1, 0, -1):
                    lower.append((r-1, jj))
                for ii in range(r-1, i, -1):
                    lower.append((ii, 0))

                return (r, c), t, mymap, upper, lower


def microdust(size, mymap):  # 미세먼지의 확산
    R, C = size
    dusts = []
    dustamount = []
    for i in range(R):  # 미세먼지 좌표와 기존 값 저장
        for j in range(C):
            if mymap[i][j] > 0:
                dusts.append((i,j))
                dustamount.append(mymap[i][j])

    index = 0
    for d in dusts:  # 일일이 돌며 확산
        addition = dustamount[index] // 5
        index += 1
        candidates = [(d[0]-1, d[1]), (d[0]+1, d[1]), (d[0], d[1]-1), (d[0], d[1]+1)]
        for c in candidates:
            if 0 <= c[0] < R and 0 <= c[1] < C:
                if mymap[c[0]][c[1]] >= 0:
                    mymap[c[0]][c[1]] += addition
                    mymap[d[0]][d[1]] -= addition


def circulate(mymap, upper, lower):  # 공기청정기의 활동
    upast = upper[-1]
    for u in upper[-2::-1]:  # 뒤의 좌표를 앞의 좌표 값으로 이동
        mymap[upast[0]][upast[1]] = mymap[u[0]][u[1]]
        upast = u
    mymap[upast[0]][upast[1]] = 0  # 맨 처음 좌표에는 0

    lpast = lower[-1]
    for l in lower[-2::-1]:
        mymap[lpast[0]][lpast[1]] = mymap[l[0]][l[1]]
        lpast = l
    mymap[lpast[0]][lpast[1]] = 0


def debug(mymap):  # 디버그용 코드
    print("===================")
    for mm in mymap:
        for m in mm:
            print(m, end="\t")
        print()
    print("===================")


def result(mymap):  # 미세먼지 수 count
    dusts = 0
    for mm in mymap:
        for m in mm:
            if m != -1:
                dusts += m
    return dusts

if __name__ == "__main__":
    size, t, mymap, upper, lower = getinput()
    for i in range(t):  # t번 반복
        microdust(size, mymap)  # 미세먼지 확산
        # debug(mymap)
        circulate(mymap, upper, lower)  # 공기청정기 역할
        # debug(mymap)
    print(result(mymap))  # 결과 출력