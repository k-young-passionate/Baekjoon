x, y, w, h = map(int, input().split())

candidate = [x, y, w - x, h - y]  # left to x, bottom to y, right to x, top to y

print(min(candidate))  # get the minimum value among candidates
