import sys

n = int(input())
li = []
out = 0
for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
if len(li) ==0:
    print(0)
else:
    sub = n*0.15
    if sub%1 == 0.5:
        sub = int(sub)+1
    else:
        sub = round(sub)

    del li[0:sub]
    del li[len(li)-sub:]
    out = sum(li)
    out = out/len(li)
    if out%1 == 0.5:
        out = int(out)+1
    else:
        out = round(out)
    print(out)