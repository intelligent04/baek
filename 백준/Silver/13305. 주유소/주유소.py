n = int(input())
weights = list(map(int,input().split()))
nodes = list(map(int,input().split()))
minimum = nodes[0]

out = 0

for i in range(1,n):
    out+=minimum*weights[i-1]
    if nodes[i]<minimum:
        minimum=nodes[i]
print(out)
