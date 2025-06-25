def dp(v,w,li):
    global mav
    if w>=k:
        return
    else:
        dp()
n,k=map(int,input().split())
li=[]
dp=[0]*(k+1)
for i in range(n):
    li.append(list(map(int,input().split())))

for w,v in li:
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
dp.sort()
print(dp[-1])
