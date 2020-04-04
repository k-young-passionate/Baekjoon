from collections import deque

test_case = int(input())

for t in range(test_case):
    result = ""
    string = input()

    stack = deque()
    index = -1
    for i in string:
        if index == -1:
            for j in range(int(i)):
                stack.append("(")
            stack.append(i)
            index += (int(i) + 1)
        else:
            diff = int(stack[index]) - int(i)
            if diff > 0:
                for j in range(diff):
                    stack.append(")")
                stack.append(i)
                index += (diff + 1)
            elif diff < 0:
                diff *= -1
                for j in range(diff):
                    stack.append("(")
                stack.append(i)
                index += (diff + 1)
            else:
                stack.append(i)
                index += 1
    last = int(stack[index])
    for i in range(last):
        stack.append(")")

    for i in stack:
        result += i
    print("Case #" + str(t) + ":", result)