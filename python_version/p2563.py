
white = [0] * 100
wp = []
for i in range(100):
    wp.append(white.copy())

n = int(input())
for _i in range(n):
    bp = list(map(int, input().split()))
    for i in range(bp[0], bp[0] + 10):
        for j in range(bp[1]-9, bp[1] + 1):
            wp[j][i] = 1

s = 0
for i in wp:
    for j in i:
        if j == 1:
            s += 1

print(s)