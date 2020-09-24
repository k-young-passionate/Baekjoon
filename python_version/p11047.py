n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for c in coins:
    divisor = k // c
    cnt += divisor
    k -= divisor * c

print(cnt)