from collections import deque

def getinput():
    inputs = list(map(int, input().split()))
    return inputs[0], inputs[1]

def go(n, k, visit):
    if n == k:
        return 0
    if n > k:
        limit = n - k
        cnt = 1
        return limit, cnt

    queue = deque()
    if n > 0 and not visit[n - 1]:
        queue.append(n-1)
        visit[n - 1] = 1

    if n < 100000 and not visit[n + 1]:
        queue.append(n+1)
        visit[n + 1] = 1

    if n < 50001 and not visit[n * 2]:
        queue.append(n*2)
        visit[n * 2] = 1

    limit = 10000000
    cnt = 0
    while True:
        if len(queue) == 0:
            break
        # print(queue)

        q = queue.popleft()
        # print(q, visit[q])


        if q == k:
            limit = visit[q]
            cnt += 1


        if limit <= visit[q]:
            continue

        if q > 0:
            queue.append(q - 1)
            visit[q - 1] = visit[q] + 1

        if q < 100000:
            queue.append(q + 1)
            visit[q + 1] = visit[q] + 1

        if q < 50001:
            queue.append(q * 2)
            visit[q * 2] = visit[q] + 1

    return limit, cnt

def result():
    n, k = getinput()
    visit = [0] * 100001
    l, c = go(n,k, visit)
    print(l)
    print(c)
