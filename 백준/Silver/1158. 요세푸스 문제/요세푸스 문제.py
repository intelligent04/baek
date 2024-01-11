n,k = map(int,input().split())
seq = k-1
li = []
print("<",sep="",end="")
for i in range(n):
    li.append(i+1)
while len(li) > 1:
    if(seq<len(li)):
        temp = li[seq]
        del(li[seq])
        print(temp,", ",sep="",end="")
        seq += k-1
    else:
        seq %= len(li)
        temp = li[seq]
        del(li[seq])
        print(temp,", ",sep="",end="")
        seq += k-1
print(li[0],">",sep="",end="")
