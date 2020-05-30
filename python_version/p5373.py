from copy import deepcopy


def getinput():  # input 받기
    test_case = int(input())
    rotate = []
    for _ in range(test_case):
        n = int(input())
        r = input().split()
        tmp = []
        for rr in r:
            idx = 0
            for i in ['U', 'F', 'L', 'B', 'R', 'D']:
                if i == rr[0]:
                    side = idx
                    break
                idx += 1
            tmp.append((side, rr[1]))
        rotate.append([n, tmp.copy()])  # 각 test case 마다 회전 보관

    cube = []
    w, r, g, o, b, y = 'w', 'r', 'g', 'o', 'b', 'y'  # 위, 앞, 왼쪽, 뒤, 오른쪽, 아래
    x = 'x'  # 빈 공간
    for _ in range(3):  # 실제 전개도 모형으로 만듬
        cube.append([x, x, x, w, w, w, x, x, x, x, x, x])
    for _ in range(3):
        cube.append([g, g, g, r, r, r, b, b, b, o, o, o])
    for _ in range(3):
        cube.append([x, x, x, y, y, y, x, x, x, x, x, x])

    return test_case, rotate, cube


def rotate(rotation, cube):  # 회전시키기
    side = rotation[0]  # 회전시킬 대상
    direction = rotation[1]  # 방향

    if side == 0:  # 위 회전
        us, ls, rs, ds = cube[0][3:6], [cube[x][3] for x in range(3)], [cube[x][5] for x in range(3)], cube[2][3:6]  # 해당 side 회전 위함
        if direction == '+':  # 시계방향
            tmp = cube[3][:3]
            for i in range(3, 12):
                cube[3][i - 3] = cube[3][i]
            for i in range(3):
                cube[3][i + 9] = tmp[i]
            for i in range(3):
                cube[i][5] = us[i]
                cube[i][3] = ds[i]
                cube[0][i+3] = ls[2-i]
                cube[2][i+3] = rs[2-i]
        else:  # 반시계방향
            tmp = cube[3][9:]
            for i in range(0, 3):
                for j in range(0, 3):
                    cube[3][j + 3 * (3 - i)] = cube[3][j + 3 * (2 - i)]
            for i in range(3):
                cube[3][i] = tmp[i]
            for i in range(3):
                cube[i][5] = ds[2-i]
                cube[i][3] = us[2-i]
                cube[0][i+3] = rs[i]
                cube[2][i+3] = ls[i]
    elif side == 5:  # 바닥
        us, ls, rs, ds = cube[6][3:6], [cube[x+6][3] for x in range(3)], [cube[x+6][5] for x in range(3)], cube[8][3:6]
        if direction == '-':
            tmp = cube[5][:3]
            for i in range(3, 12):
                cube[5][i - 3] = cube[5][i]
            for i in range(3):
                cube[5][i + 9] = tmp[i]
            for i in range(3):
                cube[i+6][5] = ds[2-i]
                cube[i+6][3] = us[2-i]
                cube[6][i+3] = rs[i]
                cube[8][i+3] = ls[i]
        else:
            tmp = cube[5][9:]
            for i in range(0, 3):
                for j in range(0, 3):
                    cube[5][j + 3 * (3 - i)] = cube[5][j + 3 * (2 - i)]
            for i in range(3):
                cube[5][i] = tmp[i]
            for i in range(3):
                cube[i+6][3] = ds[i]
                cube[i+6][5] = us[i]
                cube[6][i+3] = ls[2-i]
                cube[8][i+3] = rs[2-i]
    elif side == 1:  # 앞
        us, ls, rs, ds = cube[3][3:6], [cube[x+3][3] for x in range(3)], [cube[x+3][5] for x in range(3)], cube[5][3:6]
        u = deepcopy(cube[2][3:6])
        l = [cube[x][2] for x in range(3, 6)]
        r = [cube[x][6] for x in range(3, 6)]
        d = deepcopy(cube[6][3:6])
        if direction == "+":
            for i in range(3, 6):
                cube[i][2] = d[i - 3]
                cube[i][6] = u[i - 3]
                cube[2][i] = l[5 - i]
                cube[6][i] = r[5 - i]
            for i in range(3):
                cube[i + 3][3] = ds[i]
                cube[i + 3][5] = us[i]
                cube[3][i + 3] = ls[2 - i]
                cube[5][i + 3] = rs[2 - i]
        else:
            for i in range(3, 6):
                cube[i][2] = u[5 - i]
                cube[i][6] = d[5 - i]
                cube[2][i] = r[i - 3]
                cube[6][i] = l[i - 3]
            for i in range(3):
                cube[i + 3][3] = us[2 - i]
                cube[i + 3][5] = ds[2 - i]
                cube[3][i + 3] = rs[i]
                cube[5][i + 3] = ls[i]
    elif side == 3:  # 뒤
        us, ls, rs, ds = cube[3][9:], [cube[x+3][9] for x in range(3)], [cube[x+3][11] for x in range(3)], cube[5][9:]
        u = deepcopy(cube[0][3:6])
        r = [cube[x][0] for x in range(3, 6)]
        l = [cube[x][8] for x in range(3, 6)]
        d = deepcopy(cube[8][3:6])
        if direction == "+":
            for i in range(3, 6):
                cube[i][0] = u[5 - i]
                cube[i][8] = d[5 - i]
                cube[0][i] = l[i - 3]
                cube[8][i] = r[i - 3]
            for i in range(3):
                cube[i + 3][9] = ds[i]
                cube[i + 3][11] = us[i]
                cube[3][i + 9] = ls[2 - i]
                cube[5][i + 9] = rs[2 - i]
        else:
            for i in range(3, 6):
                cube[i][0] = d[i - 3]
                cube[i][8] = u[i - 3]
                cube[0][i] = r[5 - i]
                cube[8][i] = l[5 - i]

            for i in range(3):
                cube[i + 3][9] = us[2 - i]
                cube[i + 3][11] = ds[2 - i]
                cube[3][i + 9] = rs[i]
                cube[5][i + 9] = ls[i]
    elif side == 2:  # 좌
        us, ls, rs, ds = cube[3][:3], [cube[x+3][0] for x in range(3)], [cube[x+3][2] for x in range(3)], cube[5][:3]
        u = [cube[x][3] for x in range(3)]
        r = [cube[x+3][3] for x in range(3)]
        l = [cube[x+3][11] for x in range(3)]
        d = [cube[x+6][3] for x in range(3)]
        if direction == "+":
            for i in range(3):
                cube[i+3][11] = d[2 - i]
                cube[i+3][3] = u[i]
                cube[i][3] = l[2 - i]
                cube[i+6][3] = r[i]
            for i in range(3):
                cube[i + 3][0] = ds[i]
                cube[i + 3][2] = us[i]
                cube[3][i] = ls[2 - i]
                cube[5][i] = rs[2 - i]
        else:
            for i in range(3):
                cube[i+3][11] = u[2 - i]
                cube[i+3][3] = d[i]
                cube[i][3] = r[i]
                cube[i+6][3] = l[2 - i]
            for i in range(3):
                cube[i + 3][0] = us[2 - i]
                cube[i + 3][2] = ds[2 - i]
                cube[3][i] = rs[i]
                cube[5][i] = ls[i]
    elif side == 4:  # 우
        us, ls, rs, ds = cube[3][6:9], [cube[x+3][6] for x in range(3)], [cube[x+3][8] for x in range(3)], cube[5][6:9]
        u = [cube[x][5] for x in range(3)]
        r = [cube[x+3][9] for x in range(3)]
        l = [cube[x+3][5] for x in range(3)]
        d = [cube[x+6][5] for x in range(3)]
        if direction == "+":
            for i in range(3):
                cube[i+3][5] = d[i]
                cube[i+3][9] = u[2 - i]
                cube[i][5] = l[i]
                cube[i+6][5] = r[2 - i]
            for i in range(3):
                cube[i + 3][6] = ds[i]
                cube[i + 3][8] = us[i]
                cube[3][i + 6] = ls[2 - i]
                cube[5][i + 6] = rs[2 - i]
        else:
            for i in range(3):
                cube[i+3][5] = u[i]
                cube[i+3][9] = d[2-i]
                cube[i][5] = r[2 - i]
                cube[i+6][5] = l[i]
            for i in range(3):
                cube[i + 3][6] = us[2 - i]
                cube[i + 3][8] = ds[2 - i]
                cube[3][i + 6] = rs[i]
                cube[5][i + 6] = ls[i]


def debug(cube, ro):  # debug 용, result 대신 사용
    print('=======',ro,"========")
    idx2 = 0
    for c in cube:
        idx = 0
        if idx2%3 ==0:
            print("-------------------")
        idx2 += 1
        for cc in c:
            if idx %3 == 0:
                print("|", end="")
            idx += 1
            if cc == "x":
                print(" ", end="")
            else:
                print(cc, end="")
        print()
    print('===============')


def result(cube):  # 실제 답안 결과 출력용
    for cb in cube[:3]:
        for c in cb[3:6]:
            print(c, end="")
        print()


if __name__ == "__main__":
    tc, rotations, cube = getinput()
    for rs in rotations:  # 각 testcase 순회
        newcube = deepcopy(cube)  # 원래의 cube 변환 방지
        for r in rs[1]:  # 각 회전 순회
            rotate(r, newcube)  # 회전
        result(newcube, r)  # testcase 별 결과 출력

