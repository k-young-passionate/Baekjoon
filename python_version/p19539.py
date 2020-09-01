
n = int(input())
trees = list(map(int, input().split()))

if sum(trees) % 3 != 0:
    print("NO")
else:
    d, r = 0, 0
    for i in range(n):
        d += trees[i] // 2
        r += trees[i] % 2

    if r > d:
        print("NO")
    else:
        d -= r
        if d % 3 == 0:
            print("YES")
        else:
            print("NO")
