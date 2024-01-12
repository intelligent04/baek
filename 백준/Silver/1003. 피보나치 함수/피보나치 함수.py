t = int(input())

for i in range(t):
    n = int(input())
    if(n == 0):
        print("1 0")
        continue
    if(n == 1):
        print("0 1")
        continue
    fibo = [[1,0],[0,1]]
    zero = 0
    one = 0
    for j in range(2,n+1):
        a = fibo[j-2][0] + fibo[j-1][0]
        b = fibo[j-1][1] + fibo[j-2][1]
        fibo.append([a,b])
    print(fibo[-1][0],fibo[-1][1])
