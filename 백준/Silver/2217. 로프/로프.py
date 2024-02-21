from collections import deque
import sys

t = int(input())
q = []
max = -1
for _ in range(t):
    q.append(int(sys.stdin.readline()))
q.sort()
for i in range(1,t+1):
    if q[-i]*i > max:
        max = q[-i]*i
print(max)