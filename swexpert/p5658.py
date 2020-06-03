
def getinput():
    n, k = map(int, input().split())
    string = input()
    square = [x for x in string]

    return n, k, square


def tonumber(square):
    nums = [str(x) for x in range(10)]
    nums.append('A')
    nums.append('B')
    nums.append('C')
    nums.append('D')
    nums.append('E')
    nums.append('F')

    converter = {}
    for i in range(16):
        converter[nums[i]] = i

    num = 0
    for s in square:
        num += converter[s]
        num *= 16
    num //= 16
    return num

if __name__ == "__main__":
    test_case = int(input())
    for t in range(test_case):
        nums = []
        n, k, square = getinput()
        for i in range(n//4):
            for j in range(4):
                num = tonumber(square[j*(n//4):j*(n//4)+n//4])
                if num not in nums:
                    nums.append(num)
            tmp = square[0]
            square = square[1:]
            square.append(tmp)
        nums.sort(reverse=True)
        # print(nums)
        print("#"+str(t+1),nums[k-1])