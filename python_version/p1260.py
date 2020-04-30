
def dfs(v, con):
    stack = []
    out = []
    out.append(v)
    top = -1
    conn = con.copy()
    conn.sort(key=lambda x: x[1], reverse=True)
    for e in conn:
        if e[0] == v:
            stack.append(e)
            top += 1
    while True:
        if top == -1:
            break
        v = stack[top][1]
        stack.pop(top)
        top -= 1
        if v in out:
            continue
        out.append(v)
        for e in conn:
            if e[0] == v:
                stack.append(e)
                top += 1

    return out

def bfs(v, con):
    queue = []
    out = []
    out.append(v)
    conn = con.copy()
    conn.sort(key=lambda x: x[1], reverse=False)

    for e in conn:
        if e[0] == v:
            queue.append(e)
    while True:
        if len(queue) == 0:
            break
        v = queue[0][1]
        queue.pop(0)
        if v in out:
            continue
        out.append(v)
        for e in conn:
            if e[0] == v:
                queue.append(e)

    return out


def getinput():
    conn = []
    ips = input().split()
    ips = [int(i) for i in ips]
    for i in range(ips[1]):
        tmp = input().split()
        tmp = [int(t) for t in tmp]
        conn.append(tmp.copy())

    return ips, conn

def result():
    inputs, conn = getinput()
    n, m, v = inputs
    tmp = []
    for c in conn:
        new_c = [c[1], c[0]]
        tmp.append(new_c.copy())
        # print(new_c)
    for t in tmp:
        conn.append(t.copy())
    # print(conn)a
    dout = dfs(v, conn)
    bout = bfs(v, conn)

    for i in dout:
        print(i, end=" ")
    print()
    for i in bout:
        print(i, end=" ")
    return 0