s = 0
t = 0

li = []
for i in range(20):
    a,b,c = map(str,input().split())
    li.append([b,c])
for i in range(20):
    if li[i][1] =='A+':
        t += float(li[i][0])
        s += float(li[i][0])*(4.5)
    elif li[i][1] =='A0':
        t += float(li[i][0])
        s += float(li[i][0])*4
    elif li[i][1] =='B+':
        t += float(li[i][0])
        s += float(li[i][0])*3.5
    elif li[i][1] =='B0':
        t += float(li[i][0])
        s += float(li[i][0])*3
    elif li[i][1] =='C+':
        t += float(li[i][0])
        s += float(li[i][0])*2.5
    elif li[i][1] =='C0':
        t += float(li[i][0])
        s += float(li[i][0])*2
    elif li[i][1] =='D+':
        t += float(li[i][0])
        s += float(li[i][0])*1.5
    elif li[i][1] =='D0':
        t += float(li[i][0])
        s += float(li[i][0])*1
    elif li[i][1] =='F':
        t += float(li[i][0])
print(s/t)