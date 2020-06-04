def getinput():  # input 받기
    n, x = map(int,input().split())
    mymap = [list((map(int, input().split()))) for _ in range(n)]
    return n, x, mymap


def check(row, x):  # 해당 열/행이 활주로에 적합한지 확인
    past = row[0]
    ladder = []  # 사다리 설치 여부
    for _ in row:
        ladder.append(False)
    cnt = 1  # 평평한 지대의 길이
    for idx in range(1, len(row)):  # 앞에서 부터 증가하는 부분만 확인
        r = row[idx]
        if r == past:  # 평평시 cnt++
            cnt += 1
            continue
        else:  # 안평평
            if r + 2 == past or r == past + 2:  # 2 차이시 out
                return False
            if r > past:  # 증가 시
                if cnt < x:  # 평평지대가 x보다 짧으면 out
                    return False
                for i in range(1, x+1):  # 평평지대에 사다리 깔기
                    ladder[idx-i] = True
                cnt = 1  # 평평지대 세기 초기화
        past = r  # 이전 것 update
    past = row[-1]
    cnt = 1
    for idx in range(len(row) - 2, -1, -1):  # 거꾸로 세기
        r = row[idx]
        if r == past:
            cnt += 1
            continue
        else:
            if r > past:
                if cnt < x:
                    return False
                for i in range(1, x+1):
                    if ladder[idx+i]:
                        return False
                    ladder[idx+i] = True
                cnt = 1
        past = r
    return True


def trial(n, x, mymap):
    result = 0
    for i in mymap:  # 행 체크
        if check(i, x):
            result += 1
    for i in range(n):  # 열 체크
        col = [m[i] for m in mymap]
        if check(col, x):
            result += 1

    return result


test_case = int(input())
for T in range(test_case):
    n, x, mymap = getinput()
    result = trial(n, x, mymap)
    print("#" + str(T+1), result)