t = int(input())
li = list(map(int,input().split()))
ma = li[0]
temp = 0
tt=False
ma2=-1000
for i in li:
    if i>ma2:
        ma2=i
    if i>=0:
        tt=True
if tt==False:
    print(ma2)
    quit()
for i in range(t-1):
    temp+=li[i]
    if temp<0:
        temp=0
    if temp>ma:
        ma=temp
if temp+li[-1]>ma:
    ma = temp+li[-1]
    
print(ma)
