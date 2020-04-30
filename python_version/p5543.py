def result():
    l = []
    for i in range(5):
        l.append(int(input()))
    b = l[:3]
    d = l[3:]

    total = min(b) + min(d) - 50

    print(total)