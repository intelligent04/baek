import sys

n, m = map(int,input().split())
dic = {}
cnt = 0

for i in range(n):
    dic[sys.stdin.readline()] = 0
for i in range(m):
    temp = sys.stdin.readline()
    if  temp in dic:
        cnt+=1
print(cnt)