t = int(input())
li = []


for i in range(t):
    a,b = map(int,input().split())
    li.append([b,a])
li.sort()
for i in range(t):
    print(li[i][1],li[i][0])

