def getinput():  # input 받기
    n = int(input())
    mymap = [list(map(int, input().split())) for _ in range(n)]

    return n, mymap


# 시작은 무조건 왼쪽 위만 체크
def dfs(n, mymap, src):
    move = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # 대각선 이동
    stack = [[[mymap[src[0]][src[1]]], (src[0] + move[0][0], src[1] + move[0][1]), [(-1, -1)].copy()]]  # dfs용
    cnt = 1  # 들른 카페 수
    while len(stack) > 0:
        s = stack.pop()
        if s[1] == src:  # 출발점에 도착시 out
            if cnt < len(s[0]):
                cnt = len(s[0])
                continue
        if 0 <= s[1][0] < n and 0 <= s[1][1] < n:  # 도시 안이면
            if mymap[s[1][0]][s[1][1]] not in s[0]:  # 중복 카페 가지 않으면
                s[0].append(mymap[s[1][0]][s[1][1]])
                for m in move:
                    newpos = (s[1][0] + m[0], s[1][1] + m[1])
                    if m not in s[2] or m == s[2][-1]:  # 이전에 갔던 방향이 아니거나, 지난번 방향 유지이면 추가 
                        tmpmove = s[2].copy()
                        tmpmove.append(m)
                        stack.append([s[0].copy(), newpos, tmpmove.copy()])
    return cnt


def trial(n, mymap):
    cnt = 0
    for i in range(n):  # 모든 좌표에 대해 dfs
        for j in range(n):
            if (i, j) in [(0, 0), (0, n-1), (n-1, 0), (n-1, n-1)]:
                continue
            tmpcnt = dfs(n, mymap, (i, j))
            if tmpcnt > cnt:
                cnt = tmpcnt
    if cnt < 4:  # 사각형이 아니면
        cnt = -1
    return cnt


test_case = int(input())

for T in range(test_case):
    n, mymap = getinput()
    result = trial(n, mymap)
    print("#"+str(T+1), result)