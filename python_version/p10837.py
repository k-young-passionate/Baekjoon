k = int(input())

c = int(input())
test = []
for _ in range(c):
    m, n = map(int, input().split())
    test.append((m, n))

for i in range(c):
    m, n = test[i]
    left = k - max([m, n])
    if m > n:
        if m > left + n + 2:
            print(0)
        else:
            print(1)
    elif m < n:
        if n > left + m + 1:
            print(0)
        else:
            print(1)
    else:
        print(1)