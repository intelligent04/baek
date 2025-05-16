a1,a0 = map(int,input().split())
c=int(input())
n0=int(input())
t = True
for n in range(n0,101):
    if not a1*n+ a0 <= c*n:
        t = False
print(int(t))
    