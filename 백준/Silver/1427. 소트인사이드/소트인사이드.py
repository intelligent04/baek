line = input()
dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in (line):
    dic[int(i)] = dic[int(i)]+1
for i in range(9,-1,-1):
    print(str(i)*dic[i],sep='',end='')