a,b = map(int,input().split())
dict = {}
for i in range(a):
    name, pw = map(str,input().split(' '))
    dict[name] = pw
for i in range(b):
    name = input()
    print(dict[name])