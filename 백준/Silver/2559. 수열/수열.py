n,k = map(int,input().split())
li=list(map(int,input().split()))

now = sum(li[0:k])
dp=[sum(li[0:k])]

for i in range(len(li)-k):
    if dp[-1]<now-li[i]+li[i+k]:
        dp.append(now-li[i]+li[i+k])
    else:
        dp.insert(0,now-li[i]+li[i+k])
    now = now-li[i]+li[i+k]
    # dp.append(now)

print(dp[-1])