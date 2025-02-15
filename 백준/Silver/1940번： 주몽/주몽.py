n = int(input())
m = int(input())
cnt = 0
p1=0
p2 = n-1
li = list(map(int, input().split()))
li.sort(reverse=True)
for i in range(n):
    if li[i] >= m:
        p1 += 1
while p1 < p2:
    if li[p1] + li[p2] == m:
        cnt += 1
        p1 += 1
        p2 -= 1
    elif li[p1] + li[p2] > m:
        p1 += 1
    else:
        p2 -= 1
print(cnt)

