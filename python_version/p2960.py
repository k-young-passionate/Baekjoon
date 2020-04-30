n, k = map(int, input().split())

l = list(map(int, range(2, n+1)))
r = 0
flag = False
while True:
    m = min(l)
    for i in range(n-1):
        if l[i] % m == 0 and l[i] <= n:
            r += 1
            if r == k:
                print(l[i])
                flag = True
                break
            l[i] = n + 1

    if flag:
        break