def getSet():
    _inputs = input().split()
    nums = int(_inputs[0])
    index = int(_inputs[1])
    q = input().split()
    q = list(map(int, q))
    return nums, index, q


def find(n, index, q):
    cur = 1
    i = 0
    while True:
        curmax = max(q)
        _idx = i % n
        if q[_idx] != 0 and curmax == q[_idx]:
            # print("cur", q[_idx], ", index:", _idx)
            q[_idx] = 0
            if _idx == index:
                return cur
            cur += 1
        i += 1


def result():
    testcase = int(input())
    for i in range(testcase):
        nums, index, q = getSet()
        r = find(nums, index, q)
        print(r)

    return "exit"