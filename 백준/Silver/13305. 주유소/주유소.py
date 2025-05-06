n = int(input())
weights = list(map(int,input().split()))
nodes = list(map(int,input().split()))
paths=[nodes[0]]
out = 0

for i in range(1,n):
    out+=min(paths)*weights[i-1]
    paths.append(nodes[i])
print(out)
