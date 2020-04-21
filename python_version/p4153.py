while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    a = a**2
    b = b**2
    c = c**2

    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b

    if c == a + b:
        print("right")
    else:
        print("wrong")
