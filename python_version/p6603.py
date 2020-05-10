from itertools import combinations


def getinput():
    inputs = []
    while True:
        i = input()
        if i == "0":
            break
        i = list(map(int, i.split()))
        inputs.append(i.copy())
    return inputs


if __name__ == "__main__":
    inputs = getinput()
    for i in inputs:
        r = combinations(i[1:], 6)
        for j in r:
            cnt = 0
            for k in j:
                cnt += 1
                print(k, end="")
                if cnt != 6:
                    print(end=" ")
            print()
        print()