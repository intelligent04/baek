li = []
for i in range(8):
    li.append([int(input()),i])
li.sort()
li2 = sorted(list(li[3:]),key= lambda li: li[1])
print(sum(row[0] for row in li2))

for i in range(5):
    print(li2[i][1]+1,end=" ")


