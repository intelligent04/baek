t = int(input())
li = []
for i in range(t):
    li.append(int(input()))

total = 0
for ii in range(t):
    for i in range(1,t):
        dy = li[i] - li[i-1]
        if dy<=1:
            total += 1-dy
            li[i-1] -= 1-dy
print(total)