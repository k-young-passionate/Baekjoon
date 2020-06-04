def getinput():  # input 받기
    k = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    rot = [list(map(int, input().split())) for _ in range(k)]
    head = [0, 0, 0, 0]  # 각 자석의 머리가 어디인지
    for i in range(k):  # 각 좌석 index--, 방향을 시계 0, 반시계 1
        rot[i][0] -= 1
        if rot[i][1] == 1:
            rot[i][1] = 0
        else:
            rot[i][1] = 1
    return k, mag, rot, head


def rotate(mag, rot, head):  # 실제 회전시키기
    direction = [7, 1, 0]  # 시계, 반시계, 그대로 
    target = rot[0]  # 돌리는 자석 index
    todir = {}  # 각 자석의 회전 방향 저장
    for i in range(4):  # 기본 값으로 무회전 저장
        todir[i] = 2
    todir[target] = rot[1]  # target의 회전 방향 저장
    past = target
    for i in range(target-1, -1, -1):  # 이전 것에 의한 회전 왼쪽으로 탐색
        if mag[past][(head[past]+6)%8] == mag[i][(head[i]+2)%8]:  # 극이 같으면 그대로
            break
        else:  # 극이 다르면 움직임
            todir[i] = abs(todir[past]-1)
        past = i

    past = target
    for i in range(target+1, 4):  # 이전 것에 의한 회전 오른쪽으로 탐색
        if mag[past][(head[past]+2)%8] == mag[i][(head[i]+6)%8]:
            break
        else:
            todir[i] = abs(todir[past]-1)
        past = i

    for i in range(4):  # 실제로 head 움직임
        head[i] = (head[i] + direction[todir[i]]) % 8


def result(mag, head):  # 각 점수 구하기
    r = 0
    for i in range(4):
        r += (mag[i][head[i]] * (2**i))
    return r


test_case = int(input())

for T in range(test_case):
    k, mag, rots, head = getinput()
    for rot in rots:
        rotate(mag, rot, head)
    print("#" + str(T+1), result(mag, head))