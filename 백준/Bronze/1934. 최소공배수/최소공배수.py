t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    gcd=1
    for i in range(2,int((min(a,b))+1)):
        if a%i==0 and b%i==0:
            gcd=i
    print(int((a*b)/gcd))
        