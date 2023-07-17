import sys

n = int(sys.stdin.readline())

c = []
for i in range(10000):
    c.append(0)

for i in range(n):
    s = list(map(int,sys.stdin.readline().split()) )
    c[s[0]-1] += 1
for i in range(10000):
    for m in range(c[i]):
        print(i+1)

