n = int(input())
dp=[1,1,2,5]
def find(n):
    temp=0
    for i in range(n):
        temp+=dp[i]*dp[n-i-1]
    dp.append(temp)
for i in range(4,36):
    find(i)
print(dp[n])
