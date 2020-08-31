import time

n = int(input())

balloons = list(map(int, input().split()))
flags = [True] * n

def check(flags):
    for f in flags:
        if f:
            return False
    return True

flags[0] = False
index = 0
moves = balloons[0]
result = [1]
while not check(flags):
    if moves < 0:
        mymove = -1
    else:
        mymove = 1
    while moves:
        index += mymove
        index %= n
        if flags[index]:
            moves -= mymove
    flags[index] = False
    result.append(index+1)
    moves = balloons[index]


for r in result:
    print(r, end=" ")