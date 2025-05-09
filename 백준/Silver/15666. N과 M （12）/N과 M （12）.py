def dp(temp):
    global visited
    if len(temp)==m:
        visited.add(tuple(temp[:]))
        return
    else:
        for i in li:
            if (len(temp)==0 or i>=temp[-1]):
                temp.append(i)
                dp(temp)
                temp.pop()


n,m=map(int,input().split())
li = list(map(int,input().split()))
li.sort()


visited=set()

dp([])
visited=list(visited)
visited.sort()
for i in visited:
    print(*i)