def rev(num):
    str = ""
    for i in range(len(num)):
        str += (num[len(num)-i-1])
    return str
x,y = map(str,input().split())
print(int(rev(str(int(rev(x))+int(rev(y))))))
