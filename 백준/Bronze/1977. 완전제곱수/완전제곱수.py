m = int(input())
n = int(input())
li = []
for i in range(0,n-m+1):
    if ((m+i)**0.5)%1 == 0:
        li.append(m+i)

if len(li)>0:
    print(sum(li))
    print(li[0])
else:
    print(-1)