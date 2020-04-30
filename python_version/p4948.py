from math import sqrt

def result():
    while True:
        n = int(input())
        if n == 0:
            break
        n2 = 2 * n
        n += 1
        n3 = int(sqrt(n2))
        s = n2 - n + 1
        pn = []
        l = list(map(int, range(n, n2 + 1)))
        for i in range(2, n3 + 1):
            flag = False
            for j in pn:
                if i % j == 0:
                    flag = True
                    break
            if flag:
                continue
            pn.append(i)
        for i in pn:
            q1 = n // i
            if n % i != 0:
                q1 += 1
            q2 = n2 // i
            for j in range(q1, q2+1):
                l[j*i - n] = 0
        r = 0
        for i in l:
            if i != 0:
                r += 1

        print(r)
