n, k = map(int, input().split())
li = []
dp = [1] * (n + 1)
stack = 1
for i in range(n):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: x[1:], reverse=True)
li.insert(0, [])
for i in range(2, n + 1):
    if li[i][1:] == li[i - 1][1:]:
        dp[i] = dp[i - 1]
        stack += 1
    else:
        dp[i] += stack
        stack += 1
for i in range(1, n + 1):
    if li[i][0] == k:
        print(dp[i])
