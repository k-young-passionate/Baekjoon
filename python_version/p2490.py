def result():
    for i in range(3):
        li = list(map(int, input().split()))
        s = 0
        rst = ["E", "A", "B", "C", "D"]
        for l in li:
            s += l
        print(rst[4 - s])