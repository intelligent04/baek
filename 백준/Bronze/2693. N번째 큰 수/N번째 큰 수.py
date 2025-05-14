cnt=int(input())
for _ in range(cnt):
    li=list(map(int,input().split()))
    li.sort()
    print(li[-3])