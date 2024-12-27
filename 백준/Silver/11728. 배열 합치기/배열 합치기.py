input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = a + b
a.sort()
print(*a, sep=" ")
