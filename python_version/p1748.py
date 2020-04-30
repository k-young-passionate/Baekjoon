n = int(input())

c = 10
u = 1
s = 0
m = 1
for i in range(9):
    if n >= c:
        s += (u * (c-m))
        m = c
        c *= 10
        u += 1
    else:
        c /= 10
        c = int(c)
        q = n // c
        q -= 1
        r = n % c
        s += ((q *c +r+1) * u)
        break
print(s)



