from collections import deque


def connygo(cur, go):
    cur += go
    return cur, go+1

def check(c, b, time):
    if c[time] == b:
        return True
    else:
        return False

def browngo(cur, cony):
    cango = [cur - 1, cur + 1, cur * 2]
    queue = deque()
    for i in cango:
        if 0 <= i <= 200000:
            queue.append([i, 1])
    while True:
        if len(queue) == 0:
            return -1
        q = queue.popleft()
        # print(q)
        if check(cony, q[0], q[1]):
            return q[1]
        cango = [q[0] - 1, q[0] + 1, q[0] * 2]

        for i in cango:
            if 0 <= i <= 200000:
                queue.append([i, q[1]+1])

C, B = map(int, input().split())
accel = 1
go = 1
status = []
for i in range(1000):
    status.append(C)
    C, go = connygo(C, go)
    if C > 200000:
        break
if C <= 200000:
    status.append(C)
# print(status)
print(browngo(B, status))