n = int(input())

test_cases = []

for i in range(n):
    test_cases.append(int(input()))


results = [0] * 11
results[1] = 1
results[2] = 2
results[3] = 4

for i in range(4, 11):
    results[i] = results[i-3] + results[i-2] + results[i-1]

for t in test_cases:
    print(results[t])