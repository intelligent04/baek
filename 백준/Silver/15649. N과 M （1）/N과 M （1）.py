def dp(li):
    global visited
    if(len(li)==m):
        visited.append(li[:])
    else:
        for i in range(1,n+1):
            if i not in li:
                li.append(i)
                dp(li)
                li.pop()

n,m = map(int,input().split())
li=[]
visited=[]
dp(li)
for i in visited:
    print(*i)
