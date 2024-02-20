t = int(input())
board = [[0]*100 for _ in range(100)]
sum = 0
for i in range(t):
    x,y = map(int,input().split())
    for j in range(10):
        for k in range(10):
            board[x+j][y+k] = 1
for i in range(100):
    sum += board[i].count(1)
print(sum)