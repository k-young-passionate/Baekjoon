n = int(input())

houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))

colors = [houses[0]]

for i in range(1, n):
    rgb = []
    for j in range(3):
        rgb.append(houses[i][j] + min([colors[i - 1][(j + 1) % 3], colors[i - 1][(j + 2) % 3]]))
    colors.append(rgb.copy())

print(min(colors[-1]))