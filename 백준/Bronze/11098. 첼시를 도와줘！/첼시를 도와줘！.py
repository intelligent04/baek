t = int(input())
for i in range(t):
    n = int(input())
    li = []
    for j in range(n):
        a,b = input().split()
        a = int(a)
        li.append([a,b])
    li.sort()
    print(li[-1][1])