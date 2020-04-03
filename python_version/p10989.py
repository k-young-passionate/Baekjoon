cnt = [0] * 10001
n = int(input())

for i in range(n):
    cnt[int(input())] += 1

# print(cnt)
for i in range(10001):
    for j in range(cnt[i]):
        print(i)
