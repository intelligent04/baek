def dp(temp):
    global visited
    if len(temp)==m:
        visited.append(temp[:])
        return
    else:
        for i in li:
            temp.append(i)
            dp(temp)
            temp.pop()


n,m=map(int,input().split())
li = list(map(int,input().split()))
li.sort()
visited=[]

dp([])
for i in visited:
    print(*i)