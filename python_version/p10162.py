T = int(input())
A, B, C = 0, 0, 0
a, b, c = 300, 60, 10

A = T // a
T -= a * A
B = T // b
T -= b * B
C = T // c
T -= C * c

if T != 0:
    print(-1)
else:
    print(A,B,C)