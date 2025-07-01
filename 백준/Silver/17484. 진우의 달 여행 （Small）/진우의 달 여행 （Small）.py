def go(y, x, pre_dir, stack):
    global low
    #print(graph[y][x])
    stack += graph[y][x]
    if y == n - 1:
        if stack < low:
            low = stack
        return
    if pre_dir == -1:
        go(y + 1, x, 0, stack)
        if x + 1 < m:
            go(y + 1, x + 1, 1, stack)
    elif pre_dir == 0:
        if x - 1 >= 0:
            go(y + 1, x - 1, -1, stack)
        if x + 1 < m:
            go(y + 1, x + 1, 1, stack)
    elif pre_dir == 1:
        if x - 1 >= 0:
            go(y + 1, x - 1, -1, stack)
        go(y + 1, x, 0, stack)
    else:
        if x - 1 >= 0:
            go(y + 1, x - 1, -1, stack)
        go(y + 1, x, 0, stack)
        if x + 1 < m:
            go(y + 1, x + 1, 1, stack)


n, m = map(int, (input().split()))
graph = []
low = 600
for i in range(n):
    graph.append(list(map(int, (input().split()))))
for i in range(m):
    go(0, i, -2, 0)
print(low)
