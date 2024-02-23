inp = input()
line = list(inp)
realline = []
stack = 0
nums = []
num = ''
s = 0
cnt = line.count('-')
for i in range(len(inp)+cnt*2):
    if line[i] == '-' and stack == 0:
        line.insert(i+1,'(')
        stack += 1
    elif line[i] == '-' and stack == 1:
        line.insert(i,')')
        stack -= 1
    if stack == 1 and i == len(inp)+cnt*2-2:
        line.insert(i+1,')')

for i in range(len(inp)+cnt*2):
    if line[i] != '-' and line[i] != '+' and line[i] != '(' and line[i] != ')':
        nums.append(line[i])
        if i == len(inp)+cnt*2-1:
            for j in nums:
                num += j
            if num != '':
                realline.append(num)
            nums = []
            num = ''
            

    else:
        for j in nums:
            num += j
        if num != '':
            realline.append(num)
        nums = []
        num = ''
        realline.append(line[i])
stack = 0
for i in range(len(realline)):
    if realline[i] != '-' and realline[i] != '+' and realline[i] != '(' and realline[i] != ')':
        if stack == 1:
            s -= int(realline[i])
        else:
            s += int(realline[i])
    elif realline[i] == '(':
        stack = 1
    elif realline[i] == ')':
        stack = 0
                 

print(s)
