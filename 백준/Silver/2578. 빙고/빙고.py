li = []
li2 = []
for i in range(5):
    temp = list(map(int,input().split()))
    li.append(temp)

for i in range(5):
    temp = list(map(int,input().split()))
    li2.append(temp)

cnt = 0
t = 0
for a in range(5):
    for b in range(5):
        cnt+=1
        for i in range(5):
            for j in range(5):
                stack = 0
                if li2[a][b] == li[i][j]:
                    li[i][j] = 0
                    for x in range(5):
                        if (li[0][x] + li[1][x] + li[2][x] + li[3][x] + li[4][x]) == 0:
                            stack+=1
                        if sum(li[x]) == 0:
                            stack+=1
                    if (li[0][0] + li[1][1] + li[2][2] + li[3][3] + li[4][4]) == 0:
                        stack+=1
                    if (li[0][4] + li[1][3] + li[2][2] + li[3][1] + li[4][0]) == 0:
                        stack+=1
                    if stack>=3 and t == 0:
                        print(cnt)
                        t=1


                