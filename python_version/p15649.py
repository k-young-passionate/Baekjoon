
nums = []

def permutations(n, m):
    if len(nums) == m:
        for i in nums:
            print(i, end=" ")
        print()
        return
    for i in range(1, n+1):
        if i in nums:
            continue
        nums.append(i)
        permutations(n, m)
        nums.pop()


n, m = map(int, input().split())
permutations(n, m)
