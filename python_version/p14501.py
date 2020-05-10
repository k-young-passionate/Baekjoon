def findMax(n, sch):
    s = 0
    for i in range(0, n):
        if i + sch[i][0] <= n:
            # print("================", i, "==================")
            r = bruteforce(i, n, 0, sch)
            if r > s:
                s = r
    print(s)

def bruteforce(index, n, s, sch):
    s += sch[index][1]
    start = s
    add = sch[index][0]

    for i in range(index + add, n):
        if i + sch[i][0] <= n:
            # print(i, "in with", start)
            r = bruteforce(i, n, start, sch)
            # print("r[", i,"]: ", r)
            if r > s:
                s = r

    return s

def get( n ):
    r = []
    for i in range(n):
        got = input()
        got = got.split()
        got = (int(got[0]), int(got[1]))
        r.append(got)
    return r


if __name__ == "__main__":
    N = int(input())
    schedule = get(N)
    findMax(N, schedule)