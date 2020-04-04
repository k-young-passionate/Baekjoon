from collections import deque

def getTrace(n, k):
    result = []
    queue = deque()
    for i in range(n):
        queue.append([[i], 0])

    while True:
        if len(queue) == 0:
            break
        q = queue.popleft()
        if q[1] == n-1 and sum(q[0]) == k:
            print("???")
            result.append(q[0])
            continue
        for i in range(n):
            tmp_q = q.copy()
            print(tmp_q)
            queue.append([tmp_q[0].append(i), tmp_q[1]+1])
    return result




test_cases = int(input())

for test_case in range(test_cases):
    n, k = map(int, input().split())

    traceset = getTrace(n, k)
    print(traceset)



