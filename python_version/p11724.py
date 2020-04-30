#
#
# def result():
#     tmp_input = input().split()
#     tmp_input = [int(i) for i in tmp_input]
#     conn = []
#     n, m = tmp_input
#
#     parent = [i for i in range(n+1)]
#     for i in range(m):
#         tmp = input().split()
#         tmp = [int(t) for t in tmp]
#         mx = max(tmp)
#         mn = min(tmp)
#         parent[mx] = parent[mn]
#         conn.append(tmp.copy())
#
#     for i in range(1, n+1):
#         for j in range(i, n+1):
#             if parent[j] == i:
#                 parent[j] = parent[i]
#
#     # print(parent)
#
#     counts = [0] * (n+1)
#     cnt = 0
#     for i in parent:
#         counts[i] += 1
#
#     # print(counts)
#     for i in counts:
#         if i != 0:
#             cnt += 1
#
#     print(cnt-1)
#     return 0
import time
def dfs(c, v, conn):
    stack = []
    stack.append(c)
    v[c] = True
    while True:
        if len(stack) == 0:
            break
        print(stack)
        # print(v)
        # time.sleep(1)
        cc = stack[0]
        stack.pop(0)
        for i in conn:
            if i[0] == cc and not v[i[1]]:
                stack.append(i[1])
                v[i[1]] = True
    return v

def getinput():
    tmp_input = input().split()
    tmp_input = [int(i) for i in tmp_input]
    conn = []
    n, m = tmp_input

    for i in range(m):
        tmp = input().split()
        tmp = [int(t) for t in tmp]
        conn.append(tmp.copy())
        conn.append([tmp[1], tmp[0]])

    return n, m, conn

def result():
    st = time.time()
    oh()
    #
    # n, m, conn = getinput()
    # cnt = 0
    # visited = [False] * (n+1)
    # for i in range(1, n+1):
    #     if visited[i]:
    #         continue
    #     cnt += 1
    #     visited = dfs(i, visited, conn)
    # print(cnt)
    end = time.time()
    print((end-st))
adj = []
visited = []

def dsf(v):
  global adj, visited
  visited[v] = True
  for e in adj[v]:
    if not(visited[e]):
      dsf(e)

def oh():
    N, M = map(int, input().split())
    global adj
    adj = [[] for i in range(N + 1)]
    global visited
    visited = [False] * (N + 1)

    cnt = 0

    for i in range(M):
      input_data = list(map(int, input().split()))
      adj[input_data[0]].append(input_data[1])
      adj[input_data[1]].append(input_data[0])

    for i in range(1, len(visited)):
      if not(visited[i]):
        cnt += 1
        dsf(i)
    print(cnt)