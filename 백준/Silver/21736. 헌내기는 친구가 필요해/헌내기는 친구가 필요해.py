def dfs(vn,vm):
    global visited
    global cnt
    visited[vn][vm] = 'X'
    if board[vn][vm] == 'P':
        cnt += 1
    # for i in range(1,n):
    #     for j in range(1,m):
    #         a = tovisit[i][j][0]
    #         b = tovisit[i][j][1]
    #         if visited[a][b] != 'X':
    #                 dfs(a,b)
                

    if board[vn-1][vm] != 'X' and visited[vn-1][vm] !='X':
        dfs(vn-1,vm)
    if board[vn+1][vm] != 'X' and visited[vn+1][vm] !='X':
        dfs(vn+1,vm)
    if board[vn][vm-1] != 'X' and visited[vn][vm-1] !='X':
        dfs(vn,vm-1)
    if board[vn][vm+1] != 'X' and visited[vn][vm+1] !='X':
        dfs(vn,vm+1)

import sys
sys.setrecursionlimit(500000)
cnt = 0
a=0
b=0
n,m = map(int,(input().split()))
board = [['X']*(m+2)]
#tovisit = [['X']*(m+2)]
visited = [['X']*(m+2)]
for i in range(n):
    temp = ['X']
    temp2 = (list(str(sys.stdin.readline().strip())))
    for j in temp2:
        temp.append(j)
    temp.append('X')
    board.append(temp)
    #tovisit.append(['X','X'])
    temp =[0]*m
    temp.insert(0,'X')
    temp.append('X')
    visited.append(temp)

board.append(['X']*(m+2))
#tovisit.append(['X']*(m+2))
visited.append(['X']*(m+2))

# for i in range(1,n):
#     for j in range(1,m):
#         if board[i-1][j] == 'O' or board[i-1][j] == 'P' or board[i-1][j] == 'I':
#             tovisit[i].insert(j,[i-1,j])
#             tovisit[i-1].insert(j,[i,j])
#         if board[i+1][j] == 'O' or board[i+1][j] == 'P' or board[i+1][j] == 'I':
#             tovisit[i].insert(j,[i+1,j])
#             tovisit[i+1].insert(j,[i,j])
#         if board[i][j-1] == 'O' or board[i][j-1] == 'P' or board[i][j-1] == 'I':
#             tovisit[i].insert(j,[i,j-1])
#             tovisit[i].insert(j-1,[i,j])
#         if board[i][j+1] == 'O' or board[i-1][j+1] == 'P' or board[i-1][j+1] == 'I':
#             tovisit[i].insert(j+1,[i,j+1])  
for i in range(1,n+1):
    for j in range(1,m+1):  
        if board[i][j] == 'I':
            a=i
            b=j

dfs(a,b)
if cnt>0:
    print(cnt)
else:
    print("TT")
#print(board)
