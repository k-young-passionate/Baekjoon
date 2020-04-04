def solution(s):
    answer = []
    s = s[1:-1]
    s = s.split("},")
    for i in range(len(s)):
        s[i] = s[i][1:]
        if s[i][-1] == '}':
            s[i] = s[i][:-1]
        s[i] = s[i].split(',')
        s[i] = list(map(int, s[i]))

    s = sorted(s, key=len)

    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer