

n = int(input())

grades = list(map(int, input().split()))

print(max(grades) - min(grades))