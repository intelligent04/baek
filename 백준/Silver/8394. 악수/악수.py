n = int(input())
past1 = 2
past2 = 1
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(3, n + 1):
        now = past1 + past2
        past2 = past1
        past1 = now
        if now>1000000 and past1 > 1000000 and past2 > 1000000:
            now%=1000000
            past1 %= 1000000
            past2 %= 1000000
    print(now%10)
