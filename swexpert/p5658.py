
def getinput():
    n, k = map(int, input().split())
    string = input()
    square = [x for x in string]

    return n, k, square


def tonumber(square):  # 16진수를 10진수로
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
        for i in range(n//4):  # 총 시도해야하는 횟수
            for j in range(4):  # 체크할 변의 수
                num = tonumber(square[j*(n//4):j*(n//4)+n//4])  # 수 뽑아내기
                if num not in nums:  # 중복 방지 추가
                    nums.append(num)
            tmp = square[0]
            square = square[1:]
            square.append(tmp)  # 하나씩 움직이기
        nums.sort(reverse=True)  # 큰 수부터 정렬
        print("#"+str(t+1),nums[k-1])  # k번째 값 출력
