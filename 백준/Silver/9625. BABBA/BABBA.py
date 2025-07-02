k=int(input())
dp=[[0,0],[0,1]]
for i in range(1,k):
    dp.append([dp[i][1],dp[i][1]+dp[i][0]])
print(dp[-1][0],dp[-1][1])