def getinput():  # input 받기
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    people = []  # 사람들 좌표
    ladders = []  # 계단 좌표와 높이
    for i in range(n):
        for j in range(n):
            if space[i][j] == 1:
                people.append((i, j))
            if space[i][j] > 1:
                ladders.append([(i, j), space[i][j]])
    pset = []  # 사람들 가능한 모든 조합
    permutations(people, 0, [], [], pset)
    return n, space, ladders, pset


def permutations(people, idx, exit1, exit2, pset):  # 사람들 가능한 모든 조합 구하기
    if idx == len(people):
        pset.append([exit1, exit2])
        return
    exit1.append(people[idx])
    permutations(people, idx + 1, exit1.copy(), exit2.copy(), pset)
    exit1.pop()
    exit2.append(people[idx])
    permutations(people, idx + 1, exit1.copy(), exit2.copy(), pset)


def distance(p, exit):  # 거리 구하기
    return abs(p[0]-exit[0]) + abs(p[1]-exit[1])


def getout(ladder, pset):  # 나갈 때 까지 걸린 시간
    if len(pset) == 0:  # pset이 비어있을 경우 0 return
        return 0
    people = {}  # 각 사람당 계단 timer
    time = 0  # 걸린 시간
    exit_list = []  # 계단에 있는 사람들
    for pidx in range(len(pset)):  # people 에 계단 timer 저장
        p = pset[pidx]
        people[p] = ladder[1]
        pset[pidx] = [p, distance(p, ladder[0])]
    pset.sort(key=lambda x: x[1])
    time += pset[0][1]
    for i in range(len(pset)):  # 가장 빠르게 계단 도착하는 시간
        pset[i][1] -= time
    while True:  # 모두 나갈 때 까지 time++
        time += 1  # 시간++
        remove_list = []  # exit_list에서 내보낼 후보

        # 남은 시간 빼주고, 탈출한 사람 구하기
        for e in exit_list:
            people[e] -= 1
            if people[e] == 0:
                remove_list.append(e)
        for r in remove_list:
            exit_list.remove(r)

        # 계단 진입 가능한 인원들 들여보내기
        cnt = 0
        for i in range(len(pset)):
            pset[i][1] -= 1
            if pset[i][1] < 0 and len(exit_list) < 3:
                exit_list.append(pset[i][0])
                cnt += 1
        # 계단 진입 시, pset에서 빼주고, 모두 나갔다면 loop 탈출
        if len(pset) == 0:
            if len(exit_list) == 0:
                break
        else:
            pset = pset[cnt:]
    return time


def simulation(ladders, pset):
    time1 = getout(ladders[0], pset[0])  # set1에 대한 계산
    time2 = getout(ladders[1], pset[1])  # set2에 대한 계산
    return max(time1, time2)  # 오랜 시간 출력


test_case = int(input())

for T in range(test_case):
    result = 1000000000000  # 결과 값
    n, space, ladders, pset = getinput()
    for p in pset:  # 모든 경우의 수 시험
        tmpresult = simulation(ladders, p)  # result update
        if tmpresult < result:
            result = tmpresult
    print("#"+str(T+1), result)

