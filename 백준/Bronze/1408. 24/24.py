a,b,c = map(int,input().split(':'))
a2,b2,c2 = map(int,input().split(':'))
a4,b4,c4 = 23,59,60
if(a==a2 and b==b2 and c==c2): 
    print("00:00:00")
elif(a>a2 or a==a2 and b>b2 or a==a2 and b==b2 and c>c2):
    a3 = a-a2
    b3 = b-b2
    c3 = c-c2
    a4 -= a3
    b4 -= b3
    c4 -= c3
    if c4>=60:
        c4-=60
        b4+=1
    if b4>=60:
        b4-=60
        a4+=1
    a4,b4,c4 = str(a4),str(b4),str(c4)
    if len(a4) == 1:
        a4 ='0'+a4
    if len(b4) == 1:
        b4 ='0'+b4
    if len(c4) == 1:
        c4 ='0'+c4
    print("%s:%s:%s"%(a4,b4,c4))
elif(a<a2 or a==a2 and b<b2 or a==a2 and b==b2 and c<c2):
    a4 = a2-a
    b4 = b2-b
    c4 = c2-c
    if(c4<0):
        c4+= 60
        b4-=1
    if(b4<0):
        b4+= 60
        a4-=1
    a4,b4,c4 = str(a4),str(b4),str(c4)
    if len(a4) == 1:
        a4 ='0'+a4
    if len(b4) == 1:
        b4 ='0'+b4
    if len(c4) == 1:
        c4 ='0'+c4
    print("%s:%s:%s"%(a4,b4,c4))
