n = int(input())
li = list(map(int,input().split()))
high=0
for i in range(n):
    temp=0
    for j in range(i+1,n):
        if li[i]>li[j]:
            temp+=1
        else:
            break
    if temp>high:
        high=temp
print(high)