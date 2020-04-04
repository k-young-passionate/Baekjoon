def check(stack):
    flag = True
    ans = 0
    while flag:
        flag = False
        for i in range(len(stack) - 1):
            if stack[i] == stack[i + 1]:
                del (stack[i])
                del (stack[i])
                flag = True
                ans += 2
                break
    return stack, ans


def solution(board, moves):
    answer = 0

    stack = []
    for m in moves:
        for i in range(len(board)):
            cur = board[i][m - 1]
            if cur != 0:
                stack.append(cur)
                board[i][m - 1] = 0
                if len(stack) > 1:
                    stack, ans = check(stack)
                    answer += ans
                break

    return answer