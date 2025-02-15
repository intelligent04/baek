n = int(input())
li = [1,2]
for i in range(2,1001):
    li.append(li[i-1]+li[i-2])
print(li[n-1]%10007)