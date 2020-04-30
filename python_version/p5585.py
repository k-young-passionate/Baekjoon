
def result():
    pay = int(input())

    pay = 1000 - pay
    change = [500, 100, 50, 10, 5, 1]
    r = 0
    for i in change:
        q = pay // i
        pay -= (q * i)
        r += q

    print(r)