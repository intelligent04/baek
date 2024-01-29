def conti(n,m):
    global visited, wood
    visited[n][m] = True
    if wood[n][m] == '-' and m+1 < b and wood[n][m+1] == '-':
        conti(n,m+1)
    elif wood[n][m] == '|' and n+1 < a and wood[n+1][m] == '|':
        conti(n+1,m)
    else:
        return
result = 0
a,b = map(int,input().split())
wood = []
visited = []
for i in range(a):
    line = list(input())
    wood.append(line)

for i in range(a):
    visited.append([False]*b)
    
for n in range(a):
    for m in range(b):
        if visited[n][m] == False:
            conti(n,m)
            result += 1
print(result)
