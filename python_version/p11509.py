n = int(input())

hs = list(map(int, input().split()))

cnt = 0
result = 0
while cnt < n:
    result += 1
    m = max(hs)
    for i in range(n):
        if m == hs[i]:
            hs[i] = -1
            m -= 1
            cnt += 1

print(result)