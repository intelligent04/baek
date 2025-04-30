t= int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    circles = []
    out = 0
    for __ in range(n):
        temp = list(map(int,input().split()))
        circles.append(temp)
    for i in circles:
        if ((x1-i[0])**2 +(y1-i[1])**2)**(1/2) < i[2]:
            if ((x2-i[0])**2 +(y2-i[1])**2)**(1/2) > i[2]:
                out+=1
        else:
            if ((x2-i[0])**2 +(y2-i[1])**2)**(1/2) < i[2]:
                out+=1
    print(out)
