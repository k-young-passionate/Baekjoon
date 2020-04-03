

N = int(input())
a_tmp = input()
a = a_tmp.split()
A = [int(i) for i in a]

bc = input()
bc = bc.split()
B, C = int(bc[0]), int(bc[1])

sum = N

A = [(i-B) for i in A]
for i in A:
    if i > 0:
        sum += int(i / C)
        i = i - C * int(i / C)
        if i != 0:
            sum += 1


print(sum)