li = []
n = int(input())
for i in range(n):
    temp = list(map(int,input().split()))
    li.append(temp)
x,y = 0,0
step = li[x][y]
output=[]
visited = []
for i in range(n):
    visited.append([False]*n)

queue = []#queue에는 다음 분기점의 좌표가 담긴다
if n-1 >= x+step:
    queue.append([x+step,y])
if n-1 >= y+step:   
    queue.append([x,y+step])
while queue:
    x,y = queue.pop(0)
    step = li[x][y]
    if step == -1:
        output.append("HaruHaru")
        break
    if n-1 >= x+step and visited[x+step][y] != True:
        queue.append([x+step,y])
        visited[x+step][y] = True
    if n-1 >= y+step and visited[x][y+step] != True:
        queue.append([x,y+step])
        visited[x][y+step] = True
output.append("Hing")
print(output[0])
    

    
