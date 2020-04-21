from operator import itemgetter


def getinput():  # input 받기
    j, total = map(int, input().split())
    dang = []

    for i in range(j):
        tmp = input().split()
        dang.append([tmp[0], int(tmp[1]), int(tmp[2])])  # name, # of local, # of ratio

    realtotal = 0
    sosok = 0
    for d in dang:
        realtotal += d[2]
        sosok += d[1]

    R = 0
    birye = 0
    rr = []
    for i in range(j):
        rr.append(dang[i][2] / realtotal)
        if rr[i] >= 0.03 or dang[i][1] >= 5:
            birye += dang[i][2]
        else:
            R += dang[i][1]

    p = []  # valid ratio
    for i in range(j):
        if rr[i] >= 0.03 or dang[i][1] >= 5:
            p.append(dang[i][2] / birye)
        else:
            p.append(0)

    musosok = 253 - sosok
    R += musosok
    return 300, R, p, dang, j


def half(N, R, p, dang, numjungdang):  # 전국단위 준연동
    s = []
    # print(p)
    for i in range(numjungdang):
        s_tmp = ((N - R) * p[i] - dang[i][1])/2
        if s_tmp < 1:
            s_tmp = 0
        else:
            s_tmp = round(s_tmp)
        # print(s_tmp)
        if p[i] >= 0.03:
            s.append(s_tmp)
        else:
            s.append(0)
    return s


def cap30(p, s, numjungdang):  # 30석 캡 방식
    S = sum(s)
    tmp_s = []  # 득표비율 별 의석 수 실수 계산
    if S < 30:  # 2-1
        for i in range(numjungdang):
            tmp_s.append(p[i] * (30 - S))
            s[i] += int(tmp_s[i])  # 정숫값 더하기

            tmp_s[i] -= int(tmp_s[i])  # 소숫값만 남기기
            tmp_s[i] = [i, tmp_s[i]]

        rest = 30 - sum(s)  # 남은 의석 수
        tmp_s.sort(key=itemgetter(1), reverse=True)
        index = 0
        # print("s", s)
        while rest > 0:
            rest -= 1
            s[tmp_s[index % numjungdang][0]] += 1
            index += 1

    elif S > 30:  # 2-2
        for i in range(numjungdang):
            tmp_s.append(s[i] * 30 / S)
            s[i] = int(tmp_s[i])
            tmp_s[i] -= int(tmp_s[i])
            tmp_s[i] = [i, tmp_s[i]]

        rest = 30 - sum(s)
        tmp_s.sort(key=itemgetter(1), reverse=True)

        index = 0
        while rest > 0:
            rest -= 1
            s[tmp_s[index % numjungdang][0]] += 1
            index += 1
    return s


def basic(p, numjungdang):  # 17석에 대해 기존 의석배분방식 적용
    b = []
    tmp_b = []
    for i in range(numjungdang):
        tmp_b.append(p[i] * 17)
        b.append(int(tmp_b[i]))
        tmp_b[i] -= int(tmp_b[i])
        tmp_b[i] = [i, tmp_b[i]]

    rest = 17 - sum(b)
    tmp_b.sort(key=itemgetter(1), reverse=True)

    index = 0
    while rest > 0:
        rest -= 1
        b[tmp_b[index % numjungdang][0]] += 1
        index += 1

    return b


N, R, p, dang, j = getinput()

# print(dang)
s = half(N, R, p, dang, j)
# print(s)
s = cap30(p, s, j)
# print(s)
b = basic(p, j)
# print(b)


for i in range(j):
    dang[i].append(dang[i][1] + s[i] + b[i])

dang.sort(key=lambda x: (-x[3], x[0]))

for i in dang:
    print(i[0], i[3])