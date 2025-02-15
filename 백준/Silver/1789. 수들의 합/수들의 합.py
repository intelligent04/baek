s = int(input())

cnt = 1
sum = 0
while sum < s:
    sum += cnt
    cnt += 1

if s == 1:
    print(1)
elif sum == s:
    print(cnt-1)
else:
    print(cnt - 2)
