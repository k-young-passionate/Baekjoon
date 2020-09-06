
x = int(input())

if x > 3:
    dp = [0] * (x+1)
else:
    dp = [0] * 4

dp[2] = 1
dp[3] = 1


for i in range(4, x+1):

    if i % 6 == 0:
        dp[i] = min([dp[i-1] + 1, dp[i//2] + 1, dp[i//3] + 1])
    elif i % 3 == 0:
        dp[i] = min([dp[i-1] + 1, dp[i//3] + 1])
    elif i % 2 == 0:
        dp[i] = min([dp[i-1] + 1, dp[i//2] + 1])
    else:
        dp[i] = dp[i-1] + 1

print(dp[x])