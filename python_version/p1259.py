while True:
    n = input()
    if n == "0":  # break condition
        break

    margin = len(n) % 2  # check whether odd number or not
    front = n[:len(n)//2]  # get the first half of the string
    back = n[len(n)//2 + margin:]  # get the last half of the string
    if front == back[::-1]:  # compare each half
        print('yes')
    else:
        print('no')