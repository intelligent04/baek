n = int(input())
li = []
profit = []
dp=[0]*(n+6)

for i in range(n):
    temp = list(map(int,input().split()))
    li.append(temp)

for i in range(n-1,-1,-1):
    if n-i<li[i][0]: #남은 일수계산해서 가능한지 판별
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],li[i][1]+dp[i+li[i][0]])
print(dp[0])