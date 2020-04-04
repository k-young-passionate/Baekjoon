def rmdup(mylist):
    c = 0
    results = []
    for i in range(len(mylist)):
        i -= c
        tmp = mylist[i].copy()
        del (mylist[i])
        c += 1
        if tmp not in mylist:
            results.append(tmp)
    return results


def dfs2(mylist):
    stack = []
    index = 0
    results = []
    top = -1
    cur = [-1] * (len(mylist))
    for i in mylist[index]:
        stack.append((i, index))
        top += 1
    while True:
        c = stack[top]
        index = c[1]
        cur[index] = c[0]

        del (stack[top])
        top -= 1

        index += 1
        if index == len(mylist):
            results.append(cur.copy())
        else:
            for i in mylist[index]:
                # print(cur)
                # print(i)
                if i not in cur[:index]:
                    stack.append((i, index))
                    top += 1
        if top == -1:
            break
    return results


def dfs(mylist, curlist, index):
    results = []
    if index == len(curlist) - 1:
        for i in mylist[index]:
            curlist[index] = i
            results.append(curlist.copy())
        return results

    for i in mylist[index]:
        curlist[index] = i
        tmp = dfs(mylist, curlist, index + 1)
        for t in tmp:
            results.append(t.copy())
    return results


def getchar(strings, sample):
    mylist = []
    for e in strings:
        if len(e) == len(sample):
            flag = True
            for i in range(len(e)):
                if e[i] != sample[i] and sample[i] != "*" and e[i] != "*":
                    flag = False
                    break
            if flag:
                mylist.append(e)
    return mylist


def solution(user_id, banned_id):
    answer = 0
    mylists = []
    for b in banned_id:
        mylists.append(getchar(user_id, b))
    curlist = [-1] * len(banned_id)
    comb = dfs2(mylists)


    for c in range(len(comb)):
        comb[c] = set(comb[c])
    rcomb = rmdup(comb)
    answer = len(rcomb)



    return answer