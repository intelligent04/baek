num,j = map(int,input().split())
li = []
while num >= j:
    li.append(int(num%j))
    num //= int(j)
li.append(num)

for i in range(len(li)):
    if li[-1-i] >= 10:
        print(chr(li[-1-i]+55),sep="",end="")
    else:
        print(li[-1-i],sep="",end="")

