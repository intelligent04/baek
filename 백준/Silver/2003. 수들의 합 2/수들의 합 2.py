n, m = map(int,input().split())
li = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if sum(li[i:len(li)]) < m:
        break
    for j in range(i+1,n+1):
        if sum(li[i:j]) >= m:
            if sum(li[i:j]) > m:
                break
            else: 
                cnt += 1
                break
        
print(cnt)