import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
output = []
for i in range(len(data[0])):
    character = []
    for k in range(n):
        character.append(data[k][i])
    if character.count(character[0]) == len(character):
        output.append(character[0])
    else:
        output.append("?")
print("".join(output))