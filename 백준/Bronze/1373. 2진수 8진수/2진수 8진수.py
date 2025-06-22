n=input()
if len(n)%3 !=0:
    while len(n)%3!=0:
        n="0"+n
oct=""
i=len(n)-3
while i >= 0:
    temp=0
    temp+=4*int(n[i])
    temp+=2*int(n[i+1])
    temp+=1*int(n[i+2])
    oct=str(temp)+oct
    i-=3


    
print(oct)
