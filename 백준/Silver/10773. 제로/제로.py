t = int(input())
li = []
for i in range(t):
    temp = int(input())
    if temp == 0:
        li.pop()
    else:
        li.append(temp)
print(sum(li))