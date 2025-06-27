n = int(input())
now=0
past2=0
past1=1
if n == 0:
    print(0)
    print(0)
elif n==1 or n==-1:
    print(1)
    print(1)
elif n < 0:
    n = -n
    for i in range(2,n+1):
        now=past2-past1
        past2=past1
        past1=now
    if now>0:
        print(1)
    elif now==0:
        print(0)
    else:
        print(-1)
    print(abs(now)%1000000000)
else:
    for i in range(2, n + 1):
        now=past2+past1
        past2=past1
        past1=now
    print(1)
    print(abs(now)%1000000000)
