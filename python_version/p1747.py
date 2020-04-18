

n = int(input())

i = 2
prime = []

while True:
    if len(prime) == 0:
        prime.append(i)
    else:
        flag = True
        for p in prime:
            if i % p == 0:
                break
        if flag:
            break
        break

print(prime)