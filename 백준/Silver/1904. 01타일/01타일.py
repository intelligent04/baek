dp = [0,1,2,3,5]
left=1
right=2
out=3
n=int(input())

for i in range(3,n+1):
    out=left+right
    left=right
    right=out
    if out>157460:
        right%=157460
        left%=157460
        out%=157460

if n<=4:
    print(dp[n]%15746)
else:
    print(out%15746)
