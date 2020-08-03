arrows = {}
lensum = 0

n = int(input())

for _ in range(n):
    pos, color = map(int, input().split())
    if color not in arrows:
        arrows[color] = []
    arrows[color].append(pos)

for a in arrows:
    arrows[a].sort()
    for i in range(len(arrows[a])):
        left = 10000000000000
        right = 10000000000000
        
        if i != 0:
            left = (arrows[a][i] - arrows[a][i-1])
        if i != len(arrows[a]) - 1:
            right = (arrows[a][i+1] - arrows[a][i])
        
        lensum += min([left, right])

print(lensum)