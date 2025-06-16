def sosu(n):
    so=True
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            so=False
            break
    return so
li=[]
while True:
    temp=int(input())
    if temp==0:
        break
    else:
        li.append(temp)

nums=[]
for i in range(246913):
    nums.append(1)
for i in range(4,246913,2):
    nums[i]=0
for i in range(6,246913,3):
    nums[i]=0
for i in range(10,246913,5):
    nums[i]=0
        
for i in range(1,246913,2):
    if not sosu(i):
        nums[i]=0

for i in li:
    print(sum(nums[i+1:2*(i)+1]))
