s = int(input())

ss = 0
for i in range(1,s+1):
    ss += i
    if ss == s:
        print(i)
        break
    elif ss > s:
        print(i-1)
        break