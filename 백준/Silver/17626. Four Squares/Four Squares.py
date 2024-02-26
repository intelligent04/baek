import math

n = int(input())
#a = int(n**(0.5))

li = [0,1,2,3]
li2 = [0,1,2,3]
for i in range(4,n+1):
    temp = []
    temp.append(li[i - (int(math.sqrt(i)))**2] + 1)
    for j in range(60):
        if (int(math.sqrt(i)) - j)**2 > 0 and int(math.sqrt(i)) - j>0:
            temp.append(li[i - (int(math.sqrt(i)) - j)**2] + 1)
    li.append(min(temp))
    #li2.append(i%10)
print(li[n])
#print(li2)