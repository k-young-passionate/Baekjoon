from math import sqrt
def ispalindrome(num):
    n = str(num)

    front = n[:len(n)//2]
    if len(n)%2 == 0:
        addition = 0
    else:
        addition = 1
    back = n[len(n)//2+addition:]
    back = back[::-1]

    if front == back:
        return True
    else:
        return False

def isprime(num):
    if num == 1:
        return False
    s = int(sqrt(num))
    for i in range(2, s+1):
        if num % i == 0:
            return False
    return True



n = int(input())

i = n
prime = []

while True:
    flag = True
    if ispalindrome(i):
        if isprime(i):
            print(i)
            break
    i += 1
# print(prime)