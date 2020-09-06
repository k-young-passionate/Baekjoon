
def solve():
    n = int(input())

    stairs = []
    for _ in range(n):
        stairs.append(int(input()))

    if n == 1:
        print(stairs[0])
        return

    cost = [[(stairs[0], 1)], [(stairs[1], 1), (stairs[1] + stairs[0], 2)]]

    for i in range(2, n):
        candidates = [x for x in cost[i-2]]
        m2 = 0
        for c in candidates:
            if c[0] > m2:
                m2 = c[0]
                c2 = c
        candidates = [x for x in cost[i-1] if x[1] != 2]
        c1 = candidates[0]

        result = []
        result.append((c1[0] + stairs[i], 2))
        result.append((c2[0] + stairs[i], 1))
        cost.append(result.copy())

    print(max([x[0] for x in cost[n-1]]))

solve()