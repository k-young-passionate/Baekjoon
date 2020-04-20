t = int(input())

result = []
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h

    if h == 1:  # exception case for a one-story hotel
        number = n
        floor = 1
    else:  # general cases
        number = n // h + 1
        if floor == 0:  # the top floor cases
            floor += h
            number -= 1

    if number >= 10:  # string handling for matching the room number format
        result.append(str(floor) + str(number))
    else:
        result.append(str(floor) + "0" + str(number))

for i in result:  # print all things at a time
    print(i)