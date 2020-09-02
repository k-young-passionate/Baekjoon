m = int(input())

ratio = 1
direction = 0
aa, bb = [], []

for i in range(m):
    a, b, s = map(int, input().split())
    aa.append(a)
    bb.append(b)
    direction += s

for i in range(m):
    ratio *= bb[i]

for i in range(m):
    ratio //= aa[i]

print(direction % 2, ratio)
