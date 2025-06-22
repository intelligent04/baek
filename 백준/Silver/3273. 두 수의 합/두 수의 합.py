n = int(input())
li  = list(map(int,input().split()))
cnt = 0
x=int(input())
li.sort()
start=0
end=len(li)-1
while start<end:
    temp = li[start]+li[end]
    if temp<x:
        start+=1
    elif temp>x:
        end-=1
    else:
        cnt+=1
        start+=1
        end-=1
print(cnt)