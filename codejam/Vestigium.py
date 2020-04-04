test_case = int(input())

for i in range(test_case):
    n = int(input())
    matrix = []
    for j in range(n):
        tmp = list(map(int, input().split()))
        matrix.append(tmp.copy())

    K = 0
    for j in range(n):
        K += matrix[j][j]

    R, C = 0, 0
    for j in range(n):
        check = [0] * (n + 1)
        for k in matrix[j]:
            check[k] += 1
            if check[k] > 1:
                R += 1
                break

    for j in range(n):
        check = [0] * (n + 1)
        for k in range(n):
            check[matrix[k][j]] += 1
            if check[matrix[k][j]] > 1:
                C += 1
                break

    print("Case #" + str(i + 1) + ":", K, R, C)