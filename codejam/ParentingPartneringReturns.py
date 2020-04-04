from operator import itemgetter
test_cases = int(input())

for test_case in range(test_cases):
    result = ""
    activities = int(input())
    acts = []
    for a in range(activities):
        tmp = list(map(int, input().split()))
        tmp = [tmp[0], tmp[1], a]
        acts.append(tmp.copy())

    acts = sorted(acts, key=itemgetter(0, 1))

    # print(acts)

    c, j = -1, -1
    result_list = []

    for i in acts:
        if c <= i[0]:
            c = i[1]
            result_list.append(["C", i[2]])
            continue
        elif j <= i[0]:
            j = i[1]
            result_list.append(["J", i[2]])
            continue
        else:
            result = "IMPOSSIBLE"
            break
    if len(result_list) == activities:
        result_list = sorted(result_list, key=itemgetter(1))
        for r in result_list:
            result += r[0]
    print("Case #" + str(test_case+1) + ": " + result)