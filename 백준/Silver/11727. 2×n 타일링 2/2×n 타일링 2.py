n = int(input())
li = [1]
temp = 1
for i in range(1,1002):
    li.append(2*li[i-1]+temp)
    temp *= -1
print(li[n-1]%10007)