def getinput():
    n = int(input())

    dragon = []
    for _ in range(n):
        x, y, d, g = map(int, input().split())
        dragon.append([(x, y), d, g])

    return n, dragon


def simulation(dragon, pos):  # 실제 방향들의 set을 이용해 찍힌 점의 pos 를 return
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 방향 Index에 맞는 좌표 direction
    tmppos = []  # 방향들 저장해놓은 리스트
    mypos = [dragon[0]]  # 이번 dragon, 시작점 추가 해놓음
    tmppos.append(dragon[1])  # 시작 방향 추가
    while dragon[2] != 0:
        tmpdir = []  # 1회 iteration 의 방향
        for t in tmppos[-1::-1]:  # 방향 역순으로 traverse
            tmp = (t + 1) % 4  # overflow시 원래대로
            tmpdir.append(tmp)
        for t in tmpdir:  # tmppos에 새 방향 추가
            tmppos.append(t)
        dragon[2] -= 1  # 1회 iteration 끝

    for t in tmppos:  # mypos에 tmppos의 방향 값을 좌표 값으로 변환해 저장
        mypos.append((mypos[-1][0] + directions[t][0], mypos[-1][1] + directions[t][1]))

    for m in mypos:  # pos에 저장
        if m not in pos:
            pos.append(m)

    return pos


def getminmax(pos):  # l, u, r, d 극한값 구하기
    l, u, r, d = 100000000, 100000000, -100000000, -100000000
    for p in pos:
        if l > p[0]:
            l = p[0]
        if u > p[1]:
            u = p[1]
        if r < p[0]:
            r = p[0]
        if d < p[1]:
            d = p[1]

    return l, u, r, d


def findrect(pos):  # 사각형 찾기
    l, u, r, d = getminmax(pos)
    cnt = 0
    for i in range(l, r):  # 각각의 limit 값에서 전부 사각형 존재하는지 찾아봄 (시간 많이 걸림)
        for j in range(u, d):
            myrect = [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
            flag = True
            for m in myrect:
                if m not in pos:  # 하나라도 일치 안하면 탈출
                    flag = False
                    break
            if flag:  # 모두 일치하면 cnt++
                cnt += 1
    return cnt


if __name__ == "__main__":
    n, dragons = getinput()
    pos = []
    for dragon in dragons:  # dragon에 대해 하나씩 simulation
        pos = simulation(dragon, pos)

    print(findrect(pos))  # 결과 찾고 출력

