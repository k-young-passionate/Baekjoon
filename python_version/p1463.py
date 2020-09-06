from collections import deque

x = int(input())


queue = deque()
queue.append((x, 0))

while len(queue) != 0:
    q = queue.popleft()
    if q[0] < 1:
        continue
    if q[0] == 1:
        print(q[1])
        break
    if q[0] % 3 == 0:
        queue.append((q[0]//3, q[1]+1))
    if q[0] % 2 == 0:
        queue.append((q[0]//2, q[1]+1))

    queue.append((q[0]-1, q[1]+1))