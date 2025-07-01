import math

n = int(input())
li = []
dp = [0] * n
for i in range(n):
    li.append(float(input()))
dp[0] = li[0]
for i in range(1, n):
    dp[i] = max(li[i], dp[i - 1] * li[i])

dp.sort()
temp = round(dp[n - 1], 3)
print(f"{temp:0.3f}")