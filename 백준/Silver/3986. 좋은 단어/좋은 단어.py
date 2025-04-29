n = int(input())
li=[]
out = 0
for i in range(n):
    li.append(list(input()))
for line in li:
    stack=[]
    for i in range(len(line)):
        stack.append(line[i])
        if len(stack)>1 and stack[-1] == stack[-2]:
            stack.pop(-1)
            stack.pop(-1)
    if len(stack) == 0:
        out+=1
print(out)