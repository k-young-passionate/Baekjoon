def findroom(d, rn):
    final = rn
    crn = rn
    l = []
    while True:
        l.append(crn)
        # print(crn)
        if crn in d:
            crn = d[crn]
        else:
            final = crn
            for i in l:
                d[i] = final + 1
            break
    # print(final)
    # print(l)
    # print(d)
    return final

def solution(k, room_number):
    answer = []
    d = {}
    for i in room_number:
        # print('========================')
        answer.append(findroom(d, i))

    return answer