t = int(input())
li = []
for i in range(t):
    li.append(list(map(int,input().split())))
for i in range(t-1,0,-1):
    temp=[]
    for j in range(0,len(li[i])-1):
        temp.append(max(li[i][j],li[i][j+1]))
    for j in range(0,len(li[i])-1):
        li[i-1][j] += temp[j]
print(li[0][0])