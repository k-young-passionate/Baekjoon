def getinput():  # input 받기
    n = int(input())
    string = input()
    nums = []  # 숫자만 보관
    ops = []  # 연산자만 보관
    vals = []  # 괄호 가능성 여부만 보관, 0은 가능, 1은 괄호 존재, 2는 괄호 불가
    for s in string:
        if s in list(map(str, range(10))):
            nums.append(int(s))
        else:
            ops.append(s)
            vals.append(0)

    return n, nums, ops, vals


def operate(nums, ops):  # nums, ops 를 이용해 실제 연산
    stack = []
    stackops = []
    stack.append(nums[0])
    for n in range(len(nums[1:])):  # 곱하기들만 미리 계산
        if ops[n] == '*':
            s = stack.pop()
            stack.append(s*nums[n+1])
        else:
            stackops.append(ops[n])
            stack.append(nums[n+1])

    s = stack[0]

    for i in range(len(stack[1:])):  # +, - 계산
        if stackops[i] == '+':
            s += stack[i+1]
        else:
            s -= stack[i+1]

    return s


def precalculate(nums, ops, vals):  # vals 를 이용해 괄호 부분 미리 계산
    shrink = 0
    for i in range(len(vals)):
        if vals[i] == 1:
            if ops[i-shrink] == '+':
                tmp = nums.pop(i-shrink) + nums.pop(i-shrink)
            elif ops[i-shrink] == '-':
                tmp = nums.pop(i-shrink) - nums.pop(i-shrink)
            ops.pop(i - shrink)
            nums.insert(i - shrink, tmp)
            shrink += 1
    return nums, ops


def findresult(nums, ops, vals):  # 모든 괄호 경우의 수를 찾아서 테스트하고 최댓값을 구함
    curmax = operate(nums, ops)
    if len(nums) < 3:
        return curmax
    valslist = [vals.copy()]
    for i in range(len(ops)):  # ops 를 하나씩 탐색
        for qq in valslist:  # valslist 탐색해 ops에 괄호 추가 가능한지 확인
            q = qq.copy()
            flag = False
            if ops[i] in ['+', '-']:  # + 혹은 - 일 때만 추가
                if q[i] == 0:  # 괄호 추가 가능한 경우
                    flag = True
                    q[i] = 1
                    if i == 0:
                        q[i+1] = 2
                    elif i == len(q)-1:
                        q[i-1] = 2
                    else:
                        q[i+1] = 2
                        q[i-1] = 2
            if flag:  # 괄호 추가 시 valslist에 추가
                valslist.append(q.copy())

    for q in valslist:  # 모든 valslist에 대해 연산값 체크
        ns, os = nums.copy(), ops.copy()
        ns, os = precalculate(ns, os, q)
        tmpmax = operate(ns, os)
        if tmpmax > curmax:  # 최댓값 update
            curmax = tmpmax

    return curmax  # 최댓값 return


if __name__ == "__main__":
    n, nums, ops, vals = getinput()
    print(findresult(nums, ops, vals))
