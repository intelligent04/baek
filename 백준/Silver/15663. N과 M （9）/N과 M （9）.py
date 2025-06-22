def dp(temp):
    global visited
    if len(temp)==m:
        visited.add(tuple(temp[:]))
        return
    else:
        for i in li:
            if vdic[i]<dic[i]:
                temp.append(i)
                vdic[i]+=1
                dp(temp)
                vdic[i]-=1
                temp.pop()


n,m=map(int,input().split())
li = list(map(int,input().split()))
li.sort()
dic = {}
vdic = {}
for i in li:
    dic[i] = 0
    vdic[i] = 0
for i in li:
    dic[i] +=1

visited=set()

dp([])
visited=list(visited)
visited.sort()
for i in visited:
    print(*i)