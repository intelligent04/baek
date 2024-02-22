import sys

n, m = map(int,input().split())
a = {}
li = []

for i in range(n):
    a[sys.stdin.readline().strip()] = i+1
b = dict(map(reversed,a.items()))
for i in range(m):
    temp = sys.stdin.readline().strip()
    try :
        int(temp)
        print(b[int(temp)])
    except:
        print(a[temp])
