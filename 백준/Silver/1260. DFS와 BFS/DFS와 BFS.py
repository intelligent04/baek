from collections import deque
def dfs(v):
    print(v," ",sep="",end="")
    visit[v] = 1
    for i in vols[v]:
        if visit[i] != 1:
                dfs(i)
    return
def bfs(v,n):
    q = deque([v])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
    visit2[v] = True  # 해당 v 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        v = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        print(v, end=" ")  # 해당 값 출력
        for i in (vols[v]):  # 1부터 N까지 돈다
            if not visit2[i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                visit2[i] = 1  # i 값을 방문처리

n,m,v = map(int,input().split())
global visit
global vols
global visit2
global vols2
visit = []
vols = []
visit.append(0)
vols.append([])
for i in range(n):
    vols.append([])
    visit.append(0)
for i in range(m):
    a,b = map(int,input().split())
    vols[a].append(b)
    vols[b].append(a)
for i in vols:
     i.sort()
visit2 = visit[:]
vols2 = vols[:]
dfs(v)
print()
bfs(v,n)