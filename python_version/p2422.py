n , m = map(int, input().split())

enemy = {}

for i in range(1, n+1):
    enemy[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    a, b = min([a, b]), max([a, b])
    enemy[a].append(b)


result = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        if j in enemy[i]:
            continue
        for k in range(j+1, n+1):
            if k in enemy[j] or k in enemy[i]:
                continue
            result += 1

print(result)
