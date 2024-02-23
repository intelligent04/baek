import sys
sys.setrecursionlimit(10 ** 5)
def dfs(v,visit):
    visit[v] = 1
    for i in vols[v]:
        if visit[i] != 1:
            dfs(i,visit)

n,m = map(int,input().split())
vols = []
visit = []
cnt = 0
for i in range(n+1):
    vols.append([])
    visit.append(0)
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    vols[a].append(b)
    vols[b].append(a)
for i in range(1,n+1):
    if visit[i] != 1:
        cnt += 1
        dfs(i,visit)
        
print(cnt)