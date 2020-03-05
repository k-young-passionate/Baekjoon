
def result():
    m = []
    for i in range(9):
        m.append(int(input()))

    M = max(m)
    Mi = 0
    for i in range(9):
        if m[i] == M:
            Mi = i
            break

    print(M)
    print(Mi)