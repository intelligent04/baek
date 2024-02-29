import sys

n,m = map(int,(input().split()))
li = list(map(int,(sys.stdin.readline().split())))
#li.sort()


start = 0
end = max(li)
#li2 = [li[n//2]]
while start <= end:
    s = 0
    h = (start+end)//2
    for i in li:
        if i - h > 0:
            s += i-h
    #if max(li2[1:]) > h:
    if s>=m:
        start = h+1
    else:
        end = h-1
    #elif max(li2[1:]) <= h:
        #end = h-1
    # if s>=m:
    #     li2.append(h)
    
print(end)
