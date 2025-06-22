t=int(input())
li=[1,2]
for i in range(3,10001,2):
    ad = True
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            ad=False
            break
    if ad:
        li.append(i)


for _ in range(t):
    out=[]
    n=int(input())
    mid = n/2
    for i in range(len(li)-1):
        if li[i]<=mid<=li[i+1]:
            left=i
            right=i
    else:
        while left>=0 and right<=len(li):
            if li[left]+li[right]==n:
                out.append([li[left],li[right]])
                break
            elif li[left]+li[right]>n:
                left-=1
            elif li[left]+li[right]<n:
                right+=1



    print(*out[0])



