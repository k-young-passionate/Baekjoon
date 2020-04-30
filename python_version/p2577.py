

def result():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    n = n1 * n2 * n3
    cnt = [0] * 10
    while n != 0:
        cnt[n % 10] += 1
        n //= 10

    for i in cnt:
        print(i)