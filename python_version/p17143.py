def getinput():  # 인풋받기, 자료형 잘 정하자!
    R, C, M = map(int, input().split())
    sharks = {}  # dictioinary 에 상어 위치 저장
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        if d <= 2:  # 위아래 0 / 좌우 1, 방향은 고정하고, speed를 +-로 바꿈
            if d == 1:
                s *= -1
            d = 0
        else:
            if d == 4:
                s *= -1
            d = 1
        sharks[r, c] =  [s, d, z]  # 스피드, 방향, 사이즈 순

    return R, C, M, sharks


def getshark(r, c, sharks):  # 상어 잡기
    minrow = r+1
    for i in range(1, r+1):  # 가장 가까이에 있는 상어 잡기
        if (i, c) in sharks:
            if minrow > i:
                minrow = i
    if minrow == r+1:  # 상어 없으면 0 리턴
        return 0

    size = sharks[(minrow, c)][2]
    sharks.pop((minrow, c))
    return size  # 잡은 상어 크기 리턴


def sharkmove(R, C, sharks):  # 상어 이동시키기
    newsharks = {}  # 새로운 상어 위치 저장용
    for pos in sharks:  # 모든 상어에 대해 움직임
        s = sharks[pos]
        r, c = pos
        if s[1] == 0:  # 상어가 위아래로 움직일 때
            r += s[0]  # 상어 이동
            while not (0 < r <= R):  # 이동 후 위치 정상화 (bound 밖으로 나가면 정정)
                if r > R:
                    r = R - (r - R)
                    s[0] *= -1
                if r < 1:
                    r *= -1
                    r += 2
                    s[0] *= -1
        else:  # 상어가 좌우로 움직일 때
            c += s[0]
            while not (0 < c <= C):
                if c > C:
                    c = C - (c - C)
                    s[0] *= -1
                if c < 1:
                    c *= -1
                    c += 2
                    s[0] *= -1

        if (r, c) not in newsharks:
            newsharks[(r, c)] = []
        newsharks[(r, c)].append([s[0], s[1], s[2]])  # 상어 추가
    newsharks = sharkeat(newsharks)  # 위치 겹칠 경우 잡아먹기
    return newsharks


def sharkeat(sharks):  # 같은 위치에 대해 상어를 하나만 남김
    for pos in sharks:  # 모든 위치 체크
        if len(sharks[pos]) > 1:  # 겹치는 상어 존재 시, 가장 큰 상어만 남김김
            maxsize = 0
            for s in sharks[pos]:
                if maxsize < s[2]:
                    maxsize = s[2]
                    maxs = s
            sharks[pos] = maxs
        else:  # 상어 혼자 시, 이중 array를 단일 array 로 변환
            sharks[pos] = sharks[pos][0]
    return sharks


def debug(r, c, sharks, i, size):  # 디버그용 출력용
    print(sharks)
    print("===========",i,"============")
    for j in range(1, c+1):
        print(j, end="| ")
    print()
    for i in range(1,r+1):
        for j in range(1,c+1):
            if (i, j) in sharks:
                print(sharks[(i,j)][2], end="| ")
            else:
                print(" ", end="| ")
        print()
    print("=======",size, "=======")

if __name__ == "__main__":
    r, c, m, sharks = getinput()
    sizes = 0  # 총 사이즈
    for i in range(1, c+1):  # 낚시왕 이동
        # debug(r, c, sharks, i, sizes)
        sizes += getshark(r, i, sharks)  # 상어 잡기
        if i != c:
            sharks = sharkmove(r, c, sharks)  # 상어 이동

    print(sizes)  # 결과 출력