n = int(input())


for _ in range(n):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a, b = [0] * 4, [0] * 4
    for ai in range(1, len(A)):
        a[A[ai]-1] += 1
    for bi in range(1, len(B)):
        b[B[bi]-1] += 1

    aa, bb = 0, 0
    for i in range(4):
        aa += a[i] * (1000 ** i)
        bb += b[i] * (1000 ** i)
    print("result: ",aa, bb)

    if aa > bb:
        print('A')
    elif aa < bb:
        print('B')
    else:
        print('D')
    
    