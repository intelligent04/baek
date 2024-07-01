t = int(input())
rings = list(map(int,input().split()))
for i in range(1,len(rings)):
    for b in range(1,1000):
        for a in range(1,1000):
            if a/b == rings[0]/rings[i]:
                break
        if a/b == rings[0]/rings[i]:
                print(a,"/",b,sep="")
                break
    
