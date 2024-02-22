import sys


t = int(input())
for _ in range(t):
    s = 1
    wears = {}
    n = int(input())
    for i in range(n):
        temp = list(map(str,input().split()))
        if temp[1] not in wears:
            wears[temp[1]] = 1
        else:
            wears[temp[1]] = wears[temp[1]] + 1
    
    li = list(wears.values())
    for i in li:
        s *= (i + 1)
    print(s-1)
    