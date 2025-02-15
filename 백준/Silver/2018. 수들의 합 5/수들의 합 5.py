n=int(input())
start=1
end=1
cnt=0
s = 1
while start <= n:
    if s == n:
        cnt+=1
        s-= start
        start+=1
        
    elif s<n:
        end+=1
        s += end
    else:
        s-= start
        start+=1

print(cnt)