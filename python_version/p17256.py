




# b.x = c.x - a.z
# b.y = c.y / a.y
# b.z = c.z - a.x
def result():
    a = input().split()
    c = input().split()
    a = list(map(int, a))
    c = list(map(int, c))

    b = [c[0] - a[2] , int(c[1] / a[1]), c[2] - a[0]]

    r = ""
    for i in b:
        r += str(i) + " "
    print(r)