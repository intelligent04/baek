n = int(input())
dp = []
li = []
for i in range(n):
    temp = int(input())
    li.append(temp)
if n <= 2:
    print(sum(li))
elif n == 3:
    print(max(li[0] + li[2], li[1] + li[2]))
else:
    dp.append(li[0])
    dp.append(li[0] + li[1])
    dp.append(max(li[0] + li[2], li[1] + li[2]))
    for i in range(3, n):
        dp.append(max(li[i] + dp[i - 2], li[i] + li[i - 1] + dp[i - 3]))
    print(dp[-1])
