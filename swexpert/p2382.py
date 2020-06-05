
def getinput():
    n, m, k = map(int, input().split())
    micro = {}  # key: 미생물 좌표, value: [size, 방향]
    for _ in range(k):
        c, r, num, dir = map(int, input().split())
        if dir == 1:  # 각 방향에 대해 실 방향으로 update
            dir = (-1, 0)
        elif dir == 2:
            dir = (1, 0)
        elif dir == 3:
            dir = (0, -1)
        else:
            dir = (0, 1)

        micro[(c, r)] = [num, dir]
    return n, m, k, micro


def simulation(n, micro):  # 미생물 이동
    new_micro = {}
    for i in micro:  # 모든 미생물을 움직여 new_micro에 저장
        new_pos = (i[0] + micro[i][1][0], i[1] + micro[i][1][1])
        num = micro[i][0]
        dir = micro[i][1]
        # 혹시나 border에 갈 경우
        if new_pos[0] in [0, n-1] or new_pos[1] in [0, n-1]:
            num = num // 2
            dir = (-dir[0], -dir[1])

        if new_pos not in new_micro:  # 겹칠 수 있으므로 각 좌표에 대해 빈 리스트로 생성
            new_micro[new_pos] = []

        new_micro[new_pos].append([num, dir])  # 리스트에 append

    for i in new_micro:  # 붙은 미생물들 합치기
        if len(new_micro[i]) > 1:  # 여러 군집 섞일 때
            new_micro[i].sort(key=lambda x: x[0], reverse=True)  # sorting
            num = 0
            dir = new_micro[i][0][1]  # 가장 큰 군집의 방향
            for n in new_micro[i]:  # 군집 합치기
                num += n[0]
            new_micro[i] = [num, dir]  # 단일화
        else:
            new_micro[i] = new_micro[i][0]  # 이중 리스트 > 단일 리스트
    micro = new_micro  # micro 를 업데이트
    return micro


def getresult(micro):  # 결과 도출, 있는 모든 key(좌표)의 num값을 더해줌
    result = 0
    for m in micro:
        result += micro[m][0]
    return result


test_case = int(input())

for T in range(test_case):
    result = 0
    n, m, k, micro = getinput()
    for _ in range(m):  # m번 시행
        micro = simulation(n, micro)  # 미생물 현황 update
    # print(micro)
    result = getresult(micro)

    print("#"+str(T+1), result)