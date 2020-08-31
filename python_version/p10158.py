w, h = map(int, input().split())
x, y = map(int, input().split())

t = int(input())

xMove = t % (2 * w)
yMove = t % (2 * h)

xList = list(range(x, w+1)) + list(range(w-1, -1, -1)) + list(range(1, x))
yList = list(range(y, h+1)) + list(range(h-1, -1, -1)) + list(range(1, y))

print(xList[xMove], yList[yMove])
